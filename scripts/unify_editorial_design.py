#!/usr/bin/env python3
"""
Apply uniform editorial design to all pages in marques, reviews, and koopgids categories.
"""

import os
import re
import glob

# List of files to process (excluding already rewritten ones)
marques_files = [
    '/Users/marc/Desktop/italiaanse-percolator/marques/alessi/index.html',
    '/Users/marc/Desktop/italiaanse-percolator/marques/bialetti/fiammetta.html',
    '/Users/marc/Desktop/italiaanse-percolator/marques/grosche/index.html',
    '/Users/marc/Desktop/italiaanse-percolator/marques/index.html'
]

review_files = [
    '/Users/marc/Desktop/italiaanse-percolator/alessi-9090-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/alessi-la-conica-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/alessi-moka-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/alessi-pulcina-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/alle-reviews.html',
    '/Users/marc/Desktop/italiaanse-percolator/bialetti-alpina-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/bialetti-brikka-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/bialetti-dama-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/bialetti-fiammetta-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/bialetti-mini-express-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/bialetti-moka-timer-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/bialetti-musa-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/bialetti-venus-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/cilio-classico-electric-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/cloer-5928-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/delonghi-alicia-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/giannini-giannina-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/grosche-milano-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/rommelsbacher-eko366-review.html',
    '/Users/marc/Desktop/italiaanse-percolator/stelton-collar-review.html'
]

koopgids_files = [
    '/Users/marc/Desktop/italiaanse-percolator/koopgids/beste-koffiebonen-italiaanse-percolator.html',
    '/Users/marc/Desktop/italiaanse-percolator/koopgids/hoe-kies-je-de-juiste-percolator.html',
    '/Users/marc/Desktop/italiaanse-percolator/koopgids/hoe-onderhoud-je-een-percolator.html',
    '/Users/marc/Desktop/italiaanse-percolator/koopgids/italiaanse-percolator-gebruiken-handleiding.html',
    '/Users/marc/Desktop/italiaanse-percolator/koopgids/percolator-vs-espressoapparaat.html',
    '/Users/marc/Desktop/italiaanse-percolator/koopgids/wat-is-italiaanse-percolator-mokapot.html'
]

all_files = marques_files + review_files + koopgids_files

def process_file(filepath):
    """Apply editorial design transformations to a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        print(f"Skipping {filepath} (cannot read)")
        return
    
    original_content = content
    
    # Fix malformed CSS
    content = re.sub(r'border: 1px solid var\(--border\);\s*\.5rem;', 'border: 1px solid var(--border); border-radius: 0.5rem;', content)
    content = re.sub(r'font-size: 0\.75rem;\s*padding: 0\.2rem 0\.6rem;\s*\.2rem;', '', content)
    content = re.sub(r'background: #f5f0ea; font-size: 0\.75rem; padding: 0\.2rem 0\.6rem; \.2rem;', '', content)
    content = re.sub(r'\.2rem;', '', content)
    content = re.sub(r'%;', '', content)
    content = re.sub(r'\.3rem;', '', content)
    
    # Replace section classes with inline editorial styles
    content = re.sub(r'<section class="section-sm">', '<section style="padding: 3rem 0;">', content)
    content = re.sub(r'<section class="section-sm" style="background:var\(--surface-soft\);">', '<section style="background: #fafafa; padding: 3rem 0;">', content)
    content = re.sub(r'<section class="section" style="background:var\(--surface-soft\);">', '<section style="background: #fafafa; padding: 3rem 0;">', content)
    content = re.sub(r'<section class="section">', '<section style="padding: 3rem 0;">', content)
    
    # Replace heading styles with editorial serif headings
    content = re.sub(
        r'<h2 style="font-size: 2rem; font-weight: 700; margin-bottom: var\(--sp-4\); text-align: center;">',
        '<h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1.5rem; text-align: center; color: var(--coffee);">',
        content
    )
    content = re.sub(
        r'<h2 style="font-size: 2rem; font-weight: 700; margin-bottom: var\(--sp-4\);">',
        '<h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1.5rem; color: var(--coffee);">',
        content
    )
    
    # Replace card styles with editorial card styles
    content = re.sub(
        r'<div class="card" style="border: 1px solid var\(--border\); \.5rem; border: 1px solid var\(--border\); border-radius: 0\.5rem;">',
        '<div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">',
        content
    )
    content = re.sub(
        r'<div class="card" style="border: 1px solid var\(--border\); \.5rem; border: 1px solid var\(--border\); border-radius: 0\.5rem;" style="padding: var\(--sp-6\); border-radius: var\(--r-lg\); ">',
        '<div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">',
        content
    )
    
    # Replace gradient buttons with simple coffee buttons
    content = re.sub(
        r'background:linear-gradient\(135deg,var\(--coffee\),#8B4513\)',
        'background: var(--coffee)',
        content
    )
    
    # Replace double borders
    content = re.sub(
        r'border: 1px solid var\(--border\); border: 1px solid var\(--border\);',
        'border: 1px solid var(--border);',
        content
    )
    
    # Replace text-dim class with inline style
    content = re.sub(r'class="text-dim"', 'style="color: var(--text-dim); line-height: 1.7;"', content)
    
    # Replace btn-outline with simple border button
    content = re.sub(
        r'class="btn btn-outline"',
        'style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text);"',
        content
    )
    
    # Replace btn-primary with simple coffee button
    content = re.sub(
        r'class="btn btn-primary"',
        'style="background: var(--coffee); color: white; padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem;"',
        content
    )
    
    # Remove emojis from text
    content = re.sub(r'&#x2615;', '', content)
    content = re.sub(r'&#x1F3A8;', '', content)
    content = re.sub(r'&#x1F4B0;', '', content)
    content = re.sub(r'&#x23F1;', '', content)
    content = re.sub(r'&#x1F9FD;', '', content)
    content = re.sub(r'&#x1F370;', '', content)
    content = re.sub(r'&#x2714;', '', content)
    content = re.sub(r'&#x2715;', '', content)
    content = re.sub(r'&#x274C;', '', content)
    content = re.sub(r'&#x2605;', '', content)
    content = re.sub(r'&#x2606;', '', content)
    content = re.sub(r'&#x1F6CD;', '', content)
    
    # Only write if content changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all files
changed_count = 0
for filepath in all_files:
    if os.path.exists(filepath):
        if process_file(filepath):
            changed_count += 1
            print(f"Updated: {os.path.basename(filepath)}")
    else:
        print(f"Not found: {filepath}")

print(f"\nTotal files updated: {changed_count}")
