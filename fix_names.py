"""
Récupère le vrai titre Bol.com pour chaque produit, reconstruit les liens affiliés avec le bon &name=
"""
import re, json, time, requests
from pathlib import Path
from urllib.parse import quote, unquote

AFFILIATE_ID = "1519207"
HTML_DIR = Path(__file__).parent
PRODUCTS_FILE = HTML_DIR / "all_products.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "nl-NL,nl;q=0.9",
}

def get_bol_title(slug, product_id):
    url = f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        # Chercher le titre dans le JSON-LD ou og:title ou h1
        m = re.search(r'"name"\s*:\s*"([^"]{10,})"', r.text)
        if m:
            title = m.group(1)
            # Nettoyer les escapes JSON
            title = title.replace('\\u00e8', 'è').replace('\\u00e9', 'é').replace('\\u00ea', 'ê')
            title = title.replace('\\u00fc', 'ü').replace('\\u00e4', 'ä').replace('\\u00f6', 'ö')
            return title

        # Fallback: og:title
        m2 = re.search(r'<meta property="og:title" content="([^"]+)"', r.text)
        if m2:
            return m2.group(1)

        return None
    except Exception as e:
        print(f"   Erreur: {e}")
        return None

def make_affiliate_url(slug, product_id, name):
    product_url = f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/"
    return (
        f"https://partner.bol.com/click/click?"
        f"p=2&t=url&s={AFFILIATE_ID}&f=TXL"
        f"&url={quote(product_url, safe='')}"
        f"&name={quote(name, safe='')}"
    )

def update_html_files(slug, product_id, old_name, new_affiliate_url):
    """Remplace les liens pour ce produit dans tous les HTML"""
    pattern = re.compile(
        rf'href="https://partner\.bol\.com/click/click\?p=2&t=url&s={AFFILIATE_ID}&f=TXL'
        rf'&url=https%3A%2F%2Fwww\.bol\.com%2Fnl%2Fnl%2Fp%2F{re.escape(slug)}%2F{product_id}%2F'
        rf'&name=[^"]*"'
    )
    count_total = 0
    for html_file in list(HTML_DIR.glob("*.html")) + list((HTML_DIR / "producten").glob("*.html")):
        content = html_file.read_text(encoding="utf-8")
        new_content, count = pattern.subn(f'href="{new_affiliate_url}"', content)
        if count:
            html_file.write_text(new_content, encoding="utf-8")
            count_total += count
    return count_total

def main():
    products = json.load(open(PRODUCTS_FILE, encoding="utf-8"))
    print(f"🔍 {len(products)} produits — récupération des vrais titres Bol.com")
    print("=" * 65)

    updated = 0
    for p in products:
        slug = p.get("slug", "")
        product_id = p.get("product_id", "")
        if not (slug and product_id):
            print(f"[{p['id']:02d}] ⚠️  Sans ID — ignoré")
            continue

        print(f"[{p['id']:02d}] {slug[:55]}...", end=" ")
        title = get_bol_title(slug, product_id)
        time.sleep(1.5)

        if title:
            p["bol_name"] = title
            p["affiliate_url"] = make_affiliate_url(slug, product_id, title)
            count = update_html_files(slug, product_id, p.get("name", ""), p["affiliate_url"])
            print(f"✅ {count} liens → {title[:40]}...")
            updated += 1
        else:
            print(f"⚠️  Titre non trouvé")

    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print("=" * 65)
    print(f"✅ {updated}/{len(products)} produits mis à jour")
    print(f"💾 all_products.json sauvegardé")

if __name__ == "__main__":
    main()
