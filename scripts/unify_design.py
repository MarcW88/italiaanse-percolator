#!/usr/bin/env python3
"""
Unify navbar and footer across all HTML pages to match the editorial design.
Handles both root-level pages (href="...") and subdirectory pages (href="../...").
"""

import os
import re

ROOT = '/Users/marc/Desktop/italiaanse-percolator'

# Pages to skip (already done or special)
SKIP = {'boutique.html', 'index.html', 'sitemap.html', 'faq-template-generator.html',
        'boutique_old.html', 'italiaanse-percolator-kopen.html'}


def make_nav(prefix=""):
    """Generate editorial navbar. prefix is '' for root, '../' for subdirs."""
    return f'''    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="{prefix}index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="{prefix}index.html" class="nav-link">Home</a></li>
                    <li><a href="{prefix}beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
                    <li><a href="{prefix}alle-reviews.html" class="nav-link">Reviews</a></li>
                    <li><a href="{prefix}koopgids/index.html" class="nav-link">Koopgids</a></li>
                    <li><a href="{prefix}marques/index.html" class="nav-link">Merken</a></li>
                    <li><a href="{prefix}boutique.html" class="nav-link">Alle modellen</a></li>
                </ul>
            </div>
        </div>
    </nav>'''


def make_footer(prefix=""):
    """Generate minimal editorial footer."""
    return f'''    <footer class="footer">
        <div class="container">
            <div style="display: grid; grid-template-columns: 2fr repeat(3, 1fr); gap: 3rem; margin-bottom: 3rem;">
                <div>
                    <p style="font-family: var(--font-serif); font-size: 1.2rem; color: white; margin-bottom: 1rem;">Italiaanse Percolator</p>
                    <p style="color: #999; font-size: 0.85rem; line-height: 1.7; margin-bottom: 0;">Onafhankelijke gids voor Italiaanse moka-percolators. Wij testen, vergelijken en selecteren de beste modellen sinds 2017.</p>
                </div>
                <div>
                    <h4 style="color: white; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">Gidsen</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}beste-italiaanse-percolators.html" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Top 10 percolators</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}koopgids/index.html" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Koopgids</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}koopgids/hoe-kies-je-de-juiste-percolator.html" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Keuzehulp</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: white; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">Merken</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}marques/bialetti/" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Bialetti</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}marques/alessi/" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Alessi</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}marques/index.html" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Alle merken</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: white; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">Info</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}over-ons.html" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Over ons</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}contact.html" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Contact</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="{prefix}privacy.html" style="color: #aaa; font-size: 0.85rem; text-decoration: none;">Privacy</a></li>
                    </ul>
                </div>
            </div>
            <div style="border-top: 1px solid #333; padding-top: 1.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <p style="color: #666; font-size: 0.8rem; margin: 0;">&copy; 2025 Italiaanse Percolator. Alle rechten voorbehouden.</p>
                <p style="color: #666; font-size: 0.8rem; margin: 0;">Deze site bevat partnerlinks. Bij aankoop ontvangen wij een commissie, zonder extra kosten voor jou.</p>
            </div>
        </div>
    </footer>'''


def get_depth(relpath):
    """Return prefix based on directory depth."""
    parts = relpath.split('/')
    depth = len(parts) - 1
    if depth == 0:
        return ""
    elif depth == 1:
        return "../"
    elif depth == 2:
        return "../../"
    return "../" * depth


def process_file(filepath, relpath):
    """Replace navbar and footer in a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    prefix = get_depth(relpath)

    # Replace navbar: from <nav to </nav>
    nav_match = re.search(r'<nav\b[^>]*>.*?</nav>', content, re.DOTALL)
    if nav_match:
        content = content[:nav_match.start()] + make_nav(prefix) + content[nav_match.end():]

    # Replace footer: from <footer to </footer> (including any comments before it)
    # First remove footer comments like <!-- Footer Optimized v2.0 -->
    content = re.sub(r'\s*<!-- Footer[^>]*-->\s*', '\n', content)

    footer_match = re.search(r'<footer\b[^>]*>.*?</footer>', content, re.DOTALL)
    if footer_match:
        content = content[:footer_match.start()] + make_footer(prefix) + content[footer_match.end():]

    # Also remove the sticky CTA button if present
    content = re.sub(r'<!-- Sticky CTA.*?</div>\s*', '', content, flags=re.DOTALL)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    updated = 0
    skipped = 0
    errors = 0

    # Collect all HTML files
    html_files = []

    # Root level
    for f in os.listdir(ROOT):
        if f.endswith('.html') and f not in SKIP:
            html_files.append((os.path.join(ROOT, f), f))

    # Subdirectories
    for subdir in ['koopgids', 'marques', 'marques/bialetti', 'marques/alessi',
                    'marques/grosche', 'vergelijking']:
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
