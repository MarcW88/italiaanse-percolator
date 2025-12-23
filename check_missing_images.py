#!/usr/bin/env python3
"""
Script pour vérifier les images non-utilisées et suggérer des matches
"""

import json
import os
from difflib import SequenceMatcher

# Chemins
JSON_FILE = 'all_products.json'
IMAGES_DIR = 'Images'

def normalize_name(name):
    """Normalise un nom pour le matching"""
    name = os.path.splitext(name)[0].strip()
    return name

def similarity(a, b):
    """Calcule la similarité entre deux chaînes"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def main():
    # Lire le JSON
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    # Lister toutes les images
    all_images = set(f for f in os.listdir(IMAGES_DIR) 
                     if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')))
    
    # Images utilisées
    used_images = set()
    for product in products:
        img_path = product.get('image', '')
        if img_path.startswith('Images/'):
            img_file = img_path.replace('Images/', '')
            used_images.add(img_file)
    
    # Images non-utilisées
    unused_images = all_images - used_images
    
    print(f"📊 STATISTIQUES:")
    print(f"  • Total images: {len(all_images)}")
    print(f"  • Images utilisées: {len(used_images)}")
    print(f"  • Images non-utilisées: {len(unused_images)}")
    
    # Produits sans image
    products_without_image = []
    for product in products:
        img_path = product.get('image', '')
        if not img_path or not os.path.exists(img_path):
            products_without_image.append(product)
    
    print(f"  • Produits sans image: {len(products_without_image)}")
    
    # Afficher les images non-utilisées
    if unused_images:
        print(f"\n📷 IMAGES NON-UTILISÉES ({len(unused_images)}):")
        for img in sorted(unused_images):
            print(f"   • {img}")
    
    # Suggérer des matches pour les produits sans image
    if products_without_image and unused_images:
        print(f"\n🔍 SUGGESTIONS DE MATCH:")
        for product in products_without_image:
            product_name = product['name']
            best_match = None
            best_score = 0
            
            for img in unused_images:
                img_name = normalize_name(img)
                score = similarity(product_name, img_name)
                if score > best_score:
                    best_score = score
                    best_match = img
            
            if best_score > 0.5:  # Seuil de similarité
                print(f"\n  Produit: {product_name}")
                print(f"    → Image suggérée: {best_match}")
                print(f"    → Similarité: {best_score:.2%}")

if __name__ == '__main__':
    main()
