"""
Apply the 2-column guide layout (hero + sidebar) to all blog articles in koopgids/.
Skips files that already have the layout applied.
"""
import re
from pathlib import Path

# ── CSS block (same as hoe-kies-je-de-juiste-percolator.html) ────────────────
CSS = """<style>
/* ── Guide 2-column layout ─────────────────────────────────────────── */
.guide-badge{display:inline-block;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--coffee);background:#fdf3ee;border:1px solid #f0d6c8;border-radius:2rem;padding:.18rem .65rem;margin-bottom:.85rem;}
.guide-breadcrumb{font-size:.77rem;color:var(--text-light);margin-bottom:.85rem;}
.guide-breadcrumb a{color:var(--text-light);text-decoration:none;}
.guide-breadcrumb a:hover{color:var(--coffee);}
.guide-breadcrumb span{margin:0 .3rem;}
.guide-meta-row{display:flex;align-items:center;gap:.9rem;flex-wrap:wrap;margin:.9rem 0 1.4rem;}
.guide-author-avatar{width:34px;height:34px;border-radius:50%;background:#b85c38;color:white;font-size:.82rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.guide-author-name{font-size:.82rem;font-weight:600;color:var(--text);line-height:1.2;}
.guide-author-role{font-size:.72rem;color:var(--text-light);}
.guide-meta-sep{width:1px;height:22px;background:var(--border);flex-shrink:0;}
.guide-meta-item{font-size:.77rem;color:var(--text-dim);}
.guide-meta-item strong{color:var(--text);font-weight:600;}
.guide-layout-wrap{max-width:1060px!important;}
.guide-layout{display:grid;grid-template-columns:1fr 278px;gap:3rem;align-items:start;padding:var(--sp-10) 0 var(--sp-16);}
.guide-main-col{min-width:0;}
.guide-sidebar-col{min-width:0;}
.guide-sidebar-sticky{position:sticky;top:5.5rem;}
.guide-sidebar-card{background:#fafafa;border:1px solid var(--border);border-radius:.65rem;padding:1.1rem 1.25rem;margin-bottom:1.1rem;}
.guide-sidebar-label{font-size:.64rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--text-light);margin:0 0 .7rem;display:block;}
.guide-toc-list{list-style:none;padding:0;margin:0;counter-reset:toc-c;}
.guide-toc-list li{counter-increment:toc-c;margin-bottom:.22rem;}
.guide-toc-list a{display:flex;align-items:baseline;gap:.4rem;font-size:.79rem;color:var(--text-dim);text-decoration:none;line-height:1.4;padding:.12rem 0;}
.guide-toc-list a::before{content:counter(toc-c);font-size:.63rem;font-weight:700;color:#ccc;min-width:.85rem;flex-shrink:0;}
.guide-toc-list a:hover,.guide-toc-list a.toc-active{color:var(--coffee);}
.guide-toc-list a.toc-active::before{color:var(--coffee);}
.guide-pick{padding:.5rem 0;border-bottom:1px solid var(--border);}
.guide-pick:last-child{border-bottom:none;padding-bottom:0;}
.guide-pick-lbl{font-size:.63rem;text-transform:uppercase;letter-spacing:.06em;color:var(--text-light);margin-bottom:.1rem;}
.guide-pick-name{font-size:.82rem;font-weight:600;color:var(--text);}
.guide-pick-detail{font-size:.77rem;color:var(--text-dim);}
.guide-pick-link{font-size:.77rem;color:var(--coffee);text-decoration:none;font-weight:600;}
.guide-pick-link:hover{text-decoration:underline;}
.guide-progress{position:fixed;top:0;left:0;height:2px;background:var(--coffee);z-index:9999;width:0%;transition:width .1s linear;pointer-events:none;}
/* Spacing overrides */
.guide-main-col.blog-article{padding:0;}
.guide-main-col .blog-article section,.guide-main-col section{margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid var(--border);}
.guide-main-col section:last-of-type{border-bottom:none;margin-bottom:0;}
.guide-main-col .blog-article h2,.guide-main-col h2{font-family:var(--font-serif);font-size:clamp(1.2rem,2vw,1.5rem);font-weight:400;border-bottom:none;padding-bottom:0;margin-bottom:.75rem;}
.guide-main-col .blog-article h3,.guide-main-col h3{margin-top:1.1rem;margin-bottom:.35rem;font-size:.97rem;}
.guide-main-col .blog-article h4,.guide-main-col h4{margin-top:.85rem;margin-bottom:.25rem;}
.guide-main-col .blog-article p,.guide-main-col p{margin-bottom:.65rem;font-size:.92rem;line-height:1.7;}
.guide-main-col .blog-article ul,.guide-main-col .blog-article ol{margin-bottom:.65rem;}
.guide-main-col .blog-article li{margin-bottom:.2rem;font-size:.92rem;}
.guide-main-col .blog-compare{gap:1.25rem;margin:1rem 0;}
.guide-main-col .blog-callout{margin:1rem 0;}
.guide-main-col .blog-scenarios{gap:1rem;margin:1rem 0;}
.guide-main-col table th,.guide-main-col .blog-article th{background:#f5f0ea;color:var(--text);border-bottom:2px solid var(--border);}
.guide-main-col table td,.guide-main-col .blog-article td{font-size:.87rem;}
.guide-main-col table,.guide-main-col .blog-article table{margin:.75rem 0;}
@media(max-width:900px){
  .guide-layout-wrap{max-width:740px!important;}
  .guide-layout{grid-template-columns:1fr;gap:0;}
  .guide-sidebar-col{order:-1;margin-bottom:1.5rem;}
  .guide-sidebar-sticky{position:static;}
  .guide-toc-list{display:flex;flex-wrap:wrap;gap:.3rem;}
  .guide-toc-list li{margin:0;}
  .guide-toc-list a{font-size:.74rem;background:#f0ebe5;padding:.2rem .55rem;border-radius:2rem;}
  .guide-toc-list a::before{display:none;}
  .guide-meta-sep{display:none;}
}
</style>
"""

# ── JS block ──────────────────────────────────────────────────────────────────
JS = """<script>
(function(){
  var bar = document.getElementById('guide-progress');
  var article = document.getElementById('guide-article');
  if (bar && article) {
    window.addEventListener('scroll', function() {
      var total = article.offsetTop + article.offsetHeight - window.innerHeight;
      bar.style.width = Math.min(100, Math.max(0, window.scrollY / total * 100)) + '%';
    }, {passive: true});
  }
  var tocLinks = document.querySelectorAll('.guide-toc-list a');
  if (tocLinks.length && article) {
    var sections = Array.from(tocLinks).map(function(a){ return document.getElementById(a.getAttribute('href').slice(1)); }).filter(Boolean);
    window.addEventListener('scroll', function() {
      var current = sections[0];
      sections.forEach(function(s){ if (window.scrollY >= s.offsetTop - 130) current = s; });
      tocLinks.forEach(function(a){ a.classList.remove('toc-active'); });
      var activeLink = document.querySelector('.guide-toc-list a[href="#' + current.id + '"]');
      if (activeLink) activeLink.classList.add('toc-active');
    }, {passive: true});
  }
})();
</script>
"""

# ── Sidebar picks (same for all articles) ────────────────────────────────────
SIDEBAR_PICKS = """<div class="guide-sidebar-card">
<span class="guide-sidebar-label">Onze top keuzes</span>
<div class="guide-pick">
<div class="guide-pick-lbl">Beste overall</div>
<div class="guide-pick-name">Bialetti Fiammetta</div>
<div class="guide-pick-detail">&euro;25&ndash;45 &middot; Aluminium &middot; 9.2/10</div>
<a href="../bialetti-fiammetta-review.html" class="guide-pick-link">Bekijk review &rarr;</a>
</div>
<div class="guide-pick">
<div class="guide-pick-lbl">Beste voor inductie</div>
<div class="guide-pick-name">Bialetti Venus</div>
<div class="guide-pick-detail">&euro;40&ndash;65 &middot; RVS &middot; 8.8/10</div>
<a href="../bialetti-venus-review.html" class="guide-pick-link">Bekijk review &rarr;</a>
</div>
<div class="guide-pick">
<div class="guide-pick-lbl">Beste design</div>
<div class="guide-pick-name">Alessi Pulcina</div>
<div class="guide-pick-detail">&euro;80&ndash;120 &middot; Aluminium &middot; 8.5/10</div>
<a href="../alessi-pulcina-review.html" class="guide-pick-link">Bekijk review &rarr;</a>
</div>
</div>
<div class="guide-sidebar-card" style="background:var(--coffee);border-color:var(--coffee);">
<span class="guide-sidebar-label" style="color:rgba(255,255,255,0.6);">Vergelijk alle modellen</span>
<p style="font-size:.82rem;color:white;margin:0 0 .8rem;line-height:1.55;">Bekijk onze complete vergelijking van alle percolators op prijs, materiaal en score.</p>
<a href="../beste-italiaanse-percolators.html" style="display:block;text-align:center;background:white;color:var(--coffee);border-radius:.4rem;padding:.5rem;font-size:.82rem;font-weight:700;text-decoration:none;">Bekijk top 10 &rarr;</a>
</div>"""


def parse_meta(meta_text):
    """Parse 'Category · Leestijd: X minuten · Bijgewerkt: month year' """
    parts = [p.strip() for p in meta_text.split('·')]
    badge = parts[0] if parts else 'Koopgids'
    leestijd = ''
    bijgewerkt = ''
    for p in parts[1:]:
        if 'Leestijd' in p or 'minuten' in p:
            m = re.search(r'(\d+)\s*minuten?', p)
            leestijd = m.group(1) + ' min' if m else p.strip()
        elif 'Bijgewerkt' in p or re.search(r'\d{4}', p):
            bijgewerkt = re.sub(r'Bijgewerkt\s*:\s*', '', p).strip()
    return badge.strip(), leestijd, bijgewerkt


def strip_html(s):
    return re.sub(r'<[^>]+>', '', s).strip()


def build_new_hero(badge, h1_text, leestijd, bijgewerkt, intro_html):
    meta_items = []
    if leestijd:
        meta_items.append(f'<span class="guide-meta-item"><strong>{leestijd}</strong> leestijd</span>')
    if bijgewerkt:
        meta_items.append(f'<span class="guide-meta-item">Update: {bijgewerkt}</span>')

    meta_sep = '<span class="guide-meta-sep"></span>'
    meta_row = meta_sep.join(meta_items)

    h1_short = strip_html(h1_text)[:55]

    return (
        '<header class="blog-hero">\n'
        '<div class="blog-container">\n'
        '<nav class="guide-breadcrumb" aria-label="Breadcrumb">'
        '<a href="../index.html">Home</a><span>/</span>'
        '<a href="../koopgids/index.html">Koopgids</a><span>/</span>'
        f'<span>{h1_short}</span>'
        '</nav>\n'
        f'<span class="guide-badge">{badge}</span>\n'
        f'<h1>{h1_text}</h1>\n'
        '<div class="guide-meta-row">\n'
        '<div class="guide-author-avatar" aria-hidden="true">L</div>\n'
        '<div><div class="guide-author-name">Lisa De Boer</div>'
        '<div class="guide-author-role">Koffiejournalist</div></div>\n'
        f'<span class="guide-meta-sep"></span>\n{meta_row}\n'
        '</div>\n'
        + (f'<p class="blog-intro-text">{intro_html}</p>\n' if intro_html else '')
        + '</div>\n</header>'
    )


def build_sidebar_toc(toc_items):
    items_html = '\n'.join(
        f'<li><a href="{href}">{label}</a></li>'
        for href, label in toc_items
    )
    return (
        '<div class="guide-sidebar-card">\n'
        '<span class="guide-sidebar-label">Inhoudsopgave</span>\n'
        '<nav aria-label="Inhoudsopgave">\n'
        '<ol class="guide-toc-list">\n'
        f'{items_html}\n'
        '</ol>\n'
        '</nav>\n'
        '</div>'
    )


def transform(html, filename):
    """Apply 2-column guide layout to a blog article HTML file."""

    # Already transformed?
    if 'guide-layout' in html:
        print(f'  SKIP (already transformed): {filename}')
        return html

    # ── 1. Add CSS ────────────────────────────────────────────────────────────
    html = html.replace('</head>', CSS + '</head>', 1)

    # ── 2. Parse hero metadata ────────────────────────────────────────────────
    meta_m = re.search(r'<p class="blog-meta">(.*?)</p>', html, re.S)
    meta_text = strip_html(meta_m.group(1)) if meta_m else ''
    badge, leestijd, bijgewerkt = parse_meta(meta_text)

    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S)
    h1_text = h1_m.group(1).strip() if h1_m else ''

    intro_m = re.search(r'<p class="blog-intro-text">(.*?)</p>', html, re.S)
    intro_html = intro_m.group(1).strip() if intro_m else ''

    # ── 3. Parse existing ToC links ───────────────────────────────────────────
    toc_nav_m = re.search(r'<nav class="blog-toc">.*?</nav>', html, re.S)
    toc_items = []
    if toc_nav_m:
        toc_items = re.findall(r'<li><a href="(#[^"]+)">(.*?)</a></li>', toc_nav_m.group(0))

    # ── 4. Replace old hero section ───────────────────────────────────────────
    # Remove breadcrumb div if present (some files have it before the hero)
    html = re.sub(
        r'<div class="blog-container" style="padding-top[^"]*"[^>]*>.*?</div>\s*(?=<header)',
        '', html, count=1, flags=re.S
    )

    # Replace old hero
    old_hero_m = re.search(
        r'<header class="blog-hero">.*?</header>',
        html, re.S
    )
    if old_hero_m:
        new_hero = build_new_hero(badge, h1_text, leestijd, bijgewerkt, intro_html)
        html = html[:old_hero_m.start()] + new_hero + html[old_hero_m.end():]

    # ── 5. Replace <main> opening + blog-toc nav ──────────────────────────────
    html = re.sub(
        r'<main>\s*<div class="blog-container">\s*<article class="blog-article">\s*<nav class="blog-toc">.*?</nav>',
        (
            '<div class="guide-progress" id="guide-progress"></div>\n'
            '<main>\n'
            '<div class="blog-container guide-layout-wrap">\n'
            '<div class="guide-layout">\n'
            '<article class="blog-article guide-main-col" id="guide-article">'
        ),
        html, count=1, flags=re.S
    )

    # ── 6. Replace </article></div></main> with sidebar + closing ─────────────
    toc_sidebar = build_sidebar_toc(toc_items) if toc_items else ''

    sidebar_html = (
        '\n\n<aside class="guide-sidebar-col">\n'
        '<div class="guide-sidebar-sticky">\n\n'
        + toc_sidebar + '\n\n'
        + SIDEBAR_PICKS + '\n\n'
        '</div>\n'
        '</aside>\n\n'
        '</div>\n'
        '</div>\n'
        '</main>'
    )

    html = re.sub(
        r'</article>\s*</div>\s*</main>',
        '</article>' + sidebar_html,
        html, count=1, flags=re.S
    )

    # ── 7. Add JS before </body> ──────────────────────────────────────────────
    if 'guide-progress' in html and 'toc-active' not in html:
        html = html.replace('</body>', JS + '</body>', 1)

    return html


# ── Run ───────────────────────────────────────────────────────────────────────
TARGET_FILES = [
    'koopgids/beste-koffiebonen-italiaanse-percolator.html',
    'koopgids/hoe-onderhoud-je-een-percolator.html',
    'koopgids/italiaanse-percolator-gebruiken-handleiding.html',
    'koopgids/percolator-vs-espressoapparaat.html',
    'koopgids/wat-is-italiaanse-percolator-mokapot.html',
]

for path_str in TARGET_FILES:
    path = Path(path_str)
    html = path.read_text(encoding='utf-8')
    new_html = transform(html, path.name)
    if new_html != html:
        path.write_text(new_html, encoding='utf-8')
        print(f'OK: {path.name}')
    else:
        print(f'UNCHANGED: {path.name}')
