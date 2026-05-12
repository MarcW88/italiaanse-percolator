#!/usr/bin/env python3
"""
Update navigation to use dropdown menus for simplified structure.
"""

import os
import re
import glob

# Find all HTML files to update
html_files = glob.glob('/Users/marc/Desktop/italiaanse-percolator/**/*.html', recursive=True)

# Exclude templates
html_files = [f for f in html_files if '/templates/' not in f]

def update_navigation(content):
    """Replace old navigation with dropdown navigation."""
    
    old_nav = '''    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="index.html" class="nav-link">Home</a></li>
                    <li><a href="beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
                    <li><a href="alle-reviews.html" class="nav-link">Reviews</a></li>
                    <li><a href="koopgids/index.html" class="nav-link">Koopgids</a></li>
                    <li><a href="marques/index.html" class="nav-link">Merken</a></li>
                    <li><a href="boutique.html" class="nav-link">Alle modellen</a></li>
                </ul>
            </div>
        </div>
    </nav>'''
    
    new_nav = '''    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="index.html" class="nav-link">Home</a></li>
                    <li class="nav-item dropdown">
                        <a href="beste-italiaanse-percolators.html" class="nav-link dropdown-toggle">Guides ▾</a>
                        <ul class="dropdown-menu">
                            <li><a href="beste-italiaanse-percolators.html" class="dropdown-link">Top 10</a></li>
                            <li><a href="koopgids/index.html" class="dropdown-link">Koopgids</a></li>
                            <li><a href="alle-reviews.html" class="dropdown-link">Reviews</a></li>
                        </ul>
                    </li>
                    <li><a href="marques/index.html" class="nav-link">Merken</a></li>
                    <li class="nav-item dropdown">
                        <a href="boutique.html" class="nav-link dropdown-toggle">Shop ▾</a>
                        <ul class="dropdown-menu">
                            <li><a href="boutique.html" class="dropdown-link">Alle modellen</a></li>
                            <li><a href="categories/percolators.html" class="dropdown-link">Percolators</a></li>
                            <li><a href="categories/elektrische-percolators.html" class="dropdown-link">Elektrisch</a></li>
                            <li><a href="categories/accessoires.html" class="dropdown-link">Accessoires</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <script>
        // Dropdown toggle functionality
        document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
            toggle.addEventListener('click', function(e) {
                e.preventDefault();
                const dropdown = this.parentElement;
                dropdown.classList.toggle('active');
            });
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.dropdown')) {
                document.querySelectorAll('.dropdown.active').forEach(d => d.classList.remove('active'));
            }
        });
    </script>'''
    
    return content.replace(old_nav, new_nav)

def process_file(filepath):
    """Update navigation in a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        print(f"Skipping {filepath} (cannot read)")
        return
    
    original_content = content
    
    # Update navigation
    content = update_navigation(content)
    
    # Only write if content changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all files
changed_count = 0
for filepath in html_files:
    if process_file(filepath):
        changed_count += 1
        print(f"Updated: {os.path.basename(filepath)}")

print(f"\nTotal files updated: {changed_count}")
