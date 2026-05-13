#!/usr/bin/env python3
"""Inject 2-column sidebar layout into all review pages."""
from bs4 import BeautifulSoup
import glob, os

REVIEW_PAGES = [
    ("bialetti-moka-review.html",           "Bialetti Moka Express"),
    ("bialetti-fiammetta-review.html",       "Bialetti Fiammetta"),
    ("bialetti-venus-review.html",           "Bialetti Venus"),
    ("bialetti-brikka-review.html",          "Bialetti Brikka"),
    ("bialetti-alpina-review.html",          "Bialetti Alpina"),
    ("bialetti-musa-review.html",            "Bialetti Musa"),
    ("bialetti-dama-review.html",            "Bialetti Dama"),
    ("bialetti-mini-express-review.html",    "Bialetti Mini Express"),
    ("bialetti-moka-timer-review.html",      "Bialetti Moka Timer"),
    ("alessi-9090-review.html",              "Alessi 9090"),
    ("alessi-pulcina-review.html",           "Alessi Pulcina"),
    ("alessi-la-conica-review.html",         "Alessi La Conica"),
    ("alessi-moka-review.html",              "Alessi Moka"),
    ("stelton-collar-review.html",           "Stelton Collar"),
    ("grosche-milano-review.html",           "Grosche Milano"),
    ("giannini-giannina-review.html",        "Giannini Giannina"),
    ("cilio-classico-electric-review.html",  "Cilio Classico Electric"),
    ("cloer-5928-review.html",               "Cloer 5928"),
    ("delonghi-alicia-review.html",          "De'Longhi Alicia"),
    ("rommelsbacher-eko366-review.html",     "Rommelsbacher EKO366"),
]

def get_product_image(soup):
    img = soup.find(class_='product-image')
    if img and img.get('src'):
        return img['src']
    stage = soup.find(class_='product-stage')
    if stage:
        img = stage.find('img')
        if img and img.get('src'):
            return img['src']
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 's-bol.com' in src or 'media.bol.com' in src:
            return src
    return ''

def get_affiliate_link(soup):
    cta = soup.find(class_='review-cta')
    if cta:
        link = cta.find('a')
        if link and link.get('href'):
            return link['href']
    actions = soup.find(class_='hero-actions')
    if actions:
        link = actions.find('a')
        if link and link.get('href'):
            return link['href']
    for link in soup.find_all('a', rel=True):
        if 'sponsored' in link.get('rel', []):
            return link.get('href', '#')
    return '#'

def process(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    if soup.find(class_='review-layout'):
        print(f'  Skip {filename} (already done)')
        return

    h1 = soup.find('h1')
    product_name = h1.get_text(strip=True) if h1 else ''
    img_src  = get_product_image(soup)
    affil    = get_affiliate_link(soup)

    # Build related links (max 8, skip current page)
    links_html = ''
    count = 0
    for href, name in REVIEW_PAGES:
        if href == filename or count >= 8:
            continue
        links_html += f'<li><a href="{href}">{name}</a></li>\n'
        count += 1

    img_tag = (f'<img class="sidebar-product-image" src="{img_src}" '
               f'alt="{product_name}" loading="lazy">') if img_src else ''

    sidebar_html = f"""<aside class="review-sidebar">
<div class="sidebar-box">
<div class="sidebar-box-header">Aanbevolen</div>
{img_tag}
<div class="sidebar-product-body">
<p class="sidebar-product-name">{product_name}</p>
<a class="btn btn-primary btn-block" href="{affil}" rel="sponsored" target="_blank">Bekijk prijs op Bol.com →</a>
</div>
</div>
<div class="sidebar-box">
<div class="sidebar-box-header">Meer reviews</div>
<ul class="sidebar-links-list">
{links_html}</ul>
</div>
</aside>"""

    sidebar_tag = BeautifulSoup(sidebar_html, 'html.parser').find('aside')

    sections = soup.find_all('section', class_='section-sm')
    if not sections:
        print(f'  No sections in {filename}')
        return

    # Wrap sections in review-layout > review-main
    review_layout = soup.new_tag('div', **{'class': 'review-layout'})
    review_main   = soup.new_tag('div', **{'class': 'review-main'})

    sections[0].insert_before(review_layout)
    review_layout.append(review_main)

    for section in sections:
        section.extract()
        review_main.append(section)

    review_layout.append(sidebar_tag)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f'  OK  {filename}')

base = '/Users/marc/Desktop/italiaanse-percolator'
for fp in sorted(glob.glob(f'{base}/*-review.html')):
    process(fp)
print('Done.')
