"""
add_new_products.py
Ajoute les nouveaux produits Bol.com à la boutique :
- Cherche chaque produit sur Bol.com pour trouver slug + product_id
- Récupère le vrai titre via og:title
- Génère la page HTML producten/
- Met à jour all_products.json
"""
import json, re, time, requests
from pathlib import Path
from urllib.parse import quote

AFFILIATE_ID = "1519207"
BASE_DIR = Path(__file__).parent
PRODUCTS_FILE = BASE_DIR / "all_products.json"
PRODUCTEN_DIR = BASE_DIR / "producten"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "nl-NL,nl;q=0.9",
}

# ─── Liste des nouveaux produits ────────────────────────────────────────────
NEW_PRODUCTS = [
    # Bialetti manquants
    {"search": "Bialetti MINI EXPRESS Kandinsky Set 2 kopjes", "price": 43.50, "merk": "Bialetti", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 2, "type": "Cafetière percolateur"},
    {"search": "Bialetti Moka Exclusive Moka Express Blauw", "price": 50.05, "merk": "Bialetti", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 3, "type": "Cafetière percolateur"},
    {"search": "Bialetti Dama Gran Gala 1 kops aluminium", "price": 33.74, "merk": "Bialetti", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 1, "type": "Cafetière percolateur"},
    {"search": "Bialetti 90th Anniversary Moka Express 3tz Backpack", "price": 74.85, "merk": "Bialetti", "materiaal": "RVS", "inductie": "Non", "capaciteit": 3, "type": "Cafetière percolateur"},
    {"search": "Bialetti Moka Exclusive Moka Express Roze", "price": 87.50, "merk": "Bialetti", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 3, "type": "Cafetière percolateur"},
    {"search": "Bialetti Mini Express Rood Koffiepakket 3 x 250gr", "price": 76.95, "merk": "Bialetti", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 2, "type": "Cafetière percolateur"},
    {"search": "Bialetti Mini Express Deco Glamour 2 kopjes 90ml", "price": 80.35, "merk": "Bialetti", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 2, "type": "Cafetière percolateur"},
    {"search": "Bialetti Stranger Things Percolator Mini Express 2 kopjes", "price": 59.90, "merk": "Bialetti", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 2, "type": "Cafetière percolateur"},
    {"search": "Bialetti Moka Exclusive Moka Express Rood aluminium", "price": 50.05, "merk": "Bialetti", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 3, "type": "Cafetière percolateur"},
    # Non-Bialetti
    {"search": "Intirilife Espressomaker aluminium zwart 3 kopjes mokkapot 160ml", "price": 22.99, "merk": "Intirilife", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 3, "type": "Cafetière percolateur"},
    {"search": "Hakal Line Percolator XL espressomaker 12 Kops inductie", "price": 29.95, "merk": "Hakal Line", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 12, "type": "Cafetière percolateur"},
    {"search": "Pezzetti ITALEXPRESS Aluminium 6 kopjes Zwart koffiezetapparaat", "price": 38.85, "merk": "PEZZETTI", "materiaal": "Aluminium", "inductie": "Oui", "capaciteit": 6, "type": "Cafetière percolateur"},
    {"search": "Alessi Percolator Pulcina MDL02 6 Rood Michele De Lucchi", "price": 84.95, "merk": "Alessi", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 6, "type": "Cafetière percolateur"},
    {"search": "GAT Italia Mokaccina Doppio Mini Express percolator 2 kops 100ml", "price": 29.59, "merk": "G.A.T. Italia", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 2, "type": "Cafetière percolateur"},
    {"search": "Gnali Zani Venezia Espressomaker Rood 6 Kopjes", "price": 59.99, "merk": "Gnali & Zani", "materiaal": "Aluminium", "inductie": "Oui", "capaciteit": 6, "type": "Cafetière percolateur"},
    {"search": "Ibili Espressomaker 9 kops inductie aluminium", "price": 37.51, "merk": "Ibili", "materiaal": "Aluminium", "inductie": "Oui", "capaciteit": 9, "type": "Cafetière percolateur"},
    {"search": "Pezzetti PENTAEXPRESS Aluminium 3 kopjes Blauw", "price": 38.99, "merk": "PEZZETTI", "materiaal": "Aluminium", "inductie": "Oui", "capaciteit": 3, "type": "Cafetière percolateur"},
    {"search": "GEFU Espressopot Nando roestvrijstaal 4 kops", "price": 60.00, "merk": "GEFU", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 4, "type": "Cafetière percolateur"},
    {"search": "Leonardo Percolator Caffe Per Me Zwart 4 Kops RVS", "price": 25.90, "merk": "Leonardo", "materiaal": "RVS", "inductie": "Non", "capaciteit": 4, "type": "Cafetière percolateur"},
    {"search": "House of Husk Moka Pot Percolator Zwart 4 Kops RVS Espressomaker 300ml", "price": 52.98, "merk": "House of Husk", "materiaal": "RVS", "inductie": "Non", "capaciteit": 4, "type": "Cafetière percolateur"},
    {"search": "GAT Italia Tricolore 1 kops Percolator 50ml Made in Italy", "price": 22.99, "merk": "G.A.T. Italia", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 1, "type": "Cafetière percolateur"},
    {"search": "Pedrini MyMoka induction Moka pot Blauw Roestvrijstaal", "price": 39.25, "merk": "Pedrini", "materiaal": "Aluminium", "inductie": "Oui", "capaciteit": 2, "type": "Cafetière percolateur"},
    {"search": "Kinghoff Aluminium Espressomaker KH-1886 6 Kopjes Zwart Houten Handvat Inductie 300ml", "price": 24.95, "merk": "Kinghoff", "materiaal": "Aluminium", "inductie": "Oui", "capaciteit": 6, "type": "Cafetière percolateur"},
    {"search": "Pezzetti STEELEXPRESS Roestvrij staal 6 kopjes Indigoblauw inductie", "price": 46.04, "merk": "PEZZETTI", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 6, "type": "Cafetière percolateur"},
    {"search": "Bo-Camp Pastel Percolator Turenne Aluminium 6 Kopjes", "price": 19.99, "merk": "Bo-Camp", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 6, "type": "Cafetière percolateur"},
    {"search": "DeLonghi Alicia EMKM 4 Elektrische Moka Express 0.4l", "price": 79.00, "merk": "De'Longhi", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 4, "type": "Cafetière électrique"},
    {"search": "Royal Swiss Percolator 9 koffiekopjes Koffie Machine Inductie Roestvrijstaal espressomaker", "price": 24.99, "merk": "Royal Swiss", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 9, "type": "Cafetière percolateur"},
    {"search": "Leopold Vienna Percolator Otto 4-kops RVS Glas", "price": 31.39, "merk": "Leopold Vienna", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 4, "type": "Cafetière percolateur"},
    {"search": "DeLonghi EMKP 42.B Semi-automatische elektrische Moka koffiezetapparaat", "price": 102.81, "merk": "De'Longhi", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 4, "type": "Cafetière électrique"},
    {"search": "Klausberg Espressokoffiezetapparaat KB-7846 9 Kopjes RVS Inductie 450ml Percolator", "price": 24.95, "merk": "Klausberg", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 9, "type": "Cafetière percolateur"},
    {"search": "Kela Latina Espressomaker 6 kops RVS", "price": 66.00, "merk": "Kela", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 6, "type": "Cafetière percolateur"},
    {"search": "Alessi Moka 6 cups aluminium percolator", "price": 60.00, "merk": "Alessi", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 6, "type": "Cafetière percolateur"},
    {"search": "DeLonghi Alicia Plus EMKP 21.B Volledig automatisch Elektrische Moka Express", "price": 94.13, "merk": "De'Longhi", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 2, "type": "Cafetière électrique"},
    {"search": "Verk Group Koffie Percolator 12 koffie 600ml aluminium", "price": 15.85, "merk": "Verk Group", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 12, "type": "Cafetière percolateur"},
    {"search": "GAT Italia Regina RVS 4 kops Percolator 200ml Inductie Made in Italy", "price": 55.99, "merk": "G.A.T. Italia", "materiaal": "RVS", "inductie": "Oui", "capaciteit": 4, "type": "Cafetière percolateur"},
    {"search": "Kela Italia Espressomaker 9 kops aluminium", "price": 27.61, "merk": "Kela", "materiaal": "Aluminium", "inductie": "Non", "capaciteit": 9, "type": "Cafetière percolateur"},
]

# ─── Bol.com helpers ─────────────────────────────────────────────────────────
def search_bol(search_term):
    """Retourne (slug, product_id) du premier résultat Bol.com."""
    url = f"https://www.bol.com/nl/nl/s/?searchtext={quote(search_term)}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        m = re.search(r'/nl/nl/p/([\w\-]+)/(\d{13,16})/', r.text)
        if m:
            return m.group(1), m.group(2)
    except Exception:
        pass
    return None, None

def get_bol_title(slug, product_id):
    """Récupère le titre via og:title."""
    url = f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        m = re.search(r'<meta property="og:title" content="([^"]+)"', r.text)
        if m:
            title = re.sub(r'\s*\|\s*bol(\.com)?\s*$', '', m.group(1)).strip()
            return title
    except Exception:
        pass
    return None

def make_affiliate_url(slug, product_id, name):
    product_url = f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/"
    return (
        f"https://partner.bol.com/click/click?p=2&t=url&s={AFFILIATE_ID}&f=TXL"
        f"&url={quote(product_url, safe='')}"
        f"&name={quote(name, safe='')}"
    )

def stars(rating):
    full = int(rating)
    return "★" * full + "☆" * (5 - full)

# ─── Génération HTML ──────────────────────────────────────────────────────────
def generate_html(p):
    name = p["bol_name"]
    slug = p["slug"]
    price_str = f"€{p['price']:.2f}".replace(".", ",")
    inductie_str = "Ja" if p["inductie"] == "Oui" else "Nee"
    rating_stars = stars(p["rating"])
    affiliate_url = p["affiliate_url"]
    merk = p["merk"]
    materiaal = p["materiaal"]
    capaciteit = p["capaciteit"]
    reviews = p["reviews"]
    rating = p["rating"]

    desc_short = f"{name} - {materiaal} percolator voor {capaciteit} kopjes" if capaciteit else f"{name} - {materiaal}"
    inductie_text = "Geschikt voor inductie." if p["inductie"] == "Oui" else "Geschikt voor gas, elektrisch en keramisch."

    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | Italiaanse Percolator</title>
    <meta name="description" content="{name} - {desc_short} - Prijs: {price_str} - {rating}★ ({reviews} reviews)">
    <link rel="stylesheet" href="../style.css">
    <link rel="canonical" href="https://italiaanse-percolator.nl/producten/{slug}.html">
    <link rel="icon" type="image/svg+xml" href="../favicon.svg">
    <link rel="icon" type="image/svg+xml" sizes="16x16" href="../favicon-simple.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="../favicon.svg">
    <meta name="theme-color" content="#D2691E">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;700&family=DM+Serif+Display:ital,wght@0,400&display=swap" rel="stylesheet">
    <script type="application/ld+json">
    {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{name}",
    "description": "{name} - {materiaal} percolator. {inductie_text}",
    "brand": {{
        "@type": "Brand",
        "name": "{merk}"
    }},
    "category": "Percolator",
    "material": "{materiaal}",
    "url": "https://italiaanse-percolator.nl/producten/{slug}.html",
    "offers": {{
        "@type": "Offer",
        "price": "{p['price']}",
        "priceCurrency": "EUR",
        "availability": "https://schema.org/InStock",
        "seller": {{
            "@type": "Organization",
            "name": "Italiaanse Percolator"
        }}
    }},
    "aggregateRating": {{
        "@type": "AggregateRating",
        "ratingValue": {rating},
        "reviewCount": {reviews},
        "bestRating": "5",
        "worstRating": "1"
    }},
    "additionalProperty": [
        {{
            "@type": "PropertyValue",
            "name": "Capaciteit",
            "value": "{capaciteit} kopjes"
        }},
        {{
            "@type": "PropertyValue",
            "name": "Materiaal",
            "value": "{materiaal}"
        }},
        {{
            "@type": "PropertyValue",
            "name": "Inductie geschikt",
            "value": "{'Ja' if p['inductie'] == 'Oui' else 'Nee'}"
        }}
    ]
}}
    </script>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="../index.html" class="nav-brand">Italiaanse Percolator</a>
                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li><a href="../beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
                    <li><a href="../koopgids/index.html" class="nav-link">Koopgids</a></li>
                    <li><a href="../vergelijking/index.html" class="nav-link">Vergelijking</a></li>
                    <li><a href="../over-ons.html" class="nav-link">Over ons</a></li>
                    <li><a href="../boutique.html" class="nav-link" style="background: #D2691E; color: white; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600;">Winkel</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container" style="padding: 2rem 0;"><div style="display: flex; flex-direction: column; width: 100%;">
        <nav style="margin-bottom: 2rem; font-size: 0.9rem; color: #666;">
            <a href="../index.html" style="color: #666; text-decoration: none;">Home</a> &gt;
            <a href="../boutique.html" style="color: #666; text-decoration: none;">Winkel</a> &gt;
            <span style="color: #D2691E; font-weight: 600;">{name}</span>
        </nav>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-bottom: 3rem;">
            <div>
                <img src="../images/producten/{slug}.jpg" alt="{name}"
                     style="width: 100%; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.15);"
                     onerror="this.src='../Images/bialetti-moka-express-1.jpg'">
            </div>
            <div>
                <h1 style="font-size: 2.2rem; margin-bottom: 1rem; line-height: 1.2;">{name}</h1>
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="color: #ffd700; font-size: 1.3rem;">{rating_stars}</div>
                    <span style="color: #666; font-size: 1rem;">({reviews} beoordelingen)</span>
                </div>
                <div style="font-size: 2.5rem; font-weight: bold; color: #D2691E; margin-bottom: 2rem;">{price_str}</div>
                <div style="margin-bottom: 2rem;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">Productbeschrijving</h3>
                    <p style="color: #666; line-height: 1.6; font-size: 1rem;">
                        De {name} is een hoogwaardige <a href="../index.html" style="color: #D2691E; text-decoration: none; font-weight: 600;">italiaanse percolator</a> van {merk}. Gemaakt van {materiaal.lower()} voor een authentieke espresso-ervaring. {inductie_text}
                    </p>
                </div>
                <div style="margin-bottom: 2rem;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">Specificaties</h3>
                    <ul style="list-style: none; padding: 0;">
                        <li style="padding: 0.5rem 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;"><span style="font-weight: 600;">Merk:</span><span> {merk}</span></li>
                        <li style="padding: 0.5rem 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;"><span style="font-weight: 600;">Materiaal:</span><span> {materiaal}</span></li>
                        <li style="padding: 0.5rem 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;"><span style="font-weight: 600;">Capaciteit:</span><span> {capaciteit} kopjes</span></li>
                        <li style="padding: 0.5rem 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;"><span style="font-weight: 600;">Inductie:</span><span> {inductie_str}</span></li>
                    </ul>
                </div>
                <div style="margin-bottom: 2rem;">
                    <a href="{affiliate_url}" target="_blank" rel="sponsored"
                       style="display: inline-block; background: linear-gradient(135deg, #D2691E, #B8541A); color: white; padding: 1rem 2rem; text-decoration: none; border-radius: 8px; font-size: 1.1rem; font-weight: 600; box-shadow: 0 4px 15px rgba(210, 105, 30, 0.3); transition: all 0.3s ease;">
                        Koop nu op Bol.com →
                    </a>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.9rem; color: #666;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #28a745;">✓</span>Gratis retourneren binnen 30 dagen</div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #28a745;">✓</span>Snelle levering via Bol.com</div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #28a745;">✓</span>Betrouwbare klantenservice</div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #28a745;">✓</span>Veilig betalen</div>
                </div>
            </div>
        </div>

        <section style="margin: 3rem 0; display: block; clear: both; width: 100%;">
            <div style="max-width: 1000px; margin: 0 auto;">
                <h3 style="font-size: 1.5rem; margin-bottom: 2rem; color: #2c2c2c; font-weight: 600; text-align: center;">Productbeschrijving</h3>
                <div style="background: #f8f9fa; padding: 2.5rem; border-radius: 12px; border-left: 4px solid #D2691E; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                    <p style="margin-bottom: 1.5rem; color: #333; line-height: 1.7; font-size: 1rem;">De {name} is een uitstekende keuze voor liefhebbers van authentieke Italiaanse espresso. Met zijn {materiaal.lower()} constructie biedt dit apparaat duurzaamheid en stijl in één.</p>
                    <p style="margin-bottom: 1.5rem; color: #333; line-height: 1.7; font-size: 1rem;">{inductie_text} Perfect voor dagelijks gebruik in de moderne keuken. De traditionele moka-methode zorgt voor een rijke, aromatische espresso die je direct aan een Italiaans café doet denken.</p>
                    <p style="margin-bottom: 1.5rem; color: #333; line-height: 1.7; font-size: 1rem;">Met een capaciteit van {capaciteit} kopjes is deze percolator ideaal voor {"een persoon" if capaciteit <= 2 else "kleine gezelschappen" if capaciteit <= 4 else "grotere groepen"}. Geniet elke ochtend van een perfect kopje espresso met de {merk} {name.split(merk)[-1].strip() if merk in name else name}.</p>
                </div>
            </div>
        </section>

        <section style="margin-bottom: 3rem; display: block; clear: both; width: 100%;">
            <h2 style="font-size: 2rem; margin-bottom: 2rem;">Veelgestelde Vragen over de {name}</h2>
            <div style="max-width: 800px;">
                <div style="border: 1px solid #ddd; border-radius: 8px; margin-bottom: 1rem;">
                    <button onclick="toggleFaq(1)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Waarom smaakt mijn koffie bitter?
                        <span id="faq-icon-1">+</span>
                    </button>
                    <div id="faq-content-1" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        Bittere koffie komt vaak door te hoge temperatuur, te fijne maling, of te lang op het vuur laten staan. Gebruik middelhoog vuur en haal direct van het vuur wanneer de koffie klaar is.
                    </div>
                </div>
                <div style="border: 1px solid #ddd; border-radius: 8px; margin-bottom: 1rem;">
                    <button onclick="toggleFaq(2)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Is de {name} geschikt voor inductie?
                        <span id="faq-icon-2">+</span>
                    </button>
                    <div id="faq-content-2" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        {"Ja, deze percolator is geschikt voor inductieplaten." if p['inductie'] == 'Oui' else "Nee, deze percolator is niet direct geschikt voor inductie. Gebruik een inductie-adapter voor het beste resultaat."}
                    </div>
                </div>
                <div style="border: 1px solid #ddd; border-radius: 8px;">
                    <button onclick="toggleFaq(3)" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        Hoeveel kopjes koffie maakt de {name}?
                        <span id="faq-icon-3">+</span>
                    </button>
                    <div id="faq-content-3" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        Deze percolator maakt {capaciteit} kopjes per zetbeurt. Let op: dit zijn Italiaanse espresso-kopjes (ongeveer 50ml), niet grote mokken.
                    </div>
                </div>
            </div>
        </section>
    </div></main>

    <footer class="footer">
        <div class="container">
            <div class="footer-top" style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-bottom: 3rem; padding-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.1);">
                <div>
                    <h3 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem; color: white;">Italiaanse Percolator</h3>
                    <p style="color: #D1D5DB; line-height: 1.7; margin-bottom: 1.5rem; font-size: 0.95rem;"><strong>De #1 gids voor Italiaanse moka-percolators in Nederland &amp; België.</strong></p>
                </div>
                <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                    <h4 style="color: white; margin-bottom: 1rem; font-size: 1rem;">📬 Moka Insiders Newsletter</h4>
                    <form style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                        <input type="email" placeholder="je@email.com" style="flex: 1; padding: 0.75rem; border: 1px solid #555; border-radius: 6px; background: rgba(255,255,255,0.1); color: white; font-size: 0.9rem;" />
                        <button type="submit" style="background: #D2691E; color: white; padding: 0.75rem 1.5rem; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">Aanmelden</button>
                    </form>
                </div>
            </div>
            <div class="footer-bottom" style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
                <p style="color: #D1D5DB; font-size: 0.85rem; line-height: 1.6; margin: 0;">
                    <strong style="color: white;">© 2025 Italiaanse Percolator.</strong> Alle rechten voorbehouden.<br/><br/>
                    <strong style="color: #999;">Affiliate Kennisgeving:</strong> Als Bol.com partner verdienen wij aan kwalificerende aankopen.
                </p>
            </div>
        </div>
    </footer>

    <script>
    function toggleFaq(num) {{
        const content = document.getElementById(`faq-content-${{num}}`);
        const icon = document.getElementById(`faq-icon-${{num}}`);
        if (content.style.display === 'none') {{
            content.style.display = 'block';
            icon.textContent = '-';
        }} else {{
            content.style.display = 'none';
            icon.textContent = '+';
        }}
    }}
    </script>
</body>
</html>"""
    return html

# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    products = json.load(open(PRODUCTS_FILE, encoding="utf-8"))
    existing_slugs = {p["slug"] for p in products}
    next_id = max(p["id"] for p in products) + 1

    print(f"Store actuel: {len(products)} produits")
    print(f"Produits à traiter: {len(NEW_PRODUCTS)}")
    print("=" * 70)

    added = 0
    for item in NEW_PRODUCTS:
        search = item["search"]
        print(f"[{next_id}] Recherche: {search[:55]}...", end=" ", flush=True)

        slug, product_id = search_bol(search)
        time.sleep(1.5)

        if not slug or not product_id:
            print("⚠️  Pas trouvé sur Bol.com")
            continue

        if slug in existing_slugs:
            print(f"✅ Déjà présent ({slug[:40]})")
            continue

        title = get_bol_title(slug, product_id)
        time.sleep(1.5)

        if not title:
            title = search.strip()

        affiliate_url = make_affiliate_url(slug, product_id, title)

        new_product = {
            "id": next_id,
            "name": title,
            "slug": slug,
            "price": item["price"],
            "rating": 4.3,
            "reviews": 25,
            "description": f"{item['materiaal']} percolator - {item['capaciteit']} kopjes",
            "inductie": item["inductie"],
            "capaciteit": item["capaciteit"],
            "merk": item["merk"],
            "materiaal": item["materiaal"],
            "type": item["type"],
            "image": f"images/producten/{slug}.jpg",
            "product_id": product_id,
            "bol_name": title,
            "affiliate_url": affiliate_url,
        }

        html = generate_html(new_product)
        html_path = PRODUCTEN_DIR / f"{slug}.html"
        html_path.write_text(html, encoding="utf-8")

        products.append(new_product)
        existing_slugs.add(slug)
        next_id += 1
        added += 1
        print(f"✅ → {title[:45]}")

    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print("=" * 70)
    print(f"✅ {added} nouveaux produits ajoutés")
    print(f"💾 all_products.json: {len(products)} produits total")

if __name__ == "__main__":
    main()
