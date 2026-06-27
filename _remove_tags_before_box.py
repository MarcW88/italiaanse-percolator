#!/usr/bin/env python3
import os
import glob

# Trouver tous les fichiers de review
review_files = glob.glob('*-review.html')

for file_path in review_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chercher la commercial box
    box_marker = '<div class="review-commercial-box">'
    box_index = content.find(box_marker)
    
    if box_index == -1:
        print(f"Skipping {file_path} - no commercial box found")
        continue
    
    # Chercher les balises </section> et </div> avant la box
    # On cherche en arrière depuis la position de la box
    before_box = content[:box_index].rstrip()
    
    # Vérifier si les balises sont présentes
    if before_box.endswith('</div>'):
        # Supprimer </div>
        before_box = before_box[:-6].rstrip()
        print(f"Removed </div> from {file_path}")
    
    if before_box.endswith('</section>'):
        # Supprimer </section>
        before_box = before_box[:-10].rstrip()
        print(f"Removed </section> from {file_path}")
    
    # Reconstruire le contenu
    new_content = before_box + '\n\n' + content[box_index:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Done!")
