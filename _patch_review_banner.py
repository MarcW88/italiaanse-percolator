#!/usr/bin/env python3
import re, glob, os

review_files = glob.glob('/Users/marc/Desktop/italiaanse-percolator/*review*.html')
review_files = [f for f in review_files if 'alle-reviews' not in f]

for filepath in sorted(review_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract H1 text
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    if not h1_match:
        print(f"SKIP (no h1): {os.path.basename(filepath)}")
        continue
    title = h1_match.group(1).strip()

    # Case 1: old-style breadcrumb div (not yet converted)
    old_breadcrumb = re.search(
        r'<div class="container">\s*<div class="breadcrumbs">.*?</div>\s*</div>',
        content, re.DOTALL
    )
    # Case 2: already converted banner but missing h1
    already_banner = re.search(
        r'<section style="background: #f5f0ea;[^"]*">\s*<div class="container">\s*<p[^>]*>.*?</p>\s*</div>\s*</section>',
        content, re.DOTALL
    )

    new_banner = (
        '<section style="background: #f5f0ea; padding: 3rem 0 2.5rem;">\n'
        '<div class="container">\n'
        '<p style="font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.75rem;">'
        '<a href="index.html" style="color: var(--text-light); text-decoration: none;">Home</a>'
        ' / <a href="alle-reviews.html" style="color: var(--text-light); text-decoration: none;">Reviews</a>'
        f' / {title}</p>\n'
        f'<h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3vw, 2.4rem); font-weight: 400; margin-bottom: 0;">{title}</h1>\n'
        '</div>\n'
        '</section>'
    )

    if old_breadcrumb:
        content = content[:old_breadcrumb.start()] + new_banner + content[old_breadcrumb.end():]
    elif already_banner:
        content = content[:already_banner.start()] + new_banner + content[already_banner.end():]
    else:
        print(f"SKIP (unknown structure): {os.path.basename(filepath)}")
        continue

    # Remove old h1 from article-content (target specifically the one right after article-content div)
    content = re.sub(r'(<div class="article-content">)\s*<h1[^>]*>.*?</h1>\s*', r'\1\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"OK: {os.path.basename(filepath)} — {title}")
