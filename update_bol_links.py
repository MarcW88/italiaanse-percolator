"""
Script pour télécharger le feed Bol.com via FTP et mettre à jour
les liens affiliés dans tous les fichiers HTML.

Usage:
    python update_bol_links.py

Pré-requis:
    pip install ftplib (inclus dans Python standard)
    
Credentials FTP: à récupérer sur https://partner.bol.com > Productfeed
"""

import ftplib
import csv
import io
import json
import os
import re
import gzip
from pathlib import Path
from urllib.parse import quote

# ============================================================
# CONFIGURATION - Remplir avant de lancer
# ============================================================

FTP_HOST     = "apm-feed.unftp.bol.com"
FTP_USER     = ""   # ← Ton username FTP (depuis partner.bol.com)
FTP_PASS     = ""   # ← Ton password FTP (depuis partner.bol.com)
AFFILIATE_ID = "1066120"  # Déjà présent dans tes liens

# Dossier contenant les fichiers HTML
HTML_DIR = Path(__file__).parent

# ============================================================
# ÉTAPE 1 : Télécharger le feed depuis le FTP Bol.com
# ============================================================

def download_feed():
    print("📡 Connexion au FTP Bol.com...")
    
    ftp = ftplib.FTP_TLS()
    ftp.connect(FTP_HOST, 21)
    ftp.auth()
    ftp.login(FTP_USER, FTP_PASS)
    ftp.prot_p()
    ftp.set_pasv(True)

    print("📂 Fichiers disponibles:")
    files = ftp.nlst()
    for f in files:
        print(f"   - {f}")

    # Prendre le premier fichier CSV ou GZ disponible
    feed_file = None
    for f in files:
        if f.endswith(".csv") or f.endswith(".csv.gz") or f.endswith(".gz"):
            feed_file = f
            break

    if not feed_file:
        print("❌ Aucun fichier feed trouvé")
        ftp.quit()
        return None

    print(f"\n⬇️  Téléchargement de: {feed_file}")
    data = bytearray()
    ftp.retrbinary(f"RETR {feed_file}", data.extend)
    ftp.quit()

    print(f"✅ Téléchargé: {len(data)} bytes")
    return bytes(data), feed_file

# ============================================================
# ÉTAPE 2 : Parser le feed CSV
# ============================================================

def parse_feed(data, filename):
    print("\n📊 Parsing du feed...")

    # Décompresser si GZ
    if filename.endswith(".gz"):
        import gzip
        data = gzip.decompress(data)

    content = data.decode("utf-8", errors="replace")
    reader = csv.DictReader(io.StringIO(content), delimiter=";")

    products = {}
    for row in reader:
        # Champs courants dans le feed Bol.com
        ean     = row.get("EAN", row.get("ean", ""))
        name    = row.get("Naam", row.get("naam", row.get("name", row.get("title", ""))))
        url     = row.get("URL", row.get("url", row.get("Producturl", row.get("producturl", ""))))
        price   = row.get("Prijs", row.get("prijs", row.get("price", "")))
        brand   = row.get("Merk", row.get("merk", row.get("brand", "")))

        if not url or not name:
            continue

        # Créer le lien affilié
        affiliate_url = make_affiliate_link(url)

        products[name.lower()] = {
            "name":          name,
            "ean":           ean,
            "url":           url,
            "affiliate_url": affiliate_url,
            "price":         price,
            "brand":         brand,
        }

    print(f"✅ {len(products)} produits chargés depuis le feed")
    return products

def make_affiliate_link(product_url):
    encoded = quote(product_url, safe="")
    return f"https://partner.bol.com/click/click?p=2&t=url&s={AFFILIATE_ID}&f=TXL&url={encoded}"

# ============================================================
# ÉTAPE 3 : Mapper les produits aux pages HTML
# ============================================================

# Mapping manuel : nom du fichier HTML → mots-clés pour trouver le bon produit
PAGE_PRODUCT_MAP = {
    "bialetti-moka-review.html":       ["bialetti moka express"],
    "bialetti-brikka-review.html":     ["bialetti brikka"],
    "bialetti-venus-review.html":      ["bialetti venus"],
    "bialetti-musa-review.html":       ["bialetti musa"],
    "bialetti-alpina-review.html":     ["bialetti alpina"],
    "bialetti-dama-review.html":       ["bialetti dama"],
    "bialetti-fiammetta-review.html":  ["bialetti fiammetta"],
    "bialetti-mini-express-review.html": ["bialetti mini express"],
    "bialetti-moka-timer-review.html": ["bialetti moka timer"],
    "alessi-9090-review.html":         ["alessi 9090"],
    "alessi-la-conica-review.html":    ["alessi la conica"],
    "alessi-moka-review.html":         ["alessi moka"],
    "alessi-pulcina-review.html":      ["alessi pulcina"],
    "grosche-milano-review.html":      ["grosche milano"],
    "giannini-giannina-review.html":   ["giannini giannina"],
    "stelton-collar-review.html":      ["stelton collar"],
    "delonghi-alicia-review.html":     ["delonghi alicia"],
    "rommelsbacher-eko366-review.html":["rommelsbacher eko"],
    "cilio-classico-electric-review.html": ["cilio classico"],
    "cloer-5928-review.html":          ["cloer 5928"],
}

def find_best_match(keywords, products):
    """Cherche le meilleur produit dans le feed pour une page donnée"""
    for keyword in keywords:
        keyword_lower = keyword.lower()
        # Correspondance exacte
        if keyword_lower in products:
            return products[keyword_lower]
        # Correspondance partielle
        for name, product in products.items():
            if keyword_lower in name or all(w in name for w in keyword_lower.split()):
                return product
    return None

# ============================================================
# ÉTAPE 4 : Mettre à jour les fichiers HTML
# ============================================================

def update_html_files(products):
    print("\n✏️  Mise à jour des fichiers HTML...")

    results = {}
    updated = 0
    not_found = []

    for html_file, keywords in PAGE_PRODUCT_MAP.items():
        filepath = HTML_DIR / html_file
        if not filepath.exists():
            print(f"   ⚠️  Fichier non trouvé: {html_file}")
            continue

        product = find_best_match(keywords, products)
        if not product:
            print(f"   ❌ Produit non trouvé pour: {html_file} (mots-clés: {keywords})")
            not_found.append(html_file)
            continue

        new_url = product["affiliate_url"]
        content = filepath.read_text(encoding="utf-8")

        # Remplacer tous les liens partner.bol.com dans ce fichier
        old_pattern = re.compile(
            r'href="https://partner\.bol\.com/click/click\?[^"]*"'
        )
        new_href = f'href="{new_url}"'
        new_content, count = old_pattern.subn(new_href, content)

        if count > 0:
            filepath.write_text(new_content, encoding="utf-8")
            print(f"   ✅ {html_file}: {count} lien(s) mis à jour → {product['name']} ({product['price']})")
            updated += 1
            results[html_file] = {
                "product": product["name"],
                "ean": product["ean"],
                "price": product["price"],
                "affiliate_url": new_url,
                "links_updated": count
            }
        else:
            print(f"   ⚠️  {html_file}: aucun lien à remplacer")

    # Sauvegarder le rapport
    report_path = HTML_DIR / "bol_links_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 {updated}/{len(PAGE_PRODUCT_MAP)} pages mises à jour")
    if not_found:
        print(f"⚠️  Produits non trouvés pour: {', '.join(not_found)}")
    print(f"📄 Rapport sauvegardé: {report_path}")

# ============================================================
# MAIN
# ============================================================

def main():
    if not FTP_USER or not FTP_PASS:
        print("❌ Remplis FTP_USER et FTP_PASS en haut du script !")
        print("   → Va sur https://partner.bol.com > Productfeed")
        return

    # 1. Télécharger le feed
    result = download_feed()
    if not result:
        return
    data, filename = result

    # Sauvegarder le feed localement (pour éviter de re-télécharger)
    feed_path = HTML_DIR / f"bol_feed_{filename}"
    with open(feed_path, "wb") as f:
        f.write(data)
    print(f"💾 Feed sauvegardé: {feed_path}")

    # 2. Parser le feed
    products = parse_feed(data, filename)
    if not products:
        print("❌ Aucun produit parsé. Vérifie le format du feed.")
        return

    # Optionnel: sauvegarder les produits en JSON pour inspection
    products_path = HTML_DIR / "bol_products.json"
    with open(products_path, "w", encoding="utf-8") as f:
        json.dump(list(products.values())[:50], f, ensure_ascii=False, indent=2)
    print(f"💾 Aperçu produits: {products_path} (50 premiers)")

    # 3. Mettre à jour les HTML
    update_html_files(products)

if __name__ == "__main__":
    main()
