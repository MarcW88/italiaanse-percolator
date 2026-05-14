#!/usr/bin/env python3
"""
Script pour vérifier quelles descriptions sont réellement différentes dans les fichiers
"""

import pandas as pd
import re
from pathlib import Path

def get_current_description(html_file):
    """Récupère la description actuelle du fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern pour trouver la section Productbeschrijving
    pattern = r'<h2 class="section-title">Productbeschrijving</h2>\s*<div class="description">\s*<p>(.*?)</p>\s*</div>'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    return None

def main():
    """Fonction principale"""
    df = pd.read_excel('/Users/marc/Desktop/product-beschrijving.xlsx', header=None)
    
    print(f"Total de descriptions dans le fichier: {len(df)}")
    print(f"\nVérification des descriptions dans les fichiers...\n")
    
    already_updated = 0
    needs_update = 0
    no_description = 0
    needs_update_urls = []
    
    for index, row in df.iterrows():
        url = row[0]
        new_description = row[1]
        
        if pd.isna(url) or pd.isna(new_description):
            continue
        
        # Convertir l'URL en chemin de fichier
        if 'https://italiaanse-percolator.nl/' in url:
            relative_path = url.replace('https://italiaanse-percolator.nl/', '')
            html_file = Path(relative_path)
        else:
            continue
        
        if not html_file.exists():
            continue
        
        current_desc = get_current_description(html_file)
        
        if current_desc is None:
            print(f"✗ Pas de description trouvée: {html_file.name}")
            no_description += 1
            needs_update_urls.append(url)
        else:
            # Comparer les descriptions (nettoyées)
            current_clean = ' '.join(current_desc.split())
            new_clean = ' '.join(new_description.split())
            
            if current_clean == new_clean:
                already_updated += 1
            else:
                print(f"✗ Description différente: {html_file.name}")
                needs_update += 1
                needs_update_urls.append(url)
    
    print(f"\n=== RÉSUMÉ ===")
    print(f"✓ Déjà à jour: {already_updated}")
    print(f"✗ Besoin de mise à jour: {needs_update}")
    print(f"✗ Pas de description trouvée: {no_description}")
    
    if needs_update_urls:
        print(f"\n=== URLs qui ont besoin d'une mise à jour (premières 10) ===")
        for url in needs_update_urls[:10]:
            print(f"- {url}")

if __name__ == '__main__':
    main()
