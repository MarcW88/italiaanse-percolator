#!/usr/bin/env python3
"""
Script pour mettre à jour les boîtes auteur avec les photos réelles
"""

import os
import re
from pathlib import Path

def update_author_photos(file_path):
    """Met à jour les boîtes auteur avec les photos réelles"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remplacer Marco
    content = re.sub(
        r'<div class="author-avatar" style="background:#6f4e37;">M</div>',
        '<div class="author-avatar"><img src="marco.jpeg" alt="Marco Rossi"/></div>',
        content
    )
    
    # Remplacer Lisa
    content = re.sub(
        r'<div class="author-avatar" style="background:#2d6a4f;">L</div>',
        '<div class="author-avatar"><img src="lisa.jpeg" alt="Lisa De Vries"/></div>',
        content
    )
    
    # Remplacer D (autre couleur)
    content = re.sub(
        r'<div class="author-avatar" style="background:#[0-9a-fA-F]{6};">D</div>',
        '<div class="author-avatar"><img src="lisa.jpeg" alt="Lisa De Vries"/></div>',
        content
    )
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path.name} - Mis à jour")
        return True
    else:
        print(f"✓ {file_path.name} - Déjà à jour ou pas de boîte auteur")
        return False

def main():
    """Traite tous les fichiers HTML dans le répertoire courant et sous-répertoires"""
    directory = Path('.')
    html_files = list(directory.glob('**/*.html'))
    
    print(f"Traitement de {len(html_files)} fichiers HTML...\n")
    
    updated_count = 0
    for html_file in html_files:
        if update_author_photos(html_file):
            updated_count += 1
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
