#!/usr/bin/env python3
"""
Script pour restructurer l'encadré Onze beoordeling dans toutes les pages reviews
- Image à gauche (entièrement visible)
- Notes à droite
- Korte oordeel en-dessous
"""

import re
from pathlib import Path

def restructure_rating_box(file_path):
    """Restructure le rating box avec image à gauche et notes à droite"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Trouver l'image du produit (différents formats possibles)
    image_pattern = r'<img[^>]*class="(blog-hero-image|product-image)"[^>]*src="([^"]+)"[^>]*alt="([^"]+)"'
    image_match = re.search(image_pattern, content)
    
    image_html = ""
    if image_match:
        image_src = image_match.group(2)
        image_alt = image_match.group(3)
        image_html = f'<img alt="{image_alt}" class="rating-hero-image" src="{image_src}"/>'
    
    # Trouver le rating box (div ou ul) - avec ou sans id
    rating_pattern_div = r'<h2[^>]*(?:id="onze-beoordeling")?[^>]*>Onze beoordeling</h2>\s*<div class="rating-box">.*?</div>'
    rating_pattern_ul = r'<h2[^>]*(?:id="onze-beoordeling")?[^>]*>Onze beoordeling</h2>\s*<ul>.*?</ul>'
    
    rating_match = re.search(rating_pattern_div, content, re.DOTALL)
    rating_pattern = rating_pattern_div
    if not rating_match:
        rating_match = re.search(rating_pattern_ul, content, re.DOTALL)
        rating_pattern = rating_pattern_ul
    
    if not rating_match:
        print(f"✗ {file_path.name} - Rating box non trouvé")
        return False
    
    rating_box = rating_match.group(0)
    
    # Trouver le korte oordeel
    kort_pattern = r'<h2[^>]*id="kort-oordeel"[^>]*>.*?</h2>\s*<p>(.*?)</p>'
    kort_match = re.search(kort_pattern, content, re.DOTALL)
    
    kort_html = ""
    if kort_match:
        kort_html = f'''<div class="kort-oordeel-section">
<h2 id="kort-oordeel">Kort oordeel</h2>
<p>{kort_match.group(1)}</p>
</div>'''
    
    # Créer la nouvelle structure avec korte oordeel à l'intérieur
    kort_html_inside = ""
    if kort_match:
        kort_html_inside = f'''<div class="kort-oordeel-section">
<h2 id="kort-oordeel">Oordeel</h2>
<p>{kort_match.group(1)}</p>
</div>'''
    
    new_structure = f'''<div class="rating-box-top">
<h2 id="onze-beoordeling">Onze beoordeling</h2>
<div class="rating-hero-layout">
<div class="rating-hero-image-container">
{image_html}
</div>
<div class="rating-hero-content">
{rating_box}
{kort_html_inside}
</div>
</div>
</div>'''
    
    # Supprimer l'ancien rating box
    content = re.sub(rating_pattern, '', content, flags=re.DOTALL)
    
    # Supprimer l'ancienne korte oordeel
    if kort_match:
        content = re.sub(kort_pattern, '', content, flags=re.DOTALL)
    
    # Insérer la nouvelle structure après le h1
    h1_pattern = r'(<h1[^>]*>.*?</h1>)'
    content = re.sub(h1_pattern, r'\1\n' + new_structure, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path.name} - Rating box restructuré")
        return True
    else:
        print(f"✗ {file_path.name} - Pas de changement")
        return False

def main():
    """Fonction principale"""
    directory = Path('.')
    review_files = [
        'alessi-9090-review.html',
        'alessi-la-conica-review.html',
        'alessi-moka-review.html',
        'alessi-pulcina-review.html',
        'bialetti-alpina-review.html',
        'bialetti-brikka-review.html',
        'bialetti-dama-review.html',
        'bialetti-fiammetta-review.html',
        'bialetti-mini-express-review.html',
        'bialetti-moka-review.html',
        'bialetti-moka-timer-review.html',
        'bialetti-musa-review.html',
        'bialetti-venus-review.html',
        'cilio-classico-electric-review.html',
        'cloer-5928-review.html',
        'delonghi-alicia-review.html',
        'giannini-giannina-review.html',
        'grosche-milano-review.html',
        'rommelsbacher-eko366-review.html',
        'stelton-collar-review.html'
    ]
    
    print(f"Restructuration de {len(review_files)} pages review...\n")
    
    updated_count = 0
    for review_file in review_files:
        file_path = Path(review_file)
        if file_path.exists():
            if restructure_rating_box(file_path):
                updated_count += 1
        else:
            print(f"✗ {review_file} - Non trouvé")
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
