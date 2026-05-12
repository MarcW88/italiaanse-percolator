#!/usr/bin/env python3
"""
Clean product titles and translate English content to Dutch.
- Shorten keyword-stuffed titles to essentials
- Translate English titles and descriptions to Dutch
- Strip HTML from descriptions
"""

import json
import re
import time
import html
from pathlib import Path
from deep_translator import GoogleTranslator

INPUT = Path(__file__).parent.parent / "all_products.json"
OUTPUT = INPUT  # Overwrite in place
BACKUP = INPUT.with_suffix(".json.bak")

translator = GoogleTranslator(source='en', target='nl')

# ─── Language detection ─────────────────────────────────────────────
EN_WORDS = {
    'with', 'for', 'the', 'and', 'from', 'this', 'that', 'your', 'you',
    'stainless', 'steel', 'coffee', 'maker', 'filter', 'travel', 'portable',
    'resistant', 'heat', 'material', 'offers', 'brewing', 'made', 'high',
    'quality', 'designed', 'perfect', 'ideal', 'easy', 'use', 'durable',
    'lightweight', 'features', 'suitable', 'capacity', 'premium', 'enjoy',
    'allows', 'when', 'also', 'just', 'very', 'which', 'into', 'even',
    'while', 'about', 'they', 'will', 'been', 'have', 'each', 'than',
    'other', 'more', 'only', 'most', 'over', 'after', 'before', 'does',
    'because', 'great', 'beautiful', 'strong', 'smooth'
}

NL_WORDS = {
    'voor', 'van', 'met', 'het', 'een', 'die', 'dat', 'zijn', 'wordt',
    'door', 'ook', 'maar', 'niet', 'wel', 'nog', 'kan', 'aan', 'bij',
    'koffie', 'kopjes', 'kops', 'geschikt', 'materiaal', 'aluminium',
    'percolator', 'espresso', 'inductie', 'kopje', 'roestvrij', 'staal',
    'zwart', 'zilver', 'rood', 'groen', 'blauw', 'goud', 'bruin', 'wit',
    'maat', 'kleur', 'leverbaar', 'gratis', 'verzending', 'kopen',
    'gemaakt', 'ideaal', 'perfect', 'duurzaam', 'capaciteit'
}


def is_english(text):
    """Detect if text is primarily English."""
    if not text:
        return False
    words = set(re.findall(r'[a-z]+', text.lower()))
    en_count = len(words & EN_WORDS)
    nl_count = len(words & NL_WORDS)
    # If significantly more English words than Dutch
    return en_count >= 4 and en_count > nl_count * 1.5


# ─── HTML stripping ────────────────────────────────────────────────
def strip_html(text):
    """Remove HTML tags and decode entities."""
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# ─── Title cleaning ────────────────────────────────────────────────
def clean_title(name, brand="", product_type=""):
    """Shorten a keyword-stuffed title to its essentials."""
    if not name:
        return name

    original = name

    # Remove common filler/duplicate patterns
    # Remove content in multiple consecutive dashes/pipes
    # "Product A - Synoniem A - Synoniem B - Synoniem C" → "Product A"
    parts = re.split(r'\s*[-–—|]\s*', name)

    if len(parts) > 3:
        # Keep first 2-3 meaningful parts, skip redundant ones
        kept = []
        seen_words = set()
        for part in parts:
            part = part.strip()
            if not part:
                continue
            # Check if this part adds new info or is just a synonym
            part_words = set(re.findall(r'[a-zA-Z]{3,}', part.lower()))
            # If >60% of words already seen, it's redundant
            if seen_words and len(part_words & seen_words) > len(part_words) * 0.6:
                continue
            seen_words |= part_words
            kept.append(part)
            if len(' - '.join(kept)) > 80:
                break
        name = ' - '.join(kept[:3])

    # Remove repeated words like "tea strainer herb strainer tea leaf egg tea strainer"
    words = name.split()
    if len(words) > 8:
        deduped = []
        seen = set()
        for w in words:
            key = w.lower().rstrip('.,;:!?')
            if key not in seen or len(key) <= 2:
                deduped.append(w)
                seen.add(key)
        name = ' '.join(deduped)

    # Truncate at 80 chars on a word boundary
    if len(name) > 85:
        truncated = name[:82].rsplit(' ', 1)[0]
        if len(truncated) > 40:
            name = truncated

    # Clean up trailing punctuation
    name = name.rstrip(' -–—|,;:')

    return name


# ─── Translation with batching ────────────────────────────────────
def translate_text(text, max_len=4500):
    """Translate English text to Dutch via Google Translate."""
    if not text or len(text.strip()) < 10:
        return text
    try:
        # Google Translate has a ~5000 char limit
        if len(text) > max_len:
            text = text[:max_len]
        result = translator.translate(text)
        return result if result else text
    except Exception as e:
        print(f"  ⚠ Translation error: {e}")
        return text


def translate_batch(texts, batch_size=10):
    """Translate a list of texts, with rate limiting."""
    results = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        for text in batch:
            results.append(translate_text(text))
        if i + batch_size < len(texts):
            time.sleep(1)  # Rate limit
    return results


# ─── Main ──────────────────────────────────────────────────────────
def main():
    print("Loading products...")
    with open(INPUT, encoding='utf-8') as f:
        products = json.load(f)

    # Backup
    print(f"Backing up to {BACKUP}...")
    with open(BACKUP, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    stats = {
        'titles_shortened': 0,
        'titles_translated': 0,
        'descs_translated': 0,
        'descs_html_cleaned': 0,
        'total': len(products)
    }

    # Phase 1: Clean all titles
    print("\n=== Phase 1: Cleaning titles ===")
    for p in products:
        original = p.get('name', '')
        cleaned = clean_title(original, p.get('brand', ''), p.get('type', ''))
        if cleaned != original:
            p['name'] = cleaned
            stats['titles_shortened'] += 1

    print(f"  Shortened {stats['titles_shortened']} titles")

    # Phase 2: Strip HTML from all descriptions
    print("\n=== Phase 2: Stripping HTML from descriptions ===")
    for p in products:
        desc = p.get('description', '')
        if '<' in desc and '>' in desc:
            p['description'] = strip_html(desc)
            stats['descs_html_cleaned'] += 1

    print(f"  Cleaned HTML from {stats['descs_html_cleaned']} descriptions")

    # Phase 3: Detect and translate English titles
    print("\n=== Phase 3: Translating English titles ===")
    en_title_products = [(i, p) for i, p in enumerate(products) if is_english(p.get('name', ''))]
    print(f"  Found {len(en_title_products)} English titles")

    for idx, (i, p) in enumerate(en_title_products):
        original = p['name']
        translated = translate_text(original)
        if translated and translated != original:
            products[i]['name'] = clean_title(translated)
            stats['titles_translated'] += 1
            print(f"  [{idx+1}/{len(en_title_products)}] {original[:50]}... → {products[i]['name'][:50]}...")
        if idx % 10 == 9:
            time.sleep(1)

    # Phase 4: Detect and translate English descriptions
    print("\n=== Phase 4: Translating English descriptions ===")
    en_desc_products = [(i, p) for i, p in enumerate(products) if is_english(p.get('description', ''))]
    print(f"  Found {len(en_desc_products)} English descriptions")

    for idx, (i, p) in enumerate(en_desc_products):
        original = p['description']
        translated = translate_text(original)
        if translated and translated != original:
            products[i]['description'] = translated
            stats['descs_translated'] += 1
            if idx < 5:
                print(f"  [{idx+1}/{len(en_desc_products)}] Translated {len(original)} chars")
        if idx % 10 == 9:
            time.sleep(1)
        if idx % 50 == 49:
            print(f"  ... {idx+1}/{len(en_desc_products)} done")

    # Phase 5: Update slugs for renamed products
    print("\n=== Phase 5: Saving ===")
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"\n=== DONE ===")
    print(f"  Total products: {stats['total']}")
    print(f"  Titles shortened: {stats['titles_shortened']}")
    print(f"  Titles translated EN→NL: {stats['titles_translated']}")
    print(f"  Descriptions translated EN→NL: {stats['descs_translated']}")
    print(f"  Descriptions HTML cleaned: {stats['descs_html_cleaned']}")


if __name__ == '__main__':
    main()
