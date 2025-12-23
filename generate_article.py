#!/usr/bin/env python3
"""
Script rapide pour générer un article avec un mot-clé spécifique
"""

import sys
sys.path.insert(0, '/Users/marc/Desktop/italiaanse-percolator')

from blog_generator_advanced import AdvancedBlogGenerator
import os
from dotenv import load_dotenv

# Charger .env
load_dotenv()

def main():
    # Mot-clé spécifique
    keyword = "Wat is een Italiaanse percolator (mokapot) en hoe werkt hij precies?"
    
    print(f"\n🚀 Génération d'article pour: {keyword}\n")
    
    # Charger clé API
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Clé API manquante!")
        return
    
    print("✅ Clé API chargée")
    print("📝 Mode: Sans scraping (plus rapide)\n")
    
    # Créer le générateur
    generator = AdvancedBlogGenerator(api_key)
    
    # Générer l'article (sans scraping pour plus de rapidité)
    try:
        filepath = generator.generate_full_pipeline(keyword, scrape_serps=False)
        
        if filepath:
            print(f"\n{'='*70}")
            print(f"🎉 ARTICLE GÉNÉRÉ AVEC SUCCÈS!")
            print(f"{'='*70}")
            print(f"\n📂 Fichier: {filepath}")
            print(f"\n💡 Ouvrir le fichier dans un navigateur pour voir le résultat")
        else:
            print("\n❌ Échec de génération")
    
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
