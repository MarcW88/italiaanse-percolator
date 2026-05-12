#!/usr/bin/env python3
from pathlib import Path
import json
import math
import html
from datetime import date

ROOT = Path('/Users/marc/Desktop/italiaanse-percolator')
PER_PAGE = 24
SITE = 'https://italiaanse-percolator.nl'

CATEGORY_CONFIG = {
    'percolators': {
        'title': 'Percolators kopen',
        'h1': 'Alle percolators',
        'description': 'Vergelijk klassieke Italiaanse percolators voor gas, elektrisch, keramisch en inductie.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur',
    },
    'elektrische-percolators': {
        'title': 'Elektrische percolators kopen',
        'h1': 'Elektrische percolators',
        'description': 'Vergelijk elektrische percolators en moka apparaten zonder kookplaat.',
        'filter': lambda p: p.get('type') == 'Cafetière électrique',
    },
    'accessoires': {
        'title': 'Percolator accessoires kopen',
        'h1': 'Percolator accessoires',
        'description': 'Onderdelen, filters, ringen en accessoires voor percolators en koffiezetters.',
        'filter': lambda p: p.get('type') == 'Accessoire',
    },
    'percolators-inductie': {
        'title': 'Inductie percolators kopen',
        'h1': 'Percolators voor inductie',
        'description': 'Vind percolators die geschikt zijn voor inductiekookplaten.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and p.get('inductie') == 'Oui',
    },
    'percolators-aluminium': {
        'title': 'Aluminium percolators kopen',
        'h1': 'Aluminium percolators',
        'description': 'Klassieke aluminium moka pots voor authentieke Italiaanse koffie.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and 'aluminium' in (p.get('materiaal') or '').lower(),
    },
    'percolators-rvs': {
        'title': 'RVS percolators kopen',
        'h1': 'RVS percolators',
        'description': 'Duurzame roestvrijstalen percolators, vaak geschikt voor inductie.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and any(x in (p.get('materiaal') or '').lower() for x in ['rvs', 'roestvrij', 'inox', 'acier']),
    },
    'percolators-1-2-kops': {
        'title': '1 en 2 kops percolators kopen',
        'h1': '1 en 2 kops percolators',
        'description': 'Compacte percolators voor één persoon of kleine espresso-momenten.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and str(p.get('capaciteit') or '').strip() in {'1', '2'},
    },
    'percolators-3-kops': {
        'title': '3 kops percolators kopen',
        'h1': '3 kops percolators',
        'description': 'Populaire 3-kops moka pots voor dagelijks gebruik.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and str(p.get('capaciteit') or '').strip() == '3',
    },
    'percolators-6-kops': {
        'title': '6 kops percolators kopen',
        'h1': '6 kops percolators',
        'description': '6-kops percolators voor gezinnen en meerdere espresso’s tegelijk.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and str(p.get('capaciteit') or '').strip() == '6',
    },
    'percolators-9-kops': {
        'title': '9 kops percolators kopen',
        'h1': '9 kops percolators',
        'description': 'Grote 9-kops percolators voor meerdere koffiedrinkers.',
        'filter': lambda p: p.get('type') == 'Cafetière percolateur' and str(p.get('capaciteit') or '').strip() == '9',
    },
    'inductie-adapters': {
        'title': 'Inductie adapters kopen',
        'h1': 'Inductie adapters',
        'description': 'Adapters voor het gebruiken van klassieke percolators op inductie.',
        'filter': lambda p: 'adapter' in (p.get('name') or '').lower() or 'inductie-adapter' in (p.get('description') or '').lower(),
    },
    'onderhoudssets': {
        'title': 'Onderhoudssets voor percolators',
        'h1': 'Onderhoudssets',
        'description': 'Rubberen ringen, filters en onderhoudssets voor moka pots.',
        'filter': lambda p: any(x in (p.get('name') or '').lower() for x in ['onderhoud', 'ringen', 'filterplaat', 'filterplaatje', 'rubber']),
    },
}

NAV_ROOT = '''    <nav class="navbar">
        <div class="container"><div class="nav-container">
            <a href="{prefix}index.html" class="nav-brand">Italiaanse Percolator</a>
            <ul class="nav-menu">
                <li><a href="{prefix}index.html" class="nav-link">Home</a></li>
                <li class="nav-item dropdown"><a href="{prefix}beste-italiaanse-percolators.html" class="nav-link dropdown-toggle">Gidsen</a>
                    <ul class="dropdown-menu"><li><a href="{prefix}beste-italiaanse-percolators.html" class="dropdown-link">Top 10</a></li><li><a href="{prefix}koopgids/index.html" class="dropdown-link">Koopgids</a></li><li><a href="{prefix}alle-reviews.html" class="dropdown-link">Reviews</a></li><li><a href="{prefix}vergelijking/index.html" class="dropdown-link">Vergelijking</a></li></ul>
                </li>
                <li><a href="{prefix}marques/index.html" class="nav-link">Merken</a></li>
                <li class="nav-item dropdown"><a href="{prefix}boutique.html" class="nav-link dropdown-toggle active">Shop</a>
                    <ul class="dropdown-menu"><li><a href="{prefix}boutique.html" class="dropdown-link">Alle modellen</a></li><li><a href="{prefix}categories/percolators.html" class="dropdown-link">Percolators</a></li><li><a href="{prefix}categories/elektrische-percolators.html" class="dropdown-link">Elektrisch</a></li><li><a href="{prefix}categories/accessoires.html" class="dropdown-link">Accessoires</a></li></ul>
                </li>
            </ul>
        </div></div>
    </nav>'''

FOOTER = '''    <footer class="footer"><div class="container">
        <div class="footer-content"><div><p style="font-family: var(--font-serif); font-size: 1.2rem; color: white; margin-bottom: 1rem;">Italiaanse Percolator</p><p style="color: #999; font-size: 0.85rem; line-height: 1.7; margin-bottom: 0;">Onafhankelijke gids voor Italiaanse moka-percolators.</p></div><div><h4>Gidsen</h4><a href="{prefix}beste-italiaanse-percolators.html">Top 10 percolators</a><br><a href="{prefix}koopgids/index.html">Koopgids</a></div><div><h4>Merken</h4><a href="{prefix}marques/bialetti/">Bialetti</a><br><a href="{prefix}marques/alessi/">Alessi</a></div><div><h4>Info</h4><a href="{prefix}over-ons.html">Over ons</a><br><a href="{prefix}contact.html">Contact</a></div></div>
        <div class="footer-bottom">© 2025 Italiaanse Percolator. Alle rechten voorbehouden.</div>
    </div></footer>'''


def fmt_price(p):
    price = p.get('price')
    return f"€{price:.2f}".replace('.', ',') if isinstance(price, (int, float)) else ''


def card(p, prefix):
    badges = []
    if p.get('inductie') == 'Oui':
        badges.append('Inductie')
    if p.get('capaciteit'):
        badges.append(f"{p['capaciteit']} kops")
    if p.get('materiaal'):
        badges.append(p['materiaal'])
    badge_html = ''.join(f'<span style="font-size:0.72rem;color:var(--text-light);border:1px solid var(--border);padding:0.2rem 0.5rem;border-radius:0.5rem;">{html.escape(str(b))}</span>' for b in badges[:3])
    name = html.escape(p.get('name') or '')
    img = html.escape(p.get('image') or f'{prefix}Images/placeholder-product.jpg')
    slug = html.escape(p.get('slug') or '')
    aff = html.escape(p.get('affiliate_url') or '#')
    rating = p.get('rating') or ''
    rating_html = f'<span style="font-size:0.78rem;color:var(--text-light);">{rating}/5</span>' if rating else ''
    return f'''            <div style="border:1px solid var(--border);overflow:hidden;background:white;transition:border-color 0.2s;border-radius:0.5rem;display:flex;flex-direction:column;height:100%;" onmouseover="this.style.borderColor='var(--coffee)'" onmouseout="this.style.borderColor='var(--border)'">
                <div style="background:#fafafa;padding:1rem;text-align:center;"><img src="{img}" alt="{name}" loading="lazy" style="height:160px;width:100%;object-fit:contain;" onerror="this.src='{prefix}Images/placeholder-product.jpg'"></div>
                <div style="padding:1rem;">
                    <div style="display:flex;gap:0.35rem;flex-wrap:wrap;margin-bottom:0.5rem;">{badge_html}</div>
                    <h3 style="font-size:0.88rem;font-weight:600;line-height:1.35;margin-bottom:0.5rem;height:2.4rem;overflow:hidden;">{name}</h3>
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
                        <span style="font-size:1.1rem;font-weight:700;">{fmt_price(p)}</span>
                        {rating_html}
                    </div>
                    <a href="{aff}" target="_blank" rel="sponsored" style="display:block;text-align:center;padding:0.55rem;background:var(--coffee);color:white;text-decoration:none;border-radius:0.3rem;font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Bekijk op Bol.com</a>
                    <a href="{prefix}producten/{slug}.html" style="display:block;text-align:center;padding:0.45rem;border:1px solid var(--border);color:var(--text-dim);text-decoration:none;border-radius:0.3rem;font-size:0.78rem;">Details</a>
                </div>
            </div>'''


def page_url(kind, slug, page):
    if kind == 'boutique':
        return 'boutique.html' if page == 1 else f'boutique.html?page={page}'
    return f'categories/{slug}.html' if page == 1 else f'categories/{slug}.html?page={page}'


def local_path(kind, slug, page):
    # Only generate page 1 as base file; query parameters handled by JS
    if kind == 'boutique':
        return ROOT / 'boutique.html'
    return ROOT / f'categories/{slug}.html'


def pagination(kind, slug, current, total, prefix):
    if total <= 1:
        return ''
    links = []
    if current > 1:
        href = prefix + page_url(kind, slug, current - 1)
        links.append(f'<a href="{href}" class="pagination-link">Vorige</a>')
    start = max(1, current - 2)
    end = min(total, current + 2)
    if start > 1:
        links.append(f'<a href="{prefix + page_url(kind, slug, 1)}" class="pagination-link">1</a>')
        if start > 2:
            links.append('<span class="pagination-gap">…</span>')
    for n in range(start, end + 1):
        href = prefix + page_url(kind, slug, n)
        cls = 'pagination-link active' if n == current else 'pagination-link'
        links.append(f'<a href="{href}" class="{cls}">{n}</a>')
    if end < total:
        if end < total - 1:
            links.append('<span class="pagination-gap">…</span>')
        links.append(f'<a href="{prefix + page_url(kind, slug, total)}" class="pagination-link">{total}</a>')
    if current < total:
        links.append(f'<a href="{prefix + page_url(kind, slug, current + 1)}" class="pagination-link">Volgende</a>')
    return '<nav class="shop-pagination" aria-label="Paginering">' + ''.join(links) + '</nav>'


def render(kind, slug, products, page, total_pages, title, h1, description):
    prefix = '' if kind == 'boutique' else '../'
    url_path = page_url(kind, slug, page)
    canonical = f'{SITE}/{url_path}'
    title_full = title if page == 1 else f'{title} - pagina {page}'
    meta = description if page == 1 else f'{description} Pagina {page} van {total_pages}.'
    start = (page - 1) * PER_PAGE
    items = products[start:start + PER_PAGE]
    grid = '\n'.join(card(p, prefix) for p in items)
    cats_prefix = prefix + 'categories/'
    category_links = (
        f'<a href="{cats_prefix}percolators.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Percolators</a>'
        f'<a href="{cats_prefix}elektrische-percolators.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Elektrisch</a>'
        f'<a href="{cats_prefix}accessoires.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Accessoires</a>'
        f'<a href="{cats_prefix}percolators-inductie.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Inductie</a>'
        f'<a href="{cats_prefix}percolators-aluminium.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">Aluminium</a>'
        f'<a href="{cats_prefix}percolators-rvs.html" style="color: var(--text-dim); text-decoration: none; padding: 0.4rem 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem;">RVS</a>'
    )
    products_json = json.dumps(products, ensure_ascii=False)
    base_url = page_url(kind, slug, 1)
    
    # Category-specific content
    intro_html = ''
    content_below_html = ''
    faq_html = ''
    
    if kind == 'category' and slug == 'percolators':
        intro_html = '''
    <div style="background:#fafafa;padding:2rem 0;margin-bottom:2rem;">
        <div class="container" style="max-width:800px;">
            <p><strong>Op zoek naar een échte Italiaanse koffiebeleving thuis?</strong> Met een Italiaanse percolator zet je sterke, aromatische koffie zoals in een bar in Rome – zonder dure volautomaat of ingewikkelde instellingen. Of je nu één kopje drinkt of koffie zet voor het hele gezin, in onze collectie vind je de italiaanse percolator die past bij jouw fornuis, budget en koffieritueel.</p>
            <p>Bij Italiaanse‑Percolator.nl vind je uitsluitend percolators die getest zijn op smaak, gebruiksgemak en duurzaamheid. Denk aan klassieke aluminium mokapotten voor gas of elektrisch, maar ook moderne roestvrijstalen modellen die geschikt zijn voor inductie. We helpen je kiezen op basis van formaat (van 1 tot 12 koppen), warmtebron en gewenste koffiesterkte, zodat je precies de juiste italiaanse percolator kunt kopen.</p>
            <a href="#percolator-lees-meer" style="color:var(--coffee);text-decoration:none;font-weight:600;">Lees meer &raquo;</a>
        </div>
    </div>'''
        content_below_html = '''
    <div id="percolator-lees-meer" style="background:#fafafa;padding:3rem 0;margin-top:3rem;">
        <div class="container" style="max-width:800px;">
            <h2 style="font-family:var(--font-serif);font-size:1.8rem;font-weight:400;margin-bottom:1.5rem;">Welke italiaanse percolator moet ik kopen?</h2>
            <p style="color:var(--text-dim);line-height:1.7;margin-bottom:1rem;">De keuze voor de juiste percolator hangt vooral af van drie dingen: je warmtebron, het aantal kopjes dat je gemiddeld zet en hoe sterk je jouw koffie wilt. Klassieke aluminium mokapotten werken perfect op gas en elektrisch, terwijl roestvrijstalen modellen vaak geschikt zijn voor inductie. Let daarnaast op het aantal koppen: een 3-kops percolator is ideaal voor 1 à 2 personen, terwijl 6-kops en 9-kops modellen beter passen bij gezinnen of koffiedrinkers die meerdere kopjes per keer zetten.</p>
            <p style="color:var(--text-dim);line-height:1.7;">Een Italiaanse percolator is bewust eenvoudig: water onderin, gemalen koffie in het filter en enkele minuten later een volle, geconcentreerde koffie bovenin. Met de juiste maling en hoeveelheid koffie haal je een smaak die dicht in de buurt komt van espresso, maar dan met het karakteristieke Italiaanse ritueel op het fornuis. In elke productfiche geven we aan voor welk fornuis het model geschikt is, hoeveel kopjes je ermee zet en welke maling we adviseren. Zo kun je met een gerust hart de italiaanse percolator kopen die het beste bij jou past.</p>
        </div>
    </div>'''
        faq_html = '''
    <section style="padding:3rem 0;">
        <div class="container" style="max-width:800px;">
            <h2 style="font-family:var(--font-serif);font-size:1.8rem;font-weight:400;margin-bottom:2rem;">Veelgestelde vragen over een italiaanse percolator kopen</h2>
            <div style="display:flex;flex-direction:column;gap:1.5rem;">
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Wat is een italiaanse percolator precies?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Een italiaanse percolator – vaak mokapot genoemd – is een klassiek koffiezetapparaat dat je op het fornuis gebruikt. Het water wordt onderin verwarmd, door de gemalen koffie omhoog geperst en komt als sterke, aromatische koffie in het bovenste deel terecht.</p>
                </div>
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Is een italiaanse percolator geschikt voor inductie?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Dat hangt af van het materiaal. Aluminium percolators werken meestal niet op inductie, terwijl roestvrijstalen modellen vaak wel inductiegeschikt zijn. In onze productbeschrijvingen staat altijd duidelijk aangegeven of een percolator op inductie gebruikt kan worden.</p>
                </div>
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Hoeveel kopjes koffie kan ik met een percolator zetten?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Percolators worden uitgedrukt in "koppen", meestal tussen 1 en 12. Een 3-kops percolator levert ongeveer 2 kleine tot 3 espresso-achtige kopjes op, een 6-kops is geschikt voor 3 à 4 koffiedrinkers. Kies liever iets groter als je vaak bezoek hebt of meerdere kopjes achter elkaar drinkt.</p>
                </div>
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Welke koffie gebruik ik in een italiaanse percolator?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Voor een Italiaanse percolator gebruik je een maling tussen espresso en filter in: fijner dan filterkoffie, maar niet zo fijn als voor een espressomachine. Te fijne maling kan bitterheid geven, te grof zorgt voor een waterige koffie.</p>
                </div>
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Wat zijn de voordelen van een italiaanse percolator?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Je hebt geen dure machine nodig, zet snel sterke koffie met veel aroma en geniet van een authentiek Italiaans ritueel op het fornuis. Bovendien nemen percolators weinig ruimte in en zijn ze eenvoudig schoon te maken.</p>
                </div>
            </div>
        </div>
    </section>'''
    elif kind == 'category' and slug == 'elektrische-percolators':
        intro_html = '''
    <div style="background:#fafafa;padding:2rem 0;margin-bottom:2rem;">
        <div class="container" style="max-width:800px;">
            <p><strong>Wil je zonder gedoe verse koffie zetten, gewoon met één druk op de knop?</strong> Met een elektrische percolator combineer je de volle smaak van traditionele percolatorkoffie met het gemak van een modern apparaat. Je hebt geen fornuis nodig: stekker in het stopcontact, water en koffie erin, en de percolator regelt de temperatuur en doorlooptijd voor je.</p>
            <p>Of je nu een compacte elektrische percolator zoekt voor 2–6 kopjes aan de ontbijttafel, of een grotere variant voor familie, kantoor of feestjes: in onze selectie vind je makkelijk het model dat bij jouw gebruik past. Filter op inhoud, materiaal (RVS of aluminium), warmhoudfunctie en design om snel de juiste elektrische percolator te kopen.</p>
            <a href="#elektrische-percolator-lees-meer" style="color:var(--coffee);text-decoration:none;font-weight:600;">Lees meer over elektrische percolators &raquo;</a>
        </div>
    </div>'''
        content_below_html = '''
    <div id="elektrische-percolator-lees-meer" style="background:#fafafa;padding:3rem 0;margin-top:3rem;">
        <div class="container" style="max-width:800px;">
            <h2 style="font-family:var(--font-serif);font-size:1.8rem;font-weight:400;margin-bottom:1.5rem;">Welke elektrische percolator past bij mij?</h2>
            <p style="color:var(--text-dim);line-height:1.7;margin-bottom:1rem;">Bij het kiezen van een elektrische percolator zijn vooral de inhoud, warmhoudmogelijkheden en het gebruiksgemak belangrijk. Kleinere modellen van 2 tot 6 kopjes zijn ideaal voor thuis, terwijl grotere percolators met 10+ kopjes handig zijn voor vergaderingen, brunches of feestjes. Veel elektrische percolators schakelen automatisch uit en houden de koffie daarna nog een tijd op drinktemperatuur, zodat je niet hoeft op te letten of de koffie "doorkookt".</p>
            <p style="color:var(--text-dim);line-height:1.7;">Een elektrische percolator is interessant als je de smaak van percolatorkoffie wilt, maar geen zin hebt in een fornuis of aparte kookplaat. Je zet de kan neer waar je wilt, vult water en gemalen koffie, en de rest gaat vanzelf. In de productbeschrijving vermelden we steeds hoeveel kopjes je per zetbeurt maakt, of er een warmhoudfunctie is, welk materiaal gebruikt is en hoe lang het snoer is. Zo kun je met vertrouwen de elektrische percolator kopen die precies past bij jouw keuken, kantoor of vakantiehuis.</p>
        </div>
    </div>'''
        faq_html = '''
    <section style="padding:3rem 0;">
        <div class="container" style="max-width:800px;">
            <h2 style="font-family:var(--font-serif);font-size:1.8rem;font-weight:400;margin-bottom:2rem;">Veelgestelde vragen over een elektrische percolator kopen</h2>
            <div style="display:flex;flex-direction:column;gap:1.5rem;">
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Wat is een elektrische percolator precies?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Een elektrische percolator is een percolator met een ingebouwd verwarmingselement. In plaats van op gas of inductie plaats je het apparaat gewoon op het aanrecht, steekt de stekker in het stopcontact en het water wordt automatisch verhit tot de koffie klaar is.</p>
                </div>
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Wat zijn de voordelen van een elektrische percolator?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Je hebt geen fornuis nodig, de temperatuur en zetduur zijn constant en veel modellen hebben een warmhoudfunctie. Dat maakt een elektrische percolator ideaal als je meerdere kopjes achter elkaar wilt schenken zonder erbij te moeten blijven.</p>
                </div>
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Hoeveel kopjes koffie kan ik met een elektrische percolator zetten?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Dat verschilt per model: er zijn compacte toestellen voor 2–4 kopjes, maar ook grote elektrische percolators voor 10 tot 40+ kopjes. In de productinformatie staat altijd duidelijk het maximale aantal kopjes per zetbeurt vermeld.</p>
                </div>
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Welke koffie gebruik ik in een elektrische percolator?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Gebruik gemalen koffie met een maling tussen filter en espresso in. Te fijne maling kan zorgen voor een bittere smaak, te grof geeft eerder een slappe koffie. Vaak werkt een speciale "percolator" of "moka" maling het best.</p>
                </div>
                <div>
                    <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">Is een elektrische percolator geschikt voor op kantoor of bij feestjes?</h3>
                    <p style="color:var(--text-dim);line-height:1.7;">Ja, zeker. Vooral de grotere modellen zijn ideaal voor kantoor, brunch of feest: je zet in één keer een volle kan en dankzij de warmhoudfunctie blijft de koffie langer op temperatuur. Dat is praktischer dan steeds aparte kopjes zetten met een volautomaat.</p>
                </div>
            </div>
        </div>
    </section>'''
    
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title_full)} | Italiaanse Percolator</title>
    <meta name="description" content="{html.escape(meta)}">
    <link rel="stylesheet" href="{prefix}style.css">
    <link rel="canonical" href="{canonical}">
    <link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg">
</head>
<body>
{NAV_ROOT.format(prefix=prefix)}
    <section style="background:#f5f0ea;padding:3rem 0 2.5rem;"><div class="container" style="max-width:780px;">
        <p style="font-size:0.78rem;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.75rem;"><a href="{prefix}index.html" style="color:var(--text-light);text-decoration:none;">Home</a> / Shop</p>
        <h1 style="font-family:var(--font-serif);font-size:clamp(1.8rem,3vw,2.4rem);font-weight:400;margin-bottom:0.75rem;">{html.escape(h1)}</h1>
        <p style="color:var(--text-dim);font-size:1rem;max-width:540px;">{html.escape(description)} {len(products)} producten gevonden.</p>
    </div></section>
    <div style="border-bottom:1px solid var(--border);padding:1rem 0;"><div class="container" style="display:flex;gap:1.5rem;flex-wrap:wrap;font-size:0.85rem;">
        {category_links}
    </div></div>
{intro_html}
    <main class="container" style="padding:2.5rem 0;">
        <p id="page-info" style="color:var(--text-dim);margin-bottom:1.5rem;">Pagina laden...</p>
        <div id="products-grid" class="shop-product-grid"></div>
        <div id="pagination"></div>
    </main>
{content_below_html}
{faq_html}
{FOOTER.format(prefix=prefix)}
    <script>
    const allProducts = {products_json};
    const perPage = {PER_PAGE};
    const baseUrl = '{base_url}';
    let currentPage = 1;
    
    function getPageUrl(page) {{
        return page === 1 ? baseUrl : baseUrl + '?page=' + page;
    }}
    
    function getPageFromUrl() {{
        const params = new URLSearchParams(window.location.search);
        const p = parseInt(params.get('page'));
        return isNaN(p) ? 1 : p;
    }}
    
    function renderPage(page) {{
        const start = (page - 1) * perPage;
        const items = allProducts.slice(start, start + perPage);
        const totalPages = Math.ceil(allProducts.length / perPage);
        
        const grid = document.getElementById('products-grid');
        grid.innerHTML = items.map(p => {{
            const badges = [];
            if (p.inductie === 'Oui') badges.push('Inductie');
            if (p.capaciteit) badges.push(p.capaciteit + ' kops');
            if (p.materiaal) badges.push(p.materiaal);
            const badgeHTML = badges.map(b => `<span style="font-size:0.72rem;color:var(--text-light);border:1px solid var(--border);padding:0.2rem 0.5rem;border-radius:0.5rem;">${{b}}</span>`).join('');
            const price = p.price ? `€${{p.price.toFixed(2)}}` : '';
            const rating = p.rating ? `{{p.rating}}/5` : '';
            const ratingHTML = rating ? `<span style="font-size:0.78rem;color:var(--text-light);">${{rating}}</span>` : '';
            return `<div style="border:1px solid var(--border);overflow:hidden;background:white;transition:border-color 0.2s;border-radius:0.5rem;display:flex;flex-direction:column;height:100%;" onmouseover="this.style.borderColor='var(--coffee)'" onmouseout="this.style.borderColor='var(--border)'">
                <div style="background:#fafafa;padding:1rem;text-align:center;"><img src="${{p.image || '{prefix}Images/placeholder-product.jpg'}}" alt="${{p.name}}" loading="lazy" style="height:160px;width:100%;object-fit:contain;" onerror="this.src='{prefix}Images/placeholder-product.jpg'"></div>
                <div style="padding:1rem;">
                    <div style="display:flex;gap:0.35rem;flex-wrap:wrap;margin-bottom:0.5rem;">${{badgeHTML}}</div>
                    <h3 style="font-size:0.88rem;font-weight:600;line-height:1.35;margin-bottom:0.5rem;height:2.4rem;overflow:hidden;">${{p.name}}</h3>
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
                        <span style="font-size:1.1rem;font-weight:700;">${{price}}</span>
                        ${{ratingHTML}}
                    </div>
                    <a href="${{p.affiliate_url || '#'}}" target="_blank" rel="sponsored" style="display:block;text-align:center;padding:0.55rem;background:var(--coffee);color:white;text-decoration:none;border-radius:0.3rem;font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Bekijk op Bol.com</a>
                    <a href="{prefix}producten/${{p.slug}}.html" style="display:block;text-align:center;padding:0.45rem;border:1px solid var(--border);color:var(--text-dim);text-decoration:none;border-radius:0.3rem;font-size:0.78rem;">Details</a>
                </div>
            </div>`;
        }}).join('');
        
        document.getElementById('page-info').textContent = `Pagina ${{page}} van ${{totalPages}} · producten ${{start + 1}}-${{Math.min(start + perPage, allProducts.length)}} van ${{allProducts.length}}`;
        
        const pagination = document.getElementById('pagination');
        if (totalPages <= 1) {{ pagination.innerHTML = ''; return; }}
        
        let html = '';
        if (page > 1) {{
            html += `<a href="${{getPageUrl(page - 1)}}" class="pagination-link">Vorige</a>`;
        }}
        const startPage = Math.max(1, page - 2);
        const endPage = Math.min(totalPages, page + 2);
        for (let i = startPage; i <= endPage; i++) {{
            const active = i === page ? ' active' : '';
            html += `<a href="${{getPageUrl(i)}}" class="pagination-link${{active}}">${{i}}</a>`;
        }}
        if (page < totalPages) {{
            html += `<a href="${{getPageUrl(page + 1)}}" class="pagination-link">Volgende</a>`;
        }}
        pagination.innerHTML = html;
    }}
    
    document.addEventListener('DOMContentLoaded', () => {{
        currentPage = getPageFromUrl();
        renderPage(currentPage);
    }});
    </script>
</body>
</html>'''


def write_pages(kind, slug, products, title, h1, description):
    total = max(1, math.ceil(len(products) / PER_PAGE))
    urls = []
    for page in range(1, total + 1):
        path = local_path(kind, slug, page)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(kind, slug, products, page, total, title, h1, description), encoding='utf-8')
        urls.append(page_url(kind, slug, page))
    return urls


def main():
    products = json.loads((ROOT / 'all_products.json').read_text(encoding='utf-8'))
    products = sorted(products, key=lambda p: (p.get('type') or '', p.get('brand') or '', p.get('name') or ''))
    urls = []
    urls += write_pages('boutique', '', products, 'Alle modellen vergelijken', 'Alle modellen vergeleken', 'Bekijk Italiaanse percolators, elektrische koffiezetters en accessoires met eigen SEO-pagina per paginastap.')
    for slug, cfg in CATEGORY_CONFIG.items():
        items = [p for p in products if cfg['filter'](p)]
        urls += write_pages('category', slug, items, cfg['title'], cfg['h1'], cfg['description'])
    today = date.today().isoformat()
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f'  <url><loc>{SITE}/{u}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>')
    sitemap.append('</urlset>')
    (ROOT / 'sitemap-boutique.xml').write_text('\n'.join(sitemap) + '\n', encoding='utf-8')
    print('Generated URLs:', len(urls))
    print('Boutique pages:', math.ceil(len(products) / PER_PAGE))

if __name__ == '__main__':
    main()
