#!/usr/bin/env python3
import re
import glob
import os

review_files = glob.glob('/Users/marc/Desktop/italiaanse-percolator/*review*.html')
review_files = [f for f in review_files if 'alle-reviews' not in f]

for filepath in sorted(review_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace image src paths to use ../Images/ prefix
    # Match img src with various patterns and replace with ../Images/filename
    def fix_image_path(match):
        full_tag = match.group(0)
        # Extract the current src value
        src_match = re.search(r'src="([^"]+)"', full_tag)
        if not src_match:
            return full_tag
        
        current_src = src_match.group(1)
        
        # If it already has ../Images/, skip
        if '../Images/' in current_src or 'Images/' in current_src:
            return full_tag
        
        # Extract just the filename
        filename = current_src.split('/')[-1]
        
        # Replace with ../Images/filename
        new_src = f'../Images/{filename}'
        return full_tag.replace(f'src="{current_src}"', f'src="{new_src}"')
    
    # Match img tags
    content = re.sub(r'<img[^>]+>', fix_image_path, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"OK: {os.path.basename(filepath)}")
