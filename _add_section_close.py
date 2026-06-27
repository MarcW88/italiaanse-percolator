#!/usr/bin/env python3
import os

# Pages à traiter
PAGES_TO_PROCESS = [
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
    
    # Vérifier si </section> est déjà présent avant <footer>
    footer_index = content.find('<footer>')
    if footer_index == -1:
        print(f"Skipping {page} - no footer found")
        continue
    
    # Chercher </section> avant le footer
    section_before_footer = content.rfind('</section>', 0, footer_index)
    if section_before_footer != -1:
        print(f"Skipping {page} - </section> already present before footer")
        continue
    
    # Ajouter </section> avant <footer>
    new_content = content[:footer_index].rstrip() + '\n</section>\n\n' + content[footer_index:]
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Added </section> to {page}")

print("Done!")
