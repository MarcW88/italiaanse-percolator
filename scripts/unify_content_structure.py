#!/usr/bin/env python3
"""
Unify content structure across all pages to match editorial style.
Replaces dark heroes, gradient buttons, emojis, card shadows with editorial equivalents.
Preserves actual content text.
"""

import os
import re

ROOT = '/Users/marc/Desktop/italiaanse-percolator'

# Pages to skip
SKIP = {'index.html', 'boutique.html', 'sitemap.html', 'faq-template-generator.html',
        'boutique_old.html', 'italiaanse-percolator-kopen.html', 'categories', 'producten',
        'scripts', 'images', 'Images', 'node_modules', '.git', 'blog', 'templates'}


def replace_dark_hero(content):
    """Replace dark gradient hero with cream editorial header."""
    # Pattern: <section with linear-gradient background
    pattern = r'<section[^>]*background:\s*linear-gradient[^>]*>(.*?)</section>'
    
    def replacer(match):
        inner = match.group(1)
        # Extract title and description if present
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', inner, re.DOTALL)
        desc_match = re.search(r'<p[^>]*>(.*?)</p>', inner, re.DOTALL)
        
        title = title_match.group(1).strip() if title_match else "Kopje"
        desc = desc_match.group(1).strip() if desc_match else ""
        
        # Remove text-shadow and other inline styles from title
        title = re.sub(r'text-shadow:[^;]+;?', '', title)
        title = re.sub(r'color:\s*white;', '', title)
        
        # Clean up description
        desc = re.sub(r'text-shadow:[^;]+;?', '', desc)
        desc = re.sub(r'color:\s*rgba?\([^)]+\);?', '', desc)
        
        return f'''  <section style="background: #f5f0ea; padding: 3rem 0 2.5rem;">
    <div class="container" style="max-width: 780px;">
      <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3vw, 2.4rem); font-weight: 400; margin-bottom: 0.75rem; color: var(--coffee);">{title}</h1>
      {f'<p style="color: var(--text-dim); font-size: 1rem; max-width: 540px;">{desc}</p>' if desc else ''}
    </div>
  </section>'''
    
    return re.sub(pattern, replacer, content, flags=re.DOTALL)


def replace_gradient_buttons(content):
    """Replace gradient buttons with simple editorial buttons."""
    # Pattern: btn with linear-gradient
    pattern = r'(class="[^"]*btn[^"]*")([^>]*style="[^"]*linear-gradient[^"]*")'
    
    def replacer(match):
        classes = match.group(1)
        # Remove gradient style, keep simple
        return f'{classes} style="background: var(--coffee); color: white; border: none; padding: 0.6rem 1.2rem; border-radius: 0.3rem; font-weight: 600;"'
    
    return re.sub(pattern, replacer, content)


def remove_emojis(content):
    """Remove common emojis from content."""
    emojis = ['🏆', '📬', '🔥', '⭐', '✅', '🛍️', '👥', '💬', '🔐', '⚖️', '📖', '⚡', '🎯', '💡', '🌍', '📅', '🔄']
    for emoji in emojis:
        content = content.replace(emoji, '')
    return content


def simplify_card_shadows(content):
    """Simplify heavy card shadows to editorial borders."""
    # Replace heavy box-shadows with simple borders
    content = re.sub(r'box-shadow:\s*0\s+\d+px\s+\d+px\s+rgba?\([^)]+\);?', '', content)
    # Add simple border if card class exists
    content = re.sub(r'(class="[^"]*card[^"]*")', r'\1 style="border: 1px solid var(--border); border-radius: 0.5rem;"', content)
    return content


def simplify_badges(content):
    """Remove or simplify badges."""
    # Remove review-badge colored backgrounds
    content = re.sub(r'style="background:\s*#[a-fA-F0-9]+;[^"]*"', 'style="background: #f5f0ea; color: var(--coffee); font-size: 0.75rem; padding: 0.2rem 0.6rem; border-radius: 0.2rem;"', content)
    return content


def process_file(filepath, relpath):
    """Apply all transformations to a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Apply transformations
    content = replace_dark_hero(content)
    content = replace_gradient_buttons(content)
    content = remove_emojis(content)
    content = simplify_card_shadows(content)
    content = simplify_badges(content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    updated = 0
    skipped = 0
    errors = 0

    html_files = []

    # Root level
    for f in os.listdir(ROOT):
        if f.endswith('.html') and f not in SKIP:
            html_files.append((os.path.join(ROOT, f), f))

    # Subdirectories
    for subdir in ['koopgids', 'marques', 'marques/bialetti', 'marques/alessi',
                    'marques/grosche', 'vergelijking', 'veelgestelde-vragen',
                    'garantie-retourbeleid']:
        dirpath = os.path.join(ROOT, subdir)
        if os.path.isdir(dirpath):
            for f in os.listdir(dirpath):
                if f.endswith('.html'):
                    relpath = os.path.join(subdir, f)
                    html_files.append((os.path.join(ROOT, relpath), relpath))

    print(f"Processing {len(html_files)} files...\n")

    for filepath, relpath in sorted(html_files, key=lambda x: x[1]):
        try:
            changed = process_file(filepath, relpath)
            if changed:
                updated += 1
                print(f"  ✓ {relpath}")
            else:
                skipped += 1
                print(f"  - {relpath} (no changes)")
        except Exception as e:
            errors += 1
            print(f"  ✗ {relpath}: {e}")

    print(f"\n=== DONE ===")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors:  {errors}")


if __name__ == '__main__':
    main()
