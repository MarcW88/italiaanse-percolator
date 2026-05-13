#!/usr/bin/env python3
"""Update product descriptions from Excel file"""
import pandas as pd
from pathlib import Path
import re
from urllib.parse import urlparse

def extract_filename_from_url(url):
    """Extract HTML filename from URL"""
    path = urlparse(url).path
    filename = path.split('/')[-1]
    return filename

def slugify_text(text):
    """Slugify text for matching"""
    import re
    s = text.lower().strip()
    s = re.sub(r'[àáâãä]', 'a', s)
    s = re.sub(r'[èéêë]', 'e', s)
    s = re.sub(r'[ìíîï]', 'i', s)
    s = re.sub(r'[òóôõö]', 'o', s)
    s = re.sub(r'[ùúûü]', 'u', s)
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s[:80]

def find_product_file(url):
    """Find the HTML file for a given URL"""
    producten_dir = Path('producten')
    
    # Extract filename from URL
    filename = extract_filename_from_url(url)
    
    # Try exact match
    exact_file = producten_dir / filename
    if exact_file.exists():
        return exact_file
    
    return None

def update_description_in_file(file_path, new_description):
    """Update the description in an HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = False
    
    # Update meta description
    meta_pattern = r'<meta name="description" content="[^"]*">'
    if re.search(meta_pattern, content):
        content = re.sub(meta_pattern, f'<meta name="description" content="{new_description}">', content)
        updated = True
    
    # Update JSON-LD description
    json_ld_pattern = r'"description"\s*:\s*"[^"]*"'
    if re.search(json_ld_pattern, content):
        content = re.sub(json_ld_pattern, f'"description": "{new_description}"', content)
        updated = True
    
    # Update product-intro section if it exists
    intro_pattern = r'<p class="product-intro">[^<]*</p>'
    if re.search(intro_pattern, content):
        content = re.sub(intro_pattern, f'<p class="product-intro">{new_description}</p>', content)
        updated = True
    
    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    # Read Excel file
    df = pd.read_excel('/Users/marc/Desktop/descriptions.xlsx', header=None)
    
    print(f"Total products in Excel: {len(df)}")
    
    # Process each product
    updated_count = 0
    not_found_count = 0
    
    for idx, row in df.iterrows():
        url = row[0]
        description = row[1]
        
        if pd.isna(description) or description == '':
            print(f"Skipping {url}: no description")
            continue
        
        # Try to find the product file using URL
        product_file = find_product_file(url)
        
        if product_file:
            print(f"Updating {product_file.name}")
            if update_description_in_file(product_file, description):
                updated_count += 1
            else:
                print(f"  Warning: Could not find description pattern in {product_file.name}")
        else:
            print(f"Not found: {url}")
            not_found_count += 1
    
    print(f"\nSummary:")
    print(f"Updated: {updated_count} files")
    print(f"Not found: {not_found_count} files")

if __name__ == '__main__':
    main()
