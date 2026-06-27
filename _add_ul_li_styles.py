#!/usr/bin/env python3
import os
import glob
import re

# Trouver tous les fichiers de review
review_files = glob.glob('*-review.html')

for file_path in review_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remplacer <ul> par <ul style="color: var(--text-dim); font-size: 0.95rem; line-height: 1.7;">
    content = re.sub(r'<ul>', '<ul style="color: var(--text-dim); font-size: 0.95rem; line-height: 1.7;">', content)
    
    # Remplacer <li> par <li style="color: var(--text-dim); font-size: 0.95rem; line-height: 1.7;">
    content = re.sub(r'<li>', '<li style="color: var(--text-dim); font-size: 0.95rem; line-height: 1.7;">', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes needed for {file_path}")

print("Done!")
