"""Shared template for all generated blog articles."""
from pathlib import Path
import re

_ref = Path('koopgids/hoe-onderhoud-je-een-percolator.html').read_text(encoding='utf-8')
_nav_end = _ref.find('<div class="mobile-menu-overlay"></div>') + len('<div class="mobile-menu-overlay"></div>')
NAV = _ref[:_nav_end]
_f_start = _ref.find('<footer class="footer">')
FOOTER = _ref[_f_start:]

CSS = """<style>
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
.guide-progress{position:fixed;top:0;left:0;height:2px;background:var(--coffee);z-index:9999;width:0%;transition:width .1s linear;pointer-events:none;}
.guide-main-col.blog-article{padding:0;}
.guide-main-col section{margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid var(--border);}
.guide-main-col section:last-of-type{border-bottom:none;margin-bottom:0;}
.guide-main-col h2{font-family:var(--font-serif);font-size:clamp(1.2rem,2vw,1.5rem);font-weight:400;margin-bottom:.75rem;}
.guide-main-col h3{margin-top:1.1rem;margin-bottom:.35rem;font-size:.97rem;font-weight:600;}
.guide-main-col p{margin-bottom:.65rem;font-size:.92rem;line-height:1.75;color:var(--text);}
.guide-main-col ul,.guide-main-col ol{margin-bottom:.65rem;padding-left:1.5rem;}
.guide-main-col li{margin-bottom:.3rem;font-size:.92rem;line-height:1.65;}
.guide-main-col .blog-callout{border-left:3px solid var(--coffee);padding:.75rem 1.1rem;margin:1rem 0;background:#fdf9f6;}
.guide-main-col .blog-callout p{margin-bottom:.3rem;}
.guide-main-col .blog-faq details{border-bottom:1px solid var(--border);}
.guide-main-col .blog-faq summary{cursor:pointer;font-weight:600;padding:.75rem 0;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:.92rem;}
.guide-main-col .blog-faq summary::-webkit-details-marker{display:none;}
.guide-main-col .blog-faq summary::after{content:'+';color:var(--text-dim);font-size:1.1rem;font-weight:400;flex-shrink:0;}
.guide-main-col .blog-faq details[open] summary::after{content:'\2212';}
.guide-main-col .blog-faq details p{padding:0 0 .75rem;color:var(--text-dim);line-height:1.7;font-size:.88rem;}
.g-table-wrap{overflow-x:auto;margin:.75rem 0;}
.g-table{width:100%;border-collapse:collapse;font-size:.87rem;}
.g-table th{background:#f5f0ea;color:var(--text);padding:.6rem .9rem;text-align:left;font-weight:600;border-bottom:2px solid var(--border);}
.g-table td{padding:.55rem .9rem;border-bottom:1px solid var(--border);color:var(--text-dim);vertical-align:top;}
.g-table tr:last-child td{border-bottom:none;}
.g-table tr:hover td{background:#fafafa;}
@media(max-width:900px){
  .guide-layout{grid-template-columns:1fr;gap:0;}
  .guide-sidebar-col{order:-1;margin-bottom:1.5rem;}
  .guide-sidebar-sticky{position:static;}
  .guide-toc-list{display:flex;flex-wrap:wrap;gap:.3rem;}
  .guide-toc-list li{margin:0;}
  .guide-toc-list a{font-size:.74rem;background:#f0ebe5;padding:.2rem .55rem;border-radius:2rem;}
  .guide-toc-list a::before{display:none;}
  .guide-meta-sep{display:none;}
}
</style>"""

JS = """<script>
(function(){
  var bar=document.getElementById('guide-progress'),art=document.getElementById('guide-article');
  if(bar&&art)window.addEventListener('scroll',function(){var t=art.offsetTop+art.offsetHeight-window.innerHeight;bar.style.width=Math.min(100,Math.max(0,window.scrollY/t*100))+'%';},{passive:true});
  var ls=document.querySelectorAll('.guide-toc-list a');
  if(ls.length&&art){var ss=Array.from(ls).map(function(a){return document.getElementById(a.getAttribute('href').slice(1));}).filter(Boolean);window.addEventListener('scroll',function(){var c=ss[0];ss.forEach(function(s){if(window.scrollY>=s.offsetTop-130)c=s;});ls.forEach(function(a){a.classList.remove('toc-active');});var al=document.querySelector('.guide-toc-list a[href="#'+c.id+'"]');if(al)al.classList.add('toc-active');},{passive:true});}
})();
</script>"""

PICKS = """<div class="guide-sidebar-card">
<span class="guide-sidebar-label">Onze top keuzes</span>
<div class="guide-pick"><div class="guide-pick-lbl">Beste overall</div><div class="guide-pick-name">Bialetti Fiammetta</div><div class="guide-pick-detail">&euro;25&ndash;45 &middot; Aluminium &middot; 9.2/10</div><a href="../bialetti-fiammetta-review.html" class="guide-pick-link">Bekijk &rarr;</a></div>
<div class="guide-pick"><div class="guide-pick-lbl">Beste voor inductie</div><div class="guide-pick-name">Bialetti Venus</div><div class="guide-pick-detail">&euro;40&ndash;65 &middot; RVS &middot; 8.8/10</div><a href="../bialetti-venus-review.html" class="guide-pick-link">Bekijk &rarr;</a></div>
<div class="guide-pick"><div class="guide-pick-lbl">Beste design</div><div class="guide-pick-name">Alessi Pulcina</div><div class="guide-pick-detail">&euro;80&ndash;120 &middot; Aluminium &middot; 8.5/10</div><a href="../alessi-pulcina-review.html" class="guide-pick-link">Bekijk &rarr;</a></div>
</div>
<div class="guide-sidebar-card" style="background:var(--coffee);border-color:var(--coffee);">
<p style="font-size:.82rem;color:white;margin:0 0 .7rem;line-height:1.5;">Alle percolators vergeleken op prijs, materiaal en score.</p>
<a href="../beste-italiaanse-percolators.html" style="display:block;text-align:center;background:white;color:var(--coffee);border-radius:.4rem;padding:.45rem;font-size:.82rem;font-weight:700;text-decoration:none;">Bekijk top 10 &rarr;</a>
</div>"""


def build_page(filename, title, meta_desc, badge, leestijd, update, intro, toc, body):
    toc_items = '\n'.join(f'<li><a href="#{i}">{l}</a></li>' for i, l in toc)
    sidebar_toc = f'<div class="guide-sidebar-card"><span class="guide-sidebar-label">Inhoudsopgave</span><nav><ol class="guide-toc-list">{toc_items}</ol></nav></div>'
    short = re.sub(r'<[^>]+>', '', title)[:52]
    page = f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{meta_desc}"/>
<link rel="stylesheet" href="../style.css"/>
<link rel="canonical" href="https://italiaanse-percolator.nl/koopgids/{filename}"/>
<link rel="icon" href="../favicon.svg" type="image/svg+xml"/>
{CSS}
</head>
<body class="blog-page">
{NAV}
<header class="blog-hero">
<div class="blog-container">
<nav class="guide-breadcrumb"><a href="../index.html">Home</a><span>/</span><a href="../koopgids/index.html">Koopgids</a><span>/</span><span>{short}</span></nav>
<span class="guide-badge">{badge}</span>
<h1>{title}</h1>
<div class="guide-meta-row">
<div class="guide-author-avatar">L</div>
<div><div class="guide-author-name">Lisa De Boer</div><div class="guide-author-role">Koffiejournalist</div></div>
<span class="guide-meta-sep"></span>
<span class="guide-meta-item"><strong>{leestijd} min</strong> leestijd</span>
<span class="guide-meta-sep"></span>
<span class="guide-meta-item">Update: {update}</span>
</div>
<p class="blog-intro-text">{intro}</p>
</div>
</header>
<div class="guide-progress" id="guide-progress"></div>
<main>
<div class="blog-container guide-layout-wrap">
<div class="guide-layout">
<article class="blog-article guide-main-col" id="guide-article">
{body}
</article>
<aside class="guide-sidebar-col">
<div class="guide-sidebar-sticky">
{sidebar_toc}
{PICKS}
</div>
</aside>
</div>
</div>
</main>
{FOOTER}
{JS}
</body>
</html>"""
    out = Path(f'koopgids/{filename}')
    out.write_text(page, encoding='utf-8')
    print(f'OK: {filename}')
