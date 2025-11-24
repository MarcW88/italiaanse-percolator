#!/usr/bin/env python3
"""
Script pour s'assurer que toutes les sections sont en layout vertical
"""

import re
import os
from pathlib import Path

def fix_vertical_layout(file_path):
    """Corrige le layout pour que les sections soient verticales"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # S'assurer que la section description a un display block et clear
        content = re.sub(
            r'(<section style="margin: 3rem 0;">)',
            r'<section style="margin: 3rem 0; display: block; clear: both; width: 100%;">',
            content
        )
        
        # S'assurer que la section vergelijkbare producten est aussi en block
        content = re.sub(
            r'(<section style="margin-bottom: 3rem;">)',
            r'<section style="margin-bottom: 3rem; display: block; clear: both; width: 100%;">',
            content
        )
        
        # Ajouter un conteneur principal pour forcer le layout vertical
        if '<main class="container"' in content:
            content = re.sub(
                r'(<main class="container"[^>]*>)',
                r'\1<div style="display: flex; flex-direction: column; width: 100%;">',
                content
            )
            
            # Fermer le conteneur avant le footer
            content = re.sub(
                r'(</main>)',
                r'</div>\1',
                content
            )
        
        # Écrire le fichier modifié
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur avec {file_path}: {e}")
        return False

def main():
    print("📐 Correction du layout vertical des pages produits...")
    
    # Lister tous les fichiers produits
    producten_dir = Path("producten")
    if not producten_dir.exists():
        print("❌ Dossier producten non trouvé")
        return
    
    fixed_count = 0
    total_files = 0
    
    for file_path in producten_dir.glob("*.html"):
        total_files += 1
        filename = file_path.name
        
        if fix_vertical_layout(str(file_path)):
            print(f"✅ Layout vertical corrigé: {filename}")
            fixed_count += 1
        else:
            print(f"❌ Échec pour: {filename}")
    
    print(f"\n🎯 RÉSULTATS:")
    print(f"✅ {fixed_count}/{total_files} pages corrigées")
    print(f"\n📋 Layout forcé:")
    print("   - display: block sur toutes les sections")
    print("   - clear: both pour éviter les flottants")
    print("   - width: 100% pour forcer la pleine largeur")
    print("   - flex-direction: column sur le conteneur principal")

if __name__ == "__main__":
    main()
