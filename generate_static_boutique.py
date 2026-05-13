#!/usr/bin/env python3
"""Generate static boutique.html with products pre-rendered in HTML source"""
import json
from pathlib import Path

def generate_product_card(product):
    """Generate HTML for a single product card"""
    badges = []
    if product.get('inductie') == 'Oui':
        badges.append('Inductie')
    if product.get('capaciteit'):
        badges.append(f"{product['capaciteit']} kops")
    if product.get('materiaal'):
        badges.append(product['materiaal'])
    
    badge_html = ''.join([
        f'<span style="font-size:0.72rem;color:var(--text-light);border:1px solid var(--border);padding:0.2rem 0.5rem;border-radius:0.5rem;">{badge}</span>'
        for badge in badges
    ])
    
    price = f"€{product['price']:.2f}" if product.get('price') else ''
    rating = f"{product['rating']}/5" if product.get('rating') else ''
    rating_html = f'<span style="font-size:0.78rem;color:var(--text-light);">{rating}</span>' if rating else ''
    
    image = product.get('image') or 'Images/placeholder-product.jpg'
    name = product.get('name', '')
    slug = product.get('slug', '')
    affiliate_url = product.get('affiliate_url') or '#'
    
    return f'''<div style="border:1px solid var(--border);overflow:hidden;background:white;transition:border-color 0.2s;border-radius:0.5rem;display:flex;flex-direction:column;height:100%;" onmouseover="this.style.borderColor='var(--coffee)'" onmouseout="this.style.borderColor='var(--border)'">
                <div style="background:#fafafa;padding:1rem;text-align:center;"><img src="{image}" alt="{name}" loading="lazy" style="height:160px;width:100%;object-fit:contain;" onerror="this.src='Images/placeholder-product.jpg'"></div>
                <div style="padding:1rem;">
                    <div style="display:flex;gap:0.35rem;flex-wrap:wrap;margin-bottom:0.5rem;">{badge_html}</div>
                    <h3 style="font-size:0.88rem;font-weight:600;line-height:1.35;margin-bottom:0.5rem;height:2.4rem;overflow:hidden;">{name}</h3>
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
                        <span style="font-size:1.1rem;font-weight:700;">{price}</span>
                        {rating_html}
                    </div>
                    <a href="{affiliate_url}" target="_blank" rel="sponsored" style="display:block;text-align:center;padding:0.55rem;background:var(--coffee);color:white;text-decoration:none;border-radius:0.3rem;font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Koop product</a>
                    <span style="display:block;text-align:center;font-size:0.72rem;color:var(--text-light);">via Bol.com</span>
                    <a href="producten/{slug}.html" style="display:block;text-align:center;padding:0.45rem;border:1px solid var(--border);color:var(--text-dim);text-decoration:none;border-radius:0.3rem;font-size:0.78rem;">Details</a>
                </div>
            </div>'''

def generate_pagination(page, total_pages):
    """Generate pagination HTML"""
    html = '<div id="pagination">'
    
    if page > 1:
        prev_page = page - 1
        html += f'<a href="boutique-page-{prev_page}.html" class="pagination-link">Vorige</a>'
    
    start_page = max(1, page - 2)
    end_page = min(total_pages, page + 2)
    
    for i in range(start_page, end_page + 1):
        active = ' active' if i == page else ''
        if i == 1:
            html += f'<a href="boutique.html" class="pagination-link{active}">{i}</a>'
        else:
            html += f'<a href="boutique-page-{i}.html" class="pagination-link{active}">{i}</a>'
    
    if page < total_pages:
        next_page = page + 1
        html += f'<a href="boutique-page-{next_page}.html" class="pagination-link">Volgende</a>'
    
    html += '</div>'
    return html

def main():
    # Load products
    with open('all_products.json', 'r', encoding='utf-8') as f:
        all_products = json.load(f)
    
    # Read current boutique.html template
    with open('boutique.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Generate all pages
    per_page = 24
    total_pages = len(all_products) // per_page + (1 if len(all_products) % per_page else 0)
    
    import re
    
    for page in range(1, total_pages + 1):
        start = (page - 1) * per_page
        items = all_products[start:start + per_page]
        
        # Generate product cards HTML
        cards_html = ''.join([generate_product_card(p) for p in items])
        
        # Replace the products-grid content
        pattern = r'<div id="products-grid" class="shop-product-grid"></div>'
        replacement = f'<div id="products-grid" class="shop-product-grid">{cards_html}</div>'
        
        static_html = re.sub(pattern, replacement, template)
        
        # Update page info
        page_info_pattern = r'<p id="page-info" style="color:var\(--text-dim\);margin-bottom:1\.5rem;">Pagina laden\.\.\.</p>'
        page_info_replacement = f'<p id="page-info" style="color:var(--text-dim);margin-bottom:1.5rem;">Pagina {page} van {total_pages} · producten {start + 1}-{min(start + per_page, len(all_products))} van {len(all_products)}</p>'
        
        static_html = re.sub(page_info_pattern, page_info_replacement, static_html)
        
        # Update title
        title_pattern = r'<title>.*?</title>'
        title_replacement = f'<title>Alle modellen vergelijken - pagina {page} | Italiaanse Percolator</title>'
        static_html = re.sub(title_pattern, title_replacement, static_html)
        
        # Update canonical
        canonical_pattern = r'<link rel="canonical" href=".*?">'
        if page == 1:
            canonical_replacement = '<link rel="canonical" href="https://italiaanse-percolator.nl/boutique.html">'
        else:
            canonical_replacement = f'<link rel="canonical" href="https://italiaanse-percolator.nl/boutique-page-{page}.html">'
        static_html = re.sub(canonical_pattern, canonical_replacement, static_html)
        
        # Replace pagination
        pagination_pattern = r'<div id="pagination"></div>'
        pagination_replacement = generate_pagination(page, total_pages)
        static_html = re.sub(pagination_pattern, pagination_replacement, static_html)
        
        # Save file
        if page == 1:
            filename = 'boutique.html'
        else:
            filename = f'boutique-page-{page}.html'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(static_html)
        
        print(f"Generated {filename} with {len(items)} products")
    
    print(f"\nDone: Generated {total_pages} pages")
    print(f"Total products: {len(all_products)}")

if __name__ == '__main__':
    main()
