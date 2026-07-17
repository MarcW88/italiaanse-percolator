from pathlib import Path

f = Path('koopgids/hoe-kies-je-de-juiste-percolator.html')
html = f.read_text(encoding='utf-8')

old = (
    '<div class="blog-container" style="padding-top:var(--sp-4);padding-bottom:var(--sp-2);">\n'
    '<div class="breadcrumbs">\n'
    '<a href="../index.html">Home</a><span>\u203a</span>\n'
    '<a href="../koopgids/index.html">Koopgids</a><span>\u203a</span>\n'
    '<span>Hoe kies je de juiste percolator?</span>\n'
    '</div>\n'
    '</div>\n'
    '<header class="blog-hero">\n'
    '<div class="blog-container">\n'
    '<p class="blog-meta">Leestijd: 12 minuten \xa0\u00b7\xa0 Laatste update: november 2025 \xa0\u00b7\xa0 Gebaseerd op 50+ onafhankelijke tests</p>\n'
    '<h1>Hoe kies je de juiste percolator?</h1>\n'
    '<p class="blog-intro-text">Een Italiaanse percolator kiezen lijkt eenvoudig, maar de keuze bepaalt dagelijks de kwaliteit van je koffie. Na het intensief testen van meer dan 50 percolators over 8 jaar weten wij precies welke factoren het verschil maken \u2014 van materiaal en grootte tot kookplaat compatibiliteit en budget.</p>\n'
    '\n'
    '</div>\n'
    '</header>'
)

new = (
    '<header class="blog-hero">\n'
    '<div class="blog-container">\n'
    '<nav class="guide-breadcrumb" aria-label="Breadcrumb">'
    '<a href="../index.html">Home</a><span>/</span>'
    '<a href="../koopgids/index.html">Koopgids</a><span>/</span>'
    '<span>Hoe kies je de juiste percolator?</span>'
    '</nav>\n'
    '<span class="guide-badge">Koopgids</span>\n'
    '<h1>Hoe kies je de juiste percolator?</h1>\n'
    '<div class="guide-meta-row">\n'
    '<div class="guide-author-avatar" aria-hidden="true">L</div>\n'
    '<div><div class="guide-author-name">Lisa De Boer</div>'
    '<div class="guide-author-role">Koffiejournalist</div></div>\n'
    '<span class="guide-meta-sep"></span>\n'
    '<span class="guide-meta-item"><strong>12 min</strong> leestijd</span>\n'
    '<span class="guide-meta-sep"></span>\n'
    '<span class="guide-meta-item">Update: nov. 2025</span>\n'
    '<span class="guide-meta-sep"></span>\n'
    '<span class="guide-meta-item">50+ tests</span>\n'
    '</div>\n'
    '<p class="blog-intro-text">Een Italiaanse percolator kiezen lijkt eenvoudig, maar de keuze bepaalt dagelijks de kwaliteit van je koffie. Na het intensief testen van meer dan 50 percolators over 8 jaar weten wij precies welke factoren het verschil maken \u2014 van materiaal en grootte tot kookplaat compatibiliteit en budget.</p>\n'
    '</div>\n'
    '</header>'
)

if old in html:
    html = html.replace(old, new, 1)
    f.write_text(html, encoding='utf-8')
    print('OK: hero section replaced')
else:
    print('NOT FOUND')
    idx = html.find('<div class="breadcrumbs">')
    print(repr(html[max(0,idx-50):idx+300]))
