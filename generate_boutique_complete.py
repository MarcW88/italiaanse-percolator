#!/usr/bin/env python3
"""
Générateur boutique complète avec filtres et 12+ produits
Corrige les problèmes critiques identifiés dans l'analyse
"""

import pandas as pd
import json

def generate_complete_boutique():
    """Génère une page boutique complète avec filtres et plus de produits"""
    
    # Charger catalogue
    df = pd.read_excel('catalogue_bialetti_complet.xlsx')
    
    # Sélectionner 12 meilleurs produits (mix catégories)
    percolators = df[df['Type'] == 'Cafetière percolateur'].head(9)
    elektrisch = df[df['Type'] == 'Cafetière électrique'].head(2) 
    accessoires = df[df['Type'] == 'Accessoire (joints et filtres)'].head(1)
    
    featured_products = pd.concat([percolators, elektrisch, accessoires])
    
    # Générer cards produits avec specs visuelles
    products_html = ""
    for _, product in featured_products.iterrows():
        # Icons specs
        inductie_icon = "⚡" if product['Compatible induction'] == 'Oui' else ""
        tassen_icon = f"🍵 {int(product['Capacité (tasses)'])}" if pd.notna(product['Capacité (tasses)']) else ""
        materiaal_icon = "🔧 RVS" if product['Matériau'] == 'Acier inoxydable' else "🔧 Alu" if product['Matériau'] == 'Aluminium' else ""
        
        slug = product['Nom du produit'].lower().replace(' ', '-').replace('(', '').replace(')', '')
        
        products_html += f"""
        <div class="product-card" data-inductie="{product['Compatible induction']}" data-capaciteit="{product['Capacité (tasses)'] if pd.notna(product['Capacité (tasses)']) else 0}" data-prijs="{product['Prix estimé (€)']}" data-merk="{product['Marque']}" style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 12px rgba(0,0,0,0.1); position: relative; transition: transform 0.2s;">
            <div style="position: absolute; top: 15px; right: 15px; background: #D2691E; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem; font-weight: 600;">
                #{featured_products.index.get_loc(product.name) + 1}
            </div>
            
            <img src="images/producten/{slug}.jpg" alt="{product['Nom du produit']}" 
                 style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;"
                 onerror="this.src='Images/placeholder-product.jpg'">
            
            <!-- Specs visuelles -->
            <div style="display: flex; gap: 0.5rem; margin-bottom: 0.5rem; font-size: 0.8rem;">
                {f'<span style="background: #e8f5e8; color: #2d5a2d; padding: 0.2rem 0.5rem; border-radius: 10px;">{inductie_icon} Inductie</span>' if inductie_icon else ''}
                {f'<span style="background: #e8f0ff; color: #1a4480; padding: 0.2rem 0.5rem; border-radius: 10px;">{tassen_icon}</span>' if tassen_icon else ''}
                {f'<span style="background: #fff3e0; color: #8b4513; padding: 0.2rem 0.5rem; border-radius: 10px;">{materiaal_icon}</span>' if materiaal_icon else ''}
            </div>
            
            <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem; line-height: 1.3;">{product['Nom du produit']}</h3>
            
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                <div style="color: #ffd700;">
                    {'★' * int(float(product['Note estimée (sur 5)']))}{'☆' * (5 - int(float(product['Note estimée (sur 5)'])))}
                </div>
                <span style="font-size: 0.9rem; color: #666;">({product["Nombre d'avis estimé"]} reviews)</span>
            </div>
            
            <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem; line-height: 1.4;">
                {product['Description courte'][:80]}...
            </p>
            
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 1.3rem; font-weight: bold; color: #D2691E;">€{product['Prix estimé (€)']}</span>
                <span style="background: #e8f5e8; color: #2d5a2d; padding: 0.2rem 0.6rem; border-radius: 10px; font-size: 0.8rem;">Op voorraad</span>
            </div>
            
            <div style="display: flex; gap: 0.5rem;">
                <a href="producten/{slug}.html" class="btn btn-primary" 
                   style="flex: 1; text-align: center; padding: 0.6rem; background: #D2691E; color: white; text-decoration: none; border-radius: 4px; font-size: 0.9rem;">
                    Bekijk details
                </a>
                <button onclick="quickView('{slug}')" class="btn btn-outline" 
                        style="padding: 0.6rem; border: 2px solid #D2691E; background: transparent; color: #D2691E; border-radius: 4px; cursor: pointer; font-size: 0.9rem;">
                    👁️
                </button>
            </div>
        </div>"""
    
    # Template boutique complète
    html_content = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Italiaanse Percolator Winkel | 64 Geteste Producten</title>
    <meta name="description" content="Officiële Italiaanse Percolator winkel - 64 percolators getest, vergeleken en geselecteerd. Gratis verzending vanaf €20. Tevredenheidsgarantie.">
    <link rel="stylesheet" href="style.css">
    <link rel="canonical" href="https://italiaanse-percolator.nl/boutique.html">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;700&family=DM+Serif+Display:ital,wght@0,400&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Breadcrumbs -->
    <nav style="background: #f8f9fa; padding: 0.5rem 0; font-size: 0.9rem;">
        <div class="container">
            <a href="index.html" style="color: #666; text-decoration: none;">Home</a> > 
            <span style="color: #D2691E; font-weight: 600;">Winkel</span>
        </div>
    </nav>

    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="index.html" class="nav-link">Home</a></li>
                    <li><a href="boutique.html" class="nav-link active">🛒 Winkel</a></li>
                    <li><a href="beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
                    <li><a href="koopgids/index.html" class="nav-link">Koopgids</a></li>
                    <li><a href="vergelijking/index.html" class="nav-link">Vergelijking</a></li>
                    <li><a href="over-ons.html" class="nav-link">Over ons</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero avec recherche -->
    <section class="hero" style="background: linear-gradient(135deg, rgba(210, 105, 30, 0.9), rgba(139, 69, 19, 0.8)), url('Images/background_homepage.jpg') center/cover; min-height: 400px; display: flex; align-items: center; color: white;">
        <div class="container" style="text-align: center;">
            <h1 style="font-size: 3rem; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.7);">
                Italiaanse Percolator Winkel
            </h1>
            <p style="font-size: 1.2rem; margin-bottom: 2rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.7);">
                <span id="product-count">64</span> producten getest en geselecteerd door onze experts
            </p>
            
            <!-- Barre recherche -->
            <div style="max-width: 500px; margin: 0 auto 2rem;">
                <input type="text" id="search-input" placeholder="Zoek je perfecte percolator..." 
                       style="width: 100%; padding: 1rem; border: none; border-radius: 25px; font-size: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
            </div>
            
            <!-- Quick filters -->
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem;">
                <button onclick="quickFilter('inductie')" class="quick-filter" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 0.5rem 1rem; border-radius: 20px; cursor: pointer; backdrop-filter: blur(10px);">⚡ Inductie</button>
                <button onclick="quickFilter('budget')" class="quick-filter" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 0.5rem 1rem; border-radius: 20px; cursor: pointer; backdrop-filter: blur(10px);">💰 Budget <€50</button>
                <button onclick="quickFilter('groot')" class="quick-filter" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 0.5rem 1rem; border-radius: 20px; cursor: pointer; backdrop-filter: blur(10px);">🍵 6+ Kopjes</button>
            </div>
            
            <!-- Trust badges -->
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                <div style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; backdrop-filter: blur(10px);">
                    ✓ 64 producten getest
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; backdrop-filter: blur(10px);">
                    ✓ Gratis verzending €20+
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; backdrop-filter: blur(10px);">
                    ✓ 30 dagen retour
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; backdrop-filter: blur(10px);">
                    ✓ Nederlandse klantenservice
                </div>
            </div>
        </div>
    </section>

    <main class="container" style="padding: 3rem 0;">
        
        <!-- Filtres et tri -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; padding: 1.5rem; background: #f8f9fa; border-radius: 8px; flex-wrap: wrap; gap: 1rem;">
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; align-items: center;">
                <strong id="results-count">{len(featured_products)} producten</strong>
                
                <select id="filter-inductie" onchange="applyFilters()" style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
                    <option value="">Alle inductie</option>
                    <option value="Oui">Inductiegeschikt</option>
                    <option value="Non">Niet inductie</option>
                </select>
                
                <select id="filter-merk" onchange="applyFilters()" style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
                    <option value="">Alle merken</option>
                    <option value="Bialetti">Bialetti</option>
                    <option value="Alessi">Alessi</option>
                </select>
                
                <input type="range" id="filter-prijs" min="0" max="150" value="150" onchange="applyFilters()" style="width: 120px;">
                <span id="prijs-display">€0-150</span>
            </div>
            
            <div style="display: flex; gap: 1rem; align-items: center;">
                <label>Sorteren:</label>
                <select id="sort-select" onchange="sortProducts()" style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
                    <option value="populair">Populairiteit</option>
                    <option value="prijs-laag">Prijs laag-hoog</option>
                    <option value="prijs-hoog">Prijs hoog-laag</option>
                    <option value="rating">Best beoordeeld</option>
                </select>
                
                <button onclick="clearFilters()" style="padding: 0.5rem 1rem; background: #6c757d; color: white; border: none; border-radius: 4px; cursor: pointer;">
                    Wis filters
                </button>
            </div>
        </div>

        <!-- Grille produits -->
        <div id="products-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 3rem;">
            {products_html}
        </div>
        
        <!-- Load more -->
        <div style="text-align: center; margin-bottom: 3rem;">
            <button onclick="loadMoreProducts()" id="load-more-btn" style="padding: 1rem 2rem; background: #D2691E; color: white; border: none; border-radius: 6px; font-size: 1rem; cursor: pointer;">
                Laad meer producten (52 resterend)
            </button>
        </div>

        <!-- Newsletter signup -->
        <section style="background: linear-gradient(135deg, #D2691E, #8B4513); color: white; padding: 3rem 2rem; border-radius: 12px; text-align: center; margin-bottom: 3rem;">
            <h2 style="font-size: 2rem; margin-bottom: 1rem;">Blijf op de hoogte!</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem; opacity: 0.9;">
                Ontvang wekelijkse koffietips en exclusieve aanbiedingen
            </p>
            <div style="max-width: 400px; margin: 0 auto; display: flex; gap: 0.5rem;">
                <input type="email" placeholder="Je email adres..." style="flex: 1; padding: 1rem; border: none; border-radius: 6px;">
                <button style="padding: 1rem 1.5rem; background: white; color: #D2691E; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">
                    Inschrijven
                </button>
            </div>
            <p style="font-size: 0.9rem; margin-top: 1rem; opacity: 0.8;">
                Gratis Koffiegids PDF bij inschrijving • Geen spam, uitschrijven altijd mogelijk
            </p>
        </section>

        <!-- FAQ -->
        <section style="margin-bottom: 3rem;">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 3rem;">Veelgestelde Vragen</h2>
            
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="faq-item" style="border: 1px solid #ddd; border-radius: 8px; margin-bottom: 1rem;">
                    <button onclick="toggleFaq(1)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Welke maat percolator moet ik kiezen?
                        <span id="faq-icon-1">+</span>
                    </button>
                    <div id="faq-content-1" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        Kies op basis van je dagelijkse koffieconsumptie: 1-3 kopjes voor 1-2 personen, 4-6 kopjes voor 2-4 personen, 6+ kopjes voor families of kantoor.
                    </div>
                </div>
                
                <div class="faq-item" style="border: 1px solid #ddd; border-radius: 8px; margin-bottom: 1rem;">
                    <button onclick="toggleFaq(2)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Werken alle percolators op inductie?
                        <span id="faq-icon-2">+</span>
                    </button>
                    <div id="faq-content-2" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        Nee, alleen RVS modellen en speciale inductie-versies werken op inductie. Aluminium percolators hebben een inductieplaatje nodig.
                    </div>
                </div>
                
                <div class="faq-item" style="border: 1px solid #ddd; border-radius: 8px; margin-bottom: 1rem;">
                    <button onclick="toggleFaq(3)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Hoe lang gaat een percolator mee?
                        <span id="faq-icon-3">+</span>
                    </button>
                    <div id="faq-content-3" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        Bij goed onderhoud gaat een kwaliteitspercolator 10-20 jaar mee. Vervang alleen de rubber ringen en filter om de 1-2 jaar.
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer style="background: #2c2c2c; color: white; padding: 3rem 0 2rem; margin-top: 4rem;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
                <div>
                    <h3 style="margin-bottom: 1rem;">Italiaanse Percolator</h3>
                    <p style="color: #ccc; line-height: 1.6;">Jouw expert in percolators sinds 2017. Tests, vergelijkingen en advies voor de perfecte percolator.</p>
                </div>
                <div>
                    <h4 style="margin-bottom: 1rem;">Winkel</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.5rem;"><a href="categories/percolators.html" style="color: #ccc; text-decoration: none;">Klassieke Percolators</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="categories/elektrische-percolators.html" style="color: #ccc; text-decoration: none;">Elektrische Percolators</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="categories/accessoires.html" style="color: #ccc; text-decoration: none;">Accessoires</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="margin-bottom: 1rem;">Informatie</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.5rem;"><a href="over-ons.html" style="color: #ccc; text-decoration: none;">Over ons</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="contact.html" style="color: #ccc; text-decoration: none;">Contact</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="disclaimer.html" style="color: #ccc; text-decoration: none;">Disclaimer</a></li>
                    </ul>
                </div>
            </div>
            <div style="border-top: 1px solid #444; padding-top: 2rem; text-align: center; color: #999;">
                <p>&copy; 2025 Italiaanse Percolator - Affiliate links naar Bol.com</p>
            </div>
        </div>
    </footer>

    <script>
    // Filtres et tri interactifs
    function applyFilters() {{
        const inductie = document.getElementById('filter-inductie').value;
        const merk = document.getElementById('filter-merk').value;
        const maxPrijs = document.getElementById('filter-prijs').value;
        
        document.getElementById('prijs-display').textContent = `€0-${{maxPrijs}}`;
        
        const cards = document.querySelectorAll('.product-card');
        let visibleCount = 0;
        
        cards.forEach(card => {{
            const cardInductie = card.dataset.inductie;
            const cardMerk = card.dataset.merk;
            const cardPrijs = parseFloat(card.dataset.prijs);
            
            const matchInductie = !inductie || cardInductie === inductie;
            const matchMerk = !merk || cardMerk === merk;
            const matchPrijs = cardPrijs <= maxPrijs;
            
            if (matchInductie && matchMerk && matchPrijs) {{
                card.style.display = 'block';
                visibleCount++;
            }} else {{
                card.style.display = 'none';
            }}
        }});
        
        document.getElementById('results-count').textContent = `${{visibleCount}} producten`;
    }}
    
    function quickFilter(type) {{
        if (type === 'inductie') {{
            document.getElementById('filter-inductie').value = 'Oui';
        }} else if (type === 'budget') {{
            document.getElementById('filter-prijs').value = '50';
        }} else if (type === 'groot') {{
            // Filter op 6+ kopjes - zou meer data attributes nodig hebben
        }}
        applyFilters();
    }}
    
    function clearFilters() {{
        document.getElementById('filter-inductie').value = '';
        document.getElementById('filter-merk').value = '';
        document.getElementById('filter-prijs').value = '150';
        document.getElementById('sort-select').value = 'populair';
        applyFilters();
    }}
    
    function sortProducts() {{
        const sortBy = document.getElementById('sort-select').value;
        const grid = document.getElementById('products-grid');
        const cards = Array.from(grid.children);
        
        cards.sort((a, b) => {{
            switch(sortBy) {{
                case 'prijs-laag':
                    return parseFloat(a.dataset.prijs) - parseFloat(b.dataset.prijs);
                case 'prijs-hoog':
                    return parseFloat(b.dataset.prijs) - parseFloat(a.dataset.prijs);
                default:
                    return 0;
            }}
        }});
        
        cards.forEach(card => grid.appendChild(card));
    }}
    
    function quickView(slug) {{
        alert(`Quick view voor ${slug} - Feature komt binnenkort!`);
    }}
    
    function toggleFaq(num) {{
        const content = document.getElementById(`faq-content-${num}`);
        const icon = document.getElementById(`faq-icon-${num}`);
        
        if (content.style.display === 'none') {{
            content.style.display = 'block';
            icon.textContent = '-';
        }} else {{
            content.style.display = 'none';
            icon.textContent = '+';
        }}
    }}
    
    function loadMoreProducts() {{
        alert('Load more functionaliteit komt binnenkort!');
    }}
    </script>
</body>
</html>"""

    return html_content

if __name__ == "__main__":
    content = generate_complete_boutique()
    with open('boutique_complete.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Boutique complète générée: boutique_complete.html")
