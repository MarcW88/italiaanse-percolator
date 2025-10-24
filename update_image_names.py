#!/usr/bin/env python3
"""
Script pour mettre à jour tous les liens d'images avec les nouveaux noms simplifiés
"""

import os
import re
from pathlib import Path

def update_images_in_file(file_path):
    """Met à jour les liens d'images dans un fichier HTML"""
    print(f"Mise à jour des images dans: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Déterminer le niveau de profondeur du fichier
    relative_path = os.path.relpath(file_path, '/Users/marc/Desktop/italiaanse-percolator')
    depth = len(Path(relative_path).parts) - 1
    image_prefix = '../Images/' if depth > 0 else 'Images/'
    
    # Correspondances anciennes images -> nouveaux noms
    replacements = [
        # Anciens noms complets vers nouveaux noms
        (r'Capture d\'écran 2025-10-13 à 19\.29\.06\.png', 'italiaanse-percolator.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.31\.09\.png', 'italiaanse-percolator-2.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.31\.34\.png', 'italiaanse-percolator-3.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.32\.02\.png', 'italiaanse-percolator-4.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.32\.16\.png', 'italiaanse-percolator-5.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.32\.26\.png', 'italiaanse-percolator-6.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.46\.52\.png', 'italiaanse-percolator-7.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.47\.10\.png', 'italiaanse-percolator-8.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.47\.35\.png', 'italiaanse-percolator9.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.47\.50\.png', 'italiaanse-percolator10.png'),
        (r'Capture d\'écran 2025-10-13 à 19\.48\.39\.png', 'italiaanse-percolator11.png'),
    ]
    
    # Appliquer les corrections
    changes_made = False
    for old_pattern, new_name in replacements:
        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_name, content)
            changes_made = True
    
    # Sauvegarder si des changements ont été faits
    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Images mises à jour dans {file_path}")
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
    
    print(f"🔍 Trouvé {len(html_files)} fichiers HTML à mettre à jour")
    print("=" * 60)
    
    corrected_count = 0
    for html_file in sorted(html_files):
        if update_images_in_file(html_file):
            corrected_count += 1
    
    print("=" * 60)
    print(f"✅ Mise à jour terminée!")
    print(f"📊 {corrected_count}/{len(html_files)} fichiers modifiés")
    print(f"🖼️  Nouveaux noms d'images:")
    print(f"   • italiaanse-percolator.png (Bialetti Fiammetta)")
    print(f"   • italiaanse-percolator-2.png (Bialetti Venus)")
    print(f"   • italiaanse-percolator-3.png (Alessi Pulcina)")
    print(f"   • italiaanse-percolator-4.png (Bialetti Brikka)")
    print(f"   • italiaanse-percolator-5.png (Comparaison tailles)")
    print(f"   • italiaanse-percolator-6.png (Bialetti vs Alessi)")
    print(f"   • italiaanse-percolator-7.png (Lifestyle)")
    print(f"   • italiaanse-percolator-8.png (Onderdelen/maten)")
    print(f"   • italiaanse-percolator9.png (Espresso machine)")
    print(f"   • italiaanse-percolator10.png (Inductie test)")
    print(f"   • italiaanse-percolator11.png (Reiniging)")

if __name__ == "__main__":
    main()
