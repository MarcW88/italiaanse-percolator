#!/usr/bin/env python3
"""
Générateur e-commerce pour Italiaanse Percolator
Crée pages catégories et fiches produits à partir du catalogue Excel
"""

import pandas as pd
import os
from urllib.parse import quote
import re

def slugify(text):
    """Convertit texte en slug URL-friendly"""
    text = str(text).lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def generate_product_page(product, index):
    """Génère une fiche produit individuelle"""
    
    slug = slugify(product['Nom du produit'])
    filename = f"produits/{slug}.html"
    
    # Template fiche produit
    html_content = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product['Nom du produit']} | Italiaanse Percolator</title>
    <meta name="description" content="{product['Description courte']} - Prijs: €{product['Prix estimé (€)']} - {product['Note estimée (sur 5)']}★ ({product["Nombre d'avis estimé"]} reviews)">
    <link rel="stylesheet" href="../style.css">
    <link rel="canonical" href="https://italiaanse-percolator.nl/produits/{slug}.html">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="../index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li><a href="../categories/percolateurs.html" class="nav-link">Percolateurs</a></li>
                    <li><a href="../categories/accessoires.html" class="nav-link">Accessoires</a></li>
                    <li><a href="../categories/electriques.html" class="nav-link">Électriques</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container" style="padding: 2rem 0;">
        <!-- Breadcrumb -->
        <nav style="margin-bottom: 2rem; font-size: 0.9rem; color: #666;">
            <a href="../index.html">Home</a> > 
            <a href="../categories/{slugify(product['Type'])}.html">{product['Type']}</a> > 
            <span>{product['Nom du produit']}</span>
        </nav>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-bottom: 3rem;">
            <!-- Image produit -->
            <div>
                <img src="../images/produits/{slug}.jpg" alt="{product['Nom du produit']}" 
                     style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"
                     onerror="this.src='../Images/placeholder-product.jpg'">
            </div>

            <!-- Infos produit -->
            <div>
                <h1 style="font-size: 2rem; margin-bottom: 1rem;">{product['Nom du produit']}</h1>
                
                <!-- Rating et avis -->
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                    <div style="color: #ffd700; font-size: 1.2rem;">
                        {'★' * int(float(product['Note estimée (sur 5)']))}{'☆' * (5 - int(float(product['Note estimée (sur 5)'])))}
                    </div>
                    <span style="color: #666;">{product['Note estimée (sur 5)']} ({product["Nombre d'avis estimé"]} avis)</span>
                </div>

                <!-- Prix -->
                <div style="font-size: 2rem; font-weight: bold; color: #D2691E; margin-bottom: 1.5rem;">
                    €{product['Prix estimé (€)']}
                </div>

                <!-- Description -->
                <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 2rem; color: #555;">
                    {product['Description courte']}
                </p>

                <!-- Spécifications -->
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem;">
                    <h3 style="margin-bottom: 1rem;">Spécifications</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
                        <div><strong>Marque:</strong> {product['Marque']}</div>
                        <div><strong>Type:</strong> {product['Type']}</div>
                        {f'<div><strong>Capacité:</strong> {product["Capacité (tasses)"]} tasses</div>' if pd.notna(product['Capacité (tasses)']) else ''}
                        {f'<div><strong>Volume:</strong> {product["Volume (ml)"]}ml</div>' if pd.notna(product['Volume (ml)']) else ''}
                        {f'<div><strong>Matériau:</strong> {product["Matériau"]}</div>' if pd.notna(product['Matériau']) else ''}
                        {f'<div><strong>Couleur:</strong> {product["Couleur"]}</div>' if pd.notna(product['Couleur']) else ''}
                        <div><strong>Induction:</strong> {'Oui' if product['Compatible induction'] == 'Oui' else 'Non'}</div>
                        <div><strong>Disponibilité:</strong> {product['Disponibilité']}</div>
                    </div>
                </div>

                <!-- CTA Achat -->
                <div style="display: flex; gap: 1rem;">
                    <a href="{product['URL']}" target="_blank" rel="nofollow" 
                       class="btn btn-primary btn-lg" 
                       style="flex: 1; text-align: center; padding: 1rem 2rem; background: #D2691E; color: white; text-decoration: none; border-radius: 5px; font-weight: 600;">
                        Acheter sur Bol.com →
                    </a>
                    <button onclick="window.print()" class="btn btn-outline" 
                            style="padding: 1rem; border: 2px solid #D2691E; background: transparent; color: #D2691E; border-radius: 5px; cursor: pointer;">
                        📄 Imprimer
                    </button>
                </div>

                <!-- Trust badges -->
                <div style="display: flex; gap: 1rem; margin-top: 1.5rem; font-size: 0.9rem; color: #666;">
                    <span>✓ Livraison gratuite dès €20</span>
                    <span>✓ Retour gratuit 30 jours</span>
                    <span>✓ Service client NL</span>
                </div>
            </div>
        </div>

        <!-- Description détaillée -->
        <section style="margin-bottom: 3rem;">
            <h2>Description détaillée</h2>
            <p>Le <strong>{product['Nom du produit']}</strong> de {product['Marque']} est {product['Description courte'].lower()}. 
            {f"Cette percolateur de {product['Capacité (tasses)']} tasses" if pd.notna(product['Capacité (tasses)']) else "Ce produit"} 
            est parfait pour les amateurs de café italien authentique.</p>
            
            {f'<p>Avec une capacité de <strong>{product["Volume (ml)"]}ml</strong>, ' if pd.notna(product['Volume (ml)']) else ''}
            {f'ce modèle en <strong>{product["Matériau"]}</strong> ' if pd.notna(product['Matériau']) else 'ce modèle '}
            {'est compatible avec les plaques à induction' if product['Compatible induction'] == 'Oui' else 'fonctionne sur toutes les sources de chaleur sauf induction'}.
            </p>
        </section>

        <!-- Produits similaires -->
        <section>
            <h2>Produits similaires</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
                <!-- Sera rempli dynamiquement -->
            </div>
        </section>
    </main>

    <footer style="background: #f8f9fa; padding: 2rem 0; margin-top: 3rem; text-align: center; color: #666;">
        <p>&copy; 2025 Italiaanse Percolator - Affiliate links naar Bol.com</p>
    </footer>
</body>
</html>"""

    return filename, html_content

def generate_category_page(category_name, products):
    """Génère une page catégorie avec liste de produits"""
    
    slug = slugify(category_name)
    filename = f"categories/{slug}.html"
    
    # Générer cards produits
    products_html = ""
    for _, product in products.iterrows():
        product_slug = slugify(product['Nom du produit'])
        products_html += f"""
        <div class="product-card" style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: transform 0.2s;">
            <img src="../images/produits/{product_slug}.jpg" alt="{product['Nom du produit']}" 
                 style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;"
                 onerror="this.src='../Images/placeholder-product.jpg'">
            
            <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
                <a href="../produits/{product_slug}.html" style="text-decoration: none; color: #333;">
                    {product['Nom du produit']}
                </a>
            </h3>
            
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                <div style="color: #ffd700;">
                    {'★' * int(float(product['Note estimée (sur 5)']))}{'☆' * (5 - int(float(product['Note estimée (sur 5)'])))}
                </div>
                <span style="font-size: 0.9rem; color: #666;">({product["Nombre d'avis estimé"]})</span>
            </div>
            
            <p style="font-size: 0.9rem; color: #666; margin-bottom: 1rem; line-height: 1.4;">
                {product['Description courte'][:100]}...
            </p>
            
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 1.3rem; font-weight: bold; color: #D2691E;">
                    €{product['Prix estimé (€)']}
                </span>
                <a href="../produits/{product_slug}.html" class="btn btn-primary" 
                   style="padding: 0.5rem 1rem; background: #D2691E; color: white; text-decoration: none; border-radius: 4px; font-size: 0.9rem;">
                    Voir détails
                </a>
            </div>
        </div>"""

    # Template page catégorie
    html_content = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{category_name} | Italiaanse Percolator</title>
    <meta name="description" content="Découvrez notre sélection de {category_name.lower()} - {len(products)} produits testés et comparés. Livraison gratuite dès €20.">
    <link rel="stylesheet" href="../style.css">
    <link rel="canonical" href="https://italiaanse-percolator.nl/categories/{slug}.html">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="../index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li><a href="percolateurs.html" class="nav-link">Percolateurs</a></li>
                    <li><a href="accessoires.html" class="nav-link">Accessoires</a></li>
                    <li><a href="electriques.html" class="nav-link">Électriques</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container" style="padding: 2rem 0;">
        <!-- Header catégorie -->
        <header style="text-align: center; margin-bottom: 3rem;">
            <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">{category_name}</h1>
            <p style="font-size: 1.1rem; color: #666; max-width: 600px; margin: 0 auto;">
                Découvrez notre sélection de {len(products)} {category_name.lower()} testés et comparés par nos experts.
            </p>
        </header>

        <!-- Filtres et tri -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; padding: 1rem; background: #f8f9fa; border-radius: 8px;">
            <div>
                <strong>{len(products)} produits</strong>
            </div>
            <div style="display: flex; gap: 1rem; align-items: center;">
                <label>Trier par:</label>
                <select onchange="sortProducts(this.value)" style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
                    <option value="name">Nom A-Z</option>
                    <option value="price-asc">Prix croissant</option>
                    <option value="price-desc">Prix décroissant</option>
                    <option value="rating">Note client</option>
                </select>
            </div>
        </div>

        <!-- Grille produits -->
        <div id="products-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            {products_html}
        </div>
    </main>

    <footer style="background: #f8f9fa; padding: 2rem 0; margin-top: 3rem; text-align: center; color: #666;">
        <p>&copy; 2025 Italiaanse Percolator - Affiliate links naar Bol.com</p>
    </footer>

    <script>
    function sortProducts(criteria) {{
        // JavaScript pour tri dynamique
        const grid = document.getElementById('products-grid');
        const products = Array.from(grid.children);
        
        products.sort((a, b) => {{
            switch(criteria) {{
                case 'name':
                    return a.querySelector('h3').textContent.localeCompare(b.querySelector('h3').textContent);
                case 'price-asc':
                    return parseFloat(a.querySelector('.price').textContent.replace('€', '')) - 
                           parseFloat(b.querySelector('.price').textContent.replace('€', ''));
                case 'price-desc':
                    return parseFloat(b.querySelector('.price').textContent.replace('€', '')) - 
                           parseFloat(a.querySelector('.price').textContent.replace('€', ''));
                default:
                    return 0;
            }}
        }});
        
        products.forEach(product => grid.appendChild(product));
    }}
    </script>
</body>
</html>"""

    return filename, html_content

def main():
    """Fonction principale"""
    print("🚀 Génération e-commerce Italiaanse Percolator...")
    
    # Charger catalogue
    try:
        df = pd.read_excel('catalogue_bialetti_complet.xlsx')
        print(f"✅ Catalogue chargé: {len(df)} produits")
    except Exception as e:
        print(f"❌ Erreur lecture catalogue: {e}")
        return
    
    # Créer dossiers
    os.makedirs('categories', exist_ok=True)
    os.makedirs('produits', exist_ok=True)
    
    # Générer pages catégories
    categories = df['Type'].value_counts()
    print(f"\n📁 Génération {len(categories)} catégories...")
    
    for category, count in categories.items():
        products = df[df['Type'] == category]
        filename, content = generate_category_page(category, products)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {filename} - {count} produits")
    
    # Générer fiches produits
    print(f"\n🛍️ Génération {len(df)} fiches produits...")
    
    for index, product in df.iterrows():
        filename, content = generate_product_page(product, index)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if index % 10 == 0:
            print(f"✅ {index + 1}/{len(df)} produits générés...")
    
    print(f"\n🎉 E-commerce généré avec succès!")
    print(f"📊 {len(categories)} catégories | {len(df)} produits")
    print(f"📁 Fichiers dans: categories/ et produits/")

if __name__ == "__main__":
    main()
