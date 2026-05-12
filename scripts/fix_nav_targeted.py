#!/usr/bin/env python3
import os
import re

ROOT = '/Users/marc/Desktop/italiaanse-percolator'
TARGETS = [
    'index.html',
    'boutique.html',
    'beste-italiaanse-percolators.html',
    'alle-reviews.html',
    'over-ons.html',
    'contact.html',
    'privacy.html',
    'disclaimer.html',
    'marques/index.html',
    'marques/bialetti/index.html',
    'marques/bialetti/fiammetta.html',
    'marques/alessi/index.html',
    'marques/grosche/index.html',
    'koopgids/index.html',
    'koopgids/hoe-kies-je-de-juiste-percolator.html',
    'koopgids/hoe-onderhoud-je-een-percolator.html',
    'koopgids/percolator-vs-espressoapparaat.html',
    'koopgids/wat-is-italiaanse-percolator-mokapot.html',
    'koopgids/italiaanse-percolator-gebruiken-handleiding.html',
    'koopgids/beste-koffiebonen-italiaanse-percolator.html',
    'vergelijking/index.html',
    'vergelijking/bialetti-vs-alessi.html',
]
TARGETS += [f for f in os.listdir(ROOT) if f.endswith('-review.html')]


def prefix_for(rel):
    return '../' * rel.count('/')


def active_for(rel):
    if rel == 'index.html':
        return 'home'
    if rel == 'boutique.html' or rel.startswith('categories/'):
        return 'shop'
    if rel.startswith('marques/'):
        return 'merken'
    if rel.startswith('koopgids/') or rel == 'beste-italiaanse-percolators.html' or rel == 'alle-reviews.html' or rel.endswith('-review.html') or rel.startswith('vergelijking/'):
        return 'guides'
    return ''


def nav(rel):
    p = prefix_for(rel)
    active = active_for(rel)
    return f'''    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="{p}index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="{p}index.html" class="nav-link{' active' if active == 'home' else ''}">Home</a></li>
                    <li class="nav-item dropdown">
                        <a href="{p}beste-italiaanse-percolators.html" class="nav-link dropdown-toggle{' active' if active == 'guides' else ''}">Guides</a>
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


def replace_nav(content, rel):
    content = re.sub(r'\s*<script>\s*// Dropdown toggle functionality.*?</script>', '', content, flags=re.S)
    return re.sub(r'\s*<nav class="navbar">.*?</nav>', '\n' + nav(rel), content, count=1, flags=re.S)

for rel in TARGETS:
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    updated = replace_nav(content, rel)
    updated = updated.replace('border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;', 'border: 1px solid var(--border); border-radius: 0.5rem;')
    updated = updated.replace('border: 1px solid var(--border); .25rem; border: 1px solid var(--border); border-radius: 0.5rem;', 'border: 1px solid var(--border); border-radius: 0.5rem;')
    updated = updated.replace('width: 100%; .5rem;', 'width: 100%; border-radius: 0.5rem;')
    if updated != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(rel)
