#!/usr/bin/env python3
"""
Script pour mettre à jour toutes les pages produits en néerlandais
avec section "vergelijkbare producten" pour maillage interne
"""

import pandas as pd
import json
import re
import os
from pathlib import Path

def slugify(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def get_similar_products(current_product, all_products, max_similar=4):
    """Trouve des produits similaires pour le maillage interne"""
    similar = []
    
    # Même marque
    same_brand = [p for p in all_products if p['Marque'] == current_product['Marque'] and p['Nom du produit'] != current_product['Nom du produit']]
    similar.extend(same_brand[:2])
    
    # Même type
    same_type = [p for p in all_products if p['Type'] == current_product['Type'] and p['Nom du produit'] != current_product['Nom du produit'] and p not in similar]
    similar.extend(same_type[:2])
    
    # Même gamme de prix (±20€)
    try:
        current_price = float(str(current_product['Prix estimé (€)']).replace(',', '.'))
        price_range = []
        for p in all_products:
            try:
                p_price = float(str(p['Prix estimé (€)']).replace(',', '.'))
                if abs(p_price - current_price) <= 20 and p['Nom du produit'] != current_product['Nom du produit'] and p not in similar:
                    price_range.append(p)
            except:
                continue
    except:
        price_range = []
    similar.extend(price_range[:2])
    
    return similar[:max_similar]

def generate_product_page(product, similar_products):
    """Génère une page produit complète en néerlandais"""
    
    slug = slugify(product['Nom du produit'])
    
    # Déterminer la catégorie pour breadcrumb
    category_map = {
        'Cafetière percolateur': 'percolators',
        'Cafetière électrique': 'elektrische-percolators', 
        'Accessoire (joints et filtres)': 'accessoires',
        'Adaptateur induction': 'inductie-adapters',
        "Kit d'entretien": 'onderhoudssets'
    }
    
    category_slug = category_map.get(product['Type'], 'percolators')
    category_name_nl = {
        'percolators': 'Percolators',
        'elektrische-percolators': 'Elektrische Percolators',
        'accessoires': 'Accessoires',
        'inductie-adapters': 'Inductie Adapters',
        'onderhoudssets': 'Onderhoudssets'
    }
    
    # Specs en néerlandais
    specs_nl = []
    if pd.notna(product['Capacité (tasses)']) and product['Capacité (tasses)'] > 0:
        specs_nl.append(f"Capaciteit: {int(product['Capacité (tasses)'])} kopjes")
    
    specs_nl.append(f"Materiaal: {product['Matériau'] if pd.notna(product['Matériau']) else 'Aluminium'}")
    specs_nl.append(f"Inductie: {'Ja' if product['Compatible induction'] == 'Oui' else 'Nee'}")
    specs_nl.append(f"Merk: {product['Marque']}")
    
    # Trust badges néerlandais
    trust_badges = [
        "Gratis retourneren binnen 30 dagen",
        "Snelle levering via Bol.com", 
        "Betrouwbare klantenservice",
        "Veilig betalen"
    ]
    
    # Générer HTML des produits similaires
    similar_html = ""
    for similar in similar_products:
        similar_slug = slugify(similar['Nom du produit'])
        similar_html += f'''
        <div class="similar-product" style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 12px rgba(0,0,0,0.1); text-align: center;">
            <img src="../images/producten/{similar_slug}.jpg" alt="{similar['Nom du produit']}" 
                 style="width: 100%; height: 150px; object-fit: cover; border-radius: 6px; margin-bottom: 1rem;"
                 onerror="this.src='../Images/placeholder-product.jpg'">
            <h4 style="font-size: 1rem; margin-bottom: 0.5rem; line-height: 1.3;">{similar['Nom du produit']}</h4>
            <div style="color: #ffd700; margin-bottom: 0.5rem;">
                {'★' * int(float(similar['Note estimée (sur 5)']))}{'☆' * (5 - int(float(similar['Note estimée (sur 5)'])))}
            </div>
            <div style="font-size: 1.2rem; font-weight: bold; color: #D2691E; margin-bottom: 1rem;">€{similar['Prix estimé (€)']}</div>
            <a href="{slugify(similar['Nom du produit'])}.html" 
               style="display: inline-block; padding: 0.5rem 1rem; background: #D2691E; color: white; text-decoration: none; border-radius: 4px; font-size: 0.9rem;">
                Bekijk details
            </a>
        </div>'''
    
    html_content = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product['Nom du produit']} | Italiaanse Percolator</title>
    <meta name="description" content="{product['Nom du produit']} - {product['Description courte']} - Prijs: €{product['Prix estimé (€)']} - {product['Note estimée (sur 5)']}★ ({product["Nombre d'avis estimé"]} reviews)">
    <link rel="stylesheet" href="../style.css">
    <link rel="canonical" href="https://italiaanse-percolator.nl/producten/{slug}.html">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;700&family=DM+Serif+Display:ital,wght@0,400&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="../index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li><a href="../beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
                    <li><a href="../koopgids/index.html" class="nav-link">Koopgids</a></li>
                    <li><a href="../vergelijking/index.html" class="nav-link">Vergelijking</a></li>
                    <li><a href="../over-ons.html" class="nav-link">Over ons</a></li>
                    <li><a href="../italiaanse-percolator-kopen.html" class="nav-link" style="background: #D2691E; color: white; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600;">Winkel</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container" style="padding: 2rem 0;">
        <!-- Breadcrumb -->
        <nav style="margin-bottom: 2rem; font-size: 0.9rem; color: #666;">
            <a href="../index.html" style="color: #666; text-decoration: none;">Home</a> > 
            <a href="../categories/{category_slug}.html" style="color: #666; text-decoration: none;">{category_name_nl[category_slug]}</a> > 
            <span style="color: #D2691E; font-weight: 600;">{product['Nom du produit']}</span>
        </nav>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-bottom: 3rem;">
            <!-- Image produit -->
            <div>
                <img src="../images/producten/{slug}.jpg" alt="{product['Nom du produit']}" 
                     style="width: 100%; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.15);"
                     onerror="this.src='../Images/placeholder-product.jpg'">
            </div>

            <!-- Infos produit -->
            <div>
                <h1 style="font-size: 2.2rem; margin-bottom: 1rem; line-height: 1.2;">{product['Nom du produit']}</h1>
                
                <!-- Rating et avis -->
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="color: #ffd700; font-size: 1.3rem;">
                        {'★' * int(float(product['Note estimée (sur 5)']))}{'☆' * (5 - int(float(product['Note estimée (sur 5)'])))}
                    </div>
                    <span style="color: #666; font-size: 1rem;">({product["Nombre d'avis estimé"]} beoordelingen)</span>
                </div>

                <!-- Prix -->
                <div style="font-size: 2.5rem; font-weight: bold; color: #D2691E; margin-bottom: 2rem;">
                    €{product['Prix estimé (€)']}
                </div>

                <!-- Description -->
                <div style="margin-bottom: 2rem;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">Productbeschrijving</h3>
                    <p style="color: #666; line-height: 1.6; font-size: 1rem;">
                        {product['Description courte']}
                    </p>
                </div>

                <!-- Specifications -->
                <div style="margin-bottom: 2rem;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">Specificaties</h3>
                    <ul style="list-style: none; padding: 0;">
                        {''.join([f'<li style="padding: 0.5rem 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;"><span style="font-weight: 600;">{spec.split(":")[0]}:</span><span>{spec.split(":")[1]}</span></li>' for spec in specs_nl])}
                    </ul>
                </div>

                <!-- CTA Button -->
                <div style="margin-bottom: 2rem;">
                    <a href="{product['URL']}" target="_blank" rel="nofollow" 
                       style="display: inline-block; background: linear-gradient(135deg, #D2691E, #B8541A); color: white; padding: 1rem 2rem; text-decoration: none; border-radius: 8px; font-size: 1.1rem; font-weight: 600; box-shadow: 0 4px 15px rgba(210, 105, 30, 0.3); transition: all 0.3s ease;">
                        Koop nu op Bol.com →
                    </a>
                </div>

                <!-- Trust badges -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.9rem; color: #666;">
                    {''.join([f'<div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #28a745;">✓</span>{badge}</div>' for badge in trust_badges])}
                </div>
            </div>
        </div>

        <!-- Vergelijkbare producten -->
        <section style="margin-bottom: 3rem;">
            <h2 style="font-size: 2rem; margin-bottom: 2rem; text-align: center;">Vergelijkbare Producten</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                {similar_html}
            </div>
        </section>

        <!-- FAQ Section -->
        <section style="margin-bottom: 3rem;">
            <h2 style="font-size: 2rem; margin-bottom: 2rem;">Veelgestelde Vragen</h2>
            
            <div style="max-width: 800px;">
                <div style="border: 1px solid #ddd; border-radius: 8px; margin-bottom: 1rem;">
                    <button onclick="toggleFaq(1)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Hoe gebruik ik deze percolator?
                        <span id="faq-icon-1">+</span>
                    </button>
                    <div id="faq-content-1" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        Vul het onderste reservoir met water tot de veiligheidsklep. Plaats gemalen koffie in het filter (niet aandrukken). Schroef de delen samen en zet op middelhoog vuur. Wanneer de koffie begint te borrelen, haal van het vuur.
                    </div>
                </div>
                
                <div style="border: 1px solid #ddd; border-radius: 8px; margin-bottom: 1rem;">
                    <button onclick="toggleFaq(2)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Welke maling moet ik gebruiken?
                        <span id="faq-icon-2">+</span>
                    </button>
                    <div id="faq-content-2" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        Gebruik een middelfijne maling, iets grover dan voor espresso maar fijner dan voor filterkoffie. De maling mag niet te fijn zijn anders verstopt het filter.
                    </div>
                </div>
                
                <div style="border: 1px solid #ddd; border-radius: 8px;">
                    <button onclick="toggleFaq(3)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Hoe onderhoud ik mijn percolator?
                        <span id="faq-icon-3">+</span>
                    </button>
                    <div id="faq-content-3" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        Spoel na gebruik met warm water (geen zeep). Droog goed af. Vervang de rubber ring en filter jaarlijks. Bewaar met open deksel om vochtophoping te voorkomen.
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer style="background: #2c2c2c; color: white; padding: 3rem 0 2rem;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
                <div>
                    <h3 style="margin-bottom: 1rem;">Italiaanse Percolator</h3>
                    <p style="color: #ccc; line-height: 1.6;">Jouw expert in percolators sinds 2017. Tests, vergelijkingen en advies voor de perfecte percolator.</p>
                </div>
                <div>
                    <h4 style="margin-bottom: 1rem;">Winkel</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.5rem;"><a href="../categories/percolators.html" style="color: #ccc; text-decoration: none;">Klassieke Percolators</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../categories/elektrische-percolators.html" style="color: #ccc; text-decoration: none;">Elektrische Percolators</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../categories/accessoires.html" style="color: #ccc; text-decoration: none;">Accessoires</a></li>
                    </ul>
                </div>
            </div>
            <div style="border-top: 1px solid #444; padding-top: 2rem; text-align: center; color: #999;">
                <p>&copy; 2025 Italiaanse Percolator - Affiliate links naar Bol.com</p>
            </div>
        </div>
    </footer>

    <script>
    function toggleFaq(num) {{
        const content = document.getElementById(`faq-content-${{num}}`);
        const icon = document.getElementById(`faq-icon-${{num}}`);
        
        if (content.style.display === 'none') {{
            content.style.display = 'block';
            icon.textContent = '-';
        }} else {{
            content.style.display = 'none';
            icon.textContent = '+';
        }}
    }}
    </script>
</body>
</html>'''

    return html_content

def main():
    # Charger le catalogue
    df = pd.read_excel('catalogue_bialetti_complet.xlsx')
    print(f"✅ Catalogue chargé: {len(df)} produits")
    
    # Créer le dossier producten s'il n'existe pas
    Path('producten').mkdir(exist_ok=True)
    
    # Générer toutes les pages produits
    updated_count = 0
    
    for _, product in df.iterrows():
        # Trouver des produits similaires
        similar_products = get_similar_products(product, df.to_dict('records'))
        
        # Générer la page
        html_content = generate_product_page(product, similar_products)
        
        # Sauvegarder
        slug = slugify(product['Nom du produit'])
        filename = f'producten/{slug}.html'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        updated_count += 1
        
        if updated_count % 10 == 0:
            print(f"✅ {updated_count} pages mises à jour...")
    
    print(f"🎯 TERMINÉ: {updated_count} pages produits mises à jour en néerlandais")
    print("📋 Chaque page contient maintenant:")
    print("   - Contenu 100% néerlandais")
    print("   - Navigation cohérente avec bouton Winkel")
    print("   - Breadcrumbs corrects")
    print("   - Section 'Vergelijkbare Producten' (4 produits)")
    print("   - FAQ en néerlandais")
    print("   - Trust badges adaptés")
    print("   - Maillage interne optimisé")

if __name__ == "__main__":
    main()
