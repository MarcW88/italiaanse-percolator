#!/usr/bin/env python3
"""
Script pour mettre à jour les images dans les pages HTML individuelles des produits
"""

import json
import os
import re

# Chemins
JSON_FILE = 'all_products.json'
PRODUCTS_DIR = 'producten'

def update_product_page(html_path, product_image):
    """Met à jour l'image dans une page produit HTML"""
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Patterns possibles pour les images
    patterns = [
        # <img src="..." alt="..."
        r'<img\s+src="([^"]+)"\s+alt="[^"]*"',
        # <img src="..." class="..."
        r'<img\s+src="([^"]+)"\s+class="[^"]*"',
        # <img class="..." src="..."
        r'<img\s+class="[^"]*"\s+src="([^"]+)"',
        # Simple img src
        r'<img[^>]+src="([^"]+)"[^>]*>',
    ]
    
    # Chercher et remplacer les images produits (pas les icônes ni logos)
    updated = False
    for pattern in patterns:
        matches = re.finditer(pattern, html_content)
        for match in matches:
            current_image = match.group(1)
            # Ignorer les icônes, logos, et images externes
            if any(x in current_image.lower() for x in ['icon', 'logo', 'http', 'svg', 'favicon']):
                continue
            
            # Si c'est une image produit, la remplacer
            if 'images/' in current_image.lower() or 'bialetti' in current_image.lower():
                # Calculer le chemin relatif correct depuis producten/
                new_image = f"../{product_image}"
                html_content = html_content.replace(f'src="{current_image}"', f'src="{new_image}"')
                updated = True
                break
        
        if updated:
            break
    
    if updated:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return True
    
    return False

def main():
    # Lire le JSON
    print(f"📖 Lecture de {JSON_FILE}...")
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    print(f"✅ {len(products)} produits chargés")
    
    # Mettre à jour les pages HTML
    updated_count = 0
    not_found = []
    
    print(f"\n🔄 Mise à jour des pages HTML...")
    for product in products:
        slug = product['slug']
        image = product.get('image', '')
        
        html_path = os.path.join(PRODUCTS_DIR, f"{slug}.html")
        
        if os.path.exists(html_path):
            if update_product_page(html_path, image):
                print(f"  ✏️  {slug}.html")
                updated_count += 1
        else:
            not_found.append(slug)
    
    print(f"\n✅ {updated_count} pages HTML mises à jour!")
    
    if not_found:
        print(f"\n⚠️  {len(not_found)} pages HTML non trouvées:")
        for slug in not_found[:5]:
            print(f"   - {slug}.html")
        if len(not_found) > 5:
            print(f"   ... et {len(not_found) - 5} autres")
    
    print(f"\n✅ Terminé!")

if __name__ == '__main__':
    main()
