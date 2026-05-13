#!/usr/bin/env python3
"""Apply wonenmetlef-inspired structure to koopgids articles"""
import re
from pathlib import Path

def restructure_article(file_path):
    """Restructure a koopgids article with better structure"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else ''
    
    # Extract canonical URL
    canonical_match = re.search(r'<link rel="canonical" href="(.*?)">', content)
    canonical_url = canonical_match.group(1) if canonical_match else ''
    
    # Extract meta description for intro
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
    description = desc_match.group(1) if desc_match else ''
    
    # Add article-content class to main content section
    # Find the section with article content and add class
    content = re.sub(
        r'(<section style="padding: 3rem 0;">\s*<div class="container">\s*<div style="max-width: 800px; margin: 0 auto;">)',
        r'<section style="padding: 3rem 0;">\n    <div class="container">\n      <div class="article-content">',
        content
    )
    
    # Restructure header section
    header_pattern = r'(<!-- Header -->.*?</header>)'
    if re.search(header_pattern, content, re.DOTALL):
        content = re.sub(
            header_pattern,
            r'''<!-- Header -->
        <header class="article-header">
            <h1 style="font-size: 2.2rem; font-weight: 400; margin-bottom: 0.5rem; font-family: var(--font-serif);">\1</h1>
            <div class="article-meta">
                <span class="article-author">Italiaanse Percolator</span>
                <span>·</span>
                <span>Koopgids</span>
            </div>
        </header>''',
            content,
            flags=re.DOTALL
        )
    
    # Restructure intro section
    intro_pattern = r'(<!-- Intro -->\s*<div style="background: linear-gradient\(135deg, #fff3e0 0%, #ffe9d0 100%\); padding: 2rem; margin: 2rem 0; border-radius: 0\.5rem;">.*?</div>)'
    if re.search(intro_pattern, content, re.DOTALL):
        content = re.sub(
            intro_pattern,
            r'''<!-- Intro -->
        <div class="article-intro">\1</div>''',
            content,
            flags=re.DOTALL
        )
    
    # Restructure table of contents
    toc_pattern = r'(<!-- Table of Contents -->\s*<div style="background: #f8f9fa; padding: 1\.5rem; margin: 2rem 0; border-radius: 0\.5rem;">.*?</div>)'
    if re.search(toc_pattern, content, re.DOTALL):
        content = re.sub(
            toc_pattern,
            r'''<!-- Table of Contents -->
        <div class="table-of-contents">\1</div>''',
            content,
            flags=re.DOTALL
        )
    
    # Restructure article sections
    section_pattern = r'(<!-- Section \d+ -->\s*<div style="margin: 2rem 0;">)'
    content = re.sub(section_pattern, r'<div class="article-section">', content)
    
    # Update h2 styling in article sections
    content = re.sub(
        r'(<div class="article-section">.*?<h2 style="font-size: 1\.4rem; margin-bottom: 1rem;">)',
        r'<div class="article-section">\n        <h2>',
        content
    )
    
    # Update h3 styling in article sections
    content = re.sub(
        r'(<div class="article-section">.*?<h3 style="font-size: 1\.2rem; margin-bottom: 0\.75rem;">)',
        r'<div class="article-section">\n        <h3>',
        content
    )
    
    # Update paragraph styling in article sections
    content = re.sub(
        r'(<p style="font-size: 1rem; line-height: 1\.7; margin-bottom: 1rem;">)',
        r'<p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    koopgids_files = [
        'koopgids/beste-koffiebonen-italiaanse-percolator.html',
        'koopgids/hoe-kies-je-de-juiste-percolator.html',
        'koopgids/hoe-onderhoud-je-een-percolator.html',
        'koopgids/italiaanse-percolator-gebruiken-handleiding.html',
        'koopgids/percolator-vs-espressoapparaat.html',
        'koopgids/wat-is-italiaanse-percolator-mokapot.html',
    ]
    
    for file_path in koopgids_files:
        path = Path(file_path)
        if not path.exists():
            print(f"Skipping {file_path}: file not found")
            continue
        
        if restructure_article(path):
            print(f"Restructured {file_path}")

if __name__ == '__main__':
    main()
