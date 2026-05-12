#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('/Users/marc/Desktop/italiaanse-percolator')
BRAND_LINKS = {
    'bialetti': ('Bialetti', '../marques/bialetti/'),
    'alessi': ('Alessi', '../marques/alessi/'),
    'grosche': ('Grosche', '../marques/grosche/'),
}

# 1. Navigation label and FAQ class normalization across HTML files.
for path in ROOT.glob('**/*.html'):
    if '.git' in path.parts:
        continue
    original = path.read_text(encoding='utf-8', errors='ignore')
    content = original.replace('>Guides<', '>Gidsen<')
    content = content.replace('class="nav-link dropdown-toggle active">Guides', 'class="nav-link dropdown-toggle active">Gidsen')
    content = content.replace('class="nav-link dropdown-toggle">Guides', 'class="nav-link dropdown-toggle">Gidsen')

    if 'Veelgestelde' in content or 'FAQ' in content:
        content = re.sub(r'(<section[^>]*>\s*<div class="container">\s*<div style="max-width: 850px; margin: 0 auto;">\s*<h2[^>]*>Veelgestelde[^<]*</h2>)', lambda m: m.group(1).replace('<section', '<section class="faq-section"', 1) if 'class=' not in m.group(1).split('>')[0] else m.group(1), content)
        content = re.sub(r'<div style="border: 1px solid #E2E8F0;[^>]*">\s*<button onclick="toggleFaq\((\d+)\)"', r'<div class="faq-item"><button class="faq-question" onclick="toggleFaq(\1)"', content)
        content = re.sub(r'<div id="faq-(\d+)" style="display: none; padding:[^\"]*">', r'<div id="faq-\1" class="faq-answer" style="display: none;">', content)
        content = re.sub(r'<div style="background: white; padding: 1\.5rem; ">\s*<h4([^>]*) onclick="toggleFAQ\(this\)"', r'<div class="faq-item"><h4 class="faq-question"\1 onclick="toggleFAQ(this)"', content)
        content = re.sub(r'<p style="color: #555; line-height: 1\.8; display: none; margin-top: 1rem; font-size: 0\.9rem;">', r'<p class="faq-answer" style="display: none;">', content)

    if content != original:
        path.write_text(content, encoding='utf-8')
        print(path.relative_to(ROOT))

# 2. Remove incoherent Kopje CTA sections on brand pages.
for path in (ROOT / 'marques').glob('**/*.html'):
    original = path.read_text(encoding='utf-8', errors='ignore')
    content = re.sub(
        r'\n\s*<!-- CTA Section -->\s*<section style="background: #f5f0ea; padding: 3rem 0 2\.5rem;">\s*<div class="container" style="max-width: 780px;">\s*<h1[^>]*>Kopje</h1>.*?</section>\s*',
        '\n',
        original,
        flags=re.S,
    )
    if content != original:
        path.write_text(content, encoding='utf-8')
        print(path.relative_to(ROOT))

# 3. Product internal links: one brand link when supported, and one Percolator category link.
for path in (ROOT / 'producten').glob('*.html'):
    original = path.read_text(encoding='utf-8', errors='ignore')
    content = re.sub(r'\n\s*<section class="product-internal-links">.*?</section>\s*', '\n', original, flags=re.S)

    lower = content.lower()
    brand_match = re.search(r'"brand"\s*:\s*\{[^}]*"name"\s*:\s*"([^"]+)"', content, flags=re.S)
    brand_raw = brand_match.group(1).strip() if brand_match else ''
    brand_key = ''
    for key in BRAND_LINKS:
        if key in brand_raw.lower() or key in path.name.lower():
            brand_key = key
            break

    links = ['<a href="../categories/percolators.html">Percolator</a>']
    if brand_key:
        brand_name, href = BRAND_LINKS[brand_key]
        links.insert(0, f'<a href="{href}">{brand_name}</a>')

    link_html = f'''
                <section class="product-internal-links">
                    <h2 class="section-title">Verder oriënteren</h2>
                    <p>Bekijk ook {' en '.join(links)} voor meer context rond dit model.</p>
                </section>
'''
    content = content.replace('            </div>\n\n            <aside class="buy-box">', link_html + '            </div>\n\n            <aside class="buy-box">', 1)

    if content != original:
        path.write_text(content, encoding='utf-8')
        print(path.relative_to(ROOT))
