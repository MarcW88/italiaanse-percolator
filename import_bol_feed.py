#!/usr/bin/env python3
"""Extract percolator products from Bol.com feed and update all_products.json"""
import gzip
import csv
import json
import re
from pathlib import Path

FEED = Path('product-feed_kitchen-household-v2.csv.gz')
OUTPUT = Path('all_products.json')

# Keywords to match percolator-related products
INCLUDE_KW = [
    'percolator', 'moka pot', 'moka express', 'moka induction',
    'bialetti', 'cafetière', 'cafetiere', 'espresso maker',
    'espressomaker', 'espressopotje', 'koffiekan', 'moka inductie',
    'espresso kookplaat', 'stovetop espresso', 'mokkapot',
]

# Keywords to EXCLUDE (false positives)
EXCLUDE_KW = [
    'nespresso', 'dolce gusto', 'senseo', 'capsule', 'pad',
    'koffieboon', 'koffiemolen', 'waterkoker', 'stopcontact',
    'stofzuiger', 'wasmachine', 'barbecue', 'magnetron',
    'vaatwasser', 'koelkast', 'oven ', 'broodrooster',
    'frituur', 'airfryer', 'blender', 'mixer', 'juicer',
    'strijkijzer', 'lamp', 'verlichting', 'tea strainer',
]


def matches(title, desc):
    """Check if product is percolator-related"""
    text = (title + ' ' + desc).lower()
    if any(kw in text for kw in EXCLUDE_KW):
        if not any(kw in text for kw in ['percolator', 'bialetti', 'moka pot', 'moka express']):
            return False
    return any(kw in text for kw in INCLUDE_KW)


def slugify(text):
    s = text.lower().strip()
    s = re.sub(r'[àáâãä]', 'a', s)
    s = re.sub(r'[èéêë]', 'e', s)
    s = re.sub(r'[ìíîï]', 'i', s)
    s = re.sub(r'[òóôõö]', 'o', s)
    s = re.sub(r'[ùúûü]', 'u', s)
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s[:80]


def detect_type(title, desc):
    text = (title + ' ' + desc).lower()
    if any(kw in text for kw in ['elektrisch', 'electric', 'electrisch']):
        return 'Cafetière électrique'
    if any(kw in text for kw in ['filter', 'reserv', 'pakking', 'zeefje', 'rubber', 'trechter',
                                   'handgreep', 'knop', 'onderdeel', 'replacement', 'spare',
                                   'afdichtring', 'filterplaatje', 'reductiering']):
        return 'Accessoire'
    if any(kw in text for kw in ['koffie ', 'coffee ', 'gemalen']):
        if 'percolator' not in text and 'bialetti' not in text:
            return 'Accessoire'
    return 'Cafetière percolateur'


def detect_material(title):
    t = title.lower()
    if 'rvs' in t or 'roestvrij' in t or 'stainless' in t or 'inox' in t:
        return 'RVS'
    return 'Aluminium'


def detect_capacity(title):
    m = re.search(r'(\d+)\s*(?:kops|kop|cups?|kopjes?|tassen)', title.lower())
    if m:
        return int(m.group(1))
    m = re.search(r'(\d+)\s*ml', title.lower())
    if m:
        ml = int(m.group(1))
        if ml <= 50: return 1
        if ml <= 100: return 2
        if ml <= 200: return 3
        if ml <= 300: return 6
        if ml <= 500: return 9
        return 12
    return 0


def detect_induction(title, desc):
    text = (title + ' ' + desc).lower()
    if any(kw in text for kw in ['inductie', 'induction', 'inducti']):
        return 'Oui'
    return 'Non'


def detect_brand(title, brand_field):
    b = brand_field.strip('"').strip()
    if b and b.lower() not in ('merkloos / sans marque', 'merkloos', ''):
        return b
    t = title.lower()
    if 'bialetti' in t: return 'Bialetti'
    if 'alessi' in t: return 'Alessi'
    if 'gnali' in t: return 'Gnali & Zani'
    if 'cilio' in t: return 'Cilio'
    if 'leopold' in t: return 'Leopold Vienna'
    return 'Overig'


def detect_model(title, brand):
    t = title.lower()
    if brand.lower() == 'bialetti':
        if 'venus' in t: return 'Venus'
        if 'moka induction' in t or 'moka inductie' in t: return 'Moka Induction'
        if 'brikka' in t: return 'Brikka'
        if 'mini express' in t: return 'Mini Express'
        if 'rainbow' in t: return 'Rainbow'
        if 'fiammetta' in t: return 'Fiammetta'
        if 'kitty' in t: return 'Kitty'
        if 'moka express' in t or 'moka timer' in t: return 'Moka Express'
        if 'musa' in t: return 'Musa'
        if 'new venus' in t: return 'New Venus'
        return 'Overig'
    return ''


def detect_color(title):
    t = title.lower()
    colors = {
        'rood': 'Rood', 'red': 'Rood', 'rosso': 'Rood',
        'zwart': 'Zwart', 'black': 'Zwart', 'nero': 'Zwart',
        'zilver': 'Zilver', 'silver': 'Zilver',
        'groen': 'Groen', 'green': 'Groen',
        'blauw': 'Blauw', 'blue': 'Blauw',
        'roze': 'Roze', 'pink': 'Roze',
        'goud': 'Goud', 'gold': 'Goud',
        'koper': 'Koper', 'copper': 'Koper',
        'wit': 'Wit', 'white': 'Wit',
        'paars': 'Paars', 'purple': 'Paars',
        'oranje': 'Oranje', 'orange': 'Oranje',
        'geel': 'Geel', 'yellow': 'Geel',
        'creme': 'Crème', 'crème': 'Crème',
    }
    for kw, color in colors.items():
        if kw in t:
            return color
    return 'Zilver/Aluminium'


def parse_price(val):
    if not val:
        return 0
    val = val.strip('"').replace(',', '.')
    try:
        return round(float(val), 2)
    except:
        return 0


def main():
    products = []
    seen_ids = set()

    print("Reading Bol.com feed...")
    with gzip.open(FEED, 'rt', encoding='utf-8', errors='replace') as f:
        reader = csv.reader(f, delimiter='|', quotechar='"')
        header = next(reader)

        col = {h.strip('"'): i for i, h in enumerate(header)}

        row_count = 0
        match_count = 0

        for row in reader:
            row_count += 1
            if row_count % 100000 == 0:
                print(f"  ...{row_count:,} rows scanned, {match_count} matches")

            try:
                title = row[col['title']].strip('"')
                desc = row[col.get('description', 40)].strip('"') if len(row) > 40 else ''
                pid = row[col['productId']].strip('"')
            except (IndexError, KeyError):
                continue

            if pid in seen_ids:
                continue

            if not matches(title, desc):
                continue

            seen_ids.add(pid)
            match_count += 1

            price = parse_price(row[col['OfferNL.sellingPrice']] if len(row) > col['OfferNL.sellingPrice'] else '')
            list_price = parse_price(row[col.get('OfferNL.listPrice', 15)] if len(row) > 15 else '')
            image = row[col['imageUrl']].strip('"') if len(row) > col['imageUrl'] else ''
            url_nl = row[col['productPageUrlNL']].strip('"') if len(row) > col['productPageUrlNL'] else ''
            ean = row[col['ean']].strip('"') if len(row) > col['ean'] else ''
            brand_raw = row[col['brand']].strip('"') if len(row) > col['brand'] else ''
            is_deliverable = row[col.get('OfferNL.isDeliverable', 13)].strip('"') if len(row) > 13 else ''
            color_field = row[col.get('Colour', 45)].strip('"') if len(row) > 45 else ''
            material_field = row[col.get('Material', 50)].strip('"') if len(row) > 50 else ''

            brand = detect_brand(title, brand_raw)
            model = detect_model(title, brand)
            material = material_field if material_field and material_field.lower() not in ('', 'n/a') else detect_material(title)
            capacity = detect_capacity(title)
            induction = detect_induction(title, desc)
            color = color_field if color_field and color_field.lower() not in ('', 'n/a') else detect_color(title)
            prod_type = detect_type(title, desc)
            slug = slugify(title)

            affiliate_url = f"https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url={url_nl.replace(':', '%3A').replace('/', '%2F')}&name={title[:50].replace(' ', '%20')}"

            product = {
                'id': pid,
                'ean': ean,
                'name': title,
                'slug': slug,
                'type': prod_type,
                'brand': brand,
                'model': model,
                'price': price,
                'list_price': list_price,
                'image': image,
                'image_local': f"categories/images/producten/{slug}.jpg",
                'url_bol': url_nl,
                'affiliate_url': affiliate_url,
                'materiaal': material,
                'capaciteit': capacity,
                'inductie': induction,
                'color': color,
                'rating': 4.5,
                'reviews': 0,
                'deliverable': is_deliverable.strip().upper() == 'Y',
                'description': desc[:500] if desc else '',
            }
            products.append(product)

    print(f"\nDone: {row_count:,} total rows, {match_count} percolator products found")

    types = {}
    brands = {}
    for p in products:
        types[p['type']] = types.get(p['type'], 0) + 1
        brands[p['brand']] = brands.get(p['brand'], 0) + 1

    print(f"\nBy type:")
    for t, c in sorted(types.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    print(f"\nTop brands:")
    for b, c in sorted(brands.items(), key=lambda x: -x[1])[:15]:
        print(f"  {b}: {c}")

    deliverable = [p for p in products if p['deliverable'] and p['price'] > 0]
    not_deliverable = [p for p in products if not p['deliverable'] or p['price'] <= 0]
    print(f"\nDeliverable with price: {len(deliverable)}")
    print(f"Not deliverable / no price: {len(not_deliverable)}")

    OUTPUT.write_text(json.dumps(products, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\nSaved {len(products)} products to {OUTPUT}")


if __name__ == '__main__':
    main()
