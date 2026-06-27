#!/usr/bin/env python3
import os

# Pages à traiter
PAGES_TO_PROCESS = [
    'bialetti-musa-review.html',
    'alessi-9090-review.html',
    'alessi-la-conica-review.html',
    'alessi-moka-review.html',
    'alessi-pulcina-review.html',
    'cilio-classico-electric-review.html',
    'cloer-5928-review.html',
    'delonghi-alicia-review.html',
    'giannini-giannina-review.html',
    'grosche-milano-review.html',
    'rommelsbacher-eko366-review.html',
    'stelton-collar-review.html'
]

for page in PAGES_TO_PROCESS:
    if not os.path.exists(page):
        print(f"Skipping {page} - file not found")
        continue
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Supprimer l'ancienne box incorrecte (qui est après </section>)
    start_marker = '<div class="review-commercial-box">'
    end_marker = '</footer>'
    
    start_index = content.find(start_marker)
    if start_index == -1:
        print(f"Skipping {page} - no specs box found")
        continue
    
    # Trouver le </footer> après la box
    end_index = content.find(end_marker, start_index)
    if end_index == -1:
        print(f"Skipping {page} - could not find closing </footer>")
        continue
    
    # Supprimer la box (inclure les newlines avant)
    new_content = content[:start_index].rstrip() + '\n\n' + content[end_index:]
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Removed old specs box from {page}")

print("Done!")
