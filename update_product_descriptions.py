#!/usr/bin/env python3
"""
Script pour mettre à jour les meta descriptions des produits depuis beschrijvingen.xlsx
"""

import pandas as pd
import re
from pathlib import Path
from urllib.parse import urlparse

def get_html_filename_from_url(url):
    """Convertit une URL en nom de fichier HTML"""
    # Ex: https://italiaanse-percolator.nl/producten/percolator-zwart.html -> producten/percolator-zwart.html
    parsed = urlparse(url)
    path = parsed.path  # /producten/percolator-zwart.html
    # Retirer le premier slash
    if path.startswith('/'):
        path = path[1:]
    return path

def update_description(html_file, new_description):
    """Met à jour la meta description dans un fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern pour trouver la meta description (format: <meta name="description" content="...">)
    pattern = r'<meta name="description" content="([^"]*)">'
    
    # Extraire la description actuelle
    match = re.search(pattern, content)
    if match:
        current_desc = match.group(1)
        # Nettoyer les espaces et sauts de ligne pour comparaison
        current_clean = ' '.join(current_desc.split())
        new_clean = ' '.join(new_description.split())
        
        if current_clean == new_clean:
            return False  # Déjà à jour
    
    # Remplacer la description
    content = re.sub(pattern, f'<meta name="description" content="{new_description}">', content)
    
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Lit le fichier Excel et met à jour les descriptions"""
    excel_path = '/Users/marc/Desktop/beschrijvingen.xlsx'
    
    # Lire le fichier Excel
    df = pd.read_excel(excel_path)
    print(f"Lu {len(df)} descriptions depuis {excel_path}")
    
    # Les colonnes semblent être: URL (index 0) et Description (index 1)
    # On utilise les colonnes par leur position
    urls = df.iloc[:, 0]  # Première colonne
    descriptions = df.iloc[:, 1]  # Deuxième colonne
    
    updated_count = 0
    not_found_count = 0
    
    for url, desc in zip(urls, descriptions):
        if pd.isna(url) or pd.isna(desc):
            continue
            
        url = url.strip()
        desc = desc.strip()
        
        # Convertir l'URL en chemin de fichier
        html_path = get_html_filename_from_url(url)
        full_path = Path(html_path)
        
        if full_path.exists():
            if update_description(full_path, desc):
                print(f"✓ {html_path}")
                updated_count += 1
            else:
                print(f"✗ {html_path} (pas de changement)")
        else:
            print(f"✗ {html_path} (non trouvé)")
            not_found_count += 1
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour, {not_found_count} non trouvés.")

if __name__ == '__main__':
    main()
