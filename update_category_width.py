#!/usr/bin/env python3
"""
Script pour mettre à jour la largeur du texte sur les pages de catégories
Supprime les restrictions max-width pour correspondre à la home du winkel
"""

import os
import re
from pathlib import Path

def update_category_width(file_path):
    """Met à jour la largeur du texte dans un fichier de catégorie"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Supprimer max-width:780px du hero section
    content = content.replace('style="max-width:780px;"', '')
    
    # Supprimer max-width:800px du intro section
    content = content.replace('style="max-width:800px;"', '')
    
    # Supprimer max-width:540px du description
    content = content.replace('max-width:540px;', '')
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path.name} - Mis à jour")
        return True
    else:
        print(f"✓ {file_path.name} - Déjà à jour")
        return False

def main():
    """Traite tous les fichiers HTML dans le dossier categories"""
    directory = Path('categories')
    html_files = list(directory.glob('*.html'))
    
    print(f"Traitement de {len(html_files)} fichiers de catégories...\n")
    
    updated_count = 0
    for html_file in html_files:
        if update_category_width(html_file):
            updated_count += 1
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
