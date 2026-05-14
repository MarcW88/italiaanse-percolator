#!/usr/bin/env python3
"""Script pour ajouter le menu mobile à toutes les pages HTML"""

import re
from pathlib import Path

def add_mobile_menu(html_file):
    """Ajoute le menu mobile à un fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Vérifier si le menu mobile est déjà présent
    if 'mobile-menu-toggle' in content:
        print(f"✓ {html_file.name} - Menu mobile déjà présent")
        return False
    
    # 1. Ajouter le bouton hamburger après nav-brand
    pattern1 = r'(<a class="nav-brand"[^>]*>.*?</a>)'
    replacement1 = r'\1\n<button class="mobile-menu-toggle" aria-label="Menu">\n<span></span>\n<span></span>\n<span></span>\n</button>'
    content = re.sub(pattern1, replacement1, content)
    
    # 2. Ajouter l'overlay après </nav>
    pattern2 = r'(</nav>)'
    replacement2 = r'\1\n<div class="mobile-menu-overlay"></div>'
    content = re.sub(pattern2, replacement2, content, count=1)
    
    # 3. Ajouter le JavaScript avant </body>
    js_script = '''<script>
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        mobileMenuToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        mobileMenuOverlay.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    });
}

if (mobileMenuOverlay) {
    mobileMenuOverlay.addEventListener('click', () => {
        mobileMenuToggle.classList.remove('active');
        navMenu.classList.remove('active');
        mobileMenuOverlay.classList.remove('active');
        document.body.style.overflow = '';
    });
}

// Mobile dropdown toggle
const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
dropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
            e.preventDefault();
            const dropdownItem = toggle.closest('.nav-item.dropdown');
            dropdownItem.classList.toggle('active');
            const dropdownMenu = dropdownItem.querySelector('.dropdown-menu');
            dropdownMenu.classList.toggle('active');
        }
    });
});
</script>
'''
    
    pattern3 = r'(</body>)'
    replacement3 = js_script + r'\1'
    content = re.sub(pattern3, replacement3, content)
    
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {html_file.name} - Menu mobile ajouté")
        return True
    else:
        print(f"✗ {html_file.name} - Pas de modification nécessaire")
        return False

def main():
    base_dir = Path('/Users/marc/Desktop/italiaanse-percolator')
    
    # Trouver tous les fichiers HTML
    html_files = list(base_dir.glob('*.html')) + list(base_dir.rglob('*.html'))
    
    # Exclure certains fichiers
    excluded = ['sitemap*.xml', '*.py']
    html_files = [f for f in html_files if not any(pattern in f.name for pattern in excluded)]
    
    print(f"Found {len(html_files)} HTML files to process")
    
    modified_count = 0
    for html_file in html_files:
        if add_mobile_menu(html_file):
            modified_count += 1
    
    print(f"\nTotal: {modified_count} fichiers modifiés")

if __name__ == '__main__':
    main()
