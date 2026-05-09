"""
Trouve l'ID Bol.com de chaque produit en cherchant le slug exact dans les résultats de recherche.
"""

import requests
import json
import time
import re
from pathlib import Path
from urllib.parse import quote

AFFILIATE_ID = "1519207"
HTML_DIR = Path(__file__).parent
PRODUCTS_FILE = HTML_DIR / "all_products.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "nl-NL,nl;q=0.9",
}

KNOWN_IDS = {
    "bialetti-inductieplaatje-voor-inductiekooplaat-o13cm": "9200000103892026",
    "bialetti-moka-inductie-rood-4-kops-150ml-bialetti-koffie-proefpakket-3-x-250gr": "9200000120463205",
}


def find_product_id(slug, name):
    """Cherche l'ID en trouvant l'URL qui contient exactement ce slug dans les résultats"""

    if slug in KNOWN_IDS:
        return KNOWN_IDS[slug]

    # Rechercher par nom de produit
    search_url = f"https://www.bol.com/nl/nl/s/?searchtext={quote(name)}"
    try:
        r = requests.get(search_url, headers=HEADERS, timeout=15)
        # Chercher une URL qui contient le slug exact
        pattern = rf'/nl/nl/p/{re.escape(slug)}/(\d{{10,}})/'
        match = re.search(pattern, r.text)
        if match:
            return match.group(1)

        # Chercher toutes les URLs produit et trouver la plus proche
        all_urls = re.findall(r'/nl/nl/p/([^/]+)/(\d{10,})/', r.text)
        for found_slug, found_id in all_urls:
            # Vérifier si au moins 3 premiers mots du slug correspondent
            slug_words = slug.split('-')[:4]
            if all(w in found_slug for w in slug_words):
                return found_id

        return None
    except Exception as e:
        print(f"   Erreur: {e}")
        return None


def make_affiliate_link(slug, product_id, name):
    if product_id:
        product_url = f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/"
    else:
        product_url = f"https://www.bol.com/nl/nl/p/{slug}/"
    encoded_url = quote(product_url, safe="")
    encoded_name = quote(name, safe="")
    return (
        f"https://partner.bol.com/click/click?"
        f"p=2&t=url&s={AFFILIATE_ID}&f=TXL"
        f"&url={encoded_url}"
        f"&name={encoded_name}"
    )


def main():
    with open(PRODUCTS_FILE, encoding="utf-8") as f:
        products = json.load(f)

    print(f"🔍 {len(products)} produits à traiter...")
    print("=" * 60)

    found = 0
    not_found = []

    for product in products:
        slug = product["slug"]
        name = product["name"]
        print(f"[{product['id']:02d}] {name[:55]}...", end=" ")

        product_id = find_product_id(slug, name)

        if product_id:
            product["product_id"] = product_id
            product["affiliate_url"] = make_affiliate_link(slug, product_id, name)
            print(f"✅ {product_id}")
            found += 1
        else:
            product["affiliate_url"] = make_affiliate_link(slug, None, name)
            print("⚠️  sans ID")
            not_found.append({"slug": slug, "name": name})

        time.sleep(2)

    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    # Sauvegarder les non-trouvés pour review manuelle
    if not_found:
        with open(HTML_DIR / "bol_missing_ids.json", "w", encoding="utf-8") as f:
            json.dump(not_found, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print(f"✅ {found}/{len(products)} IDs trouvés")
    print(f"💾 all_products.json mis à jour")
    if not_found:
        print(f"⚠️  {len(not_found)} sans ID → bol_missing_ids.json")


if __name__ == "__main__":
    main()
