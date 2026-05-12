#!/usr/bin/env python3
"""Generate product pages for all products in all_products.json
Usage: python3 generate_product_pages.py
Re-run after updating all_products.json with import_bol_feed.py
"""
import json
import re
import html as html_mod
from pathlib import Path

ROOT = Path(__file__).parent
PRODUCTS = json.load(open(ROOT / 'all_products.json', encoding='utf-8'))
OUT_DIR = ROOT / 'producten'
OUT_DIR.mkdir(exist_ok=True)


def h(text):
    return html_mod.escape(str(text))


def stars_html(rating):
    r = round(float(rating or 4.5))
    return '★' * r + '☆' * (5 - r)


def cat_page(ptype):
    if ptype == 'Cafetière électrique':
        return 'elektrische-percolators.html'
    if ptype == 'Accessoire':
        return 'accessoires.html'
    return 'percolators.html'


def cat_label(ptype):
    if ptype == 'Cafetière électrique':
        return 'Elektrische Percolators'
    if ptype == 'Accessoire':
        return 'Accessoires'
    return 'Percolators'


def induction_nl(val):
    return 'Ja' if val == 'Oui' else 'Nee'


def kookplaten(p):
    if p.get('inductie') == 'Oui':
        return 'Alle kookplaten incl. inductie'
    if p.get('type') == 'Cafetière électrique':
        return 'Elektrisch (geen kookplaat nodig)'
    return 'Gas, elektrisch, keramisch'


def find_similar(product, all_products, n=4):
    same_type = [p for p in all_products if p['id'] != product['id'] and p['type'] == product['type'] and p['deliverable'] and p['price'] > 0]
    same_brand = [p for p in same_type if p['brand'] == product['brand']]
    others = [p for p in same_type if p['brand'] != product['brand']]
    candidates = same_brand[:2] + others[:2]
    if len(candidates) < n:
        candidates = (same_brand + others)[:n]
    return candidates[:n]


def generate_page(p, all_products):
    name = h(p['name'])
    slug = p['slug']
    brand = h(p['brand'])
    model = h(p.get('model', ''))
    price = p['price']
    price_display = f"€{price:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    list_price = p.get('list_price', 0)
    image = p.get('image', '')
    affiliate = p.get('affiliate_url', '#')
    cap = p.get('capaciteit', 0)
    mat = h(p.get('materiaal', 'Aluminium'))
    ind = induction_nl(p.get('inductie', 'Non'))
    color = h(p.get('color', ''))
    desc = h(p.get('description', ''))
    ptype = p.get('type', 'Cafetière percolateur')
    ean = p.get('ean', '')

    kicker_parts = [brand]
    if model:
        kicker_parts.append(model)
    if cap > 0:
        kicker_parts.append(f'{cap} kops')
    kicker = ' · '.join(kicker_parts)

    cap_text = f'{cap} kopjes (~{cap * 50}ml)' if cap > 0 else 'Zie beschrijving'
    persons = '1-2 personen' if cap <= 3 else '2-4 personen' if cap <= 6 else '4+ personen' if cap > 6 else ''

    intro = f'{name} kopen? '
    if ptype == 'Cafetière percolateur':
        intro += f'Deze {mat.lower()} percolator'
        if cap > 0:
            intro += f' voor {cap} kopjes is perfect voor {persons}.'
        else:
            intro += ' zet authentieke Italiaanse koffie.'
        intro += f' Direct leverbaar via Bol.com met gratis verzending.'
    elif ptype == 'Cafetière électrique':
        intro += f'Elektrische percolator van {brand}. Eenvoudig koffie zetten zonder kookplaat. Direct leverbaar.'
    else:
        intro += f'Handig accessoire voor je percolator. Direct leverbaar via Bol.com.'

    pros = []
    if brand != 'Overig':
        pros.append(f'✓ {brand} kwaliteit')
    if cap > 0:
        pros.append(f'✓ {cap} kopjes ({cap * 50}ml)')
    pros.append(f'✓ {mat}')
    if ind == 'Ja':
        pros.append('✓ Inductie geschikt')
    pros.append('✓ Gratis verzending')

    similar = find_similar(p, all_products)
    similar_html = ''
    for s in similar:
        sp = f"€{s['price']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        similar_html += f'''                <a href="{s['slug']}.html" class="similar-card">
                    <img src="{s.get('image','')}" alt="{h(s['name'][:60])}" loading="lazy" onerror="this.style.display='none'">
                    <h4>{h(s['name'][:65])}</h4>
                    <span class="card-price">{sp}</span>
                </a>
'''

    price_old_html = ''
    if list_price and list_price > price:
        lp = f"€{list_price:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        discount = round((1 - price / list_price) * 100)
        price_old_html = f'<span style="text-decoration:line-through;color:#999;font-size:1.1rem;margin-left:0.5rem;">{lp}</span> <span style="background:#e8f5e9;color:#2e7d32;font-size:0.8rem;padding:0.2rem 0.5rem;border-radius:4px;margin-left:0.5rem;">-{discount}%</span>'

    page = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} kopen | Italiaanse Percolator</title>
    <meta name="description" content="{name} kopen? Prijs: {price_display}. {mat}, {cap_text}. Direct leverbaar via Bol.com met gratis verzending.">
    <link rel="stylesheet" href="../style.css">
    <link rel="canonical" href="https://italiaanse-percolator.nl/producten/{slug}.html">
    <link rel="icon" type="image/svg+xml" href="../favicon.svg">
    <meta name="theme-color" content="#D2691E">
    <script type="application/ld+json">
    {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{name}",
    "description": "{h(desc[:200]) if desc else name}",
    "brand": {{ "@type": "Brand", "name": "{brand}" }},
    "category": "{h(cat_label(ptype))}",
    "image": "{h(image)}",
    "url": "https://italiaanse-percolator.nl/producten/{slug}.html",
    {f'"gtin13": "{ean}",' if ean and len(ean) == 13 else ''}
    "offers": {{
        "@type": "Offer",
        "price": "{price}",
        "priceCurrency": "EUR",
        "availability": "https://schema.org/InStock",
        "seller": {{ "@type": "Organization", "name": "Bol.com" }}
    }},
    "additionalProperty": [
        {{ "@type": "PropertyValue", "name": "Capaciteit", "value": "{cap_text}" }},
        {{ "@type": "PropertyValue", "name": "Materiaal", "value": "{mat}" }},
        {{ "@type": "PropertyValue", "name": "Inductie geschikt", "value": "{ind}" }}
    ]
    }}
    </script>
    <style>
        .product-layout {{ max-width:1180px;margin:0 auto;padding:2rem 1.5rem; }}
        .product-breadcrumb {{ font-size:0.85rem;color:#888;margin-bottom:2.5rem; }}
        .product-breadcrumb a {{ color:#888;text-decoration:none; }} .product-breadcrumb a:hover {{ color:#D2691E; }}
        .product-hero {{ display:grid;grid-template-columns:minmax(260px,0.8fr) minmax(0,1.2fr);gap:3rem;align-items:start;margin-bottom:3.5rem; }}
        .product-gallery img {{ width:100%;max-height:460px;object-fit:contain;background:#faf7f2;border-radius:16px;padding:2rem; }}
        .product-summary h1 {{ font-size:clamp(1.6rem,3vw,2.4rem);line-height:1.15;margin-bottom:0.75rem;color:#111; }}
        .product-kicker {{ font-size:0.85rem;color:#888;text-transform:uppercase;letter-spacing:1px;margin-bottom:0.5rem; }}
        .product-rating {{ display:flex;align-items:center;gap:0.5rem;margin-bottom:1.25rem; }}
        .product-rating .stars {{ color:#ffd700;font-size:1.3rem; }}
        .product-rating a {{ color:#666;font-size:0.9rem;text-decoration:underline;text-underline-offset:2px; }}
        .product-intro {{ font-size:1.05rem;line-height:1.7;color:#555;margin-bottom:1.5rem;max-width:580px; }}
        .product-quick-pros {{ display:flex;flex-wrap:wrap;gap:0.5rem; }}
        .product-quick-pros span {{ font-size:0.85rem;color:#333;background:#f5f5f5;padding:0.4rem 0.75rem;border-radius:4px; }}
        .content-grid {{ display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:3rem;align-items:start; }}
        .product-content {{ display:flex;flex-direction:column;gap:2.5rem; }}
        .buy-box {{ position:sticky;top:90px;border:1px solid #e5e5e5;border-radius:12px;padding:1.75rem; }}
        .buy-box .price {{ font-size:2.2rem;font-weight:700;color:#D2691E;margin-bottom:1.25rem; }}
        .buy-box .cta {{ display:block;width:100%;text-align:center;background:linear-gradient(135deg,#D2691E,#8B4513);color:white;padding:1rem;text-decoration:none;border-radius:8px;font-size:1rem;font-weight:600;margin-bottom:1.25rem;transition:opacity 0.2s; }}
        .buy-box .cta:hover {{ opacity:0.9; }}
        .buy-box .trust {{ font-size:0.8rem;color:#666;line-height:1.8; }}
        .buy-box .trust span {{ display:block; }}
        .buy-box .specs {{ border-top:1px solid #eee;margin-top:1.25rem;padding-top:1.25rem; }}
        .buy-box .specs li {{ display:flex;justify-content:space-between;font-size:0.85rem;padding:0.4rem 0;color:#444; }}
        .buy-box .specs li span:first-child {{ font-weight:600; }}
        .section-title {{ font-size:1.2rem;font-weight:600;color:#111;margin-bottom:1rem; }}
        .description p {{ color:#444;line-height:1.8;font-size:0.95rem;margin-bottom:1rem; }}
        .similar-section {{ margin-top:3.5rem;border-top:1px solid #eee;padding-top:2.5rem; }}
        .similar-section h2 {{ font-size:1.2rem;font-weight:600;margin-bottom:1.5rem;color:#111; }}
        .similar-grid {{ display:grid;grid-template-columns:repeat(4,1fr);gap:1.25rem; }}
        .similar-card {{ text-decoration:none;color:inherit;border:1px solid #eee;border-radius:8px;padding:1rem;transition:box-shadow 0.2s; }}
        .similar-card:hover {{ box-shadow:0 4px 12px rgba(0,0,0,0.08); }}
        .similar-card img {{ width:100%;height:100px;object-fit:contain;margin-bottom:0.75rem; }}
        .similar-card h4 {{ font-size:0.8rem;line-height:1.4;margin-bottom:0.5rem;color:#333;font-weight:500;height:2.2rem;overflow:hidden; }}
        .similar-card .card-price {{ font-size:0.95rem;font-weight:700;color:#D2691E; }}
        @media(max-width:900px) {{
            .product-hero {{ grid-template-columns:1fr; }}
            .content-grid {{ grid-template-columns:1fr; }}
            .buy-box {{ position:static; }}
            .similar-grid {{ grid-template-columns:repeat(2,1fr); }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="../index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li><a href="../beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
                    <li><a href="../koopgids/index.html" class="nav-link">Koopgids</a></li>
                    <li><a href="../marques/index.html" class="nav-link">Merken</a></li>
                    <li><a href="../vergelijking/index.html" class="nav-link">Vergelijking</a></li>
                    <li><a href="../over-ons.html" class="nav-link">Over ons</a></li>
                    <li><a href="../boutique.html" class="nav-link" style="background:#D2691E;color:white;padding:0.5rem 1rem;border-radius:6px;font-weight:600;">Winkel</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <main>
    <div class="product-layout">
        <nav class="product-breadcrumb">
            <a href="../index.html">Home</a> / <a href="../boutique.html">Winkel</a> / <a href="../categories/{cat_page(ptype)}">{cat_label(ptype)}</a> / <strong>{h(p['name'][:50])}</strong>
        </nav>

        <div class="product-hero">
            <div class="product-gallery">
                <img src="{h(image)}" alt="{name}" onerror="this.src='../Images/bialetti-moka-express-1.jpg'" loading="eager">
            </div>
            <div class="product-summary">
                <p class="product-kicker">{h(kicker)}</p>
                <h1>{name}</h1>
                <div class="product-rating">
                    <span class="stars">{stars_html(p.get('rating', 4.5))}</span>
                    <a href="{h(affiliate)}" target="_blank" rel="sponsored noopener">Bekijk reviews op Bol.com</a>
                </div>
                <p class="product-intro">{h(intro)}</p>
                <div class="product-quick-pros">
                    {''.join(f'<span>{h(pr)}</span>' for pr in pros)}
                </div>
            </div>
        </div>

        <div class="content-grid">
            <div class="product-content">
                <section>
                    <h2 class="section-title">Productbeschrijving</h2>
                    <div class="description">
                        <p>{h(desc) if desc else f'{name} — een kwalitatieve keuze voor koffieliefhebbers. Dit model combineert functionaliteit met stijl en is direct leverbaar via Bol.com.'}</p>
                    </div>
                </section>

                <section>
                    <h2 class="section-title">Specificaties</h2>
                    <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:0.6rem 0;font-weight:600;color:#333;width:40%;">Merk</td><td style="padding:0.6rem 0;color:#555;">{brand}</td></tr>
                        {f'<tr style="border-bottom:1px solid #eee;"><td style="padding:0.6rem 0;font-weight:600;color:#333;">Model</td><td style="padding:0.6rem 0;color:#555;">{model}</td></tr>' if model else ''}
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:0.6rem 0;font-weight:600;color:#333;">Capaciteit</td><td style="padding:0.6rem 0;color:#555;">{cap_text}</td></tr>
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:0.6rem 0;font-weight:600;color:#333;">Materiaal</td><td style="padding:0.6rem 0;color:#555;">{mat}</td></tr>
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:0.6rem 0;font-weight:600;color:#333;">Inductie geschikt</td><td style="padding:0.6rem 0;color:#555;">{ind}</td></tr>
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:0.6rem 0;font-weight:600;color:#333;">Kookplaten</td><td style="padding:0.6rem 0;color:#555;">{kookplaten(p)}</td></tr>
                        {f'<tr style="border-bottom:1px solid #eee;"><td style="padding:0.6rem 0;font-weight:600;color:#333;">Kleur</td><td style="padding:0.6rem 0;color:#555;">{color}</td></tr>' if color else ''}
                        {f'<tr style="border-bottom:1px solid #eee;"><td style="padding:0.6rem 0;font-weight:600;color:#333;">EAN</td><td style="padding:0.6rem 0;color:#555;">{ean}</td></tr>' if ean else ''}
                    </table>
                </section>
            </div>

            <aside class="buy-box">
                <div class="price">{price_display}{price_old_html}</div>
                <a href="{h(affiliate)}" target="_blank" rel="sponsored" class="cta">Koop op Bol.com →</a>
                <div class="trust">
                    <span>✓ Gratis verzending</span>
                    <span>✓ Gratis retourneren binnen 30 dagen</span>
                    <span>✓ Snelle levering via Bol.com</span>
                    <span>✓ Veilig betalen</span>
                </div>
                <ul class="specs" style="list-style:none;padding:0;margin:0;">
                    <li><span>Merk</span><span>{brand}</span></li>
                    <li><span>Capaciteit</span><span>{cap_text}</span></li>
                    <li><span>Materiaal</span><span>{mat}</span></li>
                    <li><span>Inductie</span><span>{ind}</span></li>
                </ul>
            </aside>
        </div>

        <section class="similar-section">
            <h2>Vergelijkbare Producten</h2>
            <div class="similar-grid">
{similar_html}            </div>
        </section>
    </div>
    </main>

    <footer class="footer">
        <div class="container">
            <div style="padding:2rem 0;text-align:center;">
                <p style="color:#D1D5DB;font-size:0.85rem;">© 2025 Italiaanse Percolator. Alle rechten voorbehouden.</p>
                <p style="color:#999;font-size:0.8rem;margin-top:0.5rem;">Affiliate Kennisgeving: Als Bol.com partner verdienen wij aan kwalificerende aankopen.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    return page


def main():
    deliverable = [p for p in PRODUCTS if p.get('deliverable') and p.get('price', 0) > 0]
    print(f"Generating {len(deliverable)} product pages...")

    for i, p in enumerate(deliverable):
        page_html = generate_page(p, deliverable)
        out_file = OUT_DIR / f"{p['slug']}.html"
        out_file.write_text(page_html, encoding='utf-8')

        if (i + 1) % 200 == 0:
            print(f"  ...{i + 1} pages generated")

    print(f"\nDone: {len(deliverable)} product pages in /producten/")

    types = {}
    for p in deliverable:
        types[p['type']] = types.get(p['type'], 0) + 1
    for t, c in sorted(types.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")


if __name__ == '__main__':
    main()
