#!/usr/bin/env python3
"""Replace inline product data in boutique.html with fetch from all_products.json"""
import re

def fix_boutique():
    with open('boutique.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the inline product data section
    pattern = r'const allProducts = \[.*?\];'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("Error: Could not find inline product data")
        return
    
    # Replace with fetch code
    new_code = '''let allProducts = [];
    const perPage = 24;
    const baseUrl = 'boutique.html';
    let currentPage = 1;

    // Load products from all_products.json
    fetch('all_products.json')
        .then(response => response.json())
        .then(data => {
            allProducts = data;
            init();
        })
        .catch(error => console.error('Error loading products:', error));'''
    
    content = re.sub(pattern, new_code, content, flags=re.DOTALL)
    
    # Remove duplicate declarations
    content = re.sub(r'const perPage = 24;\s*', '', content, count=1)
    content = re.sub(r'const baseUrl = \'boutique\.html\';\s*', '', content, count=1)
    
    # Write back
    with open('boutique.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Successfully modified boutique.html to load products from all_products.json")

if __name__ == '__main__':
    fix_boutique()
