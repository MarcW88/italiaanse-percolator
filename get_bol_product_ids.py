"""
Pour chaque produit dans all_products.json:
1. Accède à bol.com/nl/nl/p/[slug]/ pour obtenir l'ID produit via la redirection
2. Construit le bon lien affilié avec l'ID réel
3. Met à jour all_products.json avec le champ affiliate_url
4. Met à jour boutique.html pour utiliser product.affiliate_url

Usage: python get_bol_product_ids.py
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
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "nl-NL,nl;q=0.9",
    "Accept": "text/html,application/xhtml+xml",
}

# IDs connus depuis les liens fournis
KNOWN_IDS = {
    "bialetti-inductieplaatje-voor-inductiekooplaat-o13cm": "9200000103892026",
    "bialetti-moka-inductie-rood-4-kops-150ml-bialetti-koffie-proefpakket-3-x-250gr": "9200000120463205",
}


def get_product_id(slug):
    """Accède à bol.com avec le slug et récupère l'ID produit depuis l'URL finale"""

    # D'abord, vérifier les IDs connus
    if slug in KNOWN_IDS:
        return KNOWN_IDS[slug]

    url = f"https://www.bol.com/nl/nl/p/{slug}/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
        final_url = r.url

        # Extraire l'ID depuis l'URL finale: /nl/nl/p/[slug]/[ID]/
        match = re.search(r'/p/[^/]+/(\d{10,})', final_url)
        if match:
            return match.group(1)

        # Essayer dans le HTML si pas dans l'URL
        id_match = re.search(r'"productId"\s*:\s*"?(\d{10,})"?', r.text)
        if id_match:
            return id_match.group(1)

        return None
    except Exception as e:
        print(f"   Erreur: {e}")
        return None


def make_affiliate_link(slug, product_id, name):
    product_url = f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/"
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

    print(f"🔍 Traitement de {len(products)} produits...")
    print("=" * 60)

    found = 0
    not_found = []

    for product in products:
        slug = product["slug"]
        name = product["name"]
        print(f"[{product['id']:02d}] {name[:50]}...")

        product_id = get_product_id(slug)

        if product_id:
            affiliate_url = make_affiliate_link(slug, product_id, name)
            product["product_id"] = product_id
            product["affiliate_url"] = affiliate_url
            print(f"      ✅ ID: {product_id}")
            found += 1
        else:
            # Fallback: lien sans ID (bol.com tente quand même de résoudre)
            product_url = f"https://www.bol.com/nl/nl/p/{slug}/"
            encoded_url = quote(product_url, safe="")
            encoded_name = quote(name, safe="")
            product["affiliate_url"] = (
                f"https://partner.bol.com/click/click?"
                f"p=2&t=url&s={AFFILIATE_ID}&f=TXL"
                f"&url={encoded_url}"
                f"&name={encoded_name}"
            )
            print(f"      ⚠️  ID non trouvé - lien sans ID")
            not_found.append(slug)

        time.sleep(1.5)

    # Sauvegarder all_products.json avec affiliate_url
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print(f"✅ {found}/{len(products)} produits avec ID trouvé")
    if not_found:
        print(f"⚠️  Sans ID: {len(not_found)} produits")
    print(f"💾 all_products.json mis à jour avec affiliate_url")

    # Mettre à jour boutique.html
    update_boutique_html()


def update_boutique_html():
    """Remplace le lien Koop op Bol.com pour utiliser product.affiliate_url"""
    boutique_path = HTML_DIR / "boutique.html"
    content = boutique_path.read_text(encoding="utf-8")

    old = (
        'href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL'
        '&url=${encodeURIComponent(\'https://www.bol.com/nl/nl/s/?searchtext=\' + encodeURIComponent(product.name))}'
        '&name=${encodeURIComponent(product.name)}"'
    )
    new = 'href="${product.affiliate_url}"'

    if old in content:
        content = content.replace(old, new)
        boutique_path.write_text(content, encoding="utf-8")
        print("✅ boutique.html mis à jour → utilise product.affiliate_url")
    else:
        print("⚠️  Pattern non trouvé dans boutique.html - vérification manuelle requise")
        # Afficher ce qui est dans le fichier
        lines = [l for l in content.split('\n') if 'partner.bol.com' in l or 'Koop op' in l]
        for l in lines[:5]:
            print(f"   {l.strip()[:100]}")


if __name__ == "__main__":
    main()
