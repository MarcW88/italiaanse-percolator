#!/usr/bin/env python3
"""
Rewrite bialetti-moka-review.html with editorial style.
"""

import re

filepath = '/Users/marc/Desktop/italiaanse-percolator/bialetti-moka-review.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix malformed CSS
content = re.sub(r'border:\s*1px solid var\(--border\);\s*\.5rem;', 'border: 1px solid var(--border); border-radius: 0.5rem;', content)
content = re.sub(r'font-size:\s*0\.75rem;\s*padding:\s*0\.2rem\s*0\.6rem;\s*\.2rem;', '', content)
content = re.sub(r'\.2rem;', '', content)

# Remove emojis from score bars
content = re.sub(r'&#x2615;', '', content)  # coffee cup
content = re.sub(r'&#x1F3A8;', '', content)  # art
content = re.sub(r'&#x1F4B0;', '', content)  # money bag
content = re.sub(r'&#x23F1;', '', content)  # watch
content = re.sub(r'&#x1F9FD;', '', content)  # maintenance
content = re.sub(r'&#x1F370;', '', content)  # food
content = re.sub(r'&#x2714;', '', content)  # checkmark
content = re.sub(r'&#x2715;', '', content)  # cross
content = re.sub(r'&#x271C;', '', content)  # checkmark variant
content = re.sub(r'&#x274C;', '', content)  # cross variant
content = re.sub(r'&#x2605;', '', content)  # star
content = re.sub(r'&#x2606;', '', content)  # empty star
content = re.sub(r'&#x1F6CD;', '', content)  # shopping bags

# Hero section - score card
hero_old = '''  <section class="section-sm">
    <div class="container">
      <div class="grid" style="grid-template-columns:1fr 380px;gap:var(--sp-8);align-items:start;">
        <div>
          <h1 class="display-title mb-4">Bialetti Moka Express Review 2025: De Klassieke Referentie</h1>
          <p class="lead mb-6">Sinds 1933 is de Moka Express het symbool van de Italiaanse koffiecultuur. Iconisch achthoekig design, aluminiumconstructie en authentieke moka-smaak. We testen dit model uitgebreid en vergelijken het met moderne alternatieven.</p>
          <div class="card mb-6" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
            
              <div class="flex items-center gap-4 mb-4">
                <div class="rating-badge" style="font-size:var(--fs-xl);">9.0/10
                <div>
                  <h3 style="margin-bottom:var(--sp-2);">Tijdloze klassieker</h3>
                  <p class="text-dim">Het origineel sinds 1933</p>
                </div>
              </div>
              <div class="grid grid-2 gap-4 mb-4">
                <div>
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                    <span style="font-size:14px;">&#x2615; Koffiesmaak</span>
                    <div style="display:flex;align-items:center;gap:8px;">
                      <div style="width:80px;height:6px;background:#e5e7eb;"><div style="width:93%;height:100%;background:var(--coffee);"></div></div>
                      <span style="font-size:14px;font-weight:600;">9.3/10</span>
                    </div>
                  </div>
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                    <span style="font-size:14px;">&#x1F3A8; Design &amp; Kwaliteit</span>
                    <div style="display:flex;align-items:center;gap:8px;">
                      <div style="width:80px;height:6px;background:#e5e7eb;"><div style="width:95%;height:100%;background:var(--coffee);"></div></div>
                      <span style="font-size:14px;font-weight:600;">9.5/10</span>
                    </div>
                  </div>
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                    <span style="font-size:14px;">&#x1F4B0; Prijs/Waarde</span>
                    <div style="display:flex;align-items:center;gap:8px;">
                      <div style="width:80px;height:6px;background:#e5e7eb;"><div style="width:95%;height:100%;background:var(--coffee);"></div></div>
                      <span style="font-size:14px;font-weight:600;">9.5/10</span>
                    </div>
                  </div></div>
                <div>
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                    <span style="font-size:14px;">&#x23F1; Gebruiksgemak</span>
                    <div style="display:flex;align-items:center;gap:8px;">
                      <div style="width:80px;height:6px;background:#e5e7eb;"><div style="width:85%;height:100%;background:var(--coffee);"></div></div>
                      <span style="font-size:14px;font-weight:600;">8.5/10</span>
                    </div>
                  </div>
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                    <span style="font-size:14px;">&#x1F9FD; Onderhoud</span>
                    <div style="display:flex;align-items:center;gap:8px;">
                      <div style="width:80px;height:6px;background:#e5e7eb;"><div style="width:80%;height:100%;background:var(--coffee);"></div></div>
                      <span style="font-size:14px;font-weight:600;">8.0/10</span>
                    </div>
                  </div>
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                    <span style="font-size:14px;">&#x1F370; Traditie</span>
                    <div style="display:flex;align-items:center;gap:8px;">
                      <div style="width:80px;height:6px;background:#e5e7eb;"><div style="width:100%;height:100%;background:var(--coffee);"></div></div>
                      <span style="font-size:14px;font-weight:600;">10/10/10</span>
                    </div>
                  </div></div>
              </div>
              <div style="display:flex;gap:0.75rem;flex-wrap:wrap;">
                <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored"
                   style="flex:1;background:linear-gradient(135deg,var(--coffee),#8B4513);color:white;padding:0.75rem 1.25rem;text-decoration:none;font-weight:600;text-align:center;">
                  Bekijk prijs op Bol.com &#x2192;
                </a>
                <a href="categories/percolators.html"
                   style="flex:1;border:2px solid var(--coffee);padding:0.75rem 1.25rem;text-decoration:none;font-weight:600;text-align:center; border: 1px solid var(--border); border-radius: 0.5rem;">
                  Vergelijk alle percolators
                </a>
              </div>
            </div>
          </div>
        </div>
        <div style="position:sticky;top:100px;">
          <img src="Images/bialetti-moka-express-1.jpg" alt="Bialetti Moka Express Review 2025"
               style="width:100%;"
               onerror="this.src='Images/bialetti-moka-express-1.jpg'">
          <div style="background:white;padding:1.25rem;margin-top:1rem;">
            <div style="font-size:1.4rem;font-weight:700;margin-bottom:0.5rem;">&#x20AC;15&#x2013;35</div>
            <div style="font-size:0.85rem;color:#059669;margin-bottom:1rem;">&#x2713; Op voorraad via Bol.com</div>
            <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored"
               style="display:block;background:var(--coffee);color:white;padding:0.65rem;text-decoration:none;font-weight:600;text-align:center;font-size:0.9rem;">
              Koop op Bol.com &#x2192;
            </a>
            <a href="boutique.html" style="display:block;text-align:center;margin-top:0.75rem;font-size:0.85rem;text-decoration:none;font-weight:600;">
              &#x1F6CD; Bekijk alle modellen in de winkel
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>'''

hero_new = '''  <section style="padding: 3rem 0;">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 340px; gap: 3rem; align-items: start; max-width: 1100px; margin: 0 auto;">
        <div>
          <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3vw, 2.4rem); font-weight: 400; margin-bottom: 1rem; color: var(--coffee);">Bialetti Moka Express Review 2025: De Klassieke Referentie</h1>
          <p style="color: var(--text-dim); line-height: 1.8; margin-bottom: 2rem; font-size: 1rem;">Sinds 1933 is de Moka Express het symbool van de Italiaanse koffiecultuur. Iconisch achthoekig design, aluminiumconstructie en authentieke moka-smaak. We testen dit model uitgebreid en vergelijken het met moderne alternatieven.</p>
          
          <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white; margin-bottom: 2rem;">
              <div style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 1.5rem;">
                <div style="font-size: 2.5rem; font-weight: 700; color: var(--coffee);">9.0/10</div>
                <div>
                  <h3 style="margin-bottom: 0.25rem; color: var(--text);">Tijdloze klassieker</h3>
                  <p style="color: var(--text-dim); font-size: 0.9rem;">Het origineel sinds 1933</p>
                </div>
              </div>
              
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem;">
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 0.85rem; color: var(--text-light);">Koffiesmaak</span>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                      <div style="width: 60px; height: 5px; background: #e5e7eb; border-radius: 2px;"><div style="width: 93%; height: 100%; background: var(--coffee); border-radius: 2px;"></div></div>
                      <span style="font-size: 0.85rem; font-weight: 600; color: var(--text);">9.3/10</span>
                    </div>
                  </div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 0.85rem; color: var(--text-light);">Design & Kwaliteit</span>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                      <div style="width: 60px; height: 5px; background: #e5e7eb; border-radius: 2px;"><div style="width: 95%; height: 100%; background: var(--coffee); border-radius: 2px;"></div></div>
                      <span style="font-size: 0.85rem; font-weight: 600; color: var(--text);">9.5/10</span>
                    </div>
                  </div>
                  <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.85rem; color: var(--text-light);">Prijs/Waarde</span>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                      <div style="width: 60px; height: 5px; background: #e5e7eb; border-radius: 2px;"><div style="width: 95%; height: 100%; background: var(--coffee); border-radius: 2px;"></div></div>
                      <span style="font-size: 0.85rem; font-weight: 600; color: var(--text);">9.5/10</span>
                    </div>
                  </div>
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 0.85rem; color: var(--text-light);">Gebruiksgemak</span>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                      <div style="width: 60px; height: 5px; background: #e5e7eb; border-radius: 2px;"><div style="width: 85%; height: 100%; background: var(--coffee); border-radius: 2px;"></div></div>
                      <span style="font-size: 0.85rem; font-weight: 600; color: var(--text);">8.5/10</span>
                    </div>
                  </div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 0.85rem; color: var(--text-light);">Onderhoud</span>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                      <div style="width: 60px; height: 5px; background: #e5e7eb; border-radius: 2px;"><div style="width: 80%; height: 100%; background: var(--coffee); border-radius: 2px;"></div></div>
                      <span style="font-size: 0.85rem; font-weight: 600; color: var(--text);">8.0/10</span>
                    </div>
                  </div>
                  <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.85rem; color: var(--text-light);">Traditie</span>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                      <div style="width: 60px; height: 5px; background: #e5e7eb; border-radius: 2px;"><div style="width: 100%; height: 100%; background: var(--coffee); border-radius: 2px;"></div></div>
                      <span style="font-size: 0.85rem; font-weight: 600; color: var(--text);">10/10</span>
                    </div>
                  </div>
                </div>
              </div>
              
              <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored"
                   style="flex: 1; background: var(--coffee); color: white; padding: 0.75rem 1.25rem; text-decoration: none; font-weight: 600; text-align: center; border-radius: 0.3rem; font-size: 0.9rem;">
                  Bekijk prijs op Bol.com →
                </a>
                <a href="categories/percolators.html"
                   style="flex: 1; border: 1px solid var(--coffee); padding: 0.75rem 1.25rem; text-decoration: none; font-weight: 600; text-align: center; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">
                  Vergelijk alle percolators
                </a>
              </div>
          </div>
        </div>
        
        <div style="position: sticky; top: 100px;">
          <img src="Images/bialetti-moka-express-1.jpg" alt="Bialetti Moka Express Review 2025"
               style="width: 100%; border-radius: 0.5rem;"
               onerror="this.src='Images/bialetti-moka-express-1.jpg'">
          <div style="background: white; padding: 1.25rem; margin-top: 1rem; border: 1px solid var(--border); border-radius: 0.5rem;">
            <div style="font-size: 1.4rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--text);">€15–35</div>
            <div style="font-size: 0.85rem; color: #059669; margin-bottom: 1rem;">Op voorraad via Bol.com</div>
            <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored"
               style="display: block; background: var(--coffee); color: white; padding: 0.65rem; text-decoration: none; font-weight: 600; text-align: center; font-size: 0.9rem; border-radius: 0.3rem;">
              Koop op Bol.com →
            </a>
            <a href="boutique.html" style="display: block; text-align: center; margin-top: 0.75rem; font-size: 0.85rem; text-decoration: none; font-weight: 600; color: var(--text-dim);">
              Bekijk alle modellen in de winkel
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(hero_old, hero_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Plus/minus points section
plusminus_old = '''  <section class="section-sm" style="background:var(--surface-soft);">
    <div class="container">
      <h2 style="text-align:center;">Plus- en minpunten</h2>
      <div class="grid grid-2 gap-6" style="max-width:800px;margin:0 auto;">
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          
            <h3 style="color:#059669;margin-bottom:1rem;">&#x2714; Pluspunten</h3>
            <ul style="list-style:none;padding:0;margin:0;"><li style="padding:0.5rem 0;border-bottom:1px solid #f0f0f0;"><strong>Iconisch design:</strong> Tijdloos en herkenbaar wereldwijd</li><li style="padding:0.5rem 0;border-bottom:1px solid #f0f0f0;"><strong>Authentieke smaak:</strong> De klassieke Italiaanse koffiesmaak</li><li style="padding:0.5rem 0;border-bottom:1px solid #f0f0f0;"><strong>Betaalbaar:</strong> Uitstekende prijs-kwaliteitverhouding</li><li style="padding:0.5rem 0;border-bottom:1px solid #f0f0f0;"><strong>Lichtgewicht:</strong> Aluminium is licht en handig</li><li style="padding:0.5rem 0;border-bottom:1px solid #f0f0f0;"><strong>Snelle opwarming:</strong> Aluminium geleidt warmte snel</li><li style="padding:0.5rem 0;"><strong>Vele maten:</strong> Van 1 tot 18 kopjes beschikbaar</li></ul>
          
        </div>
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          
            <h3 style="margin-bottom:1rem;">&#x2715; Minpunten</h3>
            <ul style="list-style:none;padding:0;margin:0;"><li style="padding:0.5rem 0;border-bottom:1px solid #f0f0f0;"><strong>Niet inductiegeschikt:</strong> Werkt niet op inductiekookplaten</li><li style="padding:0.5rem 0;border-bottom:1px solid #f0f0f0;"><strong>Handwas verplicht:</strong> Niet vaatwasmachinebestendig</li><li style="padding:0.5rem 0;border-bottom:1px solid #f0f0f0;"><strong>Aluminium smaak:</strong> Eerste brouwsels kunnen metaalachtig smaken</li><li style="padding:0.5rem 0;"><strong>Gevoelig voor krassen:</strong> Aluminium krast makkelijk</li></ul>
          
        </div>
      </div>
    </div>
  </section>'''

plusminus_new = '''  <section style="background: #fafafa; padding: 3rem 0;">
    <div class="container">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; text-align: center; margin-bottom: 2rem; color: var(--coffee);">Plus- en minpunten</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; max-width: 800px; margin: 0 auto;">
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
            <h3 style="color: #059669; margin-bottom: 1rem; font-size: 1.1rem;">Pluspunten</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light); font-size: 0.9rem;"><strong>Iconisch design:</strong> Tijdloos en herkenbaar wereldwijd</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light); font-size: 0.9rem;"><strong>Authentieke smaak:</strong> De klassieke Italiaanse koffiesmaak</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light); font-size: 0.9rem;"><strong>Betaalbaar:</strong> Uitstekende prijs-kwaliteitverhouding</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light); font-size: 0.9rem;"><strong>Lichtgewicht:</strong> Aluminium is licht en handig</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light); font-size: 0.9rem;"><strong>Snelle opwarming:</strong> Aluminium geleidt warmte snel</li>
                <li style="padding: 0.5rem 0; color: var(--text-light); font-size: 0.9rem;"><strong>Vele maten:</strong> Van 1 tot 18 kopjes beschikbaar</li>
            </ul>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
            <h3 style="color: var(--text); margin-bottom: 1rem; font-size: 1.1rem;">Minpunten</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light); font-size: 0.9rem;"><strong>Niet inductiegeschikt:</strong> Werkt niet op inductiekookplaten</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light); font-size: 0.9rem;"><strong>Handwas verplicht:</strong> Niet vaatwasmachinebestendig</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light); font-size: 0.9rem;"><strong>Aluminium smaak:</strong> Eerste brouwsels kunnen metaalachtig smaken</li>
                <li style="padding: 0.5rem 0; color: var(--text-light); font-size: 0.9rem;"><strong>Gevoelig voor krassen:</strong> Aluminium krast makkelijk</li>
            </ul>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(plusminus_old, plusminus_new)

# Voor wie section
voorwie_old = '''  <section class="section-sm">
    <div class="container" style="max-width:800px;">
      <h2>Voor wie is dit model geschikt?</h2>
      <p>De Moka Express is de referentie voor iedereen die de authentieke Italiaanse koffie-ervaring zoekt. Betaalbaar, tijdloos en beschikbaar in alle maten.</p>
      <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;" style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
        
          <strong>&#x2714; Kies dit model als jij&#x2026;</strong>
          <ul style="margin-top:0.75rem;"><li>De klassieke moka-smaak wil — niet te missen</li><li>Koffie zet op gas, elektrisch of keramisch</li><li>Een betaalbaar model zoekt dat jaren meegaat</li><li>Keuze hebt uit meerdere maten (1&#x2013;12 kops)</li></ul>
        
      </div>
      <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;" style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
        
          <strong>&#x274C; Kies een alternatief als jij&#x2026;</strong>
          <ul style="margin-top:0.75rem;"><li>Een inductiekookplaat hebt &#x2192; <a href="bialetti-venus-review.html" style="font-weight:600;">Bialetti Venus</a></li><li>Meer crema en espresso-karakter wil &#x2192; <a href="bialetti-brikka-review.html" style="font-weight:600;">Bialetti Brikka</a></li><li>Geen kookplaat hebt &#x2192; <a href="bialetti-moka-timer-review.html" style="font-weight:600;">Bialetti Moka Timer (elektrisch)</a></li></ul>
        
      </div>
    </div>
  </section>'''

voorwie_new = '''  <section style="padding: 3rem 0;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1rem; color: var(--coffee);">Voor wie is dit model geschikt?</h2>
      <p style="color: var(--text-dim); line-height: 1.8; margin-bottom: 2rem;">De Moka Express is de referentie voor iedereen die de authentieke Italiaanse koffie-ervaring zoekt. Betaalbaar, tijdloos en beschikbaar in alle maten.</p>
      
      <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: #f5f0ea; margin-bottom: 1.5rem;">
          <strong style="color: var(--coffee);">Kies dit model als jij…</strong>
          <ul style="margin-top: 0.75rem; padding-left: 1.25rem; color: var(--text-light); font-size: 0.95rem; line-height: 1.7;">
              <li>De klassieke moka-smaak wil — niet te missen</li>
              <li>Koffie zet op gas, elektrisch of keramisch</li>
              <li>Een betaalbaar model zoekt dat jaren meegaat</li>
              <li>Keuze hebt uit meerdere maten (1–12 kops)</li>
          </ul>
      </div>
      
      <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
          <strong style="color: var(--text);">Kies een alternatief als jij…</strong>
          <ul style="margin-top: 0.75rem; padding-left: 1.25rem; color: var(--text-light); font-size: 0.95rem; line-height: 1.7;">
              <li>Een inductiekookplaat hebt → <a href="bialetti-venus-review.html" style="color: var(--coffee); font-weight: 600;">Bialetti Venus</a></li>
              <li>Meer crema en espresso-karakter wil → <a href="bialetti-brikka-review.html" style="color: var(--coffee); font-weight: 600;">Bialetti Brikka</a></li>
              <li>Geen kookplaat hebt → <a href="bialetti-moka-timer-review.html" style="color: var(--coffee); font-weight: 600;">Bialetti Moka Timer (elektrisch)</a></li>
          </ul>
      </div>
    </div>
  </section>'''

content = content.replace(voorwie_old, voorwie_new)

# Specifications table
specs_old = '''  <section class="section-sm" style="background:var(--surface-soft);">
    <div class="container" style="max-width:700px;">
      <h2>Specificaties</h2>
      <table style="width:100%;border-collapse:collapse;background:white;overflow:hidden;">
        <tbody><tr style="border-bottom:1px solid #f0f0f0;"><td style="padding:0.85rem 1.25rem;font-weight:600;color:#666;width:40%;">Merk</td><td style="padding:0.85rem 1.25rem;">Bialetti</td></tr>
<tr style="border-bottom:1px solid #f0f0f0;background:#fafafa;"><td style="padding:0.85rem 1.25rem;font-weight:600;color:#666;width:40%;">Model</td><td style="padding:0.85rem 1.25rem;">Moka Express</td></tr>
<tr style="border-bottom:1px solid #f0f0f0;"><td style="padding:0.85rem 1.25rem;font-weight:600;color:#666;width:40%;">Type</td><td style="padding:0.85rem 1.25rem;">Italiaanse percolator (moka pot)</td></tr>
<tr style="border-bottom:1px solid #f0f0f0;background:#fafafa;"><td style="padding:0.85rem 1.25rem;font-weight:600;color:#666;width:40%;">Capaciteit</td><td style="padding:0.85rem 1.25rem;">2 / 3 / 4 / 6 / 9 / 12 kops</td></tr>
<tr style="border-bottom:1px solid #f0f0f0;"><td style="padding:0.85rem 1.25rem;font-weight:600;color:#666;width:40%;">Materiaal</td><td style="padding:0.85rem 1.25rem;">Aluminium</td></tr>
<tr style="border-bottom:1px solid #f0f0f0;background:#fafafa;"><td style="padding:0.85rem 1.25rem;font-weight:600;color:#666;width:40%;">Warmtebron</td><td style="padding:0.85rem 1.25rem;">Gas / elektrisch / keramisch (geen inductie)</td></tr>
<tr style="border-bottom:1px solid #f0f0f0;"><td style="padding:0.85rem 1.25rem;font-weight:600;color:#666;width:40%;">Inductie geschikt</td><td style="padding:0.85rem 1.25rem;">Nee (adapter mogelijk)</td></tr>
<tr style="border-bottom:1px solid #f0f0f0;background:#fafafa;"><td style="padding:0.85rem 1.25rem;font-weight:600;color:#666;width:40%;">Prijsklasse</td><td style="padding:0.85rem 1.25rem;">Budget / middenklasse &mdash; &#x20AC;15&#x2013;35</td></tr>
</tbody>
      </table>
    </div>
  </section>'''

specs_new = '''  <section style="background: #fafafa; padding: 3rem 0;">
    <div class="container" style="max-width: 700px;">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1.5rem; color: var(--coffee);">Specificaties</h2>
      <table style="width: 100%; border-collapse: collapse; background: white; border: 1px solid var(--border); border-radius: 0.5rem; overflow: hidden;">
        <tbody>
            <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 1rem 1.25rem; font-weight: 600; color: var(--text-light); width: 40%;">Merk</td><td style="padding: 1rem 1.25rem; color: var(--text);">Bialetti</td></tr>
            <tr style="border-bottom: 1px solid var(--border); background: #fafafa;"><td style="padding: 1rem 1.25rem; font-weight: 600; color: var(--text-light); width: 40%;">Model</td><td style="padding: 1rem 1.25rem; color: var(--text);">Moka Express</td></tr>
            <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 1rem 1.25rem; font-weight: 600; color: var(--text-light); width: 40%;">Type</td><td style="padding: 1rem 1.25rem; color: var(--text);">Italiaanse percolator (moka pot)</td></tr>
            <tr style="border-bottom: 1px solid var(--border); background: #fafafa;"><td style="padding: 1rem 1.25rem; font-weight: 600; color: var(--text-light); width: 40%;">Capaciteit</td><td style="padding: 1rem 1.25rem; color: var(--text);">2 / 3 / 4 / 6 / 9 / 12 kops</td></tr>
            <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 1rem 1.25rem; font-weight: 600; color: var(--text-light); width: 40%;">Materiaal</td><td style="padding: 1rem 1.25rem; color: var(--text);">Aluminium</td></tr>
            <tr style="border-bottom: 1px solid var(--border); background: #fafafa;"><td style="padding: 1rem 1.25rem; font-weight: 600; color: var(--text-light); width: 40%;">Warmtebron</td><td style="padding: 1rem 1.25rem; color: var(--text);">Gas / elektrisch / keramisch (geen inductie)</td></tr>
            <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 1rem 1.25rem; font-weight: 600; color: var(--text-light); width: 40%;">Inductie geschikt</td><td style="padding: 1rem 1.25rem; color: var(--text);">Nee (adapter mogelijk)</td></tr>
            <tr><td style="padding: 1rem 1.25rem; font-weight: 600; color: var(--text-light); width: 40%; background: #fafafa;">Prijsklasse</td><td style="padding: 1rem 1.25rem; color: var(--text); background: #fafafa;">Budget / middenklasse — €15–35</td></tr>
        </tbody>
      </table>
    </div>
  </section>'''

content = content.replace(specs_old, specs_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# "Waarom blijft de Moka Express de referentie" section
referentie_old = '''  <section class="section-sm">
    <div class="container" style="max-width:800px;">
      <h2>Waarom blijft de Moka Express de referentie?</h2>
      <p>Het ontwerp van Alfonso Bialetti dateert uit 1933 en is sindsdien nauwelijks veranderd. Dat zegt alles. De Moka Express combineert een eenvoudige bouwwijze met een betrouwbare extractietechniek die generaties lang meegaat.</p>
      <p>De eerste paar brouwsels kunnen licht metaalachtig smaken — dit is normaal voor aluminium en verdwijnt snel. Daarna levert de Moka Express een krachtige, aromatische koffie die kenmerkend is voor de Italiaanse moka-traditie.</p>
    </div>
  </section>'''

referentie_new = '''  <section style="padding: 3rem 0;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1rem; color: var(--coffee);">Waarom blijft de Moka Express de referentie?</h2>
      <p style="color: var(--text-dim); line-height: 1.8; margin-bottom: 1rem;">Het ontwerp van Alfonso Bialetti dateert uit 1933 en is sindsdien nauwelijks veranderd. Dat zegt alles. De Moka Express combineert een eenvoudige bouwwijze met een betrouwbare extractietechniek die generaties lang meegaat.</p>
      <p style="color: var(--text-dim); line-height: 1.8;">De eerste paar brouwsels kunnen licht metaalachtig smaken — dit is normaal voor aluminium en verdwijnt snel. Daarna levert de Moka Express een krachtige, aromatische koffie die kenmerkend is voor de Italiaanse moka-traditie.</p>
    </div>
  </section>'''

content = content.replace(referentie_old, referentie_new)

# Comparison section
comparison_old = '''  <section class="section-sm" style="background:var(--surface-soft);">
    <div class="container" style="max-width:800px;">
      <h2>Vergelijk met alternatieven</h2>
      <div style="display:flex;flex-direction:column;gap:1rem;">
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          
            <div><strong>Bialetti Fiammetta</strong><p style="color:#666;font-size:0.9rem;margin:0.25rem 0 0;">Compacter aluminium model, zelfde techniek. Beter als je minder dan 3 kopjes wil.</p>
            <a href="bialetti-fiammetta-review.html" style="border:2px solid var(--coffee);padding:0.5rem 1rem;text-decoration:none;font-weight:600;white-space:nowrap;font-size:0.9rem; border: 1px solid var(--border); border-radius: 0.5rem;">Bekijk review</a>
          </div>
        </div>
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          
            <div><strong>Bialetti Brikka</strong><p style="color:#666;font-size:0.9rem;margin:0.25rem 0 0;">Variant met extra crema. Interessant als je meer espresso-karakter wilt.</p>
            <a href="bialetti-brikka-review.html" style="border:2px solid var(--coffee);padding:0.5rem 1rem;text-decoration:none;font-weight:600;white-space:nowrap;font-size:0.9rem; border: 1px solid var(--border); border-radius: 0.5rem;">Bekijk review</a>
          </div>
        </div>
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          
            <div><strong>Bialetti Venus</strong><p style="color:#666;font-size:0.9rem;margin:0.25rem 0 0;">RVS versie voor inductie. Kies dit als je inductie hebt.</p>
            <a href="bialetti-venus-review.html" style="border:2px solid var(--coffee);padding:0.5rem 1rem;text-decoration:none;font-weight:600;white-space:nowrap;font-size:0.9rem; border: 1px solid var(--border); border-radius: 0.5rem;">Bekijk review</a>
          </div>
        </div></div>
    </div>
  </section>'''

comparison_new = '''  <section style="background: #fafafa; padding: 3rem 0;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1.5rem; color: var(--coffee);">Vergelijk met alternatieven</h2>
      <div style="display: flex; flex-direction: column; gap: 1rem;">
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.25rem; background: white;">
            <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                <div>
                    <strong style="color: var(--text);">Bialetti Fiammetta</strong>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin: 0.25rem 0 0;">Compacter aluminium model, zelfde techniek. Beter als je minder dan 3 kopjes wil.</p>
                </div>
                <a href="bialetti-fiammetta-review.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; white-space: nowrap; font-size: 0.85rem; border-radius: 0.3rem; color: var(--text);">Bekijk review</a>
            </div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.25rem; background: white;">
            <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                <div>
                    <strong style="color: var(--text);">Bialetti Brikka</strong>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin: 0.25rem 0 0;">Variant met extra crema. Interessant als je meer espresso-karakter wilt.</p>
                </div>
                <a href="bialetti-brikka-review.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; white-space: nowrap; font-size: 0.85rem; border-radius: 0.3rem; color: var(--text);">Bekijk review</a>
            </div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.25rem; background: white;">
            <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                <div>
                    <strong style="color: var(--text);">Bialetti Venus</strong>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin: 0.25rem 0 0;">RVS versie voor inductie. Kies dit als je inductie hebt.</p>
                </div>
                <a href="bialetti-venus-review.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; white-space: nowrap; font-size: 0.85rem; border-radius: 0.3rem; color: var(--text);">Bekijk review</a>
            </div>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(comparison_old, comparison_new)

# FAQ section
faq_old = '''  <section class="section-sm">
    <div class="container" style="max-width:800px;">
      <h2>Veelgestelde vragen</h2>
      <div style="border:1px solid #ddd;overflow:hidden;margin-bottom:1rem; border: 1px solid var(--border); border-radius: 0.5rem;">
        <button onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'"
                style="width:100%;padding:1.2rem 1.5rem;background:white;border:none;text-align:left;font-size:1rem;font-weight:600;cursor:pointer;display:flex;justify-content:space-between; border: 1px solid var(--border); border-radius: 0.5rem;">
          Is de Moka Express geschikt voor inductie? <span>+</span>
        </button>
        <div style="display:none;padding:1rem 1.5rem 1.5rem;color:#555;line-height:1.7;">Nee, aluminium geleidt geen inductie. Je kunt een inductieadapterplaatje gebruiken als tussenoplossing. Wil je rechtstreeks op inductie, kies dan de <a href="bialetti-venus-review.html" style="">Bialetti Venus</a> (RVS).</div>
      </div>
      <div style="border:1px solid #ddd;overflow:hidden;margin-bottom:1rem; border: 1px solid var(--border); border-radius: 0.5rem;">
        <button onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'"
                style="width:100%;padding:1.2rem 1.5rem;background:white;border:none;text-align:left;font-size:1rem;font-weight:600;cursor:pointer;display:flex;justify-content:space-between; border: 1px solid var(--border); border-radius: 0.5rem;">
          Welke maat Moka Express moet ik kiezen? <span>+</span>
        </button>
        <div style="display:none;padding:1rem 1.5rem 1.5rem;color:#555;line-height:1.7;">Voor 1&#x2013;2 personen: 3 kops. Voor 2&#x2013;3 personen: 4 kops. Voor 4+ personen: 6 kops. Onthoud: 1 "kop" = circa 50ml espresso, dus geen grote koffiekop.</div>
      </div>
      <div style="border:1px solid #ddd;overflow:hidden;margin-bottom:1rem; border: 1px solid var(--border); border-radius: 0.5rem;">
        <button onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'"
                style="width:100%;padding:1.2rem 1.5rem;background:white;border:none;text-align:left;font-size:1rem;font-weight:600;cursor:pointer;display:flex;justify-content:space-between; border: 1px solid var(--border); border-radius: 0.5rem;">
          Hoe verwijder ik de aluminium bijsmaak? <span>+</span>
        </button>
        <div style="display:none;padding:1rem 1.5rem 1.5rem;color:#555;line-height:1.7;">Zet de eerste 3&#x2013;4 keer koffie die je weggooit. Gebruik nooit zeep in het koffiegedeelte. Daarna verdwijnt de bijsmaak volledig.</div>
      </div>
    </div>
  </section>'''

faq_new = '''  <section style="padding: 3rem 0;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 2rem; color: var(--coffee);">Veelgestelde vragen</h2>
      <div style="border: 1px solid var(--border); border-radius: 0.5rem; margin-bottom: 1rem; overflow: hidden; background: white;">
        <button onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'"
                style="width: 100%; padding: 1.25rem; background: white; border: none; text-align: left; font-size: 0.95rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--text);">
          Is de Moka Express geschikt voor inductie? <span style="color: var(--coffee); font-size: 1.2rem;">+</span>
        </button>
        <div style="display: none; padding: 0 1.25rem 1.25rem 1.25rem; background: #fafafa; color: var(--text-light); line-height: 1.7; font-size: 0.9rem;">Nee, aluminium geleidt geen inductie. Je kunt een inductieadapterplaatje gebruiken als tussenoplossing. Wil je rechtstreeks op inductie, kies dan de <a href="bialetti-venus-review.html" style="color: var(--coffee);">Bialetti Venus</a> (RVS).</div>
      </div>
      <div style="border: 1px solid var(--border); border-radius: 0.5rem; margin-bottom: 1rem; overflow: hidden; background: white;">
        <button onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'"
                style="width: 100%; padding: 1.25rem; background: white; border: none; text-align: left; font-size: 0.95rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--text);">
          Welke maat Moka Express moet ik kiezen? <span style="color: var(--coffee); font-size: 1.2rem;">+</span>
        </button>
        <div style="display: none; padding: 0 1.25rem 1.25rem 1.25rem; background: #fafafa; color: var(--text-light); line-height: 1.7; font-size: 0.9rem;">Voor 1–2 personen: 3 kops. Voor 2–3 personen: 4 kops. Voor 4+ personen: 6 kops. Onthoud: 1 "kop" = circa 50ml espresso, dus geen grote koffiekop.</div>
      </div>
      <div style="border: 1px solid var(--border); border-radius: 0.5rem; overflow: hidden; background: white;">
        <button onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'"
                style="width: 100%; padding: 1.25rem; background: white; border: none; text-align: left; font-size: 0.95rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--text);">
          Hoe verwijder ik de aluminium bijsmaak? <span style="color: var(--coffee); font-size: 1.2rem;">+</span>
        </button>
        <div style="display: none; padding: 0 1.25rem 1.25rem 1.25rem; background: #fafafa; color: var(--text-light); line-height: 1.7; font-size: 0.9rem;">Zet de eerste 3–4 keer koffie die je weggooit. Gebruik nooit zeep in het koffiegedeelte. Daarna verdwijnt de bijsmaak volledig.</div>
      </div>
    </div>
  </section>'''

content = content.replace(faq_old, faq_new)

# Final verdict section
verdict_old = '''  <section class="section-sm" style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
    <div class="container" style="max-width:800px;text-align:center;">
      <h2>Eindbeoordeling: 9.0/10</h2>
      <div class="rating-badge" style="font-size:2rem;margin:1rem auto;">9.0/10</div>
      <p style="max-width:600px;margin:0 auto 2rem;line-height:1.8;color:#444;">De Bialetti Moka Express is een tijdloze investering. Generaties lang meegaand, authentieke smaak en onverslaanbare prijs-kwaliteitverhouding. Voor wie geen inductie heeft en de klassieke moka-beleving wil, is dit simpelweg de beste keuze.</p>
      <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
        <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored"
           style="background:linear-gradient(135deg,var(--coffee),#8B4513);color:white;padding:0.9rem 2rem;text-decoration:none;font-weight:700;font-size:1rem;">
          Bekijk in de shop &#x2192;
        </a>
        <a href="boutique.html"
           style="border:2px solid var(--coffee);padding:0.9rem 2rem;text-decoration:none;font-weight:700;font-size:1rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          Alle modellen vergelijken
        </a>
      </div>
    </div>
  </section>'''

verdict_new = '''  <section style="background: #f5f0ea; padding: 3rem 0;">
    <div class="container" style="max-width: 800px; text-align: center;">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1rem; color: var(--coffee);">Eindbeoordeling: 9.0/10</h2>
      <div style="font-size: 2.5rem; font-weight: 700; color: var(--coffee); margin: 1rem auto;">9.0/10</div>
      <p style="max-width: 600px; margin: 0 auto 2rem; line-height: 1.8; color: var(--text-light);">De Bialetti Moka Express is een tijdloze investering. Generaties lang meegaand, authentieke smaak en onverslaanbare prijs-kwaliteitverhouding. Voor wie geen inductie heeft en de klassieke moka-beleving wil, is dit simpelweg de beste keuze.</p>
      <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
        <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored"
           style="background: var(--coffee); color: white; padding: 0.9rem 2rem; text-decoration: none; font-weight: 700; font-size: 1rem; border-radius: 0.3rem;">
          Bekijk in de shop →
        </a>
        <a href="boutique.html"
           style="border: 1px solid var(--coffee); padding: 0.9rem 2rem; text-decoration: none; font-weight: 700; font-size: 1rem; border-radius: 0.3rem; color: var(--text);">
          Alle modellen vergelijken
        </a>
      </div>
    </div>
  </section>'''

content = content.replace(verdict_old, verdict_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Related pages section
related_old = '''  <section class="section-sm">
    <div class="container" style="max-width:800px;">
      <h2 style="font-size:1.2rem;margin-bottom:1.25rem;">Gerelateerde pagina&#x27;s</h2>
      <ul style="columns:2;gap:2rem;">
        <li><a href="categories/percolators.html" style="">Vergelijk alle percolators</a></li>
        <li><a href="marques/bialetti/" style="">Alle Bialetti modellen</a></li>
        <li><a href="koopgids/index.html" style="">Koopgids percolators</a></li>
        <li><a href="beste-italiaanse-percolators.html" style="">Top 10 beste percolators</a></li>
        <li><a href="boutique.html" style="">Shop alle modellen</a></li>
        <li><a href="vergelijking/index.html" style="">Vergelijkingstool</a></li>
      </ul>
    </div>
  </section>'''

related_new = '''  <section style="padding: 3rem 0;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1.5rem; color: var(--coffee);">Gerelateerde pagina's</h2>
      <ul style="columns: 2; gap: 2rem; list-style: none; padding: 0;">
        <li style="margin-bottom: 0.5rem;"><a href="categories/percolators.html" style="color: var(--coffee); text-decoration: none;">Vergelijk alle percolators</a></li>
        <li style="margin-bottom: 0.5rem;"><a href="marques/bialetti/" style="color: var(--coffee); text-decoration: none;">Alle Bialetti modellen</a></li>
        <li style="margin-bottom: 0.5rem;"><a href="koopgids/index.html" style="color: var(--coffee); text-decoration: none;">Koopgids percolators</a></li>
        <li style="margin-bottom: 0.5rem;"><a href="beste-italiaanse-percolators.html" style="color: var(--coffee); text-decoration: none;">Top 10 beste percolators</a></li>
        <li style="margin-bottom: 0.5rem;"><a href="boutique.html" style="color: var(--coffee); text-decoration: none;">Shop alle modellen</a></li>
        <li style="margin-bottom: 0.5rem;"><a href="vergelijking/index.html" style="color: var(--coffee); text-decoration: none;">Vergelijkingstool</a></li>
      </ul>
    </div>
  </section>'''

content = content.replace(related_old, related_new)

# Similar products grid
similar_old = '''  <section class="section-sm" style="background:var(--surface-soft);">
    <div class="container">
      <h2 class="text-center mb-8">Vergelijkbare producten</h2>
      <div class="grid grid-3">
        <div class="product-card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          <div class="product-image"><img src="Images/bialetti_fiammetta.jpg" alt="Bialetti Fiammetta" onerror="this.src='Images/bialetti-moka-express-1.jpg'"></div>
          <div class="product-content">
            <h3 class="product-title">Bialetti Fiammetta</h3>
            <p class="product-subtitle">Compact, betaalbaar</p>
            <div class="product-rating"><div class="stars">&#x2605;&#x2605;&#x2605;&#x2605;&#x2605;</div><span class="rating-text">9.2/10</span></div>
            <a href="bialetti-fiammetta-review.html" class="btn btn-secondary">Bekijk review</a>
          </div>
        </div>
        <div class="product-card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          <div class="product-image"><img src="Images/bialetti_brikka.jpg" alt="Bialetti Brikka" onerror="this.src='Images/bialetti-moka-express-1.jpg'"></div>
          <div class="product-content">
            <h3 class="product-title">Bialetti Brikka</h3>
            <p class="product-subtitle">Met crema functie</p>
            <div class="product-rating"><div class="stars">&#x2605;&#x2605;&#x2605;&#x2605;&#x2606;</div><span class="rating-text">8.6/10</span></div>
            <a href="bialetti-brikka-review.html" class="btn btn-secondary">Bekijk review</a>
          </div>
        </div>
        <div class="product-card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;">
          <div class="product-image"><img src="Images/bialetti_venus.jpg" alt="Bialetti Venus" onerror="this.src='Images/bialetti-moka-express-1.jpg'"></div>
          <div class="product-content">
            <h3 class="product-title">Bialetti Venus</h3>
            <p class="product-subtitle">Voor inductie</p>
            <div class="product-rating"><div class="stars">&#x2605;&#x2605;&#x2605;&#x2605;&#x2605;</div><span class="rating-text">8.8/10</span></div>
            <a href="bialetti-venus-review.html" class="btn btn-secondary">Bekijk review</a>
          </div>
        </div></div>
    </div>
  </section>'''

similar_new = '''  <section style="background: #fafafa; padding: 3rem 0;">
    <div class="container">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; text-align: center; margin-bottom: 2rem; color: var(--coffee);">Vergelijkbare producten</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem;">
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; overflow: hidden; background: white;">
          <div style="background: #fafafa; padding: 1.5rem; text-align: center;"><img src="Images/bialetti_fiammetta.jpg" alt="Bialetti Fiammetta" onerror="this.src='Images/bialetti-moka-express-1.jpg'" style="max-height: 160px; object-fit: contain;"></div>
          <div style="padding: 1.25rem;">
            <h3 style="font-size: 1rem; margin-bottom: 0.5rem; color: var(--text);">Bialetti Fiammetta</h3>
            <p style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 1rem;">Compact, betaalbaar</p>
            <a href="bialetti-fiammetta-review.html" style="display: inline-block; padding: 0.5rem 1rem; background: var(--coffee); color: white; text-decoration: none; border-radius: 0.3rem; font-size: 0.85rem;">Bekijk review</a>
          </div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; overflow: hidden; background: white;">
          <div style="background: #fafafa; padding: 1.5rem; text-align: center;"><img src="Images/bialetti_brikka.jpg" alt="Bialetti Brikka" onerror="this.src='Images/bialetti-moka-express-1.jpg'" style="max-height: 160px; object-fit: contain;"></div>
          <div style="padding: 1.25rem;">
            <h3 style="font-size: 1rem; margin-bottom: 0.5rem; color: var(--text);">Bialetti Brikka</h3>
            <p style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 1rem;">Met crema functie</p>
            <a href="bialetti-brikka-review.html" style="display: inline-block; padding: 0.5rem 1rem; background: var(--coffee); color: white; text-decoration: none; border-radius: 0.3rem; font-size: 0.85rem;">Bekijk review</a>
          </div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; overflow: hidden; background: white;">
          <div style="background: #fafafa; padding: 1.5rem; text-align: center;"><img src="Images/bialetti_venus.jpg" alt="Bialetti Venus" onerror="this.src='Images/bialetti-moka-express-1.jpg'" style="max-height: 160px; object-fit: contain;"></div>
          <div style="padding: 1.25rem;">
            <h3 style="font-size: 1rem; margin-bottom: 0.5rem; color: var(--text);">Bialetti Venus</h3>
            <p style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 1rem;">Voor inductie</p>
            <a href="bialetti-venus-review.html" style="display: inline-block; padding: 0.5rem 1rem; background: var(--coffee); color: white; text-decoration: none; border-radius: 0.3rem; font-size: 0.85rem;">Bekijk review</a>
          </div>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(similar_old, similar_new)

# Sticky CTA
sticky_old = '''  <div class="sticky-cta" style="background:white;padding:12px 16px;box-shadow:0 -4px 12px rgba(0,0,0,0.15);border-top:1px solid #e5e7eb;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;">
      <div>
        <p style="margin:0;font-size:14px;font-weight:600;color:#1f2937;">Bialetti Moka Express Review 2025</p>
        <p style="margin:0;font-size:12px;color:#6b7280;">&#x2713; Prijs vandaag geverifieerd</p>
      </div>
      <div style="text-align:right;">
        <p style="margin:0;font-size:16px;font-weight:700;">&#x20AC;15&#x2013;35</p>
        <p style="margin:0;font-size:12px;color:#22c55e;">&#x2713; Op voorraad</p>
      </div>
    </div>
    <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored" class="btn btn-primary" style="width:100%;justify-content:center;">Bekijk bij Bol.com &#x2192;</a>
  </div>'''

sticky_new = '''  <div class="sticky-cta" style="background: white; padding: 12px 16px; box-shadow: 0 -4px 12px rgba(0,0,0,0.15); border-top: 1px solid var(--border);">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
      <div>
        <p style="margin: 0; font-size: 14px; font-weight: 600; color: var(--text);">Bialetti Moka Express Review 2025</p>
        <p style="margin: 0; font-size: 12px; color: var(--text-dim);">Prijs vandaag geverifieerd</p>
      </div>
      <div style="text-align: right;">
        <p style="margin: 0; font-size: 16px; font-weight: 700; color: var(--text);">€15–35</p>
        <p style="margin: 0; font-size: 12px; color: #22c55e;">Op voorraad</p>
      </div>
    </div>
    <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored" style="display: block; width: 100%; background: var(--coffee); color: white; padding: 0.75rem; text-decoration: none; font-weight: 600; text-align: center; border-radius: 0.3rem;">Bekijk bij Bol.com →</a>
  </div>'''

content = content.replace(sticky_old, sticky_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Review page completely rewritten with editorial style")
