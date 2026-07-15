#!/usr/bin/env python3
"""
Inject a left-hand filter sidebar into all category pages that have product grids.
Handles two page types:
  A) Embedded allProducts JS array  (9 pages)
  B) Fetch-based allProducts       (elektrische-percolators.html)
"""
import re
from pathlib import Path

BASE = Path('/Users/marc/Desktop/italiaanse-percolator/categories')

# ── Pages ────────────────────────────────────────────────────────────────────
EMBEDDED_PAGES = [
    'percolators-rvs.html',
    'percolators-aluminium.html',
    'percolators-inductie.html',
    'percolators-1-2-kops.html',
    'percolators-3-kops.html',
    'percolators-6-kops.html',
    'percolators-9-kops.html',
    'inductie-adapters.html',
    'onderhoudssets.html',
]

# ── CSS ──────────────────────────────────────────────────────────────────────
FILTER_CSS = """\
        /* ── Filter sidebar ───────────────────────────────────────────────── */
        .cat-layout{display:grid;grid-template-columns:230px 1fr;gap:2rem;align-items:start;}
        .filter-sidebar{background:#fafafa;border:1px solid var(--border);border-radius:.5rem;padding:1rem;position:sticky;top:5rem;}
        .filter-section{border-bottom:1px solid var(--border);padding:.55rem 0;}
        .filter-section:last-of-type{border-bottom:none;}
        .filter-header{display:flex;justify-content:space-between;align-items:center;width:100%;background:none;border:none;cursor:pointer;font-weight:600;font-size:.84rem;color:var(--text);padding:.2rem 0;}
        .filter-body{padding-top:.35rem;}
        .filter-option{display:flex;align-items:center;gap:.45rem;padding:.26rem 0;cursor:pointer;font-size:.81rem;color:var(--text-dim);text-decoration:none;}
        .filter-option:hover{color:var(--text);}
        .filter-option.active{color:var(--coffee);font-weight:600;}
        .filter-radio{width:13px;height:13px;border:1.5px solid #ccc;border-radius:50%;flex-shrink:0;}
        .filter-option.active .filter-radio{border-color:var(--coffee);background:var(--coffee);}
        .filter-count{font-size:.71rem;color:var(--text-light);margin-left:auto;}
        .filter-more-btn{background:none;border:none;color:var(--coffee);font-size:.76rem;cursor:pointer;padding:.15rem 0;}
        .active-filter-tag{display:inline-flex;align-items:center;gap:.25rem;background:var(--coffee);color:white;font-size:.74rem;padding:.2rem .55rem;border-radius:2rem;text-decoration:none;margin:0 .25rem .35rem 0;}
        @media(max-width:840px){.cat-layout{grid-template-columns:1fr;}.filter-sidebar{position:static;}}
"""

# ── Filter JS module ─────────────────────────────────────────────────────────
FILTER_JS = r"""
    // ── Filter sidebar module ─────────────────────────────────────────────────
    var filteredProducts = typeof allProducts !== 'undefined' ? allProducts : [];

    var PRIJS_RANGES = [
        { key:'<25',    label:'Minder dan \u20ac25',  min:0,   max:25   },
        { key:'25-50',  label:'\u20ac25 \u2013 \u20ac50',   min:25,  max:50   },
        { key:'50-100', label:'\u20ac50 \u2013 \u20ac100',  min:50,  max:100  },
        { key:'>100',   label:'Meer dan \u20ac100',   min:100, max:99999 }
    ];

    function getActiveFilters() {
        var _p = new URLSearchParams(location.search);
        return {
            merk:      _p.get('merk')      || null,
            materiaal: _p.get('materiaal') || null,
            kops:      _p.get('kops')      ? parseInt(_p.get('kops')) : null,
            inductie:  _p.get('inductie')  || null,
            prijs:     _p.get('prijs')     || null
        };
    }

    function applyFilters(products, filters) {
        return products.filter(function(p) {
            if (filters.merk      && p.brand     !== filters.merk)      return false;
            if (filters.materiaal && p.materiaal !== filters.materiaal) return false;
            if (filters.kops      && p.capaciteit !== filters.kops)     return false;
            if (filters.inductie === 'ja' && p.inductie !== 'Oui')      return false;
            if (filters.prijs) {
                var _r = null;
                for (var i=0; i<PRIJS_RANGES.length; i++) { if (PRIJS_RANGES[i].key===filters.prijs){_r=PRIJS_RANGES[i];break;} }
                if (_r && (p.price < _r.min || p.price >= _r.max)) return false;
            }
            return true;
        });
    }

    function buildFilterUrl(key, val) {
        var _p = new URLSearchParams(location.search);
        _p.delete('page');
        if (!val || _p.get(key) === String(val)) { _p.delete(key); }
        else { _p.set(key, String(val)); }
        var qs = _p.toString();
        return location.pathname + (qs ? '?' + qs : '');
    }

    function _cntFilter(allProds, key, val, af) {
        var f = Object.assign({}, af, {[key]: key==='kops' ? (val ? parseInt(val) : null) : val});
        return applyFilters(allProds, f).length;
    }

    function buildFilterSidebar(allProds, af) {
        var sidebar = document.getElementById('filter-sidebar');
        if (!sidebar) return;

        var merken     = Array.from(new Set(allProds.map(function(p){return p.brand;}).filter(Boolean))).sort();
        var materialen = Array.from(new Set(allProds.map(function(p){return p.materiaal;}).filter(Boolean))).sort();
        var kopsen     = Array.from(new Set(allProds.map(function(p){return p.capaciteit;}).filter(Boolean))).sort(function(a,b){return a-b;});

        var html = '';

        // Prijs
        var prijsItems = PRIJS_RANGES.map(function(r){
            return {val:r.key, label:r.label, cnt:_cntFilter(allProds,'prijs',r.key,af)};
        }).filter(function(x){return x.cnt>0;});
        if (prijsItems.length > 1) html += _buildSec('Prijs','prijs',prijsItems,af.prijs);

        // Merk
        var merkItems = merken.map(function(m){
            return {val:m, label:m, cnt:_cntFilter(allProds,'merk',m,af)};
        }).filter(function(x){return x.cnt>0;}).sort(function(a,b){return b.cnt-a.cnt;});
        if (merkItems.length > 1) html += _buildSec('Merk','merk',merkItems,af.merk);

        // Materiaal
        var matItems = materialen.map(function(m){
            return {val:m, label:m, cnt:_cntFilter(allProds,'materiaal',m,af)};
        }).filter(function(x){return x.cnt>0;}).sort(function(a,b){return b.cnt-a.cnt;});
        if (matItems.length > 1) html += _buildSec('Materiaal','materiaal',matItems,af.materiaal);

        // Capaciteit
        var kopsItems = kopsen.map(function(k){
            return {val:String(k), label:k+' kops', cnt:_cntFilter(allProds,'kops',String(k),af)};
        }).filter(function(x){return x.cnt>0;});
        if (kopsItems.length > 1) html += _buildSec('Capaciteit','kops',kopsItems, af.kops ? String(af.kops) : null);

        // Inductie
        if (allProds.some(function(p){return p.inductie==='Oui';})) {
            var indCnt = _cntFilter(allProds,'inductie','ja',af);
            if (indCnt > 0) html += _buildSec('Inductie','inductie',[{val:'ja',label:'Inductiegeschikt',cnt:indCnt}],af.inductie);
        }

        // Reset
        if (Object.values(af).some(Boolean)) {
            html += '<div style="padding:.5rem 0 0"><a href="'+location.pathname+'" style="font-size:.77rem;color:var(--coffee);text-decoration:none;">\u00d7 Alle filters wissen</a></div>';
        }
        sidebar.innerHTML = html;
        _buildTagsBar(af);
    }

    function _buildSec(title, key, items, activeVal) {
        var MAX = 6;
        function mkOpt(item) {
            var isActive = String(activeVal) === String(item.val);
            var url = buildFilterUrl(key, isActive ? null : item.val);
            var safeUrl = url.replace(/'/g, "\\'");
            return '<a href="'+url+'" class="filter-option'+(isActive?' active':'')+'" onclick="return _fClick(event,\''+safeUrl+'\')">'+
                '<span class="filter-radio"></span><span>'+item.label+'</span>'+
                '<span class="filter-count">('+item.cnt+')</span></a>';
        }
        var opts = items.slice(0, MAX).map(mkOpt).join('');
        var extra = '';
        if (items.length > MAX) {
            var eid = 'fex-'+key;
            extra = '<div id="'+eid+'" style="display:none">'+items.slice(MAX).map(mkOpt).join('')+'</div>'+
                '<button class="filter-more-btn" onclick="_fMore(\''+eid+'\',this)">\u2228 Plus</button>';
        }
        return '<div class="filter-section">'+
            '<button class="filter-header" onclick="_fToggle(this)"><span>'+title+'</span><span>\u2227</span></button>'+
            '<div class="filter-body">'+opts+extra+'</div></div>';
    }

    function _buildTagsBar(af) {
        var bar = document.getElementById('active-filters-bar');
        if (!bar) return;
        var tags = [];
        var labels = {merk:af.merk, materiaal:af.materiaal,
            kops: af.kops ? af.kops+' kops' : null,
            inductie: af.inductie ? 'Inductie' : null,
            prijs: af.prijs};
        for (var k in labels) {
            var v = labels[k];
            if (!v && v!==0) continue;
            var url = buildFilterUrl(k, null);
            var safeUrl = url.replace(/'/g, "\\'");
            tags.push('<a href="'+url+'" class="active-filter-tag" onclick="return _fClick(event,\''+safeUrl+'\')">'+v+' \u00d7</a>');
        }
        bar.innerHTML = tags.length ? '<div style="display:flex;flex-wrap:wrap;margin-bottom:.75rem;">'+tags.join('')+'</div>' : '';
    }

    function _fClick(e, url) {
        e.preventDefault();
        history.pushState({}, '', url);
        var f = getActiveFilters();
        filteredProducts = applyFilters(allProducts, f);
        currentPage = 1;
        renderPage(currentPage);
        buildFilterSidebar(allProducts, f);
        var grid = document.getElementById('products-grid');
        if (grid) window.scrollTo({top: grid.getBoundingClientRect().top + window.scrollY - 100, behavior:'smooth'});
        return false;
    }

    function _fToggle(btn) {
        var body = btn.nextElementSibling;
        var open = body.style.display !== 'none';
        body.style.display = open ? 'none' : 'block';
        btn.lastElementChild.textContent = open ? '\u2228' : '\u2227';
    }

    function _fMore(id, btn) {
        var el = document.getElementById(id);
        var open = el.style.display !== 'none';
        el.style.display = open ? 'none' : 'block';
        btn.textContent = open ? '\u2228 Plus' : '\u2227 Minder';
    }

    window.addEventListener('popstate', function() {
        var f = getActiveFilters();
        filteredProducts = applyFilters(allProducts, f);
        currentPage = getPageFromUrl();
        renderPage(currentPage);
        buildFilterSidebar(allProducts, f);
    });
    // ── End filter sidebar module ─────────────────────────────────────────────
"""

# ── Helpers ──────────────────────────────────────────────────────────────────

NEW_MAIN = """\
    <main class="container" style="padding:2.5rem 0;">
        <div class="cat-layout">
            <aside id="filter-sidebar" class="filter-sidebar"></aside>
            <div>
                <div id="active-filters-bar"></div>
                <p id="page-info" style="color:var(--text-dim);margin-bottom:1rem;">Pagina laden...</p>
                <div id="products-grid" class="shop-product-grid"></div>
                <div id="pagination" style="margin-top:1.5rem;"></div>
            </div>
        </div>
    </main>"""


def patch_embedded(html: str, filename: str) -> str:
    """Patch a page with embedded allProducts array. Each step is idempotent."""

    # Step 1: CSS — inject only if not already present
    if '.cat-layout{' not in html:
        css_block = '<style>\n' + FILTER_CSS + '    </style>\n'
        html = html.replace('</head>', css_block + '</head>', 1)

    # Step 2: HTML <main> structure — replace only if cat-layout div not yet present
    if 'class="cat-layout"' not in html:
        html = re.sub(
            r'<main class="container"[^>]*>.*?</main>',
            NEW_MAIN,
            html, flags=re.DOTALL, count=1
        )

    # Step 3: Filter JS module — inject only if getActiveFilters not yet present
    if 'getActiveFilters' not in html:
        html = html.replace(
            'let currentPage = 1;',
            'let currentPage = 1;\n' + FILTER_JS,
            1
        )

    # Step 4: renderPage — patch only if still using allProducts.slice
    if 'allProducts.slice' in html:
        def patch_render_page(m):
            body = m.group(0)
            body = body.replace('allProducts.slice', 'filteredProducts.slice')
            body = body.replace('allProducts.length', 'filteredProducts.length')
            return body
        html = re.sub(
            r'function renderPage\(page\)\s*\{.*?\n\s*\}(?=\s*\n\s*document\.addEventListener)',
            patch_render_page,
            html, flags=re.DOTALL, count=1
        )

    # Step 5: getPageUrl — replace only if still using old baseUrl pattern
    if '_pq.delete' not in html:
        html = re.sub(
            r"function getPageUrl\(page\)\s*\{[^}]+\}",
            ("function getPageUrl(page) {\n"
             "        var _pq = new URLSearchParams(location.search);\n"
             "        _pq.delete('page');\n"
             "        if (page > 1) _pq.set('page', page);\n"
             "        var _qs = _pq.toString();\n"
             "        return location.pathname + (_qs ? '?' + _qs : '');\n"
             "    }"),
            html, count=1
        )

    # Step 6: DOMContentLoaded — replace only if not yet calling buildFilterSidebar
    if 'buildFilterSidebar(allProducts' not in html:
        html = re.sub(
            r"document\.addEventListener\('DOMContentLoaded',\s*\(\)\s*=>\s*\{[^}]+\}\s*\);",
            ("document.addEventListener('DOMContentLoaded', () => {\n"
             "        currentPage = getPageFromUrl();\n"
             "        var _af = getActiveFilters();\n"
             "        filteredProducts = applyFilters(allProducts, _af);\n"
             "        renderPage(currentPage);\n"
             "        buildFilterSidebar(allProducts, _af);\n"
             "    });"),
            html, count=1
        )

    return html


# ── Main ─────────────────────────────────────────────────────────────────────
for filename in EMBEDDED_PAGES:
    path = BASE / filename
    if not path.exists():
        print(f'  NOT FOUND: {filename}')
        continue
    html = path.read_text(encoding='utf-8')
    new_html = patch_embedded(html, filename)
    if new_html == html:
        print(f'  SKIP (already done or no change): {filename}')
        continue
    path.write_text(new_html, encoding='utf-8')
    print(f'  OK: {filename}')

# ── elektrische-percolators.html (fetch-based) ───────────────────────────────
elec_path = BASE / 'elektrische-percolators.html'
elec = elec_path.read_text(encoding='utf-8')

if 'filter-sidebar' not in elec:
    # 1. CSS
    elec = elec.replace('</head>', '<style>' + FILTER_CSS + '</style>\n</head>', 1)

    # 2. Replace <main>
    elec = re.sub(
        r'<main class="container"[^>]*>.*?</main>',
        NEW_MAIN.replace('Pagina laden...', 'Producten laden...'),
        elec, flags=re.DOTALL, count=1
    )

    # 3. Inject filter JS after the IIFE opens and allProducts + filtered are declared
    #    Insert after `let page = 1;`
    elec = elec.replace(
        'let page = 1;',
        'let page = 1;\n' + FILTER_JS.replace(
            "var filteredProducts = typeof allProducts !== 'undefined' ? allProducts : [];",
            "// filteredProducts is managed inside the IIFE"
        ),
        1
    )

    # 4. After `filtered = [...allProducts]; render();` add filter setup
    elec = elec.replace(
        'filtered = [...allProducts];\n            render();',
        'filtered = [...allProducts];\n'
        '            filteredProducts = filtered;\n'
        '            var _af0 = getActiveFilters();\n'
        '            filtered = applyFilters(allProducts, _af0);\n'
        '            filteredProducts = filtered;\n'
        '            render();\n'
        '            buildFilterSidebar(allProducts, _af0);',
        1
    )

    # 5. Update DOMContentLoaded equivalent - popstate for this page is handled by FILTER_JS
    elec_path.write_text(elec, encoding='utf-8')
    print(f'  OK: elektrische-percolators.html')
else:
    print(f'  SKIP (already done): elektrische-percolators.html')

print('\nDone.')
