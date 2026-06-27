#!/usr/bin/env python3
import re
import glob
import os

review_files = glob.glob('/Users/marc/Desktop/italiaanse-percolator/*review*.html')
review_files = [f for f in review_files if 'alle-reviews' not in f]

for filepath in sorted(review_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add style to <h2> tags that don't already have a style attribute
    def add_h2_style(match):
        tag = match.group(0)
        if 'style=' in tag:
            return tag  # Already has style, don't modify
        # Add style attribute after <h2
        return tag.replace('<h2', '<h2 style="font-family: var(--font-serif); font-weight: 400; font-size: 1.5rem; margin-bottom: 2rem;"')
    
    # Match <h2> tags (with or without attributes)
    content = re.sub(r'<h2(\s+[^>]*)?>', add_h2_style, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"OK: {os.path.basename(filepath)}")
