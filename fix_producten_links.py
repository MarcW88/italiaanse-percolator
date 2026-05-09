"""
Corrige les liens bol.com sans tracking dans le dossier producten/
"""
import re
from pathlib import Path
from urllib.parse import quote

AFFILIATE_ID = "1519207"
PRODUCTEN_DIR = Path(__file__).parent / "producten"

def fix_file(filepath):
    content = filepath.read_text(encoding="utf-8")

    pattern = re.compile(
        r'href="https://www\.bol\.com/nl/nl/p/([^/]+)/(\d+)/"'
    )

    def replace_link(m):
        slug = m.group(1)
        product_id = m.group(2)
        name = slug.replace("-", " ").title()
        product_url = f"https://www.bol.com/nl/nl/p/{slug}/{product_id}/"
        encoded_url = quote(product_url, safe="")
        encoded_name = quote(name, safe="")
        affiliate_url = (
            f"https://partner.bol.com/click/click?"
            f"p=2&t=url&s={AFFILIATE_ID}&f=TXL"
            f"&url={encoded_url}"
            f"&name={encoded_name}"
        )
        return f'href="{affiliate_url}"'

    new_content, count = pattern.subn(replace_link, content)

    if count > 0:
        # Remplacer aussi rel="nofollow" par rel="sponsored" sur ces liens
        new_content = new_content.replace('rel="nofollow"', 'rel="sponsored"')
        filepath.write_text(new_content, encoding="utf-8")

    return count

def main():
    files = list(PRODUCTEN_DIR.glob("*.html"))
    print(f"🔍 {len(files)} fichiers dans producten/")
    print("=" * 60)

    total = 0
    for f in sorted(files):
        count = fix_file(f)
        if count:
            print(f"✅ {f.name}: {count} lien(s) corrigé(s)")
            total += count

    print("=" * 60)
    print(f"🎉 {total} liens corrigés dans {len(files)} fichiers")

if __name__ == "__main__":
    main()
