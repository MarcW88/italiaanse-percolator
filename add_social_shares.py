#!/usr/bin/env python3
"""Add social share buttons to koopgids articles"""
import re
from pathlib import Path
from urllib.parse import quote

def generate_social_share_html(url, title):
    """Generate HTML for social share buttons"""
    encoded_url = quote(url)
    encoded_title = quote(title)
    
    return f'''<div class="social-share">
  <span class="social-share-label">Deel dit artikel:</span>
  <div class="social-share-buttons">
    <a href="https://www.facebook.com/sharer/sharer.php?u={encoded_url}" target="_blank" rel="noopener" class="social-share-btn facebook" title="Deel op Facebook">f</a>
    <a href="https://twitter.com/intent/tweet?url={encoded_url}&text={encoded_title}" target="_blank" rel="noopener" class="social-share-btn twitter" title="Deel op Twitter">𝕏</a>
    <a href="https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}" target="_blank" rel="noopener" class="social-share-btn linkedin" title="Deel op LinkedIn">in</a>
    <a href="https://pinterest.com/pin/create/button/?url={encoded_url}&description={encoded_title}" target="_blank" rel="noopener" class="social-share-btn pinterest" title="Deel op Pinterest">P</a>
    <a href="mailto:?subject={encoded_title}&body={encoded_url}" class="social-share-btn email" title="Deel via email">✉</a>
    <a href="https://wa.me/?text={encoded_title}%20{encoded_url}" target="_blank" rel="noopener" class="social-share-btn whatsapp" title="Deel op WhatsApp">📱</a>
  </div>
</div>'''

def add_social_shares_to_file(file_path):
    """Add social share buttons to a koopgids article"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title for social sharing
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else ''
    
    # Extract canonical URL
    canonical_match = re.search(r'<link rel="canonical" href="(.*?)">', content)
    canonical_url = canonical_match.group(1) if canonical_match else ''
    
    # Generate social share HTML
    social_html = generate_social_share_html(canonical_url, title)
    
    # Insert social share buttons after the header section
    # Look for the header with publication date and insert after it
    header_pattern = r'(<!-- Header -->.*?</header>)'
    if re.search(header_pattern, content, re.DOTALL):
        content = re.sub(header_pattern, r'\1\n\n' + social_html, content, flags=re.DOTALL)
    else:
        # Alternative: insert after the first h1 tag
        h1_pattern = r'(<h1[^>]*>.*?</h1>)'
        if re.search(h1_pattern, content, re.DOTALL):
            content = re.sub(h1_pattern, r'\1\n\n' + social_html, content, count=1, flags=re.DOTALL)
    
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
        
        if add_social_shares_to_file(path):
            print(f"Added social shares to {file_path}")

if __name__ == '__main__':
    main()
