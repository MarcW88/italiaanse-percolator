import json, re
from urllib.parse import quote

slug = "bialetti-moka-alpina-limited-editions-3-kops-120ml"
pid = "9200000104569191"
title = "Bialetti Moka Alpina - Limited Edition percolator - 3 kops - 120ml"
affiliate_url = (
    "https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL"
    f"&url={quote('https://www.bol.com/nl/nl/p/' + slug + '/' + pid + '/', safe='')}"
    f"&name={quote(title, safe='')}"
)

# Mettre à jour all_products.json
products = json.load(open("all_products.json", encoding="utf-8"))
for p in products:
    if p["slug"] == slug:
        p["product_id"] = pid
        p["bol_name"] = title
        p["affiliate_url"] = affiliate_url
        print("JSON mis a jour:", title)
        break
with open("all_products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

# Mettre à jour le fichier HTML du produit
html_path = f"producten/{slug}.html"
content = open(html_path, encoding="utf-8").read()
new_content = re.sub(
    r'href="https://partner\.bol\.com/click/click\?[^"]+"',
    f'href="{affiliate_url}"',
    content
)
open(html_path, "w", encoding="utf-8").write(new_content)
print("HTML mis a jour")
print("URL:", affiliate_url)
