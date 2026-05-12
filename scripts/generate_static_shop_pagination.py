#!/usr/bin/env python3
from pathlib import Path
import json
import math
import html
from datetime import date

ROOT = Path('/Users/marc/Desktop/italiaanse-percolator')
PER_PAGE = 24
SITE = 'https://italiaanse-percolator.nl'

CATEGORY_CONFIG = {
    'percolators': {
        'title': 'Percolators kopen',
        'h1': 'Alle percolators',
        'description': 'Vergelijk klassieke Italiaanse percolators voor gas, elektrisch, keramisch en inductie.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur',
    },
    'elektrische-percolators': {
        'title': 'Elektrische percolators kopen',
        'h1': 'Elektrische percolators',
        'description': 'Vergelijk elektrische percolators en moka apparaten zonder kookplaat.',
        'filter': lambda p: p.get('type') == 'Cafetière électrique',
    },
    'accessoires': {
        'title': 'Percolator accessoires kopen',
        'h1': 'Percolator accessoires',
        'description': 'Onderdelen, filters, ringen en accessoires voor percolators en koffiezetters.',
        'filter': lambda p: p.get('type') == 'Accessoire',
    },
    'percolators-inductie': {
        'title': 'Inductie percolators kopen',
        'h1': 'Percolators voor inductie',
        'description': 'Vind percolators die geschikt zijn voor inductiekookplaten.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and p.get('inductie') == 'Oui',
    },
    'percolators-aluminium': {
        'title': 'Aluminium percolators kopen',
        'h1': 'Aluminium percolators',
        'description': 'Klassieke aluminium moka pots voor authentieke Italiaanse koffie.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and 'aluminium' in (p.get('materiaal') or '').lower(),
    },
    'percolators-rvs': {
        'title': 'RVS percolators kopen',
        'h1': 'RVS percolators',
        'description': 'Duurzame roestvrijstalen percolators, vaak geschikt voor inductie.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and any(x in (p.get('materiaal') or '').lower() for x in ['rvs', 'roestvrij', 'inox', 'acier']),
    },
    'percolators-1-2-kops': {
        'title': '1 en 2 kops percolators kopen',
        'h1': '1 en 2 kops percolators',
        'description': 'Compacte percolators voor één persoon of kleine espresso-momenten.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and str(p.get('capaciteit') or '').strip() in {'1', '2'},
    },
    'percolators-3-kops': {
        'title': '3 kops percolators kopen',
        'h1': '3 kops percolators',
        'description': 'Populaire 3-kops moka pots voor dagelijks gebruik.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and str(p.get('capaciteit') or '').strip() == '3',
    },
    'percolators-6-kops': {
        'title': '6 kops percolators kopen',
        'h1': '6 kops percolators',
        'description': '6-kops percolators voor gezinnen en meerdere espresso’s tegelijk.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and str(p.get('capaciteit') or '').strip() == '6',
    },
    'percolators-9-kops': {
        'title': '9 kops percolators kopen',
        'h1': '9 kops percolators',
        'description': 'Grote 9-kops percolators voor meerdere koffiedrinkers.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and str(p.get('capaciteit') or '').strip() == '9',
    },
    'inductie-adapters': {
        'title': 'Inductie adapters kopen',
        'h1': 'Inductie adapters',
        'description': 'Adapters voor het gebruiken van klassieke percolators op inductie.',
        'filter': lambda p: 'adapter' in (p.get('name') or '').lower() or 'inductie-adapter' in (p.get('description') or '').lower(),
    },
    'onderhoudssets': {
        'title': 'Onderhoudssets voor percolators',
        'h1': 'Onderhoudssets',
        'description': 'Rubberen ringen, filters en onderhoudssets voor moka pots.',
        'filter': lambda p: any(x in (p.get('name') or '').lower() for x in ['onderhoud', 'ringen', 'filterplaat', 'filterplaatje', 'rubber']),
    },
}

NAV_ROOT = '''    <nav class="navbar">
        <div class="container"><div class="nav-container">
            <a href="{prefix}index.html" class="nav-brand">Italiaanse Percolator</a>
            <ul class="nav-menu">
                <li><a href="{prefix}index.html" class="nav-link">Home</a></li>
                <li class="nav-item dropdown"><a href="{prefix}beste-italiaanse-percolators.html" class="nav-link dropdown-toggle">Gidsen</a>
                    <ul class="dropdown-menu"><li><a href="{prefix}beste-italiaanse-percolators.html" class="dropdown-link">Top 10</a></li><li><a href="{prefix}koopgids/index.html" class="dropdown-link">Koopgids</a></li><li><a href="{prefix}alle-reviews.html" class="dropdown-link">Reviews</a></li><li><a href="{prefix}vergelijking/index.html" class="dropdown-link">Vergelijking</a></li></ul>
                </li>
                <li><a href="{prefix}marques/index.html" class="nav-link">Merken</a></li>
                <li class="nav-item dropdown"><a href="{prefix}boutique.html" class="nav-link dropdown-toggle active">Shop</a>
                    <ul class="dropdown-menu"><li><a href="{prefix}boutique.html" class="dropdown-link">Alle modellen</a></li><li><a href="{prefix}categories/percolators.html" class="dropdown-link">Percolators</a></li><li><a href="{prefix}categories/elektrische-percolators.html" class="dropdown-link">Elektrisch</a></li><li><a href="{prefix}categories/accessoires.html" class="dropdown-link">Accessoires</a></li></ul>
                </li>
            </ul>
        </div></div>
    </nav>'''

FOOTER = '''    <footer class="footer"><div class="container">
        <div class="footer-content"><div><p style="font-family: var(--font-serif); font-size: 1.2rem; color: white; margin-bottom: 1rem;">Italiaanse Percolator</p><p style="color: #999; font-size: 0.85rem; line-height: 1.7; margin-bottom: 0;">Onafhankelijke gids voor Italiaanse moka-percolators.</p></div><div><h4>Gidsen</h4><a href="{prefix}beste-italiaanse-percolators.html">Top 10 percolators</a><br><a href="{prefix}koopgids/index.html">Koopgids</a></div><div><h4>Merken</h4><a href="{prefix}marques/bialetti/">Bialetti</a><br><a href="{prefix}marques/alessi/">Alessi</a></div><div><h4>Info</h4><a href="{prefix}over-ons.html">Over ons</a><br><a href="{prefix}contact.html">Contact</a></div></div>
        <div class="footer-bottom">© 2025 Italiaanse Percolator. Alle rechten voorbehouden.</div>
    </div></footer>'''


def fmt_price(p):
    price = p.get('price')
    return f"€{price:.2f}".replace('.', ',') if isinstance(price, (int, float)) else ''


def card(p, prefix):
    badges = []
    if p.get('inductie') == 'Oui':
        badges.append('Inductie')
    if p.get('capaciteit'):
        badges.append(f"{p['capaciteit']} kops")
    if p.get('materiaal'):
        badges.append(p['materiaal'])
    badge_html = ''.join(f'<span style="font-size:0.72rem;color:var(--text-light);border:1px solid var(--border);padding:0.2rem 0.5rem;border-radius:0.5rem;">{html.escape(str(b))}</span>' for b in badges[:3])
    name = html.escape(p.get('name') or '')
    img = html.escape(p.get('image') or f'{prefix}Images/placeholder-product.jpg')
    slug = html.escape(p.get('slug') or '')
    aff = html.escape(p.get('affiliate_url') or '#')
    rating = p.get('rating') or ''
    rating_html = f'<span style="font-size:0.78rem;color:var(--text-light);">{rating}/5</span>' if rating else ''
    return f'''            <div style="border:1px solid var(--border);overflow:hidden;background:white;transition:border-color 0.2s;border-radius:0.5rem;display:flex;flex-direction:column;height:100%;" onmouseover="this.style.borderColor='var(--coffee)'" onmouseout="this.style.borderColor='var(--border)'">
                <div style="background:#fafafa;padding:1rem;text-align:center;"><img src="{img}" alt="{name}" loading="lazy" style="height:160px;width:100%;object-fit:contain;" onerror="this.src='{prefix}Images/placeholder-product.jpg'"></div>
                <div style="padding:1rem;">
                    <div style="display:flex;gap:0.35rem;flex-wrap:wrap;margin-bottom:0.5rem;">{badge_html}</div>
                    <h3 style="font-size:0.88rem;font-weight:600;line-height:1.35;margin-bottom:0.5rem;height:2.4rem;overflow:hidden;">{name}</h3>
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
                        <span style="font-size:1.1rem;font-weight:700;">{fmt_price(p)}</span>
                        {rating_html}
                    </div>
                    <a href="{aff}" target="_blank" rel="sponsored" style="display:block;text-align:center;padding:0.55rem;background:var(--coffee);color:white;text-decoration:none;border-radius:0.3rem;font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Bekijk op Bol.com</a>
                    <a href="{prefix}producten/{slug}.html" style="display:block;text-align:center;padding:0.45rem;border:1px solid var(--border);color:var(--text-dim);text-decoration:none;border-radius:0.3rem;font-size:0.78rem;">Details</a>
                </div>
            </div>'''


def page_url(kind, slug, page):
    if kind == 'boutique':
        return 'boutique.html' if page == 1 else f'boutique/page/{page}.html'
    return f'categories/{slug}.html' if page == 1 else f'categories/{slug}/page/{page}.html'


def local_path(kind, slug, page):
    return ROOT / page_url(kind, slug, page)


def pagination(kind, slug, current, total, prefix):
    if total <= 1:
        return ''
    links = []
    if current > 1:
        href = prefix + page_url(kind, slug, current - 1)
        links.append(f'<a href="{href}" class="pagination-link">Vorige</a>')
    start = max(1, current - 2)
    end = min(total, current + 2)
    if start > 1:
        links.append(f'<a href="{prefix + page_url(kind, slug, 1)}" class="pagination-link">1</a>')
        if start > 2:
            links.append('<span class="pagination-gap">…</span>')
    for n in range(start, end + 1):
        href = prefix + page_url(kind, slug, n)
        cls = 'pagination-link active' if n == current else 'pagination-link'
        links.append(f'<a href="{href}" class="{cls}">{n}</a>')
    if end < total:
        if end < total - 1:
            links.append('<span class="pagination-gap">…</span>')
        links.append(f'<a href="{prefix + page_url(kind, slug, total)}" class="pagination-link">{total}</a>')
    if current < total:
        links.append(f'<a href="{prefix + page_url(kind, slug, current + 1)}" class="pagination-link">Volgende</a>')
    return '<nav class="shop-pagination" aria-label="Paginering">' + ''.join(links) + '</nav>'


def render(kind, slug, products, page, total_pages, title, h1, description):
    prefix = '' if kind == 'boutique' and page == 1 else '../../' if kind == 'boutique' else '../' if page == 1 else '../../../'
    url_path = page_url(kind, slug, page)
    canonical = f'{SITE}/{url_path}'
    title_full = title if page == 1 else f'{title} - pagina {page}'
    meta = description if page == 1 else f'{description} Pagina {page} van {total_pages}.'
    start = (page - 1) * PER_PAGE
    items = products[start:start + PER_PAGE]
    grid = '\n'.join(card(p, prefix) for p in items)
    cats_prefix = prefix + 'categories/'
    category_links = (
        f'<a href="{cats_prefix}percolators.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Percolators</a>'
        f'<a href="{cats_prefix}elektrische-percolators.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Elektrisch</a>'
        f'<a href="{cats_prefix}accessoires.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Accessoires</a>'
        f'<a href="{cats_prefix}percolators-inductie.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Inductie</a>'
        f'<a href="{cats_prefix}percolators-aluminium.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Aluminium</a>'
        f'<a href="{cats_prefix}percolators-rvs.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">RVS</a>'
    )
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title_full)} | Italiaanse Percolator</title>
    <meta name="description" content="{html.escape(meta)}">
    <link rel="stylesheet" href="{prefix}style.css">
    <link rel="canonical" href="{canonical}">
    {'<link rel="prev" href="' + SITE + '/' + page_url(kind, slug, page - 1) + '">' if page > 1 else ''}
    {'<link rel="next" href="' + SITE + '/' + page_url(kind, slug, page + 1) + '">' if page < total_pages else ''}
    <link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg">
</head>
<body>
{NAV_ROOT.format(prefix=prefix)}
    <section style="background:#f5f0ea;padding:3rem 0 2.5rem;"><div class="container" style="max-width:780px;">
        <p style="font-size:0.78rem;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.75rem;"><a href="{prefix}index.html" style="color:var(--text-light);text-decoration:none;">Home</a> / Shop</p>
        <h1 style="font-family:var(--font-serif);font-size:clamp(1.8rem,3vw,2.4rem);font-weight:400;margin-bottom:0.75rem;">{html.escape(h1)}{f' - pagina {page}' if page > 1 else ''}</h1>
        <p style="color:var(--text-dim);font-size:1rem;max-width:540px;">{html.escape(description)} {len(products)} producten gevonden.</p>
    </div></section>
    <div style="border-bottom:1px solid var(--border);padding:1rem 0;"><div class="container" style="display:flex;gap:1.5rem;flex-wrap:wrap;font-size:0.85rem;">
        {category_links}
    </div></div>
    <main class="container" style="padding:2.5rem 0;">
        <p style="color:var(--text-dim);margin-bottom:1.5rem;">Pagina {page} van {total_pages} · producten {start + 1}-{min(start + PER_PAGE, len(products))} van {len(products)}</p>
        <div class="shop-product-grid">
{grid}
        </div>
        {pagination(kind, slug, page, total_pages, prefix)}
    </main>
{FOOTER.format(prefix=prefix)}
</body>
</html>'''


def write_pages(kind, slug, products, title, h1, description):
    total = max(1, math.ceil(len(products) / PER_PAGE))
    urls = []
    for page in range(1, total + 1):
        path = local_path(kind, slug, page)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(kind, slug, products, page, total, title, h1, description), encoding='utf-8')
        urls.append(page_url(kind, slug, page))
    return urls


def main():
    products = json.loads((ROOT / 'all_products.json').read_text(encoding='utf-8'))
    products = sorted(products, key=lambda p: (p.get('type') or '', p.get('brand') or '', p.get('name') or ''))
    urls = []
    urls += write_pages('boutique', '', products, 'Alle modellen vergelijken', 'Alle modellen vergeleken', 'Bekijk Italiaanse percolators, elektrische koffiezetters en accessoires met eigen SEO-pagina per paginastap.')
    for slug, cfg in CATEGORY_CONFIG.items():
        items = [p for p in products if cfg['filter'](p)]
        urls += write_pages('category', slug, items, cfg['title'], cfg['h1'], cfg['description'])
    today = date.today().isoformat()
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f'  <url><loc>{SITE}/{u}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>')
    sitemap.append('</urlset>')
    (ROOT / 'sitemap-boutique.xml').write_text('\n'.join(sitemap) + '\n', encoding='utf-8')
    print('Generated URLs:', len(urls))
    print('Boutique pages:', math.ceil(len(products) / PER_PAGE))

if __name__ == '__main__':
    main()
