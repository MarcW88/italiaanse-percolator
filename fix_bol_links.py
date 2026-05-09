"""
Script pour trouver les vrais liens produit Bol.com et mettre à jour les HTML.

Pour chaque produit, cherche sur Bol.com et prend le premier résultat.
Génère un lien affilié correct avec le vrai product-id.

Usage:
    pip install requests beautifulsoup4
    python fix_bol_links.py
"""

import requests
import re
import time
import json
from pathlib import Path
from urllib.parse import quote, urlencode

AFFILIATE_ID = "1519207"
HTML_DIR = Path(__file__).parent

# Mapping : fichier HTML → terme de recherche Bol.com
PRODUCTS = {
    "bialetti-moka-review.html":          "Bialetti Moka Express",
    "bialetti-brikka-review.html":        "Bialetti Brikka",
    "bialetti-venus-review.html":         "Bialetti Venus",
    "bialetti-musa-review.html":          "Bialetti Musa",
    "bialetti-alpina-review.html":        "Bialetti Alpina",
    "bialetti-dama-review.html":          "Bialetti Dama",
    "bialetti-fiammetta-review.html":     "Bialetti Fiammetta",
    "bialetti-mini-express-review.html":  "Bialetti Mini Express",
    "bialetti-moka-timer-review.html":    "Bialetti Moka Timer",
    "alessi-9090-review.html":            "Alessi 9090",
    "alessi-la-conica-review.html":       "Alessi La Conica",
    "alessi-moka-review.html":            "Alessi Moka",
    "alessi-pulcina-review.html":         "Alessi Pulcina",
    "grosche-milano-review.html":         "Grosche Milano",
    "giannini-giannina-review.html":      "Giannini Giannina",
    "stelton-collar-review.html":         "Stelton Collar",
    "delonghi-alicia-review.html":        "DeLonghi Alicia",
    "rommelsbacher-eko366-review.html":   "Rommelsbacher EKO 366",
    "cilio-classico-electric-review.html":"Cilio Classico Electric",
    "cloer-5928-review.html":             "Cloer 5928",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "nl-NL,nl;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def search_bol(query):
    """Cherche un produit sur Bol.com et retourne l'URL + nom du premier résultat"""
    search_url = f"https://www.bol.com/nl/nl/s/?searchtext={quote(query)}"
    
    try:
        r = requests.get(search_url, headers=HEADERS, timeout=15)
        r.raise_for_status()

        # Extraire le premier lien produit (format /nl/nl/p/[slug]/[id]/)
        pattern = r'href="(/nl/nl/p/[^/"]+/(\d+)/)"'
        matches = re.findall(pattern, r.text)

        if not matches:
            return None, None, None

        path, product_id = matches[0]
        full_url = f"https://www.bol.com{path}"

        # Extraire le nom du produit depuis l'URL (slug)
        slug = path.split("/")[-2]
        name = slug.replace("-", " ").title()

        return full_url, product_id, name

    except Exception as e:
        print(f"   ❌ Erreur recherche: {e}")
        return None, None, None


def make_affiliate_link(product_url, product_name):
    """Génère un lien affilié Bol.com correct"""
    encoded_url = quote(product_url, safe="")
    encoded_name = quote(product_name, safe="")
    return (
        f"https://partner.bol.com/click/click?"
        f"p=2&t=url&s={AFFILIATE_ID}&f=TXL"
        f"&url={encoded_url}"
        f"&name={encoded_name}"
    )


def update_html(filepath, affiliate_url):
    """Remplace tous les liens partner.bol.com dans un fichier HTML"""
    content = filepath.read_text(encoding="utf-8")
    pattern = re.compile(r'href="https://partner\.bol\.com/click/click\?[^"]*"')
    new_content, count = pattern.subn(f'href="{affiliate_url}"', content)
    if count > 0:
        filepath.write_text(new_content, encoding="utf-8")
    return count


def main():
    print("=" * 60)
    print("🔧 Mise à jour des liens Bol.com affiliés")
    print("=" * 60)

    results = {}
    updated = 0
    failed = []

    for html_file, search_term in PRODUCTS.items():
        filepath = HTML_DIR / html_file
        if not filepath.exists():
            print(f"⚠️  Fichier non trouvé: {html_file}")
            continue

        print(f"\n🔍 {search_term}...")
        product_url, product_id, product_name = search_bol(search_term)

        if not product_url:
            print(f"   ❌ Aucun résultat Bol.com pour: {search_term}")
            failed.append(html_file)
            time.sleep(2)
            continue

        print(f"   ✅ Trouvé: {product_url}")
        affiliate_url = make_affiliate_link(product_url, product_name)
        count = update_html(filepath, affiliate_url)
        print(f"   ✏️  {count} lien(s) mis à jour dans {html_file}")

        results[html_file] = {
            "search_term":   search_term,
            "product_url":   product_url,
            "product_id":    product_id,
            "affiliate_url": affiliate_url,
            "links_updated": count,
        }
        updated += 1

        time.sleep(3)  # Pause pour éviter d'être bloqué

    # Rapport
    report_path = HTML_DIR / "bol_links_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print(f"🎉 {updated}/{len(PRODUCTS)} pages mises à jour")
    if failed:
        print(f"❌ Non trouvés: {', '.join(failed)}")
    print(f"📄 Rapport: {report_path}")


if __name__ == "__main__":
    main()
