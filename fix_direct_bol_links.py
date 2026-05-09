"""
Remplace tous les liens partner.bol.com (redirect) par des liens directs bol.com avec tracking.
Format cible: https://www.bol.com/nl/nl/p/[slug]/[id]/?Referrer=ADVNLPP...&utm_source=...
"""
import re
import json
from pathlib import Path
from urllib.parse import unquote

HTML_DIR = Path(__file__).parent

TRACKING = "?Referrer=ADVNLPPceead800093f9c9c0065bba51d681519207&utm_source=1519207&utm_medium=Affiliates&utm_campaign=CPS&utm_content=txl"

def make_direct_url(slug, product_id):
    return f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/{TRACKING}"

def fix_file(filepath):
    content = filepath.read_text(encoding="utf-8")

    # Remplacer les liens partner.bol.com qui contiennent /nl/nl/p/[slug]/[id]/
    pattern = re.compile(
        r'href="https://partner\.bol\.com/click/click\?[^"]*url=([^&"]+)[^"]*"'
    )

    def replace_partner_link(m):
        encoded_url = m.group(1)
        decoded_url = unquote(encoded_url)
        # Extraire slug et ID depuis l'URL bol.com décodée
        match = re.search(r'/nl/nl/p/([^/]+)/(\d+)/', decoded_url)
        if match:
            slug = match.group(1)
            product_id = match.group(2)
            return f'href="{make_direct_url(slug, product_id)}"'
        return m.group(0)  # Laisser inchangé si pas de match

    new_content, count = pattern.subn(replace_partner_link, content)

    if count > 0:
        filepath.write_text(new_content, encoding="utf-8")

    return count

def fix_all_products_json():
    """Met aussi à jour all_products.json"""
    products_path = HTML_DIR / "all_products.json"
    products = json.load(open(products_path, encoding="utf-8"))

    for p in products:
        slug = p.get("slug", "")
        product_id = p.get("product_id", "")
        if slug and product_id:
            p["affiliate_url"] = make_direct_url(slug, product_id)
        elif slug:
            # Sans ID : URL sans le /id/ mais avec tracking
            p["affiliate_url"] = f"https://www.bol.com/nl/nl/p/{slug}/{TRACKING}"

    with open(products_path, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print("✅ all_products.json mis à jour")

def main():
    html_files = list(HTML_DIR.glob("*.html")) + list((HTML_DIR / "producten").glob("*.html"))
    print(f"🔍 {len(html_files)} fichiers HTML à traiter...")
    print("=" * 60)

    total = 0
    for f in sorted(html_files):
        count = fix_file(f)
        if count:
            print(f"✅ {f.relative_to(HTML_DIR)}: {count} lien(s)")
            total += count

    print("=" * 60)
    print(f"🎉 {total} liens mis à jour")

    fix_all_products_json()

if __name__ == "__main__":
    main()
