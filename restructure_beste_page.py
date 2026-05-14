#!/usr/bin/env python3
"""
Restructure beste-italiaanse-percolators.html according to audit.

Target structure:
1. Simple hero (title + short intro)
2. Top 3 cards (always visible, no accordion)
3. Comparison table (desktop + mobile)
4. Test methodology (condensed)
5. Top 10 reviews (simplified, uniform format)
6. ONE consolidated "Hoe kies je" section (merge all buying guides)
7. FAQ
8. Light CTA
9. Author box
10. Footer

Keep all content, just redistribute and simplify.
"""
from pathlib import Path

ROOT = Path(__file__).parent
FILE = ROOT / 'beste-italiaanse-percolators.html'

def read_file():
    with open(FILE, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(content):
    with open(FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def consolidate_buying_guide(lines, start, end):
    """Extract and consolidate all buying guide sections into one"""
    sections = []
    
    # Extract content from each section, removing headers
    for section_start, section_end, section_name in [
        (start, end, "Kies op basis van"),
    ]:
        content_lines = []
        in_content = False
        for i in range(section_start, section_end + 1):
            line = lines[i]
            # Skip section headers but keep h3/h4 content
            if '<h2' in line and 'mb-6' in line:
                continue
            if '<h3' in line and 'mb-3' in line:
                continue
            if line.strip() and not line.strip().startswith('<!--'):
                content_lines.append(line)
        sections.extend(content_lines)
    
    return sections

def main():
    content = read_file()
    lines = content.splitlines()
    
    # Find key sections
    hero_start = None
    hero_end = None
    quick_picks_start = None
    quick_picks_end = None
    comparison_start = None
    comparison_end = None
    test_method_start = None
    test_method_end = None
    reviews_start = None
    reviews_end = None
    buying_guide_start = None
    buying_guide_end = None
    direct_comp_start = None
    direct_comp_end = None
    alternatives_start = None
    alternatives_end = None
    where_to_buy_start = None
    where_to_buy_end = None
    final_rec_start = None
    final_rec_end = None
    faq_start = None
    faq_end = None
    author_start = None
    author_end = None
    footer_start = None
    
    for i, line in enumerate(lines):
        if '<!-- Hero Section -->' in line:
            hero_start = i
        if '<!-- Breadcrumbs -->' in line:
            hero_end = i - 1
        if '<!-- Quick Picks Optimisé -->' in line:
            quick_picks_start = i
        if '<!-- Tableau Comparatif Responsive -->' in line:
            quick_picks_end = i - 1
            comparison_start = i
        if '<!-- Test Methodology (Condensed) -->' in line:
            comparison_end = i - 1
            test_method_start = i
        if '<!-- Section Reviews avec TOC Sidebar -->' in line:
            test_method_end = i - 1
            reviews_start = i
        if '<!-- Buying Guide Section -->' in line:
            reviews_end = i - 1
            buying_guide_start = i
        if '<!-- Direct Comparisons -->' in line:
            buying_guide_end = i - 1
            direct_comp_start = i
        if '<!-- Alternatives -->' in line:
            direct_comp_end = i - 1
            alternatives_start = i
        if '<!-- Where to Buy -->' in line:
            alternatives_end = i - 1
            where_to_buy_start = i
        if '<!-- Final Recommendations -->' in line:
            where_to_buy_end = i - 1
            final_rec_start = i
        if '<!-- FAQ -->' in line:
            final_rec_end = i - 1
            faq_start = i
        if '<div class="author-box">' in line:
            faq_end = i - 1
            author_start = i
        if '<footer class="footer">' in line:
            author_end = i - 1
            footer_start = i
    
    print(f"Hero: {hero_start}-{hero_end}")
    print(f"Quick Picks: {quick_picks_start}-{quick_picks_end}")
    print(f"Comparison: {comparison_start}-{comparison_end}")
    print(f"Test Method: {test_method_start}-{test_method_end}")
    print(f"Reviews: {reviews_start}-{reviews_end}")
    print(f"Buying Guide: {buying_guide_start}-{buying_guide_end}")
    print(f"Direct Comp: {direct_comp_start}-{direct_comp_end}")
    print(f"Alternatives: {alternatives_start}-{alternatives_end}")
    print(f"Where to Buy: {where_to_buy_start}-{where_to_buy_end}")
    print(f"Final Rec: {final_rec_start}-{final_rec_end}")
    print(f"FAQ: {faq_start}-{faq_end}")
    print(f"Author: {author_start}-{author_end}")
    print(f"Footer: {footer_start}")

if __name__ == '__main__':
    main()
