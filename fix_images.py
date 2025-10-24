#!/usr/bin/env python3
"""
Script pour corriger tous les liens d'images dans le site italiaanse-percolator
Utilise les vrais noms de fichiers avec espaces et caractères spéciaux
"""

import os
import re
from pathlib import Path

def fix_images_in_file(file_path):
    """Corrige les liens d'images dans un fichier HTML"""
    print(f"Correction des images dans: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Déterminer le niveau de profondeur du fichier
    relative_path = os.path.relpath(file_path, '/Users/marc/Desktop/italiaanse-percolator')
    depth = len(Path(relative_path).parts) - 1
    image_prefix = '../Images/' if depth > 0 else 'Images/'
    
    # Corrections des liens d'images - utiliser les vrais noms de fichiers
    replacements = [
        # Images avec noms raccourcis vers vrais noms
        (r'src="([^"]*/)19\.29\.06\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.29.06.png"'),
        (r'src="([^"]*/)19\.31\.09\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.31.09.png"'),
        (r'src="([^"]*/)19\.31\.34\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.31.34.png"'),
        (r'src="([^"]*/)19\.32\.02\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.32.02.png"'),
        (r'src="([^"]*/)19\.32\.16\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.32.16.png"'),
        (r'src="([^"]*/)19\.32\.26\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.32.26.png"'),
        (r'src="([^"]*/)19\.46\.52\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.46.52.png"'),
        (r'src="([^"]*/)19\.47\.10\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.47.10.png"'),
        (r'src="([^"]*/)19\.47\.35\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.47.35.png"'),
        (r'src="([^"]*/)19\.47\.50\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.47.50.png"'),
        (r'src="([^"]*/)19\.48\.39\.png"', f'src="{image_prefix}Capture d\'écran 2025-10-13 à 19.48.39.png"'),
        
        # Images avec noms complets mais mauvais chemin
        (r'src="\.\.\/Images\/Capture d\'écran ([^"]*)"', f'src="{image_prefix}Capture d\'écran \\1"'),
        (r'src="Images\/Capture d\'écran ([^"]*)"', f'src="{image_prefix}Capture d\'écran \\1"'),
    ]
    
    # Appliquer les corrections
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    # Sauvegarder si des changements ont été faits
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Images corrigées dans {file_path}")
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
        if fix_images_in_file(html_file):
            corrected_count += 1
    
    print("=" * 50)
    print(f"✅ Correction terminée!")
    print(f"📊 {corrected_count}/{len(html_files)} fichiers modifiés")
    print(f"🖼️  Les images devraient maintenant s'afficher correctement!")

if __name__ == "__main__":
    main()
