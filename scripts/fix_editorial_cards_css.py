#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('/Users/marc/Desktop/italiaanse-percolator')
TARGETS = []
TARGETS.extend(ROOT.glob('*-review.html'))
TARGETS.extend((ROOT / 'koopgids').glob('*.html'))
TARGETS.extend((ROOT / 'marques').glob('**/*.html'))
TARGETS.extend([ROOT / 'alle-reviews.html', ROOT / 'beste-italiaanse-percolators.html', ROOT / 'vergelijking/index.html', ROOT / 'vergelijking/bialetti-vs-alessi.html'])

replacements = [
    ('border: 1px solid var(--border); border-radius: 0.5rem; border: 1px solid var(--border); border-radius: 0.5rem;', 'border: 1px solid var(--border); border-radius: 0.5rem;'),
    ('border: 1px solid var(--border); border: 1px solid var(--border); border-radius: 0.5rem;', 'border: 1px solid var(--border); border-radius: 0.5rem;'),
    ('style="background: #f5f0ea; "', 'style="background: #f5f0ea; border: 1px solid var(--border); border-radius: 0.5rem; padding: 1rem;"'),
    ('style="background: var(--surface-soft);"', 'style="background: var(--surface-soft); border: 1px solid var(--border); border-radius: 0.5rem; padding: 1rem;"'),
    ('font-size: 1 color:', 'font-size: 1.2rem; color:'),
    ('width: 100 max-width:', 'width: 100%; max-width:'),
    ('width: 100 border-radius:', 'width: 100%; border-radius:'),
    ('width: 100 font-size:', 'width: 100%; font-size:'),
    ('width: 100 background:', 'width: 100%; background:'),
    ('height: 100 background:', 'height: 100%; background:'),
    ('width: 100"', 'width: 100%;"'),
    ('style="width: 100"', 'style="width: 100%;"'),
]

for path in sorted(set(TARGETS)):
    if not path.exists() or '/producten/' in str(path):
        continue
    original = path.read_text(encoding='utf-8', errors='ignore')
    content = original
    for old, new in replacements:
        content = content.replace(old, new)

    content = re.sub(r'<div class="card([^\"]*)" style="([^"]*)" style="background: #f5f0ea; ">', r'<div class="card\1" style="\2 background: #f5f0ea; border: 1px solid var(--border); border-radius: 0.5rem; padding: 1rem;">', content)
    content = re.sub(r'<div class="card([^\"]*)" style="([^"]*)" style="background: var\(--surface-soft\);">', r'<div class="card\1" style="\2 background: var(--surface-soft); border: 1px solid var(--border); border-radius: 0.5rem; padding: 1rem;">', content)
    content = re.sub(r'<div class="card([^\"]*)" style="([^"]*)" style="max-width: ([^"]*)">', r'<div class="card\1" style="\2 max-width: \3">', content)
    content = re.sub(r'<a href="([^"]*)" class="review-card" style="([^"]*)" style="text-decoration: none;">', r'<a href="\1" class="review-card" style="\2 text-decoration: none;">', content)

    content = re.sub(r'<div style="width: ([0-9]+) height: 100%; background: var\(--coffee\); ">', r'<div style="width: \1%; height: 100%; background: var(--coffee);"></div>', content)
    content = re.sub(r'<div style="width: ([0-9]+) height: 100 background: var\(--coffee\); ">', r'<div style="width: \1%; height: 100%; background: var(--coffee);"></div>', content)

    if content != original:
        path.write_text(content, encoding='utf-8')
        print(path.relative_to(ROOT))
