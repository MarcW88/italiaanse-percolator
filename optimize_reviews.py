#!/usr/bin/env python3
"""Optimize review pages by removing inline CSS and applying new template"""
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_review_data(html_content):
    """Extract key data from existing review page"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title
    title = soup.find('h1', class_='display-title')
    title_text = title.get_text(strip=True) if title else ''
    
    # Extract lead paragraph
    lead = soup.find('p', class_='lead')
    lead_text = lead.get_text(strip=True) if lead else ''
    
    # Extract rating
    rating = soup.find('div', class_='rating-badge')
    rating_text = rating.get_text(strip=True) if rating else ''
    
    # Extract specs
    specs = []
    spec_items = soup.find_all('div', style=lambda x: x and 'display:flex;justify-content:space-between' in x)
    for item in spec_items:
        label = item.find('span')
        if label:
            label_text = label.get_text(strip=True)
            # Extract rating value
            value_span = item.find('span', style=lambda x: x and 'font-weight:600' in x)
            if value_span:
                value_text = value_span.get_text(strip=True)
                # Extract percentage from bar width
                bar_div = item.find('div', style=lambda x: x and 'background:var(--coffee)' in x)
                if bar_div:
                    bar_style = bar_div.get('style', '')
                    width_match = re.search(r'width:(\d+)%', bar_style)
                    percentage = width_match.group(1) if width_match else '50'
                    specs.append({
                        'label': label_text,
                        'value': value_text,
                        'percentage': percentage
                    })
    
    # Extract affiliate URL
    affiliate_link = soup.find('a', href=lambda x: x and 'bol.com' in x)
    affiliate_url = affiliate_link.get('href', '') if affiliate_link else ''
    
    # Extract pros and cons
    pros = []
    cons = []
    
    return {
        'title': title_text,
        'lead': lead_text,
        'rating': rating_text,
        'specs': specs,
        'affiliate_url': affiliate_url,
        'pros': pros,
        'cons': cons
    }

def apply_new_template(data, original_html):
    """Apply new template with extracted data"""
    # Read template
    with open('review-template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace placeholders
    template = template.replace('REVIEW_TITLE_HERE', data['title'])
    template = template.replace('LEAD_PARAGRAPH_HERE', data['lead'])
    template = template.replace('RATING_HERE', data['rating'])
    template = template.replace('AFFILIATE_URL_HERE', data['affiliate_url'])
    
    # Generate specs HTML
    specs_html = '<div class="review-specs">\n'
    for spec in data['specs']:
        specs_html += f'''  <div class="review-spec-item">
    <div class="review-spec-label">{spec['label']}</div>
    <div class="review-spec-bar">
      <div class="review-spec-bar-bg">
        <div class="review-spec-bar-fill" style="width: {spec['percentage']}%"></div>
      </div>
      <div class="review-spec-value">{spec['value']}</div>
    </div>
  </div>\n'''
    specs_html += '</div>'
    template = template.replace('<!-- Specs will be inserted here -->', specs_html)
    
    return template

def main():
    review_files = [
        'alessi-9090-review.html',
        'alessi-la-conica-review.html',
        'alessi-moka-review.html',
        'alessi-pulcina-review.html',
        'bialetti-alpina-review.html',
        'bialetti-brikka-review.html',
        'bialetti-dama-review.html',
        'bialetti-fiammetta-review.html',
        'bialetti-mini-express-review.html',
        'bialetti-moka-review.html',
        'bialetti-moka-timer-review.html',
        'bialetti-musa-review.html',
        'bialetti-venus-review.html',
        'cilio-classico-electric-review.html',
        'cloer-5928-review.html',
        'delonghi-alicia-review.html',
        'giannini-giannina-review.html',
        'grosche-milano-review.html',
        'rommelsbacher-eko366-review.html',
        'stelton-collar-review.html',
    ]
    
    for review_file in review_files:
        file_path = Path(review_file)
        if not file_path.exists():
            print(f"Skipping {review_file}: file not found")
            continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            original_html = f.read()
        
        # Extract data
        data = extract_review_data(original_html)
        
        # Apply new template
        new_html = apply_new_template(data, original_html)
        
        # Write optimized version
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f"Optimized {review_file}")

if __name__ == '__main__':
    main()
