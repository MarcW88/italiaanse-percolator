"""
Récupère le VRAI titre produit Bol.com depuis le JSON-LD @type Product ou og:title,
puis reconstruit tous les liens affiliés avec le bon &name=
"""
import re, json, time, requests
from pathlib import Path
from urllib.parse import quote

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

        # 1. JSON-LD @type Product → "name" (le vrai nom produit)
        ld_blocks = re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', r.text, re.DOTALL)
        for block in ld_blocks:
            if '"Product"' in block or '"product"' in block:
                m = re.search(r'"name"\s*:\s*"([^"]{5,})"', block)
                if m:
                    return m.group(1)

        # 2. og:title (retire " | bol.com" à la fin)
        m2 = re.search(r'<meta property="og:title" content="([^"]+)"', r.text)
        if m2:
            title = m2.group(1)
            title = re.sub(r'\s*[|\-]\s*bol\.com.*$', '', title).strip()
            return title

        # 3. <h1 itemprop="name"> ou <h1 class="...product...">
        m3 = re.search(r'<h1[^>]*>([^<]{10,})</h1>', r.text)
        if m3:
            return m3.group(1).strip()

        return None
    except Exception as e:
        return None

def make_affiliate_url(slug, product_id, name):
    product_url = f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/"
    return (
        f"https://partner.bol.com/click/click?"
        f"p=2&t=url&s={AFFILIATE_ID}&f=TXL"
        f"&url={quote(product_url, safe='')}"
        f"&name={quote(name, safe='')}"
    )

def update_html_files(slug, product_id, new_affiliate_url):
    """Remplace TOUS les liens partner.bol.com pour ce slug+id dans tous les HTML"""
    # Pattern large qui matche peu importe l'ancien &name=
    pattern = re.compile(
        r'href="https://partner\.bol\.com/click/click\?[^"]*'
        + re.escape(f"url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2F{slug}%2F{product_id}%2F")
        + r'[^"]*"'
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
    print(f"🔍 {len(products)} produits — récupération vrais titres Bol.com")
    print("=" * 70)

    updated = 0
    for p in products:
        slug = p.get("slug", "")
        product_id = p.get("product_id", "")
        if not (slug and product_id):
            print(f"[{p['id']:02d}] ⚠️  Sans ID — ignoré")
            continue

        print(f"[{p['id']:02d}] {slug[:50]}...", end=" ", flush=True)
        title = get_bol_title(slug, product_id)
        time.sleep(1.5)

        if title:
            p["bol_name"] = title
            p["affiliate_url"] = make_affiliate_url(slug, product_id, title)
            count = update_html_files(slug, product_id, p["affiliate_url"])
            print(f"✅ ({count} liens) → {title[:45]}")
            updated += 1
        else:
            print(f"⚠️  Titre non trouvé")

    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print("=" * 70)
    print(f"✅ {updated}/{len(products)} produits mis à jour")
    print(f"💾 all_products.json sauvegardé")

if __name__ == "__main__":
    main()
