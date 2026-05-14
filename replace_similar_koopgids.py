#!/usr/bin/env python3
"""
Script pour remplacer la section Soortgelijke artikels dans les pages koopgids
avec la nouvelle structure de cartes avec images
"""

import os
import re
from pathlib import Path

# Nouvelle section Soortgelijke artikels avec cartes et images
NEW_SIMILAR_ARTICLES = '''<!-- Soortgelijke artikels -->
<div class="similar-articles">
<h3>Soortgelijke artikels</h3>
<div class="similar-articles-grid">
<a href="hoe-kies-je-de-juiste-percolator.html" class="similar-article-card">
<img alt="Hoe kies je de juiste percolator" class="similar-article-image" src="https://media.s-bol.com/YG5LYrDqrBv0/PZM67BA/1200x1050.jpg"/>
<div class="similar-article-content">
<h4 class="similar-article-title">Hoe kies je de juiste percolator?</h4>
<p class="similar-article-summary">Complete keuzegids op basis van 50+ tests.</p>
</div>
</a>
<a href="italiaanse-percolator-gebruiken-handleiding.html" class="similar-article-card">
<img alt="Gebruikshandleiding" class="similar-article-image" src="https://media.s-bol.com/YG5LYrDqrBv0/PZM67BA/1200x1050.jpg"/>
<div class="similar-article-content">
<h4 class="similar-article-title">Gebruikshandleiding</h4>
<p class="similar-article-summary">Stap voor stap de perfecte koffie zetten.</p>
</div>
</a>
<a href="percolator-vs-espressoapparaat.html" class="similar-article-card">
<img alt="Percolator vs espressoapparaat" class="similar-article-image" src="https://media.s-bol.com/YG5LYrDqrBv0/PZM67BA/1200x1050.jpg"/>
<div class="similar-article-content">
<h4 class="similar-article-title">Percolator vs espressoapparaat</h4>
<p class="similar-article-summary">Eerlijke vergelijking: kosten, smaak en gemak.</p>
</div>
</a>
</div>
</div>'''

def replace_similar_articles(file_path):
    """Remplace la section Soortgelijke artikels existante par la nouvelle structure"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern pour trouver l'ancienne section
    old_pattern = r'<p class="blog-toc-label">Soortgelijke artikels</p>\s*<div class="blog-related">.*?</div>\s*</div>'
    
    # Remplacer l'ancienne section par la nouvelle
    content = re.sub(old_pattern, NEW_SIMILAR_ARTICLES, content, flags=re.DOTALL)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path.name} - Remplacé")
        return True
    else:
        print(f"✗ {file_path.name} - Non remplacé (pattern non trouvé)")
        return False

def main():
    """Traite tous les fichiers HTML dans le dossier koopgids (sauf _backup)"""
    directory = Path('koopgids')
    html_files = [f for f in directory.glob('*.html') if f.parent.name != '_backup']
    
    print(f"Traitement de {len(html_files)} fichiers koopgids...\n")
    
    updated_count = 0
    for html_file in html_files:
        if replace_similar_articles(html_file):
            updated_count += 1
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
