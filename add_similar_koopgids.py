#!/usr/bin/env python3
"""
Script pour ajouter la section Soortgelijke artikels aux pages du koopgids
"""

import os
from pathlib import Path

# Section Soortgelijke artikels à ajouter
SIMILAR_ARTICLES = '''<!-- Soortgelijke artikels -->
<div class="similar-articles">
<h3>Soortgelijke artikels</h3>
<div class="similar-articles-grid">
<a href="../bialetti-moka-review.html" class="similar-article-card">
<img alt="Bialetti Moka Express" class="similar-article-image" src="https://media.s-bol.com/YG5LYrDqrBv0/PZM67BA/1200x1050.jpg"/>
<div class="similar-article-content">
<h4 class="similar-article-title">Bialetti Moka Express review</h4>
<p class="similar-article-summary">Le modèle original. La classique iconique qui traverse les générations.</p>
</div>
</a>
<a href="../beste-italiaanse-percolators.html" class="similar-article-card">
<img alt="Top 10 Percolators" class="similar-article-image" src="https://media.s-bol.com/YG5LYrDqrBv0/PZM67BA/1200x1050.jpg"/>
<div class="similar-article-content">
<h4 class="similar-article-title">Top 10 Percolators</h4>
<p class="similar-article-summary">Comparatif complet des meilleurs modèles de 2025.</p>
</div>
</a>
<a href="../vergelijking/index.html" class="similar-article-card">
<img alt="Comparatif" class="similar-article-image" src="https://media.s-bol.com/YG5LYrDqrBv0/PZM67BA/1200x1050.jpg"/>
<div class="similar-article-content">
<h4 class="similar-article-title">Comparatif</h4>
<p class="similar-article-summary">Bialetti vs Alessi et autres comparaisons entre marques.</p>
</div>
</a>
</div>
</div>'''

def add_similar_articles(file_path):
    """Ajoute la section Soortgelijke artikels à un fichier HTML"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si la section est déjà présente
    if 'Soortgelijke artikels' in content:
        print(f"✓ {file_path.name} - Déjà présent")
        return False
    
    # Trouver le footer et ajouter la section avant
    if '<footer class="footer">' in content:
        content = content.replace('<footer class="footer">', SIMILAR_ARTICLES + '\n<footer class="footer">')
        print(f"✓ {file_path.name} - Ajouté avant footer")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print(f"✗ {file_path.name} - Footer non trouvé")
        return False

def main():
    """Traite tous les fichiers HTML dans le dossier koopgids (sauf _backup)"""
    directory = Path('koopgids')
    html_files = [f for f in directory.glob('*.html') if f.parent.name != '_backup']
    
    print(f"Traitement de {len(html_files)} fichiers koopgids...\n")
    
    updated_count = 0
    for html_file in html_files:
        if add_similar_articles(html_file):
            updated_count += 1
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
