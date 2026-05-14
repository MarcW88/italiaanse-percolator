#!/usr/bin/env python3
"""
Script pour mettre à jour la section Productbeschrijving dans les fichiers HTML produits
avec les descriptions du fichier product-beschrijving.xlsx
"""

import pandas as pd
import re
from pathlib import Path

def update_product_description(html_file, new_description):
    """Met à jour la section Productbeschrijving dans un fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern pour trouver la section Productbeschrijving
    pattern = r'<h2 class="section-title">Productbeschrijving</h2>\s*<div class="description">\s*<p>.*?</p>\s*</div>'
    match = re.search(pattern, content, re.DOTALL)
    
    # Remplacer la description
    new_section = f'''<h2 class="section-title">Productbeschrijving</h2>
                    <div class="description">
                        <p>{new_description}</p>
                    </div>'''
    
    content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Fonction principale"""
    # Lire le fichier Excel
    df = pd.read_excel('/Users/marc/Desktop/product-beschrijving.xlsx', header=None)
    
    print(f"Total de descriptions dans le fichier: {len(df)}")
    
    updated_count = 0
    not_found_count = 0
    
    for index, row in df.iterrows():
        url = row[0]
        description = row[1]
        
        if pd.isna(url) or pd.isna(description):
            continue
        
        # Convertir l'URL en chemin de fichier
        # URL: https://italiaanse-percolator.nl/producten/...
        # Path: producten/...
        if 'https://italiaanse-percolator.nl/' in url:
            relative_path = url.replace('https://italiaanse-percolator.nl/', '')
            html_file = Path(relative_path)
        else:
            print(f"✗ URL invalide: {url}")
            not_found_count += 1
            continue
        
        if not html_file.exists():
            print(f"✗ Fichier non trouvé: {html_file}")
            not_found_count += 1
            continue
        
        # Mettre à jour la description
        if update_product_description(html_file, description):
            print(f"✓ {html_file.name} - Description mise à jour")
            updated_count += 1
        else:
            print(f"- {html_file.name} - Déjà à jour")
    
    print(f"\nTerminé!")
    print(f"✓ Fichiers mis à jour: {updated_count}")
    print(f"✗ Fichiers non trouvés: {not_found_count}")

if __name__ == '__main__':
    main()
