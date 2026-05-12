#!/usr/bin/env python3
"""
Rewrite koopgids/index.html with editorial style.
"""

import re

filepath = '/Users/marc/Desktop/italiaanse-percolator/koopgids/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix malformed CSS
content = re.sub(r'border: 1px solid var\(--border\);\s*\.5rem;', 'border: 1px solid var(--border); border-radius: 0.5rem;', content)
content = re.sub(r'font-size: 0\.75rem;\s*padding: 0\.2rem 0\.6rem;\s*\.2rem;', '', content)
content = re.sub(r'background: #f5f0ea; font-size: 0\.75rem; padding: 0\.2rem 0\.6rem; \.2rem;', '', content)
content = re.sub(r'\.2rem;', '', content)
content = re.sub(r'%;', '', content)
content = re.sub(r'\.3rem;', '', content)

# Introduction section - already good, just ensure editorial style
intro_old = '''  <!-- Introduction -->
  <section class="section-sm">
    <div class="container">
      <div style="max-width: 800px; margin: 0 auto;">
        <p style="font-size: 1.1rem; line-height: 1.7; margin-bottom: var(--sp-4); color: var(--text);">Een Italiaanse percolator is eenvoudig, betaalbaar en levert een koffie die rijk is aan smaak en traditie. Maar het juiste model kiezen is niet altijd evident: aluminium of roestvrij staal? Inductie of niet? Hoe onderhoud je het toestel zonder de smaak te beïnvloeden?</p>
        
        <p style="font-size: 1.1rem; line-height: 1.7; color: var(--text);">Op deze pagina vind je een overzicht van alles wat wij geleerd hebben na jaren van testen en vergelijken. Van materiaalkeuzе tot onderhoudstips: alle informatie die je nodig hebt om de perfecte percolator te vinden.</p>
      </div>
    </div>
  </section>'''

intro_new = '''  <!-- Introduction -->
  <section style="padding: 3rem 0;">
    <div class="container">
      <div style="max-width: 800px; margin: 0 auto;">
        <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-dim);">Een Italiaanse percolator is eenvoudig, betaalbaar en levert een koffie die rijk is aan smaak en traditie. Maar het juiste model kiezen is niet altijd evident: aluminium of roestvrij staal? Inductie of niet? Hoe onderhoud je het toestel zonder de smaak te beïnvloeden?</p>
        
        <p style="font-size: 1rem; line-height: 1.8; color: var(--text-dim);">Op deze pagina vind je een overzicht van alles wat wij geleerd hebben na jaren van testen en vergelijken. Van materiaalkeuzе tot onderhoudstips: alle informatie die je nodig hebt om de perfecte percolator te vinden.</p>
      </div>
    </div>
  </section>'''

content = content.replace(intro_old, intro_new)

# "Onze aanpak" section
aanpak_old = '''  <!-- Onze aanpak -->
  <section class="section-sm" style="background: var(--surface-soft);">
    <div class="container">
      <div class="grid" style="grid-template-columns: 1fr 300px; gap: var(--sp-8); align-items: center;">
        <div>
          <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: var(--sp-4);">Hoe wij percolators testen en beoordelen</h2>
          
          <p class="text-dim mb-4" style="font-size: 1.1rem; line-height: 1.6;">Wij testen elk model op vier belangrijke punten:</p>
          
          <div style="margin-bottom: var(--sp-6);">
            <div style="display: flex; align-items: flex-start; margin-bottom: var(--sp-3);">
              <div style="width: 8px; height: 8px; background: var(--coffee); %; margin-top: 8px; margin-right: var(--sp-3); flex-shrink: 0;"></div>
              <div>
                <strong>Gebruiksgemak</strong>: hoe praktisch is de percolator in het dagelijks gebruik?
              </div>
            </div>
            <div style="display: flex; align-items: flex-start; margin-bottom: var(--sp-3);">
              <div style="width: 8px; height: 8px; background: var(--coffee); %; margin-top: 8px; margin-right: var(--sp-3); flex-shrink: 0;"></div>
              <div>
                <strong>Smaak</strong>: levert hij een volle, aromatische koffie op?
              </div>
            </div>
            <div style="display: flex; align-items: flex-start; margin-bottom: var(--sp-3);">
              <div style="width: 8px; height: 8px; background: var(--coffee); %; margin-top: 8px; margin-right: var(--sp-3); flex-shrink: 0;"></div>
              <div>
                <strong>Onderhoud</strong>: is het schoonmaken eenvoudig en duurzaam?
              </div>
            </div>
            <div style="display: flex; align-items: flex-start; margin-bottom: var(--sp-3);">
              <div style="width: 8px; height: 8px; background: var(--coffee); %; margin-top: 8px; margin-right: var(--sp-3); flex-shrink: 0;"></div>
              <div>
                <strong>Prijs-kwaliteit</strong>: krijg je echt waar voor je geld?
              </div>
            </div>
          </div>
          
          <p style="font-size: 1rem; color: var(--text-dim); line-height: 1.6; margin-bottom: var(--sp-4);">Elk model wordt minstens één maand gebruikt voordat het in onze vergelijking verschijnt.</p>
          
          <p style="font-size: 1rem; font-weight: 600; color: var(--text);">Geen gesponsorde merken, geen verborgen links. Alleen onze eigen ervaring.</p>
        </div>
        
        <div>
          <img src="../Images/percolator-testen.png" alt="Hoe wij percolators testen" style="width: 100%; border-radius: var(--r-lg); ">
        </div>
      </div>
    </div>
  </section>'''

aanpak_new = '''  <!-- Onze aanpak -->
  <section style="background: #fafafa; padding: 3rem 0;">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 300px; gap: 3rem; align-items: center; max-width: 1000px; margin: 0 auto;">
        <div>
          <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1.5rem; color: var(--coffee);">Hoe wij percolators testen en beoordelen</h2>
          
          <p style="font-size: 1rem; line-height: 1.8; color: var(--text-dim); margin-bottom: 1.5rem;">Wij testen elk model op vier belangrijke punten:</p>
          
          <div style="margin-bottom: 2rem;">
            <div style="display: flex; align-items: flex-start; margin-bottom: 1rem;">
              <div style="width: 8px; height: 8px; background: var(--coffee); margin-top: 8px; margin-right: 1rem; flex-shrink: 0; border-radius: 50%;"></div>
              <div style="color: var(--text-light); font-size: 0.95rem;">
                <strong style="color: var(--text);">Gebruiksgemak</strong>: hoe praktisch is de percolator in het dagelijks gebruik?
              </div>
            </div>
            <div style="display: flex; align-items: flex-start; margin-bottom: 1rem;">
              <div style="width: 8px; height: 8px; background: var(--coffee); margin-top: 8px; margin-right: 1rem; flex-shrink: 0; border-radius: 50%;"></div>
              <div style="color: var(--text-light); font-size: 0.95rem;">
                <strong style="color: var(--text);">Smaak</strong>: levert hij een volle, aromatische koffie op?
              </div>
            </div>
            <div style="display: flex; align-items: flex-start; margin-bottom: 1rem;">
              <div style="width: 8px; height: 8px; background: var(--coffee); margin-top: 8px; margin-right: 1rem; flex-shrink: 0; border-radius: 50%;"></div>
              <div style="color: var(--text-light); font-size: 0.95rem;">
                <strong style="color: var(--text);">Onderhoud</strong>: is het schoonmaken eenvoudig en duurzaam?
              </div>
            </div>
            <div style="display: flex; align-items: flex-start;">
              <div style="width: 8px; height: 8px; background: var(--coffee); margin-top: 8px; margin-right: 1rem; flex-shrink: 0; border-radius: 50%;"></div>
              <div style="color: var(--text-light); font-size: 0.95rem;">
                <strong style="color: var(--text);">Prijs-kwaliteit</strong>: krijg je echt waar voor je geld?
              </div>
            </div>
          </div>
          
          <p style="font-size: 0.95rem; color: var(--text-dim); line-height: 1.8; margin-bottom: 1.5rem;">Elk model wordt minstens één maand gebruikt voordat het in onze vergelijking verschijnt.</p>
          
          <p style="font-size: 0.95rem; font-weight: 600; color: var(--text);">Geen gesponsorde merken, geen verborgen links. Alleen onze eigen ervaring.</p>
        </div>
        
        <div>
          <img src="../Images/percolator-testen.png" alt="Hoe wij percolators testen" style="width: 100%; border-radius: 0.5rem;">
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(aanpak_old, aanpak_new)

# Thematic guides section header
guides_header_old = '''  <!-- Onze thematische gidsen -->
  <section class="section">
    <div class="container">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: var(--sp-4); text-align: center;">Onze thematische gidsen</h2>
      
      <div style="max-width: 800px; margin: 0 auto; margin-bottom: var(--sp-8);">
        <p style="font-size: 1.1rem; line-height: 1.6; color: var(--text-dim);">Wil je gewoon beter begrijpen hoe percolators werken? Of ben je op zoek naar onderhoudstips? Hieronder vind je onze meest gelezen gidsen, elk gericht op een concreet thema.</p>
      </div>'''

guides_header_new = '''  <!-- Onze thematische gidsen -->
  <section style="padding: 3rem 0;">
    <div class="container">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1rem; text-align: center; color: var(--coffee);">Onze thematische gidsen</h2>
      
      <div style="max-width: 800px; margin: 0 auto; margin-bottom: 2.5rem;">
        <p style="font-size: 1rem; line-height: 1.8; color: var(--text-dim); text-align: center;">Wil je gewoon beter begrijpen hoe percolators werken? Of ben je op zoek naar onderhoudstips? Hieronder vind je onze meest gelezen gidsen, elk gericht op een concreet thema.</p>
      </div>'''

content = content.replace(guides_header_old, guides_header_new)

# Guide card pattern - rewrite all 6 guide cards
guide_card_old = '''        <!-- Guide 1 -->
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;" style="padding: var(--sp-6); border-radius: var(--r-lg); ">
          <div class="grid" style="grid-template-columns: 200px 1fr; gap: var(--sp-6); align-items: center;">
            <div>
              <img src="../Images/percolator-kiezen.png" alt="Hoe kies je de juiste percolator" style="width: 100%; border-radius: var(--r-md);">
            </div>
            <div>
              <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: var(--sp-3);">Hoe kies je de juiste percolator</h2>
              <p class="text-dim mb-4">Van materiaal tot grootte, van budget tot kookplaat: alle factoren die je moet overwegen voor de perfecte keuze. We bespreken de voor- en nadelen van aluminium versus roestvrij staal, welke maten het beste werken voor verschillende huishoudens, en hoe je budget optimaal inzet. Ook krijg je praktische tips over inductiegeschiktheid en duurzaamheid.</p>
              <div class="mb-4" style="display: flex; gap: var(--sp-2);">
                <span style="background: var(--surface-soft); padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem; color: var(--text-dim);">15 min lezen</span>
                <span style="background: var(--coffee); color: white; padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem;">Beginner vriendelijk</span>
              </div>
              <a href="hoe-kies-je-de-juiste-percolator.html" class="btn btn-outline">Lees de gids →</a>
            </div>
          </div>
        </div>'''

guide_card_new = '''        <!-- Guide 1 -->
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
          <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1.5rem; align-items: center;">
            <div>
              <img src="../Images/percolator-kiezen.png" alt="Hoe kies je de juiste percolator" style="width: 100%; border-radius: 0.5rem;">
            </div>
            <div>
              <h2 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; color: var(--text);">Hoe kies je de juiste percolator</h2>
              <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Van materiaal tot grootte, van budget tot kookplaat: alle factoren die je moet overwegen voor de perfecte keuze. We bespreken de voor- en nadelen van aluminium versus roestvrij staal, welke maten het beste werken voor verschillende huishoudens, en hoe je budget optimaal inzet. Ook krijg je praktische tips over inductiegeschiktheid en duurzaamheid.</p>
              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="background: #fafafa; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem; color: var(--text-dim);">15 min lezen</span>
                <span style="background: var(--coffee); color: white; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem;">Beginner vriendelijk</span>
              </div>
              <a href="hoe-kies-je-de-juiste-percolator.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Lees de gids →</a>
            </div>
          </div>
        </div>'''

content = content.replace(guide_card_old, guide_card_new)

# Guide 2
guide2_old = '''        <!-- Guide 2 -->
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;" style="padding: var(--sp-6); border-radius: var(--r-lg); ">
          <div class="grid" style="grid-template-columns: 200px 1fr; gap: var(--sp-6); align-items: center;">
            <div>
              <img src="../Images/percolator-reinigen.png" alt="Onderhoud en reiniging" style="width: 100%; border-radius: var(--r-md);">
            </div>
            <div>
              <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: var(--sp-3);">Onderhoud en reiniging</h2>
              <p class="text-dim mb-4">Zo houd je je percolator jarenlang in topconditie en behoud je de beste koffiesmaak. Van dagelijkse reiniging tot ontkalken. Leer waarom je nooit zeep moet gebruiken, hoe je kalkafzetting voorkomt, en welke natuurlijke reinigingsmiddelen wel werken. Plus een stap-voor-stap onderhoudsschema dat je koffie altijd perfect houdt.</p>
              <div class="mb-4" style="display: flex; gap: var(--sp-2);">
                <span style="background: var(--surface-soft); padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem; color: var(--text-dim);">12 min lezen</span>
                <span style="background: var(--sage); color: white; padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem;">Praktische tips</span>
              </div>
              <a href="hoe-onderhoud-je-een-percolator.html" class="btn btn-outline">Lees de gids →</a>
            </div>
          </div>
        </div>'''

guide2_new = '''        <!-- Guide 2 -->
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
          <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1.5rem; align-items: center;">
            <div>
              <img src="../Images/percolator-reinigen.png" alt="Onderhoud en reiniging" style="width: 100%; border-radius: 0.5rem;">
            </div>
            <div>
              <h2 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; color: var(--text);">Onderhoud en reiniging</h2>
              <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Zo houd je je percolator jarenlang in topconditie en behoud je de beste koffiesmaak. Van dagelijkse reiniging tot ontkalken. Leer waarom je nooit zeep moet gebruiken, hoe je kalkafzetting voorkomt, en welke natuurlijke reinigingsmiddelen wel werken. Plus een stap-voor-stap onderhoudsschema dat je koffie altijd perfect houdt.</p>
              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="background: #fafafa; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem; color: var(--text-dim);">12 min lezen</span>
                <span style="background: #8fa87a; color: white; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem;">Praktische tips</span>
              </div>
              <a href="hoe-onderhoud-je-een-percolator.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Lees de gids →</a>
            </div>
          </div>
        </div>'''

content = content.replace(guide2_old, guide2_new)

# Guide 3
guide3_old = '''        <!-- Guide 3 -->
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;" style="padding: var(--sp-6); border-radius: var(--r-lg); ">
          <div class="grid" style="grid-template-columns: 200px 1fr; gap: var(--sp-6); align-items: center;">
            <div>
              <img src="../Images/percolator-espressoapparaat.png" alt="Percolator vs espresso" style="width: 100%; border-radius: var(--r-md);">
            </div>
            <div>
              <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: var(--sp-3);">Percolator vs espressoapparaat</h2>
              <p class="text-dim mb-4">Wat zijn de verschillen en welke keuze past het beste bij jouw koffieritueel? Complete vergelijking met kostenanalyse. We vergelijken smaak, gebruiksgemak, onderhoudskosten en tijdsinvestering. Ontdek wanneer een percolator de betere keuze is en in welke situaties een espressoapparaat meer zin heeft. Inclusief berekening van de totale kosten over 5 jaar.</p>
              <div class="mb-4" style="display: flex; gap: var(--sp-2);">
                <span style="background: var(--surface-soft); padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem; color: var(--text-dim);">18 min lezen</span>
                <span style="background: var(--cta); color: white; padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem;">Vergelijking</span>
              </div>
              <a href="percolator-vs-espressoapparaat.html" class="btn btn-outline">Lees de gids →</a>
            </div>
          </div>
        </div>'''

guide3_new = '''        <!-- Guide 3 -->
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
          <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1.5rem; align-items: center;">
            <div>
              <img src="../Images/percolator-espressoapparaat.png" alt="Percolator vs espresso" style="width: 100%; border-radius: 0.5rem;">
            </div>
            <div>
              <h2 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; color: var(--text);">Percolator vs espressoapparaat</h2>
              <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Wat zijn de verschillen en welke keuze past het beste bij jouw koffieritueel? Complete vergelijking met kostenanalyse. We vergelijken smaak, gebruiksgemak, onderhoudskosten en tijdsinvestering. Ontdek wanneer een percolator de betere keuze is en in welke situaties een espressoapparaat meer zin heeft. Inclusief berekening van de totale kosten over 5 jaar.</p>
              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="background: #fafafa; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem; color: var(--text-dim);">18 min lezen</span>
                <span style="background: #e67e22; color: white; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem;">Vergelijking</span>
              </div>
              <a href="percolator-vs-espressoapparaat.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Lees de gids →</a>
            </div>
          </div>
        </div>'''

content = content.replace(guide3_old, guide3_new)

# Guides 4-6 (similar pattern, with different images and content)
# Guide 4
guide4_old = '''        <!-- Guide 4 - NIEUW -->
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;" style="padding: var(--sp-6); border-radius: var(--r-lg); ">
          <div class="grid" style="grid-template-columns: 200px 1fr; gap: var(--sp-6); align-items: center;">
            <div>
              <img src="../Images/bialetti-moka-express-1.jpg" alt="Wat is een mokapot" style="width: 100%; border-radius: var(--r-md);">
            </div>
            <div>
              <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: var(--sp-3);">Wat is een Italiaanse percolator (mokapot)?</h2>
              <p class="text-dim mb-4">Ontdek wat een mokapot precies is en hoe hij werkt. Van de drie onderdelen tot het stap-voor-stap zetproces met stoomdruk. Complete uitleg met schema's en vergelijkingen tussen mokapot, filterkoffie en espresso. Begrijp waarom miljoenen Italianen elke dag voor dit iconische apparaat kiezen.</p>
              <div class="mb-4" style="display: flex; gap: var(--sp-2);">
                <span style="background: var(--surface-soft); padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem; color: var(--text-dim);">12 min lezen</span>
                <span style="background: var(--coffee); color: white; padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem;">Beginner vriendelijk</span>
              </div>
              <a href="wat-is-italiaanse-percolator-mokapot.html" class="btn btn-outline">Lees de gids →</a>
            </div>
          </div>
        </div>'''

guide4_new = '''        <!-- Guide 4 - NIEUW -->
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
          <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1.5rem; align-items: center;">
            <div>
              <img src="../Images/bialetti-moka-express-1.jpg" alt="Wat is een mokapot" style="width: 100%; border-radius: 0.5rem;">
            </div>
            <div>
              <h2 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; color: var(--text);">Wat is een Italiaanse percolator (mokapot)?</h2>
              <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Ontdek wat een mokapot precies is en hoe hij werkt. Van de drie onderdelen tot het stap-voor-stap zetproces met stoomdruk. Complete uitleg met schema's en vergelijkingen tussen mokapot, filterkoffie en espresso. Begrijp waarom miljoenen Italianen elke dag voor dit iconische apparaat kiezen.</p>
              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="background: #fafafa; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem; color: var(--text-dim);">12 min lezen</span>
                <span style="background: var(--coffee); color: white; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem;">Beginner vriendelijk</span>
              </div>
              <a href="wat-is-italiaanse-percolator-mokapot.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Lees de gids →</a>
            </div>
          </div>
        </div>'''

content = content.replace(guide4_old, guide4_new)

# Guide 5
guide5_old = '''        <!-- Guide 5 - NIEUW -->
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;" style="padding: var(--sp-6); border-radius: var(--r-lg); ">
          <div class="grid" style="grid-template-columns: 200px 1fr; gap: var(--sp-6); align-items: center;">
            <div>
              <img src="../Images/bialetti-moka-express-1.jpg" alt="Mokapot gebruiken" style="width: 100%; border-radius: var(--r-md);">
            </div>
            <div>
              <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: var(--sp-3);">Italiaanse percolator gebruiken: handleiding</h2>
              <p class="text-dim mb-4">Stap-voor-stap handleiding voor beginners: van water vullen tot het perfecte moment om van het vuur te halen. Leer hoeveel koffie je nodig hebt, welke maalgraad ideaal is, en hoe je het "klaar"-moment herkent. Inclusief troubleshooting voor veelvoorkomende problemen en praktische tips voor consistent succes.</p>
              <div class="mb-4" style="display: flex; gap: var(--sp-2);">
                <span style="background: var(--surface-soft); padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem; color: var(--text-dim);">15 min lezen</span>
                <span style="background: var(--sage); color: white; padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem;">Praktische tips</span>
              </div>
              <a href="italiaanse-percolator-gebruiken-handleiding.html" class="btn btn-outline">Lees de gids →</a>
            </div>
          </div>
        </div>'''

guide5_new = '''        <!-- Guide 5 - NIEUW -->
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
          <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1.5rem; align-items: center;">
            <div>
              <img src="../Images/bialetti-moka-express-1.jpg" alt="Mokapot gebruiken" style="width: 100%; border-radius: 0.5rem;">
            </div>
            <div>
              <h2 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; color: var(--text);">Italiaanse percolator gebruiken: handleiding</h2>
              <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Stap-voor-stap handleiding voor beginners: van water vullen tot het perfecte moment om van het vuur te halen. Leer hoeveel koffie je nodig hebt, welke maalgraad ideaal is, en hoe je het "klaar"-moment herkent. Inclusief troubleshooting voor veelvoorkomende problemen en praktische tips voor consistent succes.</p>
              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="background: #fafafa; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem; color: var(--text-dim);">15 min lezen</span>
                <span style="background: #8fa87a; color: white; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem;">Praktische tips</span>
              </div>
              <a href="italiaanse-percolator-gebruiken-handleiding.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Lees de gids →</a>
            </div>
          </div>
        </div>'''

content = content.replace(guide5_old, guide5_new)

# Guide 6
guide6_old = '''        <!-- Guide 6 - NIEUW -->
        <div class="card" style="border: 1px solid var(--border); .5rem; border: 1px solid var(--border); border-radius: 0.5rem;" style="padding: var(--sp-6); border-radius: var(--r-lg); ">
          <div class="grid" style="grid-template-columns: 200px 1fr; gap: var(--sp-6); align-items: center;">
            <div>
              <img src="../Images/bialetti-moka-express-1.jpg" alt="Beste koffiebonen voor mokapot" style="width: 100%; border-radius: var(--r-md);">
            </div>
            <div>
              <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: var(--sp-3);">Welke koffiebonen voor je mokapot?</h2>
              <p class="text-dim mb-4">Complete gids over arabica vs robusta, branding (licht/medium/donker) en de perfecte blend-verhoudingen. Ontdek welke koffie-oorsprong het beste werkt, hoe je versheid herkent, en waarom maalgraad cruciaal is. Met praktische aankooptips, merkaanbevelingen en een actieplan voor consistent lekkere mokakoffie.</p>
              <div class="mb-4" style="display: flex; gap: var(--sp-2);">
                <span style="background: var(--surface-soft); padding: 0.25rem 0.75rem; border-radius: var(--r-sm); font-size: 0.875rem; color: var(--text-dim);">18 min lezen</span>
                <span style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">Koopgids</span>
              </div>
              <a href="beste-koffiebonen-italiaanse-percolator.html" class="btn btn-outline">Lees de gids →</a>
            </div>
          </div>
        </div>'''

guide6_new = '''        <!-- Guide 6 - NIEUW -->
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
          <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1.5rem; align-items: center;">
            <div>
              <img src="../Images/bialetti-moka-express-1.jpg" alt="Beste koffiebonen voor mokapot" style="width: 100%; border-radius: 0.5rem;">
            </div>
            <div>
              <h2 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; color: var(--text);">Welke koffiebonen voor je mokapot?</h2>
              <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Complete gids over arabica vs robusta, branding (licht/medium/donker) en de perfecte blend-verhoudingen. Ontdek welke koffie-oorsprong het beste werkt, hoe je versheid herkent, en waarom maalgraad cruciaal is. Met praktische aankooptips, merkaanbevelingen en een actieplan voor consistent lekkere mokakoffie.</p>
              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="background: #fafafa; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem; color: var(--text-dim);">18 min lezen</span>
                <span style="background: #f5f0ea; padding: 0.25rem 0.75rem; border-radius: 0.3rem; font-size: 0.85rem; color: var(--text);">Koopgids</span>
              </div>
              <a href="beste-koffiebonen-italiaanse-percolator.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Lees de gids →</a>
            </div>
          </div>
        </div>'''

content = content.replace(guide6_old, guide6_new)

# Tips section
tips_old = '''  <!-- Tips & veelgemaakte fouten -->
  <section class="section-sm" style="background: rgba(245, 245, 245, 0.5);">
    <div class="container">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: var(--sp-4); text-align: center;">Handige tips om de juiste keuze te maken</h2>
      
      <div style="max-width: 800px; margin: 0 auto; margin-bottom: var(--sp-8);">
        <p style="font-size: 1.1rem; line-height: 1.6; color: var(--text-dim);">Na honderden tests zien we dat veel mensen dezelfde fouten maken bij het kiezen van een percolator. Deze snelle tips helpen je die valkuilen te vermijden.</p>
      </div>
      
      <div class="grid grid-2" style="gap: var(--sp-6);">
        <div style="background: white; padding: var(--sp-4); border-radius: var(--r-md); border: 1px solid rgba(0,0,0,0.1);">
          <h4 style="font-weight: 600; margin-bottom: var(--sp-2);">Kookplaat check</h4>
          <p class="text-dim">Heb je inductie? Kies dan voor RVS modellen zoals de Bialetti Venus. Aluminium werkt niet op inductie maar is wel lichter en goedkoper.</p>
        </div>
        
        <div style="background: white; padding: var(--sp-4); border-radius: var(--r-md); border: 1px solid rgba(0,0,0,0.1);">
          <h4 style="font-weight: 600; margin-bottom: var(--sp-2);">Juiste maat</h4>
          <p class="text-dim">3 kopjes voor koppels, 6 kopjes voor gezinnen. Percolators werken het beste vol gevuld. Een te grote percolator geeft zwakkere koffie bij klein gebruik.</p>
        </div>
        
        <div style="background: white; padding: var(--sp-4); border-radius: var(--r-md); border: 1px solid rgba(0,0,0,0.1);">
          <h4 style="font-weight: 600; margin-bottom: var(--sp-2);">Budget tip</h4>
          <p class="text-dim">Tussen €35 en €50 vind je al uitstekende modellen die jaren meegaan. Duurdere modellen bieden vaak betere afwerking maar niet per se betere koffie.</p>
        </div>
        
        <div style="background: white; padding: var(--sp-4); border-radius: var(--r-md); border: 1px solid rgba(0,0,0,0.1);">
          <h4 style="font-weight: 600; margin-bottom: var(--sp-2);">Schoonmaak tip</h4>
          <p class="text-dim">Gebruik nooit afwasmiddel. Alleen warm water en natuurlijke reinigingsmiddelen. Zeep laat een smaak achter die je koffie kan beïnvloeden.</p>
        </div>
      </div>
    </div>
  </section>'''

tips_new = '''  <!-- Tips & veelgemaakte fouten -->
  <section style="background: #fafafa; padding: 3rem 0;">
    <div class="container">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1rem; text-align: center; color: var(--coffee);">Handige tips om de juiste keuze te maken</h2>
      
      <div style="max-width: 800px; margin: 0 auto; margin-bottom: 2rem;">
        <p style="font-size: 1rem; line-height: 1.8; color: var(--text-dim);">Na honderden tests zien we dat veel mensen dezelfde fouten maken bij het kiezen van een percolator. Deze snelle tips helpen je die valkuilen te vermijden.</p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; border: 1px solid var(--border);">
          <h4 style="font-weight: 600; margin-bottom: 0.75rem; color: var(--text);">Kookplaat check</h4>
          <p style="color: var(--text-dim); line-height: 1.7; font-size: 0.9rem;">Heb je inductie? Kies dan voor RVS modellen zoals de Bialetti Venus. Aluminium werkt niet op inductie maar is wel lichter en goedkoper.</p>
        </div>
        
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; border: 1px solid var(--border);">
          <h4 style="font-weight: 600; margin-bottom: 0.75rem; color: var(--text);">Juiste maat</h4>
          <p style="color: var(--text-dim); line-height: 1.7; font-size: 0.9rem;">3 kopjes voor koppels, 6 kopjes voor gezinnen. Percolators werken het beste vol gevuld. Een te grote percolator geeft zwakkere koffie bij klein gebruik.</p>
        </div>
        
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; border: 1px solid var(--border);">
          <h4 style="font-weight: 600; margin-bottom: 0.75rem; color: var(--text);">Budget tip</h4>
          <p style="color: var(--text-dim); line-height: 1.7; font-size: 0.9rem;">Tussen €35 en €50 vind je al uitstekende modellen die jaren meegaan. Duurdere modellen bieden vaak betere afwerking maar niet per se betere koffie.</p>
        </div>
        
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; border: 1px solid var(--border);">
          <h4 style="font-weight: 600; margin-bottom: 0.75rem; color: var(--text);">Schoonmaak tip</h4>
          <p style="color: var(--text-dim); line-height: 1.7; font-size: 0.9rem;">Gebruik nooit afwasmiddel. Alleen warm water en natuurlijke reinigingsmiddelen. Zeep laat een smaak achter die je koffie kan beïnvloeden.</p>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(tips_old, tips_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# FAQ section
faq_old = '''  <!-- Veelgestelde vragen -->
  <section class="section">
    <div class="container">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: var(--sp-4); text-align: center;">Veelgestelde vragen over percolators</h2>
      
      <div style="max-width: 800px; margin: 0 auto; margin-bottom: var(--sp-8);">
        <p style="font-size: 1.1rem; line-height: 1.6; color: var(--text-dim);">We krijgen vaak dezelfde vragen van lezers die net beginnen met slow coffee. Hier beantwoorden we de meest voorkomende, kort en duidelijk, zonder technische woorden.</p>
      </div>
      
      <div style="max-width: 800px; margin: 0 auto;">
        <div style="border: 1px solid rgba(0,0,0,0.1); border-radius: var(--r-md); margin-bottom: var(--sp-4); border: 1px solid var(--border); border-radius: 0.5rem;">
          <button class="faq-question" style="width: 100%; padding: var(--sp-4); text-align: left; background: none; border: none; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; border: 1px solid var(--border); border-radius: 0.5rem;">
            Wat is het verschil tussen een percolator en een espressoapparaat?
            <span style="font-size: 1.2rem;">+</span>
          </button>
          <div class="faq-answer" style="display: none; padding: 0 var(--sp-4) var(--sp-4) var(--sp-4); border-top: 1px solid rgba(0,0,0,0.1);">
            <p class="text-dim">Een percolator gebruikt stoomdruk om water door koffie te persen, terwijl een espressoapparaat veel hogere druk gebruikt. Percolators zijn eenvoudiger, goedkoper en maken mildere koffie. Espressoapparaten maken intensere koffie en kunnen melkdranken maken, maar zijn complexer en duurder.</p>
          </div>
        </div>
        
        <div style="border: 1px solid rgba(0,0,0,0.1); border-radius: var(--r-md); margin-bottom: var(--sp-4); border: 1px solid var(--border); border-radius: 0.5rem;">
          <button class="faq-question" style="width: 100%; padding: var(--sp-4); text-align: left; background: none; border: none; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; border: 1px solid var(--border); border-radius: 0.5rem;">
            Welk materiaal is beter: aluminium of roestvrij staal?
            <span style="font-size: 1.2rem;">+</span>
          </button>
          <div class="faq-answer" style="display: none; padding: 0 var(--sp-4) var(--sp-4) var(--sp-4); border-top: 1px solid rgba(0,0,0,0.1);">
            <p class="text-dim">Beide hebben voordelen. Aluminium is lichter, goedkoper en warmt sneller op, maar werkt niet op inductie. RVS is duurzamer, inductiegeschikt en makkelijker schoon te maken, maar duurder en zwaarder. Voor smaak maakt het weinig verschil.</p>
          </div>
        </div>
        
        <div style="border: 1px solid rgba(0,0,0,0.1); border-radius: var(--r-md); margin-bottom: var(--sp-4); border: 1px solid var(--border); border-radius: 0.5rem;">
          <button class="faq-question" style="width: 100%; padding: var(--sp-4); text-align: left; background: none; border: none; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; border: 1px solid var(--border); border-radius: 0.5rem;">
            Hoe vaak moet ik mijn percolator schoonmaken?
            <span style="font-size: 1.2rem;">+</span>
          </button>
          <div class="faq-answer" style="display: none; padding: 0 var(--sp-4) var(--sp-4) var(--sp-4); border-top: 1px solid rgba(0,0,0,0.1);">
            <p class="text-dim">Na elk gebruik spoelen met warm water. Wekelijks een grondige reiniging met alle onderdelen uit elkaar. Maandelijks ontkalken met azijn. Gebruik nooit zeep of afwasmiddel.</p>
          </div>
        </div>
        
        <div style="border: 1px solid rgba(0,0,0,0.1); border-radius: var(--r-md); margin-bottom: var(--sp-4); border: 1px solid var(--border); border-radius: 0.5rem;">
          <button class="faq-question" style="width: 100%; padding: var(--sp-4); text-align: left; background: none; border: none; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; border: 1px solid var(--border); border-radius: 0.5rem;">
            Welke maat percolator moet ik kiezen?
            <span style="font-size: 1.2rem;">+</span>
          </button>
          <div class="faq-answer" style="display: none; padding: 0 var(--sp-4) var(--sp-4) var(--sp-4); border-top: 1px solid rgba(0,0,0,0.1);">
            <p class="text-dim">Kies op basis van je dagelijkse consumptie: 3 kopjes voor 1-2 personen, 6 kopjes voor gezinnen. Percolators werken het beste wanneer ze vol gevuld worden, dus kies liever niet te groot.</p>
          </div>
        </div>
      </div>
    </div>
  </section>'''

faq_new = '''  <!-- Veelgestelde vragen -->
  <section style="padding: 3rem 0;">
    <div class="container">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1rem; text-align: center; color: var(--coffee);">Veelgestelde vragen over percolators</h2>
      
      <div style="max-width: 800px; margin: 0 auto; margin-bottom: 2rem;">
        <p style="font-size: 1rem; line-height: 1.8; color: var(--text-dim);">We krijgen vaak dezelfde vragen van lezers die net beginnen met slow coffee. Hier beantwoorden we de meest voorkomende, kort en duidelijk, zonder technische woorden.</p>
      </div>
      
      <div style="max-width: 800px; margin: 0 auto;">
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; margin-bottom: 1rem; overflow: hidden; background: white;">
          <button class="faq-question" style="width: 100%; padding: 1.25rem; text-align: left; background: none; border: none; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--text);">
            Wat is het verschil tussen een percolator en een espressoapparaat?
            <span style="font-size: 1.2rem; color: var(--coffee);">+</span>
          </button>
          <div class="faq-answer" style="display: none; padding: 0 1.25rem 1.25rem 1.25rem; border-top: 1px solid var(--border); color: var(--text-light); line-height: 1.7; font-size: 0.9rem;">
            Een percolator gebruikt stoomdruk om water door koffie te persen, terwijl een espressoapparaat veel hogere druk gebruikt. Percolators zijn eenvoudiger, goedkoper en maken mildere koffie. Espressoapparaten maken intensere koffie en kunnen melkdranken maken, maar zijn complexer en duurder.
          </div>
        </div>
        
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; margin-bottom: 1rem; overflow: hidden; background: white;">
          <button class="faq-question" style="width: 100%; padding: 1.25rem; text-align: left; background: none; border: none; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--text);">
            Welk materiaal is beter: aluminium of roestvrij staal?
            <span style="font-size: 1.2rem; color: var(--coffee);">+</span>
          </button>
          <div class="faq-answer" style="display: none; padding: 0 1.25rem 1.25rem 1.25rem; border-top: 1px solid var(--border); color: var(--text-light); line-height: 1.7; font-size: 0.9rem;">
            Beide hebben voordelen. Aluminium is lichter, goedkoper en warmt sneller op, maar werkt niet op inductie. RVS is duurzamer, inductiegeschikt en makkelijker schoon te maken, maar duurder en zwaarder. Voor smaak maakt het weinig verschil.
          </div>
        </div>
        
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; margin-bottom: 1rem; overflow: hidden; background: white;">
          <button class="faq-question" style="width: 100%; padding: 1.25rem; text-align: left; background: none; border: none; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--text);">
            Hoe vaak moet ik mijn percolator schoonmaken?
            <span style="font-size: 1.2rem; color: var(--coffee);">+</span>
          </button>
          <div class="faq-answer" style="display: none; padding: 0 1.25rem 1.25rem 1.25rem; border-top: 1px solid var(--border); color: var(--text-light); line-height: 1.7; font-size: 0.9rem;">
            Na elk gebruik spoelen met warm water. Wekelijks een grondige reiniging met alle onderdelen uit elkaar. Maandelijks ontkalken met azijn. Gebruik nooit zeep of afwasmiddel.
          </div>
        </div>
        
        <div style="border: 1px solid var(--border); border-radius: 0.5rem; overflow: hidden; background: white;">
          <button class="faq-question" style="width: 100%; padding: 1.25rem; text-align: left; background: none; border: none; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--text);">
            Welke maat percolator moet ik kiezen?
            <span style="font-size: 1.2rem; color: var(--coffee);">+</span>
          </button>
          <div class="faq-answer" style="display: none; padding: 0 1.25rem 1.25rem 1.25rem; border-top: 1px solid var(--border); color: var(--text-light); line-height: 1.7; font-size: 0.9rem;">
            Kies op basis van je dagelijkse consumptie: 3 kopjes voor 1-2 personen, 6 kopjes voor gezinnen. Percolators werken het beste wanneer ze vol gevuld worden, dus kies liever niet te groot.
          </div>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(faq_old, faq_new)

# Related content section
related_old = '''  <!-- Gerelateerde content -->
  <section class="section-sm" style="background: var(--surface-soft);">
    <div class="container">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: var(--sp-4); text-align: center;">Klaar om verder te lezen?</h2>
      
      <div style="max-width: 800px; margin: 0 auto; margin-bottom: var(--sp-8);">
        <p style="font-size: 1.1rem; line-height: 1.6; color: var(--text-dim); text-align: center;">Ontdek onze nieuwste tests en vergelijkingen, of leer meer over ons proces.</p>
      </div>
      
      <div class="grid grid-3" style="gap: var(--sp-6);">
        <div style="background: white; padding: var(--sp-6); border-radius: var(--r-lg); border: 1px solid rgba(0,0,0,0.1); text-align: center; border: 1px solid var(--border); border-radius: 0.5rem;">
          <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: var(--sp-3);">Top 10 Reviews</h3>
          <p class="text-dim mb-4">Bekijk onze uitgebreide tests van de beste percolators van 2025.</p>
          <a href="../beste-italiaanse-percolators.html" class="btn btn-outline">Bekijk reviews →</a>
        </div>
        
        <div style="background: white; padding: var(--sp-6); border-radius: var(--r-lg); border: 1px solid rgba(0,0,0,0.1); text-align: center; border: 1px solid var(--border); border-radius: 0.5rem;">
          <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: var(--sp-3);">Merk Vergelijkingen</h3>
          <p class="text-dim mb-4">Bialetti vs Alessi en andere directe vergelijkingen tussen merken.</p>
          <a href="../vergelijking/index.html" class="btn btn-outline">Bekijk vergelijkingen →</a>
        </div>
        
        <div style="background: white; padding: var(--sp-6); border-radius: var(--r-lg); border: 1px solid rgba(0,0,0,0.1); text-align: center; border: 1px solid var(--border); border-radius: 0.5rem;">
          <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: var(--sp-3);">Over Ons</h3>
          <p class="text-dim mb-4">Leer meer over ons testproces en waarom je ons kunt vertrouwen.</p>
          <a href="../over-ons.html" class="btn btn-outline">Lees meer →</a>
        </div>
      </div>
    </div>
  </section>'''

related_new = '''  <!-- Gerelateerde content -->
  <section style="background: #fafafa; padding: 3rem 0;">
    <div class="container">
      <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1rem; text-align: center; color: var(--coffee);">Klaar om verder te lezen?</h2>
      
      <div style="max-width: 800px; margin: 0 auto; margin-bottom: 2rem;">
        <p style="font-size: 1rem; line-height: 1.8; color: var(--text-dim); text-align: center;">Ontdek onze nieuwste tests en vergelijkingen, of leer meer over ons proces.</p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem;">
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; border: 1px solid var(--border); text-align: center;">
          <h3 style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.75rem; color: var(--text);">Top 10 Reviews</h3>
          <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Bekijk onze uitgebreide tests van de beste percolators van 2025.</p>
          <a href="../beste-italiaanse-percolators.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Bekijk reviews →</a>
        </div>
        
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; border: 1px solid var(--border); text-align: center;">
          <h3 style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.75rem; color: var(--text);">Merk Vergelijkingen</h3>
          <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Bialetti vs Alessi en andere directe vergelijkingen tussen merken.</p>
          <a href="../vergelijking/index.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Bekijk vergelijkingen →</a>
        </div>
        
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; border: 1px solid var(--border); text-align: center;">
          <h3 style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.75rem; color: var(--text);">Over Ons</h3>
          <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 1rem; font-size: 0.9rem;">Leer meer over ons testproces en waarom je ons kunt vertrouwen.</p>
          <a href="../over-ons.html" style="border: 1px solid var(--coffee); padding: 0.5rem 1rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; color: var(--text); font-size: 0.9rem;">Lees meer →</a>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(related_old, related_new)

# Final CTA section
cta_old = '''  <!-- Klaar om jouw perfecte percolator te vinden? -->
  <section class="section" style="background: rgba(210, 105, 30, 0.05);">
    <div class="container text-center">
      <div style="max-width: 650px; margin: 0 auto;">
        <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: var(--sp-4);">Klaar om jouw perfecte percolator te vinden?</h2>
        <p style="font-size: 1.1rem; color: var(--text-dim); margin-bottom: var(--sp-6); line-height: 1.6;">Ontdek onze actuele aanbevelingen en bekijk welke modellen dit jaar het beste scoren. Van budget-vriendelijk tot premium: er is voor ieder wat wils.</p>
        <a href="../beste-italiaanse-percolators.html" class="btn btn-primary btn-lg" style="background: var(--coffee); color: white; border: none; padding: 0.6rem 1.2rem; .3rem; font-weight: 600; border: 1px solid var(--border); border-radius: 0.5rem;">Bekijk de Top 10 →</a>
      </div>
    </div>
  </section>'''

cta_new = '''  <!-- Klaar om jouw perfecte percolator te vinden? -->
  <section style="background: #f5f0ea; padding: 3rem 0;">
    <div class="container" style="text-align: center;">
      <div style="max-width: 650px; margin: 0 auto;">
        <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1rem; color: var(--coffee);">Klaar om jouw perfecte percolator te vinden?</h2>
        <p style="font-size: 1rem; color: var(--text-dim); margin-bottom: 2rem; line-height: 1.8;">Ontdek onze actuele aanbevelingen en bekijk welke modellen dit jaar het beste scoren. Van budget-vriendelijk tot premium: er is voor ieder wat wils.</p>
        <a href="../beste-italiaanse-percolators.html" style="background: var(--coffee); color: white; padding: 0.75rem 2rem; text-decoration: none; font-weight: 600; border-radius: 0.3rem; display: inline-block;">Bekijk de Top 10 →</a>
      </div>
    </div>
  </section>'''

content = content.replace(cta_old, cta_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Koopgids page completely rewritten with editorial style")
