#!/usr/bin/env python3
"""
Script pour mettre à jour tous les footers du site avec la version optimisée v2.0
Gère automatiquement les chemins relatifs selon la profondeur de chaque page.
"""

import os
import re
from pathlib import Path

# Root directory du site
SITE_ROOT = Path("/Users/marc/Desktop/italiaanse-percolator")

def get_relative_path(file_path):
    """
    Calcule le chemin relatif correct pour revenir à la racine
    depuis n'importe quelle page du site.
    
    Exemples:
    - index.html (racine) → ""
    - marques/index.html (1 niveau) → "../"
    - marques/bialetti/index.html (2 niveaux) → "../../"
    """
    rel_path = file_path.relative_to(SITE_ROOT)
    depth = len(rel_path.parts) - 1  # -1 car le fichier lui-même ne compte pas
    
    if depth == 0:
        return ""
    else:
        return "../" * depth

def get_optimized_footer(base_path):
    """
    Génère le footer optimisé avec les chemins relatifs corrects
    selon la position de la page dans l'arborescence.
    """
    
    # Si page à la racine, pas de préfixe
    # Si 1 niveau de profondeur, préfixe = "../"
    # Si 2 niveaux, préfixe = "../../"
    prefix = base_path
    
    footer_html = f'''    <!-- Footer Optimized v2.0 -->
    <footer class="footer">
        <div class="container">
            <!-- SECTION 1: Main Branding + Newsletter -->
            <div class="footer-top" style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-bottom: 3rem; padding-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.1);">
                <!-- Brand Column -->
                <div>
                    <h3 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem; color: white;">
                        Italiaanse Percolator
                    </h3>
                    <p style="color: #D1D5DB; line-height: 1.7; margin-bottom: 1.5rem; font-size: 0.95rem;">
                        <strong>De #1 gids voor Italiaanse moka-percolators in Nederland & België.</strong> We testen, vergelijken en reviewen de beste modellen van Bialetti, Alessi en Grosche. Onafhankelijke expertises, geen corporate BS.
                    </p>

                    <!-- Trust Signals -->
                    <div style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem; flex-wrap: wrap;">
                        <div style="font-size: 0.85rem; color: #D1D5DB;">
                            <strong style="display: block; color: white;">10,000+</strong>
                            Lezers/maand
                        </div>
                        <div style="font-size: 0.85rem; color: #D1D5DB;">
                            <strong style="display: block; color: white;">150+</strong>
                            Producten beoordeeld
                        </div>
                        <div style="font-size: 0.85rem; color: #D1D5DB;">
                            <strong style="display: block; color: white;">8+ jaar</strong>
                            Ervaring
                        </div>
                    </div>

                    <!-- Last Updated -->
                    <p style="color: #999; font-size: 0.8rem;">
                        📅 Laatste update: December 2025 | 🔄 Maandelijks geüpdatet
                    </p>
                </div>

                <!-- Newsletter Column -->
                <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                    <h4 style="color: white; margin-bottom: 1rem; font-size: 1rem;">📬 Moka Insiders Newsletter</h4>
                    <p style="color: #D1D5DB; font-size: 0.9rem; margin-bottom: 1rem;">
                        Wekelijkse tips, reviews & exclusive deals. Geen spam, alleen koffie-goodness.
                    </p>

                    <form style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                        <input type="email" placeholder="je@email.com" style="flex: 1; padding: 0.75rem; border: 1px solid #555; border-radius: 6px; background: rgba(255,255,255,0.1); color: white; font-size: 0.9rem;" />
                        <button type="submit" style="background: #D2691E; color: white; padding: 0.75rem 1.5rem; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">Aanmelden</button>
                    </form>

                    <p style="color: #999; font-size: 0.75rem;">
                        ✓ GDPR compliant • 0% spam garantie
                    </p>
                </div>
            </div>

            <!-- SECTION 2: Main Navigation Grid -->
            <div class="footer-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
                <!-- COLUMN 1: Gidsen & Handleidingen -->
                <div class="footer-section">
                    <h4 style="color: white; margin-bottom: 1.2rem; font-size: 0.95rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Gidsen & Handleidingen</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}beste-italiaanse-percolators.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem; transition: color 0.2s;">🏆 Top 10 Beste Percolators</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}koopgids/index.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem; transition: color 0.2s;">📖 Uitgebreide Koopgids</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}marques/index.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem; transition: color 0.2s;">⚖️ Merk Vergelijking</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}koopgids/hoe-kies-je-de-juiste-percolator.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem; transition: color 0.2s;">📏 Maatgids</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}koopgids/italiaanse-percolator-gebruiken-handleiding.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem; transition: color 0.2s;">☕ Zettips</a></li>
                    </ul>
                </div>

                <!-- COLUMN 2: All Brands -->
                <div class="footer-section">
                    <h4 style="color: white; margin-bottom: 1.2rem; font-size: 0.95rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Alle Merken</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}marques/bialetti/" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">Bialetti Percolators</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}marques/alessi/" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">Alessi Percolators</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}marques/grosche/" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">Grosche Percolators</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}marques/index.html" style="color: #28a745; font-weight: 600; text-decoration: none; font-size: 0.9rem;">→ Alle Merken Overzicht</a></li>
                    </ul>
                </div>

                <!-- COLUMN 3: Populaire Reviews -->
                <div class="footer-section">
                    <h4 style="color: white; margin-bottom: 1.2rem; font-size: 0.95rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Populaire Reviews</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}alessi-pulcina-review.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">Alessi Pulcina Review</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}bialetti-moka-review.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">Bialetti Moka Express</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}grosche-milano-review.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">Grosche Milano Review</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}boutique.html" style="color: #D2691E; font-weight: 600; text-decoration: none; font-size: 0.9rem;">🛍️ Shop Boutique</a></li>
                    </ul>
                </div>

                <!-- COLUMN 4: Bedrijf -->
                <div class="footer-section">
                    <h4 style="color: white; margin-bottom: 1.2rem; font-size: 0.95rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Bedrijf</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}over-ons.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">👥 Over Ons</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}contact.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">💬 Contact</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}privacy.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">🔐 Privacybeleid</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="{prefix}disclaimer.html" style="color: #D1D5DB; text-decoration: none; font-size: 0.9rem;">⚖️ Disclaimer</a></li>
                    </ul>
                </div>
            </div>

            <!-- SECTION 3: Social & Trust -->
            <div class="footer-mid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem; padding-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.1);">
                <!-- Social Links -->
                <div>
                    <h4 style="color: white; margin-bottom: 1rem; font-size: 0.9rem; font-weight: 700;">Volg Ons</h4>
                    <div style="display: flex; gap: 1rem;">
                        <a href="#" aria-label="Facebook" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: white; text-decoration: none; transition: background 0.2s;">f</a>
                        <a href="#" aria-label="Twitter" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: white; text-decoration: none; transition: background 0.2s;">𝕏</a>
                        <a href="#" aria-label="Instagram" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: white; text-decoration: none; transition: background 0.2s;">📷</a>
                        <a href="#" aria-label="YouTube" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: white; text-decoration: none; transition: background 0.2s;">▶️</a>
                    </div>
                </div>

                <!-- Trust Badges -->
                <div>
                    <h4 style="color: white; margin-bottom: 1rem; font-size: 0.9rem; font-weight: 700;">Vertrouwen & Veiligheid</h4>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap; font-size: 0.8rem; color: #D1D5DB;">
                        <span style="display: flex; align-items: center; gap: 0.5rem;">
                            <strong>✓</strong> GDPR Compliant
                        </span>
                        <span style="display: flex; align-items: center; gap: 0.5rem;">
                            <strong>✓</strong> Reclamevrije Reviews
                        </span>
                        <span style="display: flex; align-items: center; gap: 0.5rem;">
                            <strong>✓</strong> Transparante Affiliate
                        </span>
                    </div>
                </div>
            </div>

            <!-- SECTION 4: Bottom Bar -->
            <div class="footer-bottom" style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 1.5rem;">
                    <!-- Left: Copyright & Disclosure -->
                    <div>
                        <p style="color: #D1D5DB; font-size: 0.85rem; line-height: 1.6; margin: 0;">
                            <strong style="color: white;">© 2025 Italiaanse Percolator.</strong> Alle rechten voorbehouden.
                            <br /><br />
                            <strong style="color: #999;">Affiliate Kennisgeving:</strong> Als Amazon & Bol.com partner verdienen wij aan kwalificerende aankopen. Dit beïnvloedt onze reviews niet – we zeggen altijd de waarheid.
                        </p>
                    </div>

                    <!-- Right: Additional Links -->
                    <div style="text-align: right;">
                        <p style="color: #999; font-size: 0.85rem; margin: 0 0 1rem 0;">
                            🌍 Beschikbaar in: <strong style="color: white;">Nederlands</strong>
                        </p>
                        <p style="color: #999; font-size: 0.8rem; margin: 0;">
                            <a href="#top" style="color: #D2691E; text-decoration: none;">Terug naar boven ↑</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </footer>'''
    
    return footer_html

def update_footer_in_file(file_path):
    """
    Met à jour le footer dans un fichier HTML donné.
    """
    try:
        # Lire le contenu du fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si le fichier contient un footer
        if '<footer' not in content.lower():
            print(f"⚠️  Pas de footer trouvé dans: {file_path.name}")
            return False
        
        # Calculer le chemin relatif correct
        base_path = get_relative_path(file_path)
        
        # Générer le nouveau footer avec les bons chemins
        new_footer = get_optimized_footer(base_path)
        
        # Pattern pour matcher le footer actuel (tout entre <footer> et </footer>)
        footer_pattern = r'<footer[^>]*>.*?</footer>'
        
        # Vérifier qu'on trouve bien le footer
        if not re.search(footer_pattern, content, re.DOTALL | re.IGNORECASE):
            print(f"⚠️  Footer pattern non trouvé dans: {file_path.name}")
            return False
        
        # Remplacer le footer
        new_content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL | re.IGNORECASE)
        
        # Sauvegarder le fichier
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Footer mis à jour: {file_path.relative_to(SITE_ROOT)} (depth: {len(file_path.relative_to(SITE_ROOT).parts) - 1})")
        return True
        
    except Exception as e:
        print(f"❌ Erreur avec {file_path.name}: {str(e)}")
        return False

def main():
    """
    Fonction principale: trouve tous les fichiers HTML et met à jour leurs footers.
    """
    print("🚀 Démarrage de la mise à jour des footers...")
    print("=" * 70)
    
    # Trouver tous les fichiers HTML (exclure les backups et templates)
    html_files = list(SITE_ROOT.rglob("*.html"))
    
    # Filtrer les fichiers à exclure
    excluded_patterns = ['_old', '_backup', 'template', 'test']
    html_files = [
        f for f in html_files 
        if not any(pattern in str(f).lower() for pattern in excluded_patterns)
    ]
    
    print(f"📁 {len(html_files)} fichiers HTML trouvés\n")
    
    # Compter les succès
    success_count = 0
    failed_count = 0
    
    # Mettre à jour chaque fichier
    for html_file in sorted(html_files):
        if update_footer_in_file(html_file):
            success_count += 1
        else:
            failed_count += 1
    
    # Résumé
    print("\n" + "=" * 70)
    print(f"✅ Succès: {success_count}/{len(html_files)}")
    if failed_count > 0:
        print(f"❌ Échecs: {failed_count}")
    print("🎉 Mise à jour terminée!")

if __name__ == "__main__":
    main()
