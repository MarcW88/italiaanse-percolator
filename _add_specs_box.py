#!/usr/bin/env python3
import os
import glob

# Spécifications pour chaque produit
PRODUCT_SPECS = {
    'bialetti-musa-review.html': {
        'name': 'Bialetti Musa',
        'image': 'bialetti-musa-1.jpg',
        'score': '8.5/10',
        'merk': 'Bialetti',
        'model': 'Musa',
        'materiaal': 'RVS',
        'capaciteit': '6 kopjes',
        'warmtebron': 'Gas, elektrisch, inductie',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-musa-percolator-6-kops-rvs%2F9200000038446313%2F&name=Bialetti%20Musa',
        'amazon_search': 'Bialetti Musa'
    },
    'alessi-9090-review.html': {
        'name': 'Alessi 9090',
        'image': 'alessi_9090.jpg',
        'score': '9.4/10',
        'merk': 'Alessi',
        'model': '9090',
        'materiaal': 'RVS',
        'capaciteit': '3–6 kopjes',
        'warmtebron': 'Gas, elektrisch, inductie',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Falessi-9090-percolator-3-kops-rvs%2F9200000038446313%2F&name=Alessi%209090',
        'amazon_search': 'Alessi 9090'
    },
    'alessi-la-conica-review.html': {
        'name': 'Alessi La Conica',
        'image': 'alessi_laconica.jpg',
        'score': '8.7/10',
        'merk': 'Alessi',
        'model': 'La Conica',
        'materiaal': 'RVS',
        'capaciteit': '3–6 kopjes',
        'warmtebron': 'Gas, elektrisch, inductie',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Falessi-la-conica-percolator-3-kops-rvs%2F9200000038446313%2F&name=Alessi%20La%20Conica',
        'amazon_search': 'Alessi La Conica'
    },
    'alessi-moka-review.html': {
        'name': 'Alessi Moka',
        'image': 'alessi_moka.jpg',
        'score': '8.5/10',
        'merk': 'Alessi',
        'model': 'Moka',
        'materiaal': 'Aluminium',
        'capaciteit': '1–6 kopjes',
        'warmtebron': 'Gas en elektrische kookplaat (niet voor inductie)',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Falessi-moka-percolator-3-kops-aluminium%2F9200000038446313%2F&name=Alessi%20Moka',
        'amazon_search': 'Alessi Moka'
    },
    'alessi-pulcina-review.html': {
        'name': 'Alessi Pulcina',
        'image': 'alessi_pulcina.jpg',
        'score': '8.5/10',
        'merk': 'Alessi',
        'model': 'Pulcina',
        'materiaal': 'Aluminium',
        'capaciteit': '3–6 kopjes',
        'warmtebron': 'Gas en elektrische kookplaat (niet voor inductie)',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Falessi-pulcina-percolator-3-kops-aluminium%2F9200000038446313%2F&name=Alessi%20Pulcina',
        'amazon_search': 'Alessi Pulcina'
    },
    'cilio-classico-electric-review.html': {
        'name': 'Cilio Classico Electric',
        'image': 'bialetti-moka-express-1.jpg',
        'score': '8.5/10',
        'merk': 'Cilio',
        'model': 'Classico Electric',
        'materiaal': 'RVS',
        'capaciteit': '6 kopjes',
        'warmtebron': 'Elektrisch',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fcilio-classico-electric-percolator-6-kops-rvs%2F9200000038446313%2F&name=Cilio%20Classico%20Electric',
        'amazon_search': 'Cilio Classico Electric'
    },
    'cloer-5928-review.html': {
        'name': 'Cloer 5928',
        'image': 'bialetti-moka-express-1.jpg',
        'score': '8.4/10',
        'merk': 'Cloer',
        'model': '5928',
        'materiaal': 'RVS',
        'capaciteit': '3–6 kopjes',
        'warmtebron': 'Elektrisch',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fcloer-5928-percolator-6-kops-rvs%2F9200000038446313%2F&name=Cloer%205928',
        'amazon_search': 'Cloer 5928'
    },
    'delonghi-alicia-review.html': {
        'name': "De'Longhi Alicia EMK",
        'image': 'bialetti-moka-express-1.jpg',
        'score': '8.8/10',
        'merk': "De'Longhi",
        'model': 'Alicia EMK',
        'materiaal': 'Aluminium',
        'capaciteit': '6–9 kopjes',
        'warmtebron': 'Elektrisch',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fdelonghi-alicia-emk-percolator-6-kops-aluminium%2F9200000038446313%2F&name=DeLonghi%20Alicia',
        'amazon_search': 'DeLonghi Alicia'
    },
    'giannini-giannina-review.html': {
        'name': 'Giannini Giannina',
        'image': 'bialetti-moka-express-1.jpg',
        'score': '9.1/10',
        'merk': 'Giannini',
        'model': 'Giannina',
        'materiaal': 'RVS',
        'capaciteit': '3–6 kopjes',
        'warmtebron': 'Gas, elektrisch, inductie',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fgiannini-giannina-percolator-3-kops-rvs%2F9200000038446313%2F&name=Giannini%20Giannina',
        'amazon_search': 'Giannini Giannina'
    },
    'grosche-milano-review.html': {
        'name': 'Grosche Milano',
        'image': 'grosche-milano.jpg',
        'score': '8.5/10',
        'merk': 'Grosche',
        'model': 'Milano',
        'materiaal': 'Aluminium',
        'capaciteit': '3–6–9 kopjes',
        'warmtebron': 'Gas, elektrisch, propaan',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fgrosche-milano-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Grosche%20Milano',
        'amazon_search': 'Grosche Milano'
    },
    'rommelsbacher-eko366-review.html': {
        'name': 'Rommelsbacher EKO 366',
        'image': 'bialetti-moka-express-1.jpg',
        'score': '8.7/10',
        'merk': 'Rommelsbacher',
        'model': 'EKO 366',
        'materiaal': 'RVS 18/10',
        'capaciteit': '3–6 kopjes',
        'warmtebron': 'Elektrisch',
        'onderhoud': 'Handwas met warm water, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Frommelsbacher-eko-366-percolator-6-kops-rvs%2F9200000038446313%2F&name=Rommelsbacher%20EKO%20366',
        'amazon_search': 'Rommelsbacher EKO 366'
    },
    'stelton-collar-review.html': {
        'name': 'Stelton Collar',
        'image': 'bialetti-moka-express-1.jpg',
        'score': '8.3/10',
        'merk': 'Stelton',
        'model': 'Collar',
        'materiaal': 'RVS met Teflon-coating',
        'capaciteit': '4–6 kleine kopjes',
        'warmtebron': 'Gas, elektrisch, inductie',
        'onderhoud': 'Handwas, niet in de vaatwasser',
        'bol_url': 'https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fstelton-collar-percolator-3-kops-rvs%2F9200000038446313%2F&name=Stelton%20Collar',
        'amazon_search': 'Stelton Collar'
    }
}

# Template de la box spécifications
SPECS_BOX_TEMPLATE = '''<div class="review-commercial-box">
<div class="review-commercial-header"><span>Specificaties</span><span class="review-commercial-score">Eindscore <strong>{score}</strong></span></div>
<div class="review-commercial-content">
<div class="review-commercial-image"><img src="../Images/{image}" alt="{name}" loading="lazy"></div>
<div class="review-commercial-info">
<h3>{name}</h3>
<a class="btn btn-primary" href="{bol_url}" rel="sponsored noopener" target="_blank">Bekijk prijs op Bol.com →</a>
<a class="btn btn-outline" href="https://www.amazon.nl/s?k={amazon_search}" target="_blank" rel="noopener">Vergelijk op Amazon.nl</a>
</div>
</div>
<div class="review-commercial-specs">
<table><tbody><tr><th>Merk</th><td>{merk}</td></tr>
<tr><th>Model</th><td>{model}</td></tr>
<tr><th>Materiaal</th><td>{materiaal}</td></tr>
<tr><th>Capaciteit</th><td>{capaciteit}</td></tr>
<tr><th>Warmtebron</th><td>{warmtebron}</td></tr>
<tr><th>Onderhoud</th><td>{onderhoud}</td></tr></tbody></table>
</div>
</div>
</div>
<div style="margin: 3rem 0; background: white; border: 2px solid #f5f0ea; border-radius: 0.5rem; padding: 2rem; display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center;">
<div>
<p style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; color: #8b6f4e; margin: 0 0 0.4rem 0; font-weight: 600;">Over de auteur</p>
<p style="font-size: 1.4rem; font-weight: 700; margin: 0 0 1rem 0; color: #1a1a1a;">Timo Dekker</p>
<p style="font-size: 0.9rem; line-height: 1.6; color: #555; margin: 0;">Timo begon ooit achter de bar in een Amsterdams koffietentje en raakte daar gefascineerd door hoe klein verschil in maling of hitte een kop koffie kan maken. Inmiddels werkt hij vooral thuis, waar hij Italiaanse percolators test op gas, inductie en elektrisch, van goedkope instapmodellen tot duurdere designstukken. Voor Italiaanse Percolator bundelt hij die ervaringen in praktische reviews en gidsen, zodat je weet wat een percolator in het echt doet aan je fornuis, niet alleen op de productfoto.</p></div>
<div style="display: flex; justify-content: center; align-items: center; border-radius: 0.5rem; padding: 2rem; min-height: 200px;">
<img src="../Images/marco_author.png" alt="Timo Dekker" style="max-width: 100%; height: 100%; object-fit: cover; border-radius: 0.5rem;">
</div>
</div>
</div>'''

# Pages à traiter
PAGES_TO_PROCESS = [
    'bialetti-musa-review.html',
    'alessi-9090-review.html',
    'alessi-la-conica-review.html',
    'alessi-moka-review.html',
    'alessi-pulcina-review.html',
    'cilio-classico-electric-review.html',
    'cloer-5928-review.html',
    'delonghi-alicia-review.html',
    'giannini-giannina-review.html',
    'grosche-milano-review.html',
    'rommelsbacher-eko366-review.html',
    'stelton-collar-review.html'
]

for page in PAGES_TO_PROCESS:
    if page not in PRODUCT_SPECS:
        print(f"Skipping {page} - no specs defined")
        continue
    
    specs = PRODUCT_SPECS[page]
    
    if not os.path.exists(page):
        print(f"Skipping {page} - file not found")
        continue
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si la box existe déjà
    if 'review-commercial-box' in content:
        print(f"Skipping {page} - specs box already exists")
        continue
    
    # Générer la box avec les spécifications
    specs_box = SPECS_BOX_TEMPLATE.format(
        name=specs['name'],
        image=specs['image'],
        score=specs['score'],
        merk=specs['merk'],
        model=specs['model'],
        materiaal=specs['materiaal'],
        capaciteit=specs['capaciteit'],
        warmtebron=specs['warmtebron'],
        onderhoud=specs['onderhoud'],
        bol_url=specs['bol_url'],
        amazon_search=specs['amazon_search']
    )
    
    # Trouver l'endroit où insérer (avant le footer)
    footer_index = content.find('<footer>')
    
    if footer_index != -1:
        new_content = content[:footer_index] + specs_box + '\n\n' + content[footer_index:]
        with open(page, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added specs box to {page}")
    else:
        print(f"Could not find <footer> in {page}")

print("Done!")
