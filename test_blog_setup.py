#!/usr/bin/env python3
"""
Script de test rapide pour vérifier la configuration du générateur de blog
"""

import sys

def test_imports():
    """Test des imports Python"""
    print("🔍 Test des imports...")
    
    try:
        import openai
        print("  ✅ openai")
    except ImportError:
        print("  ❌ openai manquant")
        print("     → pip3 install openai")
        return False
    
    try:
        import requests
        print("  ✅ requests")
    except ImportError:
        print("  ❌ requests manquant")
        print("     → pip3 install requests")
        return False
    
    try:
        from bs4 import BeautifulSoup
        print("  ✅ beautifulsoup4")
    except ImportError:
        print("  ❌ beautifulsoup4 manquant")
        print("     → pip3 install beautifulsoup4")
        return False
    
    return True


def test_openai_connection(api_key):
    """Test de connexion à l'API OpenAI"""
    print("\n🔐 Test de connexion OpenAI...")
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        # Test simple
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Zeg 'hallo' in het Nederlands"}
            ],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"  ✅ Connexion réussie!")
        print(f"  📝 Réponse test: {result}")
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
        return False


def test_scraping():
    """Test du scraping (optionnel)"""
    print("\n🌐 Test du scraping Google...")
    
    try:
        import requests
        from bs4 import BeautifulSoup
        
        # Test simple
        response = requests.get(
            "https://www.google.nl",
            timeout=5,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        if response.status_code == 200:
            print("  ✅ Connexion Google OK")
            print("  💡 Scraping devrait fonctionner")
            return True
        else:
            print(f"  ⚠️  Status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
        print("  💡 Conseil: Utiliser mode sans scraping")
        return False


def main():
    """Test principal"""
    print("""
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║   TEST DE CONFIGURATION - Générateur de Blog         ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
    """)
    
    # Test 1: Imports
    if not test_imports():
        print("\n❌ Installation incomplète!")
        print("\n📥 Installer les dépendances:")
        print("   pip3 install -r requirements_blog.txt")
        return
    
    # Test 2: Clé API
    print("\n" + "─" * 55)
    api_key = input("🔑 Entre ta clé API OpenAI pour tester: ").strip()
    
    if not api_key:
        print("\n⚠️  Pas de clé API fournie")
        print("💡 Pour tester la connexion, relancer avec une clé")
    else:
        if not test_openai_connection(api_key):
            print("\n❌ Problème avec la clé API!")
            print("\n🔧 Vérifier:")
            print("   • Clé API valide (commence par sk-)")
            print("   • Crédit disponible sur OpenAI")
            print("   • https://platform.openai.com/account/billing")
            return
    
    # Test 3: Scraping
    print("\n" + "─" * 55)
    test_scraping()
    
    # Résumé
    print("\n" + "=" * 55)
    print("✅ CONFIGURATION OK!")
    print("=" * 55)
    print("\n🚀 Tu peux maintenant utiliser:")
    print("   • python3 blog_generator.py (version simple)")
    print("   • python3 blog_generator_advanced.py (version complète)")
    print("\n📚 Lire README_BLOG_GENERATOR.md pour plus d'infos")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrompu")
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
