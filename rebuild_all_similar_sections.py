#!/usr/bin/env python3
"""
Rebuilds the two similar-product sections on every product page
linked from italiaanse-percolator-kopen.html:

  1. "Vergelijkbare producten van [merk]"  → 4 same-brand products (by similarity)
  2. "Andere product alternatieven"         → 4 different-brand products

Also:
  - Adds a one-line intro under each section heading
  - Removes grey border-top between the two sections (CSS fix)
  - Skips pages that are already processed (similar-intro present)
"""

import re
import json
import random
from pathlib import Path

import sys

BASE_DIR      = Path('/Users/marc/Desktop/italiaanse-percolator')
PRODUCTEN_DIR = BASE_DIR / 'producten'
ALL_PRODUCTS  = BASE_DIR / 'all_products.json'

# CLI: optional --html <file> or --type <type_value>
# Default: read from italiaanse-percolator-kopen.html
SOURCE_HTML  = None
SOURCE_TYPE  = None
args = sys.argv[1:]
if '--html' in args:
    SOURCE_HTML = BASE_DIR / args[args.index('--html') + 1]
elif '--type' in args:
    SOURCE_TYPE = args[args.index('--type') + 1]
else:
    SOURCE_HTML = BASE_DIR / 'italiaanse-percolator-kopen.html'

# ── 1. Load product catalogue ────────────────────────────────────────────────
all_products = json.loads(ALL_PRODUCTS.read_text())
by_slug = {p['slug']: p for p in all_products if p.get('slug')}

# Build per-brand pools (slug → list of products for that brand)
brand_pool: dict[str, list] = {}
for p in all_products:
    if not p.get('slug') or not p.get('image'):
        continue
    b = p.get('brand', '')
    brand_pool.setdefault(b, []).append(p)

# "Andere" pool: any product, excluding Bialetti & "Overig"
alt_pool = [p for p in all_products
            if p.get('brand') not in ('Bialetti', 'Overig', '')
            and p.get('slug') and p.get('image')]
# Fallback if too small
if len(alt_pool) < 20:
    alt_pool = [p for p in all_products
                if p.get('slug') and p.get('image')]


# ── 2. Helpers ───────────────────────────────────────────────────────────────
def similar_same_brand(current_slug: str, brand: str, n: int = 4) -> list:
    """Return n products from the same brand, sorted by similarity."""
    current = by_slug.get(current_slug, {})
    cap = current.get('capaciteit', 0)
    mat = current.get('materiaal', '')
    ind = current.get('inductie', '')
    pool = brand_pool.get(brand, [])

    def score(p):
        if p['slug'] == current_slug:
            return -1
        s = 0
        if cap and p.get('capaciteit') == cap: s += 3
        if mat and p.get('materiaal')  == mat: s += 2
        if ind and p.get('inductie')   == ind: s += 1
        return s

    candidates = sorted(pool, key=score, reverse=True)
    seen, result = set(), []
    for p in candidates:
        if p['slug'] == current_slug or p['slug'] in seen:
            continue
        seen.add(p['slug'])
        result.append(p)
        if len(result) == n:
            break
    return result


def similar_alt(current_slug: str, current_brand: str, n: int = 4) -> list:
    """Return n products from other brands, varied per page."""
    current = by_slug.get(current_slug, {})
    cap = current.get('capaciteit', 0)
    mat = current.get('materiaal', '')

    def score(p):
        s = 0
        if p.get('brand') == current_brand:  # prefer other brands
            s -= 5
        if cap and p.get('capaciteit') == cap: s += 2
        if mat and p.get('materiaal')  == mat: s += 1
        return s

    rng = random.Random(hash(current_slug) & 0xFFFFFFFF)
    scored = sorted(alt_pool, key=lambda p: (score(p), rng.random()), reverse=True)

    seen, result = set(), []
    for p in scored:
        if p['slug'] == current_slug or p['slug'] in seen:
            continue
        if p.get('brand') == current_brand:
            continue
        seen.add(p['slug'])
        result.append(p)
        if len(result) == n:
            break
    return result


def card_html(p: dict) -> str:
    price_str = f'€{p["price"]:.2f}'.replace('.', ',') if p.get('price') else ''
    return (
        f'                <a href="{p["slug"]}.html" class="similar-card">\n'
        f'                    <img src="{p["image"]}" alt="{p["name"]}" loading="lazy" onerror="this.style.display=\'none\'">\n'
        f'                    <h4>{p["name"][:60]}</h4>\n'
        f'                    <span class="card-price">{price_str}</span>\n'
        f'                </a>'
    )


def make_section(title: str, intro: str, cards: list, extra_class: str = '') -> str:
    cls = f'similar-section{" " + extra_class if extra_class else ""}'
    cards_html = '\n'.join(card_html(c) for c in cards)
    return (
        f'        <section class="{cls}">\n'
        f'            <h2>{title}</h2>\n'
        f'            <p class="similar-intro">{intro}</p>\n'
        f'            <div class="similar-grid">\n'
        f'{cards_html}\n'
        f'            </div>\n'
        f'        </section>'
    )


CSS_PATCH = (
    '        .similar-intro { font-size:0.88rem;color:#666;margin:-0.75rem 0 1.25rem; }\n'
    '        .similar-section + .similar-section { border-top:none;margin-top:2rem; }\n'
)

# ── 3. Build product list from source ────────────────────────────────────────
if SOURCE_HTML:
    src = SOURCE_HTML.read_text()
    m = re.search(r'const allProducts = (\[.*?\]);', src, re.DOTALL)
    if not m:
        raise RuntimeError(f"allProducts not found in {SOURCE_HTML}")
    page_products = [p for p in json.loads(m.group(1)) if p.get('slug')]
    print(f"Source: {SOURCE_HTML.name} → {len(page_products)} products\n")
elif SOURCE_TYPE:
    page_products = [p for p in all_products
                     if p.get('slug') and p.get('deliverable')
                     and p.get('price', 0) > 0 and p.get('type') == SOURCE_TYPE]
    print(f"Source: type='{SOURCE_TYPE}' → {len(page_products)} products\n")
else:
    raise RuntimeError("No source specified")

stats = {'modified': 0, 'skipped_done': 0, 'skipped_no_section': 0, 'not_found': 0}

for item in page_products:
    slug  = item['slug']
    brand = item.get('brand', '')

    page_path = PRODUCTEN_DIR / f'{slug}.html'
    if not page_path.exists():
        print(f"  NOT FOUND : {slug}")
        stats['not_found'] += 1
        continue

    html = page_path.read_text()

    # Skip already processed
    if 'similar-intro' in html:
        stats['skipped_done'] += 1
        continue

    # Find the block of similar-section(s)
    block_match = re.search(
        r'(<section class="similar-section[^>]*">.*</section>)',
        html, re.DOTALL
    )
    if not block_match:
        print(f"  SKIP (no section): {slug}")
        stats['skipped_no_section'] += 1
        continue

    original_block = block_match.group(1)

    # Determine brand from all_products.json (more reliable than page JS)
    product_data = by_slug.get(slug, {})
    brand = product_data.get('brand', brand) or brand

    same_cards = similar_same_brand(slug, brand, 4)
    other_cards = similar_alt(slug, brand, 4)

    # If same brand has fewer than 2 products, merge with other cards
    if len(same_cards) < 2:
        sec1 = make_section(
            f'Vergelijkbare producten van {brand}' if brand else 'Vergelijkbare producten',
            'Gelijkaardige modellen voor dezelfde koffiebeleving.',
            same_cards + other_cards[:4 - len(same_cards)]
        )
        sec2 = make_section(
            'Andere product alternatieven',
            'Kwalitatieve alternatieven van andere merken.',
            other_cards,
            extra_class='similar-section-alt'
        )
    else:
        sec1 = make_section(
            f'Vergelijkbare producten van {brand}' if brand else 'Vergelijkbare producten',
            f'Andere populaire {brand}-modellen die goed bij jouw keuze passen.' if brand else 'Andere populaire modellen.',
            same_cards
        )
        sec2 = make_section(
            'Andere product alternatieven',
            'Kwalitatieve alternatieven van andere merken voor dezelfde koffiebeleving.',
            other_cards,
            extra_class='similar-section-alt'
        )

    new_block = sec1 + '\n' + sec2

    # Inject CSS if missing
    if 'similar-intro' not in html:
        html = html.replace('    </style>', CSS_PATCH + '    </style>', 1)

    html = html.replace(original_block, new_block, 1)
    page_path.write_text(html)

    print(f"  OK : [{brand}] {slug}")
    stats['modified'] += 1

print(
    f"\n{'─'*60}\n"
    f"  Modified        : {stats['modified']}\n"
    f"  Already done    : {stats['skipped_done']}\n"
    f"  No section      : {stats['skipped_no_section']}\n"
    f"  Not found       : {stats['not_found']}\n"
    f"{'─'*60}"
)
