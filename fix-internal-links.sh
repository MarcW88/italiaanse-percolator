#!/bin/bash

# Script pour corriger les liens internes dans les descriptions produits
# Remplace index.html#italiaanse-percolator par index.html

PRODUCTEN_DIR="/Users/marc/Desktop/italiaanse-percolator/producten"

echo "🔗 Correction des liens internes dans les descriptions produits..."
echo "📁 Répertoire: $PRODUCTEN_DIR"

counter=0
total_files=$(find "$PRODUCTEN_DIR" -name "*.html" | wc -l)

# Traiter tous les fichiers HTML dans le dossier producten
for file_path in "$PRODUCTEN_DIR"/*.html; do
    if [ -f "$file_path" ]; then
        filename=$(basename "$file_path")
        counter=$((counter + 1))
        
        echo "📝 [$counter/$total_files] Traitement de: $filename"
        
        # Remplacer tous les liens index.html#italiaanse-percolator par index.html
        if grep -q "index.html#italiaanse-percolator" "$file_path"; then
            sed -i '' 's|index\.html#italiaanse-percolator|index.html|g' "$file_path"
            echo "   ✅ Liens corrigés"
        else
            echo "   ℹ️  Aucun lien à corriger"
        fi
    fi
done

echo ""
echo "🎉 Correction des liens terminée!"
echo "📊 $counter fichiers traités"
echo ""
echo "✅ Tous les liens pointent maintenant vers index.html (sans ancre)"
