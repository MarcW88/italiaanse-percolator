#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('/Users/marc/Desktop/italiaanse-percolator')
TARGETS = []
TARGETS.extend(ROOT.glob('*-review.html'))
TARGETS.extend((ROOT / 'koopgids').glob('*.html'))
TARGETS.extend([ROOT / 'beste-italiaanse-percolators.html', ROOT / 'alle-reviews.html'])
TARGETS.extend((ROOT / 'vergelijking').glob('*.html'))

for path in sorted(set(TARGETS)):
    if not path.exists():
        continue
    original = path.read_text(encoding='utf-8', errors='ignore')
    content = original

    content = re.sub(r'<body(?![^>]*class=)>', '<body class="blog-page">', content, count=1)
    content = re.sub(r'<body class="(?![^"]*blog-page)([^"]*)">', lambda m: f'<body class="{m.group(1).strip()} blog-page">', content, count=1)

    content = re.sub(
        r'width:([0-9]+)height:100background:var\(--coffee\);',
        lambda m: f'width:{m.group(1)}%; height:100%; background:var(--coffee);',
        content,
    )
    content = re.sub(
        r'width:([0-9]+)height:100%;background:var\(--coffee\);',
        lambda m: f'width:{m.group(1)}%; height:100%; background:var(--coffee);',
        content,
    )

    content = content.replace('class="display-title text-center', 'class="display-title')
    content = content.replace('class="text-center mb-8"', 'class="mb-8"')

    if content != original:
        path.write_text(content, encoding='utf-8')
        print(path.relative_to(ROOT))
