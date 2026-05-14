#!/usr/bin/env python3
"""
Script pour vérifier quelles descriptions de product-beschrijving.xlsx n'ont pas été appliquées
"""

import pandas as pd
from pathlib import Path

def main():
    """Fonction principale"""
    # Lire le fichier Excel
    df = pd.read_excel('/Users/marc/Desktop/product-beschrijving.xlsx', header=None)
    
    print(f"Total de descriptions dans le fichier: {len(df)}")
    print(f"\nVérification des fichiers...\n")
    
    found_count = 0
    not_found_count = 0
    not_found_urls = []
    
    for index, row in df.iterrows():
        url = row[0]
        description = row[1]
        
        if pd.isna(url) or pd.isna(description):
            continue
        
        # Convertir l'URL en chemin de fichier
        if 'https://italiaanse-percolator.nl/' in url:
            relative_path = url.replace('https://italiaanse-percolator.nl/', '')
            html_file = Path(relative_path)
        else:
            print(f"✗ URL invalide: {url}")
            not_found_count += 1
            not_found_urls.append(url)
            continue
        
        if not html_file.exists():
            print(f"✗ Fichier non trouvé: {html_file}")
            not_found_count += 1
            not_found_urls.append(url)
        else:
            found_count += 1
    
    print(f"\n=== RÉSUMÉ ===")
    print(f"✓ Fichiers trouvés: {found_count}")
    print(f"✗ Fichiers non trouvés: {not_found_count}")
    
    if not_found_urls:
        print(f"\n=== URLs non trouvées (premières 20) ===")
        for url in not_found_urls[:20]:
            print(f"- {url}")
        
        if len(not_found_urls) > 20:
            print(f"\n... et {len(not_found_urls) - 20} autres")

if __name__ == '__main__':
    main()
