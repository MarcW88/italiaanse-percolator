#!/usr/bin/env python3
"""
Script pour déplacer les descriptions produits en pleine largeur
sous les deux colonnes et au-dessus de "Vergelijkbare producten"
"""

import re
import os
from pathlib import Path

def fix_description_position(file_path):
    """Déplace la description produit au bon endroit"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraire toutes les descriptions produits existantes
        description_pattern = r'<!-- Uitgebreide Productbeschrijving -->\s*<div style="margin-bottom: 2rem;">.*?</div>\s*</div>'
        descriptions = re.findall(description_pattern, content, re.DOTALL)
        
        if not descriptions:
            print(f"⚠️  Aucune description trouvée dans {file_path}")
            return False
        
        # Prendre la première description (la plus pertinente)
        main_description = descriptions[0]
        
        # Supprimer toutes les descriptions existantes
        content = re.sub(description_pattern, '', content, flags=re.DOTALL)
        
        # Trouver l'endroit où insérer (après la fermeture des deux colonnes, avant vergelijkbare producten)
        insertion_pattern = r'(</div>\s*</div>\s*<!-- Vergelijkbare producten -->)'
        
        if re.search(insertion_pattern, content):
            # Insérer la description en pleine largeur
            full_width_description = f'''        </div>
        </div>

        <!-- Uitgebreide Productbeschrijving - Pleine largeur -->
        <section style="margin: 3rem 0;">
            <div style="max-width: 1000px; margin: 0 auto;">
                {main_description}
            </div>
        </section>

        <!-- Vergelijkbare producten -->'''
            
            content = re.sub(insertion_pattern, full_width_description, content)
            
            # Écrire le fichier modifié
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        else:
            print(f"⚠️  Pattern d'insertion non trouvé dans {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur avec {file_path}: {e}")
        return False

def main():
    print("🔧 Repositionnement des descriptions produits...")
    
    # Lister tous les fichiers produits
    producten_dir = Path("producten")
    if not producten_dir.exists():
        print("❌ Dossier producten non trouvé")
        return
    
    fixed_count = 0
    total_files = 0
    
    for file_path in producten_dir.glob("*.html"):
        total_files += 1
        print(f"\n📋 Traitement: {file_path.name}")
        
        if fix_description_position(str(file_path)):
            print(f"✅ Description repositionnée dans {file_path.name}")
            fixed_count += 1
        else:
            print(f"❌ Échec pour {file_path.name}")
    
    print(f"\n🎯 RÉSULTATS:")
    print(f"✅ {fixed_count}/{total_files} pages corrigées")
    print(f"\n📋 Nouvelle structure:")
    print("   1. Image + Infos produit (2 colonnes)")
    print("   2. Description détaillée (pleine largeur)")
    print("   3. Vergelijkbare producten")
    print("   4. FAQ section")

if __name__ == "__main__":
    main()
