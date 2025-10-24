#!/usr/bin/env python3
"""
Script pour corriger tous les liens dans le site italiaanse-percolator
Convertit les liens absoluts en liens relatifs pour le serveur local
"""

import os
import re
from pathlib import Path

def fix_links_in_file(file_path):
    """Corrige les liens dans un fichier HTML"""
    print(f"Correction des liens dans: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Déterminer le niveau de profondeur du fichier
    relative_path = os.path.relpath(file_path, '/Users/marc/Desktop/italiaanse-percolator')
    depth = len(Path(relative_path).parts) - 1
    prefix = '../' * depth if depth > 0 else ''
    
    # Corrections des liens de navigation
    replacements = [
        # Navigation brand
        (r'href="/"', f'href="{prefix}index.html"'),
        
        # Navigation menu
        (r'href="/beste-italiaanse-percolators/"', f'href="{prefix}beste-italiaanse-percolators.html"'),
        (r'href="/koopgids/"', f'href="{prefix}koopgids/index.html"'),
        (r'href="/vergelijking/"', f'href="{prefix}vergelijking/index.html"'),
        (r'href="/over-ons/"', f'href="{prefix}over-ons.html"'),
        (r'href="/contact/"', f'href="{prefix}contact.html"'),
        (r'href="/privacy/"', f'href="{prefix}privacy.html"'),
        (r'href="/disclaimer/"', f'href="{prefix}disclaimer.html"'),
        
        # Fiches produits
        (r'href="/bialetti-fiammetta-review/"', f'href="{prefix}bialetti-fiammetta-review.html"'),
        (r'href="/bialetti-venus-review/"', f'href="{prefix}bialetti-venus-review.html"'),
        (r'href="/alessi-pulcina-review/"', f'href="{prefix}alessi-pulcina-review.html"'),
        (r'href="/bialetti-brikka-review/"', f'href="{prefix}bialetti-brikka-review.html"'),
        
        # Guides
        (r'href="/koopgids/hoe-kies-je-de-juiste-percolator/"', f'href="{prefix}koopgids/hoe-kies-je-de-juiste-percolator.html"'),
        (r'href="/koopgids/hoe-onderhoud-je-een-percolator/"', f'href="{prefix}koopgids/hoe-onderhoud-je-een-percolator.html"'),
        (r'href="/koopgids/percolator-vs-espressoapparaat/"', f'href="{prefix}koopgids/percolator-vs-espressoapparaat.html"'),
        
        # Comparaisons
        (r'href="/vergelijking/bialetti-vs-alessi/"', f'href="{prefix}vergelijking/bialetti-vs-alessi.html"'),
        
        # CSS paths pour les sous-dossiers
        (r'href="../style.css"', f'href="{prefix}style.css"'),
    ]
    
    # Appliquer les corrections
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    # Sauvegarder si des changements ont été faits
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Liens corrigés dans {file_path}")
        return True
    else:
        print(f"  ⏭️  Aucun changement nécessaire dans {file_path}")
        return False

def main():
    """Fonction principale"""
    base_dir = '/Users/marc/Desktop/italiaanse-percolator'
    
    # Trouver tous les fichiers HTML
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"🔍 Trouvé {len(html_files)} fichiers HTML à corriger")
    print("=" * 50)
    
    corrected_count = 0
    for html_file in sorted(html_files):
        if fix_links_in_file(html_file):
            corrected_count += 1
    
    print("=" * 50)
    print(f"✅ Correction terminée!")
    print(f"📊 {corrected_count}/{len(html_files)} fichiers modifiés")
    print(f"🌐 Le site devrait maintenant fonctionner sur http://localhost:8080")

if __name__ == "__main__":
    main()
