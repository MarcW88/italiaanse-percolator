#!/usr/bin/env python3
"""Analyze possible filters from all_products.json"""
import json

def main():
    with open('all_products.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    types = set()
    brands = set()
    materials = set()
    inductie = set()
    capaciteiten = set()
    
    for p in data:
        types.add(p.get('type'))
        brands.add(p.get('brand'))
        materials.add(p.get('materiaal'))
        inductie.add(p.get('inductie'))
        capaciteiten.add(p.get('capaciteit'))
    
    print('Types:', sorted(types))
    print('Brands:', sorted(brands)[:10])
    print('Materials:', sorted(materials))
    print('Inductie:', sorted(inductie))
    print('Capaciteiten:', sorted(set([c for c in capaciteiten if c]))[:10])

if __name__ == '__main__':
    main()
