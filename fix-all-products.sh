#!/bin/bash

# Script pour corriger TOUTES les pages produits
# Usage: ./fix-all-products.sh

PRODUCTEN_DIR="/Users/marc/Desktop/italiaanse-percolator/producten"

echo "🚀 Démarrage de la correction de TOUTES les pages produits..."
echo "📁 Répertoire: $PRODUCTEN_DIR"

# Compter le nombre total de fichiers
total_files=$(find "$PRODUCTEN_DIR" -name "*.html" | wc -l)
echo "📊 Total de pages à traiter: $total_files"

counter=0

# Traiter tous les fichiers HTML dans le dossier producten
for file_path in "$PRODUCTEN_DIR"/*.html; do
    if [ -f "$file_path" ]; then
        filename=$(basename "$file_path")
        counter=$((counter + 1))
        
        echo "📝 [$counter/$total_files] Traitement de: $filename"
        
        # 1. Correction de la navigation (italiaanse-percolator-kopen.html → boutique.html)
        if grep -q "italiaanse-percolator-kopen.html" "$file_path"; then
            sed -i '' 's/italiaanse-percolator-kopen\.html/boutique.html/g' "$file_path"
            echo "   ✅ Navigation corrigée"
        fi
        
        # 2. Ajout du favicon si manquant
        if ! grep -q "favicon.svg" "$file_path"; then
            sed -i '' '/link rel="canonical"/a\
    \
    <!-- Favicon -->\
    <link rel="icon" type="image/svg+xml" href="../favicon.svg">\
    <link rel="icon" type="image/svg+xml" sizes="16x16" href="../favicon-simple.svg">\
    <link rel="apple-touch-icon" sizes="180x180" href="../favicon.svg">\
    <meta name="theme-color" content="#D2691E">
' "$file_path"
            echo "   ✅ Favicon ajouté"
        fi
        
        # 3. Vérifier si la description est trop courte (moins de 50 caractères)
        desc_length=$(grep -A 3 "Productbeschrijving" "$file_path" | grep -o '<p[^>]*>.*</p>' | sed 's/<[^>]*>//g' | wc -c)
        if [ "$desc_length" -lt 50 ]; then
            echo "   ⚠️  Description courte détectée ($desc_length chars)"
        fi
        
        # 4. Vérifier si FAQ est personnalisée
        if ! grep -q "Veelgestelde Vragen over de" "$file_path"; then
            echo "   ⚠️  FAQ non personnalisée"
        fi
        
        # 5. Vérifier si footer est uniformisé
        if ! grep -q 'footer class="footer"' "$file_path"; then
            echo "   ⚠️  Footer non uniformisé"
        fi
        
        echo "   ✅ $filename analysé"
    fi
done

echo ""
echo "🎉 Correction automatique terminée!"
echo ""
echo "📋 Actions effectuées sur $counter pages:"
echo "  ✅ Navigation corrigée (boutique.html)"
echo "  ✅ Favicon ajouté"
echo ""
echo "⚠️  Actions manuelles restantes:"
echo "  - Améliorer les descriptions courtes avec liens homepage"
echo "  - Ajouter FAQ personnalisées"
echo "  - Uniformiser les footers"
echo ""
echo "💡 Utilisez faq-template-generator.html pour créer des FAQ personnalisées"
