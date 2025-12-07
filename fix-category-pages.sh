#!/bin/bash

# Script pour uniformiser la navigation et footer des pages catégories

CATEGORIES_DIR="/Users/marc/Desktop/italiaanse-percolator/categories"

echo "🔧 Uniformisation des pages catégories..."
echo "📁 Répertoire: $CATEGORIES_DIR"

# Navigation de référence
NAV_MENU='                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li><a href="../beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
                    <li><a href="../koopgids/index.html" class="nav-link">Koopgids</a></li>
                    <li><a href="../vergelijking/index.html" class="nav-link">Vergelijking</a></li>
                    <li><a href="../over-ons.html" class="nav-link">Over ons</a></li>
                    <li><a href="../boutique.html" class="nav-link" style="background: #D2691E; color: white; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600;">Winkel</a></li>
                </ul>'

# Footer de référence
FOOTER_CONTENT='    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Italiaanse Percolator</h4>
                    <p style="color: #D1D5DB; line-height: 1.6;">De beste Italiaanse percolators getest en vergeleken. Onafhankelijke reviews voor de perfecte koffie-ervaring.</p>
                </div>
                
                <div class="footer-section">
                    <h4>Reviews</h4>
                    <a href="../beste-italiaanse-percolators.html">Top 10 Percolators</a>
                    <a href="../bialetti-fiammetta-review.html">Bialetti Fiammetta</a>
                    <a href="../bialetti-venus-review.html">Bialetti Venus</a>
                    <a href="../alessi-pulcina-review.html">Alessi Pulcina</a>
                </div>
                
                <div class="footer-section">
                    <h4>Gidsen</h4>
                    <a href="../koopgids/hoe-kies-je-de-juiste-percolator.html">Hoe kies je een percolator?</a>
                    <a href="../koopgids/hoe-onderhoud-je-een-percolator.html">Onderhoud & reiniging</a>
                    <a href="../koopgids/percolator-vs-espressoapparaat.html">Percolator vs espresso</a>
                </div>
                
                <div class="footer-section">
                    <h4>Over ons</h4>
                    <a href="../over-ons.html">Over ons</a>
                    <a href="../contact.html">Contact</a>
                    <a href="../privacy.html">Privacy</a>
                    <a href="../disclaimer.html">Disclaimer</a>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 Italiaanse Percolator. Als partner van Bol.com en Amazon verdienen wij aan kwalificerende aankopen.</p>
            </div>
        </div>
    </footer>'

counter=0
total_files=$(find "$CATEGORIES_DIR" -name "*.html" | wc -l)

# Traiter tous les fichiers HTML dans le dossier categories
for file_path in "$CATEGORIES_DIR"/*.html; do
    if [ -f "$file_path" ]; then
        filename=$(basename "$file_path")
        counter=$((counter + 1))
        
        echo "📝 [$counter/$total_files] Traitement de: $filename"
        
        # Créer un fichier temporaire
        temp_file=$(mktemp)
        
        # Traiter le fichier ligne par ligne
        in_nav_menu=false
        in_footer=false
        skip_until_closing_ul=false
        skip_until_closing_footer=false
        
        while IFS= read -r line; do
            if [[ "$line" == *"<ul class=\"nav-menu\">"* ]]; then
                echo "$line" >> "$temp_file"
                echo "$NAV_MENU" >> "$temp_file"
                skip_until_closing_ul=true
            elif [[ "$skip_until_closing_ul" == true && "$line" == *"</ul>"* ]]; then
                echo "$line" >> "$temp_file"
                skip_until_closing_ul=false
            elif [[ "$skip_until_closing_ul" == true ]]; then
                # Skip les lignes du menu existant
                continue
            elif [[ "$line" == *"<footer"* ]]; then
                echo "$FOOTER_CONTENT" >> "$temp_file"
                skip_until_closing_footer=true
            elif [[ "$skip_until_closing_footer" == true && "$line" == *"</footer>"* ]]; then
                skip_until_closing_footer=false
            elif [[ "$skip_until_closing_footer" == true ]]; then
                # Skip les lignes du footer existant
                continue
            else
                echo "$line" >> "$temp_file"
            fi
        done < "$file_path"
        
        # Remplacer le fichier original
        mv "$temp_file" "$file_path"
        
        echo "   ✅ Navigation et footer uniformisés"
    fi
done

echo ""
echo "🎉 Uniformisation terminée!"
echo "📊 $counter fichiers traités"
echo ""
echo "✅ Toutes les pages catégories ont maintenant:"
echo "   • Navigation identique à la homepage"
echo "   • Footer uniforme"
