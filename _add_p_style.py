#!/usr/bin/env python3
import re
import glob
import os

review_files = glob.glob('/Users/marc/Desktop/italiaanse-percolator/*review*.html')
review_files = [f for f in review_files if 'alle-reviews' not in f]

for filepath in sorted(review_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add style to <p> tags that don't already have a style attribute
    # Pattern: <p> followed by anything that's not style=
    def add_p_style(match):
        tag = match.group(0)
        if 'style=' in tag:
            return tag  # Already has style, don't modify
        # Add style attribute after <p
        return tag.replace('<p', '<p style="color: var(--text-dim); font-size: 0.95rem; line-height: 1.7;"')
    
    # Match <p> tags (with or without attributes)
    content = re.sub(r'<p(\s+[^>]*)?>', add_p_style, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"OK: {os.path.basename(filepath)}")
