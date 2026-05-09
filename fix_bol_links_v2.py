"""
Correction des liens mal matchés - version 2
"""

import requests
import re
import time
import json
from pathlib import Path
from urllib.parse import quote

AFFILIATE_ID = "1519207"
HTML_DIR = Path(__file__).parent

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "nl-NL,nl;q=0.9",
}

# Produits à re-chercher avec termes plus précis
# Pour les produits introuvables sur Bol.com, on utilise une URL de recherche affiliée
PRODUCTS_TO_FIX = {
    "bialetti-musa-review.html": {
        "search": "Bialetti Musa percolator rvs",
        "fallback_search": "Bialetti Musa"
    },
    "bialetti-alpina-review.html": {
        "search": "Bialetti Alpina percolator",
        "fallback_search": "Bialetti Alpina"
    },
    "bialetti-dama-review.html": {
        "search": "Bialetti Dama percolator espresso",
        "fallback_search": "Bialetti Dama"
    },
    "bialetti-fiammetta-review.html": {
        "search": "Bialetti Fiammetta elektrische percolator",
        "fallback_search": "Bialetti Fiammetta"
    },
    "grosche-milano-review.html": {
        "search": "Grosche Milano percolator koffie",
        "fallback_search": "Grosche Milano stovetop"
    },
    "giannini-giannina-review.html": {
        "search": "Giannini Giannina percolator moka",
        "fallback_search": "Giannini moka pot"
    },
    "stelton-collar-review.html": {
        "search": "Stelton koffiemaker percolator",
        "fallback_search": "Stelton espresso"
    },
    "cilio-classico-electric-review.html": {
        "search": "Cilio Classico elektrische percolator",
        "fallback_search": "Cilio espresso maker elektrisch"
    },
}


def search_bol(query):
    search_url = f"https://www.bol.com/nl/nl/s/?searchtext={quote(query)}"
    try:
        r = requests.get(search_url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        pattern = r'href="(/nl/nl/p/[^/"]+/(\d+)/)"'
        matches = re.findall(pattern, r.text)
        if not matches:
            return None, None, None
        path, product_id = matches[0]
        full_url = f"https://www.bol.com{path}"
        slug = path.split("/")[-2]
        name = slug.replace("-", " ").title()
        return full_url, product_id, name
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return None, None, None


def make_affiliate_link(product_url, product_name):
    encoded_url = quote(product_url, safe="")
    encoded_name = quote(product_name, safe="")
    return (
        f"https://partner.bol.com/click/click?"
        f"p=2&t=url&s={AFFILIATE_ID}&f=TXL"
        f"&url={encoded_url}"
        f"&name={encoded_name}"
    )


def make_search_affiliate_link(search_term):
    """Fallback : lien vers la page de recherche Bol.com"""
    search_url = f"https://www.bol.com/nl/nl/s/?searchtext={quote(search_term)}"
    encoded_url = quote(search_url, safe="")
    encoded_name = quote(search_term, safe="")
    return (
        f"https://partner.bol.com/click/click?"
        f"p=2&t=url&s={AFFILIATE_ID}&f=TXL"
        f"&url={encoded_url}"
        f"&name={encoded_name}"
    )


def update_html(filepath, affiliate_url):
    content = filepath.read_text(encoding="utf-8")
    pattern = re.compile(r'href="https://partner\.bol\.com/click/click\?[^"]*"')
    new_content, count = pattern.subn(f'href="{affiliate_url}"', content)
    if count > 0:
        filepath.write_text(new_content, encoding="utf-8")
    return count


def is_relevant(product_url, search_term):
    """Vérifie si le résultat semble pertinent"""
    keywords = search_term.lower().split()[:2]
    url_lower = product_url.lower()
    return any(kw in url_lower for kw in keywords)


def main():
    print("=" * 60)
    print("🔧 Correction des liens mal matchés")
    print("=" * 60)

    report_path = HTML_DIR / "bol_links_report.json"
    if report_path.exists():
        with open(report_path) as f:
            report = json.load(f)
    else:
        report = {}

    for html_file, config in PRODUCTS_TO_FIX.items():
        filepath = HTML_DIR / html_file
        if not filepath.exists():
            print(f"⚠️  {html_file} non trouvé")
            continue

        print(f"\n🔍 {html_file}...")

        # Essai 1 : recherche précise
        product_url, product_id, product_name = search_bol(config["search"])
        time.sleep(2)

        if product_url and is_relevant(product_url, config["search"]):
            print(f"   ✅ Trouvé: {product_url}")
            affiliate_url = make_affiliate_link(product_url, product_name)
            used = "direct"
        else:
            # Essai 2 : recherche fallback
            if product_url:
                print(f"   ⚠️  Résultat non pertinent: {product_url}")
            print(f"   🔄 Essai fallback: {config['fallback_search']}")
            product_url2, product_id2, product_name2 = search_bol(config["fallback_search"])
            time.sleep(2)

            if product_url2 and is_relevant(product_url2, config["fallback_search"]):
                product_url, product_name = product_url2, product_name2
                print(f"   ✅ Trouvé (fallback): {product_url}")
                affiliate_url = make_affiliate_link(product_url, product_name)
                used = "fallback"
            else:
                # Fallback final : lien de recherche
                print(f"   ⚠️  Produit non trouvé sur Bol.com → lien de recherche")
                affiliate_url = make_search_affiliate_link(config["fallback_search"])
                product_url = f"(recherche: {config['fallback_search']})"
                used = "search_page"

        count = update_html(filepath, affiliate_url)
        print(f"   ✏️  {count} lien(s) mis à jour [{used}]")

        report[html_file] = {
            "product_url": product_url,
            "affiliate_url": affiliate_url,
            "links_updated": count,
            "method": used,
        }

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print("✅ Correction terminée")
    print(f"📄 Rapport mis à jour: {report_path}")


if __name__ == "__main__":
    main()
