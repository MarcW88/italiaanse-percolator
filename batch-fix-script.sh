#!/bin/bash

# Script pour corriger automatiquement les pages produits
# Usage: ./batch-fix-script.sh

PRODUCTEN_DIR="/Users/marc/Desktop/italiaanse-percolator/producten"

# Liste des pages prioritaires à traiter
PRIORITY_PAGES=(
    "bialetti-moka-express-percolator-2-kops-aluminium.html"
    "bialetti-moka-express-percolator-1-kops-aluminium.html"
    "bialetti-inductieplaatje-voor-inductiekooplaat-o13cm.html"
    "bialetti-mini-express-percolator-2-kops-inductiegeschikt-met-2-kopjes.html"
    "bialetti-brikka-percolator-2-kops-aluminium.html"
)

echo "🚀 Démarrage de la correction automatique des pages produits..."

for page in "${PRIORITY_PAGES[@]}"; do
    file_path="$PRODUCTEN_DIR/$page"
    
    if [ -f "$file_path" ]; then
        echo "📝 Traitement de: $page"
        
        # 1. Correction de la navigation (italiaanse-percolator-kopen.html → boutique.html)
        sed -i '' 's/italiaanse-percolator-kopen\.html/boutique.html/g' "$file_path"
        
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
        fi
        
        echo "✅ $page traité avec succès"
    else
        echo "❌ Fichier non trouvé: $page"
    fi
done

echo "🎉 Correction automatique terminée!"
echo ""
echo "📋 Actions effectuées:"
echo "  - Navigation corrigée (boutique.html)"
echo "  - Favicon ajouté"
echo ""
echo "⚠️  Actions manuelles restantes:"
echo "  - Améliorer les descriptions avec liens homepage"
echo "  - Ajouter FAQ personnalisées"
echo "  - Uniformiser les footers"
