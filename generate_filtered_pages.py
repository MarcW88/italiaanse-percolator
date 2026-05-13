#!/usr/bin/env python3
"""Generate filtered product pages with query parameters and canonicals to main boutique.html"""
import json
import re
from pathlib import Path
import urllib.parse

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
                    <a href="{affiliate_url}" target="_blank" rel="sponsored" style="display:block;text-align:center;padding:0.55rem;background:var(--coffee);color:white;text-decoration:none;border-radius:0.3rem;font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Bekijk op Bol.com</a>
                    <a href="producten/{slug}.html" style="display:block;text-align:center;padding:0.45rem;border:1px solid var(--border);color:var(--text-dim);text-decoration:none;border-radius:0.3rem;font-size:0.78rem;">Details</a>
                </div>
            </div>'''

def filter_products(products, filter_type, filter_value):
    """Filter products based on filter type and value"""
    filtered = []
    
    if filter_type == 'type':
        filtered = [p for p in products if p.get('type') == filter_value]
    elif filter_type == 'inductie':
        if filter_value == 'oui':
            filtered = [p for p in products if p.get('inductie') == 'Oui']
        else:
            filtered = [p for p in products if p.get('inductie') == 'Non']
    elif filter_type == 'materiaal':
        filtered = [p for p in products if p.get('materiaal') == filter_value]
    elif filter_type == 'capaciteit':
        filtered = [p for p in products if p.get('capaciteit') == filter_value]
    elif filter_type == 'brand':
        filtered = [p for p in products if p.get('brand') == filter_value]
    
    return filtered

def main():
    # Load products
    with open('all_products.json', 'r', encoding='utf-8') as f:
        all_products = json.load(f)
    
    # Read boutique.html template
    with open('boutique.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Define filters
    filters = [
        ('type', 'Accessoire'),
        ('type', 'Cafetière percolateur'),
        ('type', 'Cafetière électrique'),
        ('inductie', 'oui'),
        ('inductie', 'non'),
        ('materiaal', 'Aluminium'),
        ('materiaal', 'RVS'),
        ('materiaal', 'Roestvrij staal'),
    ]
    
    per_page = 24
    generated_count = 0
    
    for filter_type, filter_value in filters:
        # Filter products
        filtered_products = filter_products(all_products, filter_type, filter_value)
        
        if not filtered_products:
            continue
        
        # Calculate pagination
        total_pages = len(filtered_products) // per_page + (1 if len(filtered_products) % per_page else 0)
        
        # Generate pages
        for page in range(1, total_pages + 1):
            start = (page - 1) * per_page
            items = filtered_products[start:start + per_page]
            
            # Generate product cards HTML
            cards_html = ''.join([generate_product_card(p) for p in items])
            
            # Replace the products-grid content
            pattern = r'<div id="products-grid" class="shop-product-grid">.*?</div>'
            replacement = f'<div id="products-grid" class="shop-product-grid">{cards_html}</div>'
            
            filtered_html = re.sub(pattern, replacement, template, flags=re.DOTALL)
            
            # Update page info
            page_info_pattern = r'<p id="page-info" style="color:var\(--text-dim\);margin-bottom:1\.5rem;">.*?</p>'
            page_info_replacement = f'<p id="page-info" style="color:var(--text-dim);margin-bottom:1.5rem;">Pagina {page} van {total_pages} · producten {start + 1}-{min(start + per_page, len(filtered_products))} van {len(filtered_products)} (filter: {filter_type}={filter_value})</p>'
            
            filtered_html = re.sub(page_info_pattern, page_info_replacement, filtered_html)
            
            # Update title
            filter_display = filter_value.replace('_', ' ').title()
            title_pattern = r'<title>.*?</title>'
            title_replacement = f'<title>{filter_display} - pagina {page} | Italiaanse Percolator</title>'
            filtered_html = re.sub(title_pattern, title_replacement, filtered_html)
            
            # Update canonical - always point to main boutique.html
            canonical_pattern = r'<link rel="canonical" href=".*?">'
            canonical_replacement = '<link rel="canonical" href="https://italiaanse-percolator.nl/boutique.html">'
            filtered_html = re.sub(canonical_pattern, canonical_replacement, filtered_html)
            
            # Update meta description
            meta_desc_pattern = r'<meta name="description" content=".*?">'
            meta_desc_replacement = f'<meta name="description" content="Bekijk {filter_display} - pagina {page} van {total_pages}. {len(filtered_products)} {filter_value} producten gevonden.">'
            filtered_html = re.sub(meta_desc_pattern, meta_desc_replacement, filtered_html)
            
            # Generate filename
            query_param = f"{filter_type}={filter_value.lower()}"
            if page == 1:
                filename = f"boutique-{filter_type}-{filter_value.lower()}.html"
            else:
                filename = f"boutique-{filter_type}-{filter_value.lower()}-page-{page}.html"
            
            # Save file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(filtered_html)
            
            print(f"Generated {filename} with {len(items)} products")
            generated_count += 1
    
    print(f"\nDone: Generated {generated_count} filtered pages")

if __name__ == '__main__':
    main()
