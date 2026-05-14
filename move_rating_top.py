#!/usr/bin/env python3
"""
Script pour déplacer le tableau Onze beoordeling au début du contenu
Version simplifiée - Juste déplacer le rating box après le h1
"""

import re
from pathlib import Path

def move_rating_to_top(file_path):
    """Déplace le rating box pour être au début après le h1"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Trouver le rating box - plusieurs formats possibles
    rating_pattern_div = r'<h2[^>]*>Onze beoordeling</h2>\s*<div class="rating-box">.*?</div>'
    rating_pattern_ul = r'<h2[^>]*>Onze beoordeling</h2>\s*<ul>.*?</ul>'
    
    rating_match = re.search(rating_pattern_div, content, re.DOTALL)
    rating_pattern = rating_pattern_div
    if not rating_match:
        rating_match = re.search(rating_pattern_ul, content, re.DOTALL)
        rating_pattern = rating_pattern_ul
    
    if not rating_match:
        print(f"✗ {file_path.name} - Rating box non trouvé")
        return False
    
    rating_box = rating_match.group(0)
    
    # Trouver le h1
    h1_pattern = r'(<h1[^>]*>.*?</h1>)'
    h1_match = re.search(h1_pattern, content)
    
    if not h1_match:
        print(f"✗ {file_path.name} - H1 non trouvé")
        return False
    
    # Supprimer l'ancien rating box
    content = re.sub(rating_pattern, '', content, flags=re.DOTALL)
    
    # Insérer le rating box après le h1
    content = re.sub(h1_pattern, r'\1\n<div class="rating-box-top">\n' + rating_box + '\n</div>\n', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path.name} - Rating box déplacé au début")
        return True
    else:
        print(f"✗ {file_path.name} - Pas de changement")
        return False

def main():
    """Traite tous les fichiers de review qui ont la section Onze beoordeling"""
    directory = Path('.')
    review_files = [
        'alessi-9090-review.html',
        'alessi-la-conica-review.html',
        'alessi-moka-review.html',
        'alessi-pulcina-review.html',
        'bialetti-dama-review.html',
        'bialetti-fiammetta-review.html',
        'bialetti-mini-express-review.html',
        'bialetti-moka-review.html',
        'bialetti-musa-review.html',
        'cilio-classico-electric-review.html',
        'cloer-5928-review.html',
        'delonghi-alicia-review.html',
        'giannini-giannina-review.html',
        'grosche-milano-review.html',
        'rommelsbacher-eko366-review.html',
        'stelton-collar-review.html'
    ]
    
    print(f"Traitement de {len(review_files)} fichiers review avec section Onze beoordeling...\n")
    
    updated_count = 0
    for review_file in review_files:
        file_path = Path(review_file)
        if file_path.exists():
            if move_rating_to_top(file_path):
                updated_count += 1
        else:
            print(f"✗ {review_file} - Non trouvé")
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
