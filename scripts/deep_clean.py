#!/usr/bin/env python3
"""
Deep clean: remove all remaining old design elements.
- Cards with border-left colored borders
- All emojis from content (not just footer)
- Heavy inline styles
- Double borders
- Color accent overuse (#D2691E)
"""

import os
import re

ROOT = '/Users/marc/Desktop/italiaanse-percolator'

SKIP = {'.git', 'node_modules', 'producten', 'scripts', 'categories', 'blog', 'templates',
        'sitemap.html', 'faq-template-generator.html', 'boutique_old.html', 'italiaanse-percolator-kopen.html'}


def remove_all_emojis(content):
    """Remove ALL emojis from content, not just footer."""
    # Extended emoji list including those in content
    emojis = ['🏆', '📬', '🔥', '⭐', '✅', '🛍️', '👥', '💬', '🔐', '⚖️', '📖', '⚡', '🎯', '💡', '🌍', '📅', '🔄',
              '☕', '🎨', '💰', '⏱️', '🛡️', '✓', '✗', '❌', '✔', '➕', '➖', '🔔', '📢', '📣', '🎉', '🎊', '🏅',
              '🥇', '🥈', '🥉', '📍', '🔍', '🔎', '💪', '🚀', '⚙️', '🛠️', '🔧', '📊', '📈', '📉', '💯', '🆗', '🆘',
              '🤝', '👍', '👎', '👌', '✋', '👏', '🙌', '👐', '🤲', '🙏', '💼', '📁', '📂', '🗂️', '📋', '📝', '📄',
              '📃', '🎵', '🎶', '🎧', '🎬', '🎥', '📷', '📸', '🖼️', '🖥️', '💻', '📱', '⌨️', '🖱️', '🖨️', '📠',
              '💾', '💿', '📀', '🎞️', '📼', '🔌', '🔋', '🔦', '🏮', '📡', '🔌', '🔋', '🔦', '🏮', '📡',
              '💡', '🔦', '🏮', '📡', '💡', '🔦', '🏮', '📡', '💡', '🔦', '🏮', '📡']
    for emoji in emojis:
        content = content.replace(emoji, '')
    return content


def simplify_colored_borders(content):
    """Replace border-left colored borders with simple borders."""
    # Pattern: border-left: 4px solid #D2691E
    content = re.sub(r'border-left:\s*\d+px\s+solid\s*#[a-fA-F0-9]+;?', '', content)
    # Remove border-radius on cards that have it
    content = re.sub(r'border-radius:\s*[0-8px]+;?', '', content)
    # Add simple border if style has other border properties
    content = re.sub(r'style="([^"]*border:[^;]*;[^"]*)"', r'style="\1 border: 1px solid var(--border); border-radius: 0.5rem;"', content)
    return content


def remove_double_borders(content):
    """Remove duplicate border declarations."""
    # Pattern: style="border: ... border: ..."
    content = re.sub(r'style="([^"]*border:\s*[^;]*;)\s*(border:\s*[^;]*;[^"]*)"', r'style="\1"', content)
    return content


def reduce_color_overuse(content):
    """Reduce overuse of #D2691E accent color."""
    # Replace #D2691E with var(--coffee) where appropriate
    content = re.sub(r'#D2691E', 'var(--coffee)', content)
    # Remove color: var(--coffee) from text where it's not needed
    content = re.sub(r'color:\s*var\(--coffee\);?\s*', '', content)
    return content


def simplify_inline_styles(content):
    """Simplify heavy inline styles."""
    # Remove padding-bottom and padding-top where they're excessive
    content = re.sub(r'padding-bottom:\s*[2-9]rem;?', '', content)
    content = re.sub(r'padding-top:\s*[2-9]rem;?', '', content)
    # Remove margin-bottom where it's excessive
    content = re.sub(r'margin-bottom:\s*[2-9]rem;?', '', content)
    return content


def clean_card_bodies(content):
    """Remove nested card-body divs that create double borders."""
    content = re.sub(r'<div class="card-body"[^>]*>(.*?)</div>', r'\1', content, flags=re.DOTALL)
    return content


def process_file(filepath, relpath):
    """Apply all deep clean transformations."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Apply transformations
    content = remove_all_emojis(content)
    content = simplify_colored_borders(content)
    content = remove_double_borders(content)
    content = reduce_color_overuse(content)
    content = simplify_inline_styles(content)
    content = clean_card_bodies(content)

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

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for f in filenames:
            if not f.endswith('.html'): continue
            fp = os.path.join(dirpath, f)
            relpath = os.path.relpath(fp, ROOT)
            html_files.append((fp, relpath))

    print(f"Processing {len(html_files)} files...\n")

    for filepath, relpath in sorted(html_files, key=lambda x: x[1]):
        try:
            changed = process_file(filepath, relpath)
            if changed:
                updated += 1
                print(f"  ✓ {relpath}")
            else:
                skipped += 1
                print(f"  - {relpath}")
        except Exception as e:
            errors += 1
            print(f"  ✗ {relpath}: {e}")

    print(f"\n=== DONE ===")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors:  {errors}")


if __name__ == '__main__':
    main()
