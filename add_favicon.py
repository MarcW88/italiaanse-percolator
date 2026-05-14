#!/usr/bin/env python3
"""
Script pour ajouter les liens favicon complets à toutes les pages HTML
"""

import os
import re
from pathlib import Path

# Les liens favicon complets à ajouter
FAVICON_LINKS = '''<link href="favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="favicon-simple.svg" rel="icon" sizes="16x16" type="image/svg+xml"/>
<link href="favicon.svg" rel="apple-touch-icon" sizes="180x180"/>
<meta content="#7B5A43" name="theme-color"/>'''

# Pattern pour trouver le favicon existant (s'il y en a un)
FAVICON_PATTERN = r'<link href="favicon\.svg" rel="icon"[^>]*>'

def add_favicon_to_file(file_path):
    """Ajoute les liens favicon complets à un fichier HTML"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si les liens complets sont déjà présents
    if 'favicon-simple.svg' in content and 'apple-touch-icon' in content:
        print(f"✓ {file_path.name} - Déjà à jour")
        return False
    
    # Trouver la position du lien favicon existant ou après le lien stylesheet
    if '<link href="favicon.svg" rel="icon"' in content:
        # Remplacer le favicon existant par les liens complets
        content = re.sub(FAVICON_PATTERN, FAVICON_LINKS, content)
        print(f"✓ {file_path.name} - Remplacé favicon existant")
    else:
        # Ajouter après le lien stylesheet
        content = content.replace('<link href="style.css" rel="stylesheet"/>',
                                   '<link href="style.css" rel="stylesheet"/>\n' + FAVICON_LINKS)
        print(f"✓ {file_path.name} - Ajouté après stylesheet")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Traite tous les fichiers HTML dans le répertoire courant"""
    directory = Path('.')
    html_files = list(directory.glob('*.html'))
    
    print(f"Traitement de {len(html_files)} fichiers HTML...\n")
    
    updated_count = 0
    for html_file in html_files:
        if add_favicon_to_file(html_file):
            updated_count += 1
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
