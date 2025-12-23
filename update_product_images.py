#!/usr/bin/env python3
"""
Script pour mettre à jour automatiquement les images des produits
en matchant les noms de fichiers avec les noms de produits
"""

import json
import os
import urllib.parse

# Chemins
JSON_FILE = 'all_products.json'
IMAGES_DIR = 'Images'

def normalize_name(name):
    """Normalise un nom pour le matching"""
    # Enlever les extensions
    name = os.path.splitext(name)[0]
    # Enlever les espaces en fin
    name = name.strip()
    return name

def find_matching_image(product_name, image_files):
    """Trouve l'image correspondant au nom du produit"""
    # Chercher une correspondance exacte
    for img_file in image_files:
        img_name = normalize_name(img_file)
        if img_name == product_name:
            return f"Images/{img_file}"
    
    # Chercher avec URL encoding (espaces -> %20)
    product_name_encoded = product_name.replace(' ', '%20')
    for img_file in image_files:
        img_name_encoded = normalize_name(img_file).replace(' ', '%20')
        if img_name_encoded == product_name_encoded:
            return f"Images/{img_file}"
    
    return None

def main():
    # Lire le JSON
    print(f"📖 Lecture de {JSON_FILE}...")
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    print(f"✅ {len(products)} produits chargés")
    
    # Lister toutes les images
    print(f"\n📁 Lecture du dossier {IMAGES_DIR}...")
    image_files = [f for f in os.listdir(IMAGES_DIR) 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    
    print(f"✅ {len(image_files)} images trouvées")
    
    # Mettre à jour les produits
    updated_count = 0
    not_found = []
    
    print(f"\n🔄 Matching des images avec les produits...")
    for product in products:
        product_name = product['name']
        current_image = product.get('image', '')
        
        # Chercher une image correspondante
        new_image = find_matching_image(product_name, image_files)
        
        if new_image:
            if new_image != current_image:
                print(f"  ✏️  {product_name}")
                print(f"     AVANT: {current_image}")
                print(f"     APRÈS: {new_image}")
                product['image'] = new_image
                updated_count += 1
        else:
            if not current_image or not os.path.exists(current_image):
                not_found.append(product_name)
    
    # Sauvegarder le JSON mis à jour
    if updated_count > 0:
        print(f"\n💾 Sauvegarde de {JSON_FILE}...")
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
        print(f"✅ {updated_count} produits mis à jour!")
    else:
        print(f"\n✨ Aucune mise à jour nécessaire")
    
    # Afficher les produits sans image
    if not_found:
        print(f"\n⚠️  {len(not_found)} produits sans image trouvée:")
        for name in not_found[:10]:  # Afficher les 10 premiers
            print(f"   - {name}")
        if len(not_found) > 10:
            print(f"   ... et {len(not_found) - 10} autres")
    
    print(f"\n✅ Terminé!")

if __name__ == '__main__':
    main()
