#!/usr/bin/env python3
"""Update product descriptions from Excel file"""
import pandas as pd
from pathlib import Path
import re
from urllib.parse import urlparse

def slugify_from_url(url):
    """Extract slug from Bol.com URL"""
    # Parse the URL and extract the last part
    path = urlparse(url).path
    # The slug is usually the last part of the path before the product ID
    # But we need to match it with the actual file names
    return path.split('/')[-1]

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

def find_product_file(product_name, url):
    """Find the HTML file for a given product"""
    producten_dir = Path('producten')
    
    # Try to create slug from product name
    name_slug = slugify_text(product_name)
    
    # Try exact match first
    exact_file = producten_dir / f"{name_slug}.html"
    if exact_file.exists():
        return exact_file
    
    # Try partial match - look for files containing key terms
    key_terms = product_name.lower().split()
    key_terms = [term for term in key_terms if len(term) > 3]
    
    best_match = None
    best_score = 0
    
    for file in producten_dir.glob('*.html'):
        file_slug = file.stem.lower()
        score = 0
        
        # Check for key terms in filename
        for term in key_terms:
            if term in file_slug:
                score += 1
        
        # Prefer files with higher score
        if score > best_score and score >= 2:
            best_score = score
            best_match = file
    
    return best_match

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
    df = pd.read_excel('catalogue_bialetti_complet.xlsx')
    
    print(f"Total products in Excel: {len(df)}")
    print(f"Columns: {df.columns.tolist()}")
    
    # Check if we have description column
    if 'Description courte' not in df.columns:
        print("Error: 'Description courte' column not found in Excel file")
        return
    
    # Process each product
    updated_count = 0
    not_found_count = 0
    
    for idx, row in df.iterrows():
        product_name = row['Nom du produit']
        description = row['Description courte']
        url = row['URL']
        
        if pd.isna(description) or description == '':
            print(f"Skipping {product_name}: no description")
            continue
        
        # Try to find the product file using product name
        product_file = find_product_file(product_name, url)
        
        if product_file:
            print(f"Updating {product_file.name}: {description}")
            if update_description_in_file(product_file, description):
                updated_count += 1
            else:
                print(f"  Warning: Could not find description pattern in {product_file.name}")
        else:
            print(f"Not found: {product_name} (from {url})")
            not_found_count += 1
    
    print(f"\nSummary:")
    print(f"Updated: {updated_count} files")
    print(f"Not found: {not_found_count} files")

if __name__ == '__main__':
    main()
