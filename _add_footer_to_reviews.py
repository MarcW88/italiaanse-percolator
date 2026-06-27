#!/usr/bin/env python3
import os
import glob

# Le nouveau footer HTML
NEW_FOOTER = '''<footer>
<div style="background:var(--coffee);padding:2.5rem 0;">
<div class="container">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;">
<div>
<p style="font-family:var(--font-serif);font-size:1.4rem;color:white;margin-bottom:0.5rem;">Heb je een vraag?</p>
<p style="color:rgba(255,255,255,0.85);font-size:0.9rem;line-height:1.6;margin:0;">Vind snel het antwoord op onze <a href="../../contact.html" style="color:white;text-decoration:underline;">FAQ</a> of neem rechtstreeks <a href="../../contact.html" style="color:white;text-decoration:underline;">contact</a> op.</p>
</div>
<div>
<p style="font-family:var(--font-serif);font-size:1.4rem;color:white;margin-bottom:0.5rem;">Schrijf je in voor onze nieuwsbrief</p>
<p style="color:rgba(255,255,255,0.85);font-size:0.9rem;margin-bottom:1rem;">Ontvang koffietips, vergelijkingen en de beste aanbevelingen in je inbox.</p>
<form onsubmit="return false;" style="display:flex;gap:0.5rem;flex-wrap:wrap;">
<input type="email" placeholder="Jouw e-mailadres" style="flex:1;min-width:200px;padding:0.6rem 1rem;border:none;border-radius:0.3rem;font-size:0.9rem;outline:none;">
<button type="submit" style="padding:0.6rem 1.4rem;background:#2a1a10;color:white;border:none;border-radius:0.3rem;font-size:0.9rem;font-weight:600;cursor:pointer;white-space:nowrap;">Inschrijven</button>
</form>
</div>
</div>
</div>
</div>
<div style="background:#2a1a10;padding:3rem 0 2rem;">
<div class="container">
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2.5rem;margin-bottom:2.5rem;">
<div>
<h4 style="color:white;font-size:0.8rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:1.2rem;padding-bottom:0.6rem;border-bottom:1px solid #3d2a1f;">Klantenservice</h4>
<ul style="list-style:none;padding:0;margin:0;">
<li style="margin-bottom:0.6rem;"><a href="../../contact.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Contact</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../over-ons.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Over ons</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../privacy.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Privacybeleid</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../disclaimer.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Disclaimer</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../cookies.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Cookiebeleid</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../sitemap.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Sitemap</a></li>
</ul>
</div>
<div>
<h4 style="color:white;font-size:0.8rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:1.2rem;padding-bottom:0.6rem;border-bottom:1px solid #3d2a1f;">Koffiegidsen</h4>
<ul style="list-style:none;padding:0;margin:0;">
<li style="margin-bottom:0.6rem;"><a href="../../beste-italiaanse-percolators.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Top 10 percolators</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../koopgids/index.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Koopgids</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../koopgids/hoe-kies-je-de-juiste-percolator.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Keuzehulp</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../alle-reviews.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Alle reviews</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../vergelijking/index.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Vergelijkingen</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../italiaanse-percolator-kopen.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Percolator kopen</a></li>
</ul>
</div>
<div>
<h4 style="color:white;font-size:0.8rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:1.2rem;padding-bottom:0.6rem;border-bottom:1px solid #3d2a1f;">Shop per categorie</h4>
<ul style="list-style:none;padding:0;margin:0;">
<li style="margin-bottom:0.6rem;"><a href="../../shop.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Alle modellen</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../categories/percolators.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Italiaanse percolators</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../categories/elektrische-percolators.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Elektrische percolators</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../categories/percolators-inductie.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Inductie percolators</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../categories/percolators-aluminium.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Aluminium percolators</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../categories/percolators-rvs.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">RVS percolators</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../shop/accessoires-italiaanse-percolator.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Percolator accessoires</a></li>
</ul>
</div>
<div>
<h4 style="color:white;font-size:0.8rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:1.2rem;padding-bottom:0.6rem;border-bottom:1px solid #3d2a1f;">Populaire merken</h4>
<ul style="list-style:none;padding:0;margin:0;">
<li style="margin-bottom:0.6rem;"><a href="../../marques/bialetti/" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Bialetti</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../marques/delonghi/" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">DeLonghi</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../marques/beem/" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Beem</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../marques/alessi/" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Alessi</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../shop/percolators/bialetti.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Bialetti shop</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../shop/percolators/bo-camp.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Bo Camp</a></li>
<li style="margin-bottom:0.6rem;"><a href="../../marques/index.html" style="color:#bbb;font-size:0.85rem;text-decoration:none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#bbb'">Alle merken →</a></li>
</ul>
</div>
</div>
<div style="border-top:1px solid #3d2a1f;padding-top:1.5rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
<div style="display:flex;align-items:center;gap:1rem;">
<span style="font-family:var(--font-serif);font-size:1rem;color:white;">Italiaanse Percolator</span>
<span style="color:#555;font-size:0.75rem;">|</span>
<span style="color:#666;font-size:0.78rem;">Onafhankelijke gids voor moka-percolators sinds 2017</span>
</div>
<div style="display:flex;gap:1.5rem;flex-wrap:wrap;">
<a href="../../privacy.html" style="color:#666;font-size:0.78rem;text-decoration:none;" onmouseover="this.style.color='#bbb'" onmouseout="this.style.color='#666'">Privacy</a>
<a href="../../disclaimer.html" style="color:#666;font-size:0.78rem;text-decoration:none;" onmouseover="this.style.color='#bbb'" onmouseout="this.style.color='#666'">Disclaimer</a>
<a href="../../cookies.html" style="color:#666;font-size:0.78rem;text-decoration:none;" onmouseover="this.style.color='#bbb'" onmouseout="this.style.color='#666'">Cookies</a>
<span style="color:#666;font-size:0.78rem;">© 2025 Italiaanse Percolator</span>
</div>
</div>
<p style="color:#555;font-size:0.75rem;margin:0.75rem 0 0;text-align:center;">Deze site bevat partnerlinks. Bij aankoop via onze links ontvangen wij een kleine commissie, zonder extra kosten voor jou.</p>
</div>
</div>
</footer>'''

# Trouver tous les fichiers de review
review_files = glob.glob('*-review.html')

for file_path in review_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si le footer existe déjà
    if '<footer>' in content:
        print(f"Skipping {file_path} - footer already exists")
        continue
    
    # Trouver l'endroit où insérer le footer (avant le script)
    # On cherche le tag <script> qui est généralement à la fin
    script_index = content.find('<script>')
    
    if script_index != -1:
        # Insérer le footer avant le script
        new_content = content[:script_index] + NEW_FOOTER + '\n\n' + content[script_index:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added footer to {file_path}")
    else:
        print(f"Could not find <script> tag in {file_path}")

print("Done!")
