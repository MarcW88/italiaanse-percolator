#!/usr/bin/env python3
"""
Script pour déplacer le tableau Onze beoordeling au-dessus dans un encadré avec l'image
"""

import re
from pathlib import Path

def move_rating_box(file_path):
    """Déplace le rating box pour être au-dessus avec l'image"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Trouver le rating box (avec ou sans id) - deux formats possibles
    # Format 1: div class="rating-box"
    # Format 2: simple ul list
    rating_pattern_div = r'<h2[^>]*>Onze beoordeling</h2>\s*<div class="rating-box">.*?</div>'
    rating_pattern_ul = r'<h2[^>]*>Onze beoordeling</h2>\s*<ul>.*?</ul>'
    
    rating_match = re.search(rating_pattern_div, content, re.DOTALL)
    rating_pattern = rating_pattern_div  # Pour le re.sub plus tard
    if not rating_match:
        rating_match = re.search(rating_pattern_ul, content, re.DOTALL)
        rating_pattern = rating_pattern_ul  # Pour le re.sub plus tard
    
    if not rating_match:
        print(f"✗ {file_path.name} - Rating box non trouvé")
        return False
    
    rating_box = rating_match.group(0)
    
    # Trouver l'image hero et la légende (supporte blog-hero-image et product-image)
    hero_image_pattern = r'<img alt="[^"]*" class="(blog-hero-image|product-image)" src="[^"]*"/>'
    hero_caption_pattern = r'<p class="(blog-hero-caption|product-image-caption)">.*?</p>'
    
    hero_image_match = re.search(hero_image_pattern, content)
    hero_caption_match = re.search(hero_caption_pattern, content, re.DOTALL)
    
    if not hero_image_match:
        print(f"✗ {file_path.name} - Hero image non trouvé")
        return False
    
    hero_image = hero_image_match.group(0)
    hero_caption = hero_caption_match.group(0) if hero_caption_match else ""
    
    # Créer le nouvel encadré avec image et rating
    new_box = f'''<div class="review-hero-box">
{hero_image}
{hero_caption}
{rating_box}
</div>'''
    
    # Supprimer l'ancien rating box
    content = re.sub(rating_pattern, '', content, flags=re.DOTALL)
    
    # Supprimer l'ancienne image hero et légende
    content = re.sub(hero_image_pattern, '', content)
    if hero_caption_match:
        content = re.sub(hero_caption_pattern, '', content, flags=re.DOTALL)
    
    # Insérer le nouvel encadré après le h1
    h1_pattern = r'(<h1 id="top">.*?</h1>)'
    content = re.sub(h1_pattern, r'\1\n' + new_box, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path.name} - Rating box déplacé")
        return True
    else:
        print(f"✗ {file_path.name} - Pas de changement")
        return False

def main():
    """Traite tous les fichiers de review"""
    directory = Path('.')
    review_files = [
        'bialetti-fiammetta-review.html',
        'bialetti-moka-review.html',
        'bialetti-venus-review.html',
        'bialetti-brikka-review.html',
        'bialetti-alpina-review.html',
        'bialetti-musa-review.html',
        'bialetti-dama-review.html',
        'bialetti-mini-express-review.html',
        'bialetti-moka-timer-review.html',
        'alessi-9090-review.html',
        'alessi-la-conica-review.html',
        'alessi-moka-review.html',
        'alessi-pulcina-review.html',
        'delonghi-alicia-review.html',
        'rommelsbacher-eko366-review.html',
        'cloer-5928-review.html',
        'cilio-classico-electric-review.html',
        'giannini-giannina-review.html',
        'stelton-collar-review.html',
        'grosche-milano-review.html'
    ]
    
    print(f"Traitement de {len(review_files)} fichiers review...\n")
    
    updated_count = 0
    for review_file in review_files:
        file_path = Path(review_file)
        if file_path.exists():
            if move_rating_box(file_path):
                updated_count += 1
        else:
            print(f"✗ {review_file} - Non trouvé")
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
