#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('/Users/marc/Desktop/italiaanse-percolator')

def prefix_for(rel: str) -> str:
    return '../' * rel.count('/')

def active_for(rel: str) -> str:
    if rel == 'index.html':
        return 'home'
    if rel == 'boutique.html' or rel.startswith('categories/') or rel.startswith('producten/'):
        return 'shop'
    if rel.startswith('marques/'):
        return 'merken'
    if rel.startswith('koopgids/') or rel == 'beste-italiaanse-percolators.html' or rel == 'alle-reviews.html' or rel.endswith('-review.html') or rel.startswith('vergelijking/'):
        return 'gidsen'
    return ''

def nav_html(rel: str) -> str:
    p = prefix_for(rel)
    active = active_for(rel)
    return f'''    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="{p}index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="{p}index.html" class="nav-link{' active' if active == 'home' else ''}">Home</a></li>
                    <li class="nav-item dropdown">
                        <a href="{p}beste-italiaanse-percolators.html" class="nav-link dropdown-toggle{' active' if active == 'gidsen' else ''}">Gidsen</a>
                        <ul class="dropdown-menu">
                            <li><a href="{p}beste-italiaanse-percolators.html" class="dropdown-link">Top 10</a></li>
                            <li><a href="{p}koopgids/index.html" class="dropdown-link">Koopgids</a></li>
                            <li><a href="{p}alle-reviews.html" class="dropdown-link">Reviews</a></li>
                            <li><a href="{p}vergelijking/index.html" class="dropdown-link">Vergelijking</a></li>
                        </ul>
                    </li>
                    <li><a href="{p}marques/index.html" class="nav-link{' active' if active == 'merken' else ''}">Merken</a></li>
                    <li class="nav-item dropdown">
                        <a href="{p}boutique.html" class="nav-link dropdown-toggle{' active' if active == 'shop' else ''}">Shop</a>
                        <ul class="dropdown-menu">
                            <li><a href="{p}boutique.html" class="dropdown-link">Alle modellen</a></li>
                            <li><a href="{p}categories/percolators.html" class="dropdown-link">Percolators</a></li>
                            <li><a href="{p}categories/elektrische-percolators.html" class="dropdown-link">Elektrisch</a></li>
                            <li><a href="{p}categories/accessoires.html" class="dropdown-link">Accessoires</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>'''

for path in ROOT.glob('**/*.html'):
    if '.git' in path.parts:
        continue
    rel = path.relative_to(ROOT).as_posix()
    original = path.read_text(encoding='utf-8', errors='ignore')
    content = re.sub(r'\s*<nav class="navbar">.*?</nav>', '\n' + nav_html(rel), original, count=1, flags=re.S)
    if content != original:
        path.write_text(content, encoding='utf-8')
        print(rel)
