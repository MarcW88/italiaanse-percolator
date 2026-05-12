#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('/Users/marc/Desktop/italiaanse-percolator')
TARGETS = []
TARGETS.extend(ROOT.glob('*-review.html'))
TARGETS.extend((ROOT / 'koopgids').glob('*.html'))
TARGETS.extend((ROOT / 'marques').glob('**/*.html'))
TARGETS.extend([ROOT / 'alle-reviews.html', ROOT / 'beste-italiaanse-percolators.html', ROOT / 'vergelijking/index.html', ROOT / 'vergelijking/bialetti-vs-alessi.html'])

for path in sorted(set(TARGETS)):
    if not path.exists():
        continue
    original = path.read_text(encoding='utf-8', errors='ignore')
    content = original

    # Merge invalid duplicate style attributes on the same element.
    content = re.sub(r'style="([^"]*)"\s+style="([^"]*)"', lambda m: f'style="{m.group(1).strip()} {m.group(2).strip()}"', content)

    # Fix avatar blocks where the initial letter div was never closed.
    content = re.sub(
        r'(display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">)([A-Z])\s*\n\s*<div>',
        r'\1\2</div>\n                      <div>',
        content,
    )

    # Fix common two-column card/list blocks where the first column div was not closed before the second starts.
    content = re.sub(r'(</ul>)\s*\n\s*<div>\s*\n\s*<h4', r'\1\n                    </div>\n                    <div>\n                      <h4', content)
    content = re.sub(r'(</ul>)\s*\n\s*<div>\s*\n\s*<h5', r'\1\n                    </div>\n                    <div>\n                      <h5', content)
    content = re.sub(r'(</p>)\s*\n\s*<div>\s*\n\s*<h5', r'\1\n                    </div>\n                    <div>\n                      <h5', content)

    # Normalize remaining broken CSS fragments.
    content = content.replace('width: 100 max-width:', 'width: 100%; max-width:')
    content = content.replace('width: 100%; max-width: 700px;', 'width: 100%; max-width: 700px;')
    content = content.replace('width: 100%; ;', 'width: 100%;')
    content = content.replace('height: 100%; ;', 'height: 100%;')
    content = content.replace('border: 1px solid var(--border); border-radius: 0.5rem; border: 1px solid var(--border); border-radius: 0.5rem;', 'border: 1px solid var(--border); border-radius: 0.5rem;')

    if content != original:
        path.write_text(content, encoding='utf-8')
        print(path.relative_to(ROOT))
