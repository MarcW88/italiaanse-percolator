#!/usr/bin/env python3
"""
Finish rewriting Bialetti brand page sections 4, 5, 6 with editorial style.
"""

import re

filepath = '/Users/marc/Desktop/italiaanse-percolator/marques/bialetti/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix malformed CSS from deep_clean
content = re.sub(r'font-size:\s*0\.75rem;\s*padding:\s*0\.2rem\s*0\.6rem;\s*\.2rem;', '', content)
content = re.sub(r'padding:\s*0\.2rem\s*0\.6rem;\s*\.2rem;', '', content)
content = re.sub(r'\.2rem;', '', content)

# SECTION 4: Editorial style
section4_old = '''    <!-- SECTION 4: Why Bialetti - Expanded (Deep Value Proposition) -->
    <section class="section">
        <div class="container">
            <div style="max-width: 900px; margin: 0 auto;">
                <h2 style="margin-bottom: 1.5rem;">Waarom Bialetti de Nummer 1 Keuze is: Meer dan alleen Traditie</h2>

                <div style="display: grid; grid-template-columns: 1fr; gap: 2rem;">
                    <div style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
                        <h3 style="margin-bottom: 1rem;">Het Ultieme Bewijs: 300+ Miljoen Verkocht</h3>
                        <p style="color: #555; line-height: 1.8;">
                            Meer dan 300 miljoen Bialetti-percolators zijn wereldwijd verkocht. Dit is niet zomaar een getal – het betekent dat <strong>meer dan 1 miljard mensen dagelijks</strong> Bialetti gebruiken. Als Bialetti slecht was, zouden die nummers niet bestaan.
                        </p>
                    </div>

                    <!-- Advantage Grid -->
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                        <div>
                            <h3 style="margin-bottom: 1rem;">Perfecte Extractie</h3>
                            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
                                De unieke driekleppige design zorgt voor <strong>optimale watertemperatuur en druk</strong>. Resultaat: rijke, complexe koffie met perfecte balans tussen body en aroma. Niet zuur, niet bitter – gewoon perfect.
                            </p>
                            <p style="color: #555; line-height: 1.8;">
                                <strong>Vergelijk met:</strong> Goedkope generieke percolators hebben slechte extractie, leading to zure of over-geëxtraheerde koffie.
                            </p>
                        </div>

                        <div>
                            <h3 style="margin-bottom: 1rem;">Duurzaamheid = Economie</h3>
                            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
                                Een Bialetti gaat <strong>10-20 jaar mee</strong> met minimaal onderhoud. Alleen de rubberring moet jaarlijks vervangen (€2). Dat betekent: je investeert €25-80 eenmalig en geniet jarenlang.
                            </p>
                            <p style="color: #555; line-height: 1.8;">
                                <strong>Vs espressomachine:</strong> €200+ upfront, kapotte onderdelen, regelmatig onderhoudskosten.
                            </p>
                        </div>

                        <div>
                            <h3 style="margin-bottom: 1rem;">Geen Batterijen, Geen Elektriciteit</h3>
                            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
                                Bialetti werkt op elke hittebron: gas, elektrisch, inductie (RVS modellen), zelfs kampvuur. Dat maakt het <strong>universeel, betrouwbaar en onafhankelijk</strong> van technologie.
                            </p>
                            <p style="color: #555; line-height: 1.8;">
                                <strong>Bonus:</strong> Geen "Error codes" of reparateurs nodig. Je bent zelfredzaam.
                            </p>
                        </div>

                        <div>
                            <h3 style="margin-bottom: 1rem;">Milieuvriendelijk</h3>
                            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
                                Aluminium en RVS zijn 100% herbruikbaar. Een Bialetti wordt nooit e-waste. Bovendien: geen elektriciteit verbruik, geen wegwerpkoffiefilters, enkel herbruikbare onderdelen.
                            </p>
                            <p style="color: #555; line-height: 1.8;">
                                <strong>Impact:</strong> Gemiddelde Bialetti gebruiker bespaart >500 kg wegwerp en ~1000 kWh elektriciteit in 10 jaar.
                            </p>
                        </div>
                    </div>

                    <!-- Price/Quality Table -->
                    <h3 style="margin-bottom: 1rem; margin-top: 2rem;">Prijs-Kwaliteit Vergelijking</h3>

                    <div style="overflow-x: auto;">
                        <table style="width: 100%; border-collapse: collapse;">
                            <thead>
                                <tr style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
                                    <th style="padding: 1rem; text-align: left;">Koffie-methode</th>
                                    <th style="padding: 1rem; text-align: center;">Initiële Investering</th>
                                    <th style="padding: 1rem; text-align: center;">Jaarlijks Onderhoud</th>
                                    <th style="padding: 1rem; text-align: center;">Levensduur</th>
                                    <th style="padding: 1rem; text-align: center;">Totale Kosten</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
                                    <td style="padding: 1rem;"><strong>Bialetti</strong></td>
                                    <td style="padding: 1rem; text-align: center;">€30-50</td>
                                    <td style="padding: 1rem; text-align: center;">€3</td>
                                    <td style="padding: 1rem; text-align: center;">15 jaren</td>
                                    <td style="padding: 1rem; text-align: center;">€80-95</td>
                                </tr>
                                <tr>
                                    <td style="padding: 1rem;"><strong>Espressomachine</strong></td>
                                    <td style="padding: 1rem; text-align: center;">€200-500</td>
                                    <td style="padding: 1rem; text-align: center;">€50-100</td>
                                    <td style="padding: 1rem; text-align: center;">8 jaren</td>
                                    <td style="padding: 1rem; text-align: center;">€600-1300</td>
                                </tr>
                                <tr style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
                                    <td style="padding: 1rem;"><strong>Koffiezetapparaat</strong></td>
                                    <td style="padding: 1rem; text-align: center;">€100-300</td>
                                    <td style="padding: 1rem; text-align: center;">€20-40</td>
                                    <td style="padding: 1rem; text-align: center;">5 jaren</td>
                                    <td style="padding: 1rem; text-align: center;">€200-500</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <p style="color: #555; line-height: 1.8; margin-top: 1.5rem; font-size: 0.9rem;">
                        <strong>Conclusie:</strong> Bialetti is niet alleen betaalbaarder upfront – het blijft betaalbaarder over de hele levenscyclus. En je geniet van betere koffie.
                    </p>
                </div>
            </div>
        </div>
    </section>'''

section4_new = '''    <section style="padding: 3rem 0;">
        <div class="container">
            <div style="max-width: 800px; margin: 0 auto;">
                <h2 style="font-family: var(--font-serif); font-size: 1.6rem; margin-bottom: 1.5rem; color: var(--coffee);">Waarom Bialetti de Nummer 1 Keuze is: Meer dan alleen Traditie</h2>

                <div style="display: grid; grid-template-columns: 1fr; gap: 2rem;">
                    <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: #f5f0ea;">
                        <h3 style="margin-bottom: 1rem; color: var(--coffee);">Het Ultieme Bewijs: 300+ Miljoen Verkocht</h3>
                        <p style="color: var(--text-light); line-height: 1.8;">
                            Meer dan 300 miljoen Bialetti-percolators zijn wereldwijd verkocht. Dit is niet zomaar een getal – het betekent dat <strong>meer dan 1 miljard mensen dagelijks</strong> Bialetti gebruiken. Als Bialetti slecht was, zouden die nummers niet bestaan.
                        </p>
                    </div>

                    <!-- Advantage Grid -->
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.25rem; background: white;">
                            <h3 style="margin-bottom: 0.75rem; color: var(--coffee); font-size: 1.1rem;">Perfecte Extractie</h3>
                            <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 0.75rem; font-size: 0.9rem;">
                                De unieke driekleppige design zorgt voor <strong>optimale watertemperatuur en druk</strong>. Resultaat: rijke, complexe koffie met perfecte balans tussen body en aroma. Niet zuur, niet bitter – gewoon perfect.
                            </p>
                            <p style="color: var(--text-dim); line-height: 1.7; font-size: 0.85rem;">
                                <strong>Vergelijk met:</strong> Goedkope generieke percolators hebben slechte extractie.
                            </p>
                        </div>

                        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.25rem; background: white;">
                            <h3 style="margin-bottom: 0.75rem; color: var(--coffee); font-size: 1.1rem;">Duurzaamheid = Economie</h3>
                            <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 0.75rem; font-size: 0.9rem;">
                                Een Bialetti gaat <strong>10-20 jaar mee</strong> met minimaal onderhoud. Alleen de rubberring moet jaarlijks vervangen (€2).
                            </p>
                            <p style="color: var(--text-dim); line-height: 1.7; font-size: 0.85rem;">
                                <strong>Vs espressomachine:</strong> €200+ upfront, kapotte onderdelen, regelmatig onderhoudskosten.
                            </p>
                        </div>

                        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.25rem; background: white;">
                            <h3 style="margin-bottom: 0.75rem; color: var(--coffee); font-size: 1.1rem;">Geen Elektriciteit</h3>
                            <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 0.75rem; font-size: 0.9rem;">
                                Bialetti werkt op elke hittebron: gas, elektrisch, inductie (RVS modellen), zelfs kampvuur. Dat maakt het <strong>universeel, betrouwbaar en onafhankelijk</strong> van technologie.
                            </p>
                            <p style="color: var(--text-dim); line-height: 1.7; font-size: 0.85rem;">
                                <strong>Bonus:</strong> Geen "Error codes" of reparateurs nodig. Je bent zelfredzaam.
                            </p>
                        </div>

                        <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.25rem; background: white;">
                            <h3 style="margin-bottom: 0.75rem; color: var(--coffee); font-size: 1.1rem;">Milieuvriendelijk</h3>
                            <p style="color: var(--text-dim); line-height: 1.7; margin-bottom: 0.75rem; font-size: 0.9rem;">
                                Aluminium en RVS zijn 100% herbruikbaar. Een Bialetti wordt nooit e-waste. Geen elektriciteit verbruik, geen wegwerpkoffiefilters.
                            </p>
                            <p style="color: var(--text-dim); line-height: 1.7; font-size: 0.85rem;">
                                <strong>Impact:</strong> Gemiddelde Bialetti gebruiker bespaart >500 kg wegwerp en ~1000 kWh elektriciteit in 10 jaar.
                            </p>
                        </div>
                    </div>

                    <!-- Price/Quality Table -->
                    <h3 style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 1rem; margin-top: 2.5rem; color: var(--coffee);">Prijs-Kwaliteit Vergelijking</h3>

                    <div style="overflow-x: auto;">
                        <table style="width: 100%; border-collapse: collapse; border: 1px solid var(--border); border-radius: 0.5rem; overflow: hidden;">
                            <thead>
                                <tr style="background: #f5f0ea;">
                                    <th style="padding: 1rem; text-align: left; font-size: 0.9rem;">Koffie-methode</th>
                                    <th style="padding: 1rem; text-align: center; font-size: 0.9rem;">Initiële Investering</th>
                                    <th style="padding: 1rem; text-align: center; font-size: 0.9rem;">Jaarlijks Onderhoud</th>
                                    <th style="padding: 1rem; text-align: center; font-size: 0.9rem;">Levensduur</th>
                                    <th style="padding: 1rem; text-align: center; font-size: 0.9rem;">Totale Kosten</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="background: white;">
                                    <td style="padding: 1rem;"><strong>Bialetti</strong></td>
                                    <td style="padding: 1rem; text-align: center;">€30-50</td>
                                    <td style="padding: 1rem; text-align: center;">€3</td>
                                    <td style="padding: 1rem; text-align: center;">15 jaren</td>
                                    <td style="padding: 1rem; text-align: center;">€80-95</td>
                                </tr>
                                <tr style="background: #fafafa;">
                                    <td style="padding: 1rem;"><strong>Espressomachine</strong></td>
                                    <td style="padding: 1rem; text-align: center;">€200-500</td>
                                    <td style="padding: 1rem; text-align: center;">€50-100</td>
                                    <td style="padding: 1rem; text-align: center;">8 jaren</td>
                                    <td style="padding: 1rem; text-align: center;">€600-1300</td>
                                </tr>
                                <tr style="background: white;">
                                    <td style="padding: 1rem;"><strong>Koffiezetapparaat</strong></td>
                                    <td style="padding: 1rem; text-align: center;">€100-300</td>
                                    <td style="padding: 1rem; text-align: center;">€20-40</td>
                                    <td style="padding: 1rem; text-align: center;">5 jaren</td>
                                    <td style="padding: 1rem; text-align: center;">€200-500</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <p style="color: var(--text-dim); line-height: 1.7; margin-top: 1.5rem; font-size: 0.9rem;">
                        <strong>Conclusie:</strong> Bialetti is niet alleen betaalbaarder upfront – het blijft betaalbaarder over de hele levenscyclus. En je geniet van betere koffie.
                    </p>
                </div>
            </div>
        </div>
    </section>'''

content = content.replace(section4_old, section4_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# SECTION 5: Editorial style
section5_old = '''    <!-- SECTION 5: Bialetti vs Competition - Explicit Detailed Comparison -->
    <section class="section" style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 1.5rem;">Bialetti vs De Concurrentie: Eerlijke Vergelijking</h2>

            <div style="max-width: 900px; margin: 0 auto;">
                <!-- Comparison 1: Bialetti vs Alessi -->
                <div style="background: white; padding: 2rem;  ">
                    <h3 style="margin-bottom: 1rem;">
                        Bialetti vs <a href="../alessi/" style="text-decoration: none;">Alessi</a>
                    </h3>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                        <div>
                            <h4 style="color: #333; margin-bottom: 0.75rem;">Bialetti</h4>
                            <ul style="color: #555; font-size: 0.9rem; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
                                <li>Prijs: €25-65</li>
                                <li>Design: Klassiek, proven</li>
                                <li>Prioriteit: Functie & Betaalbaarheid</li>
                                <li>Beste voor: Dagelijks gebruik</li>
                                <li>Modellen: 9 varianten</li>
                                <li>Beschikbaarheid: Overal</li>
                                <li>Koffie-kwaliteit: Uitstekend</li>
                            </ul>
                        </div>

                        <div>
                            <h4 style="color: #333; margin-bottom: 0.75rem;">Alessi</h4>
                            <ul style="color: #555; font-size: 0.9rem; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
                                <li>Prijs: €80-120</li>
                                <li>Design: Award-winning, modern</li>
                                <li>Prioriteit: Design-statement</li>
                                <li>Beste voor: Design-liefhebbers</li>
                                <li>Modellen: 1 hoofdmodel</li>
                                <li>Beschikbaarheid: Beperkt</li>
                                <li>Koffie-kwaliteit: Gelijk aan Bialetti</li>
                            </ul>
                        </div>
                    </div>

                    <div style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
                        <p style="margin: 0; color: #555; font-size: 0.9rem;">
                            <strong>Eindoordeel:</strong> Bialetti als je <strong>koffie + functie</strong> wilt. Alessi als je <strong>design-statement + koffie</strong> wilt en je budget omhoog kan. Beide maken even goede koffie.
                        </p>
                    </div>
                </div>

                <!-- Comparison 2: Bialetti vs Grosche -->
                <div style="background: white; padding: 2rem; ">
                    <h3 style="margin-bottom: 1rem;">
                        Bialetti vs <a href="../grosche/" style="text-decoration: none;">Grosche</a>
                    </h3>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                        <div>
                            <h4 style="color: #333; margin-bottom: 0.75rem;">Bialetti</h4>
                            <ul style="color: #555; font-size: 0.9rem; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
                                <li>Prijs: €25-65</li>
                                <li>Innovatie: Proven 90+ jaar</li>
                                <li>Prioriteit: Traditie & Authenticiteit</li>
                                <li>Beste voor: Italianen & nostalgici</li>
                                <li>Modellen: 9 varianten</li>
                                <li>Handvat: Basisch</li>
                                <li>Onderdelen: Overal beschikbaar</li>
                            </ul>
                        </div>

                        <div>
                            <h4 style="color: #333; margin-bottom: 0.75rem;">Grosche</h4>
                            <ul style="color: #555; font-size: 0.9rem; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
                                <li>Prijs: €35-55</li>
                                <li>Innovatie: Modern, safety-focus</li>
                                <li>Prioriteit: Comfort & Features</li>
                                <li>Beste voor: Modernisten</li>
                                <li>Modellen: 2 principale</li>
                                <li>Handvat: Ergonomisch geleid</li>
                                <li>Onderdelen: Beperkt verkrijgbaar</li>
                            </ul>
                        </div>
                    </div>

                    <div style="background: #f5f0ea; font-size: 0.75rem; padding: 0.2rem 0.6rem; .2rem;">
                        <p style="margin: 0; color: #555; font-size: 0.9rem;">
                            <strong>Eindoordeel:</strong> Bialetti voor <strong>authenticiteit, keuze en beschikbaarheid</strong>. Grosche voor <strong>ergonomie en moderne features</strong>. Keuze tussen traditioneel vs vernieuwd.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

section5_new = '''    <section style="background: #fafafa; padding: 3rem 0;">
        <div class="container">
            <h2 style="font-family: var(--font-serif); font-size: 1.6rem; text-align: center; margin-bottom: 2rem; color: var(--coffee);">Bialetti vs De Concurrentie: Eerlijke Vergelijking</h2>

            <div style="max-width: 800px; margin: 0 auto;">
                <!-- Comparison 1: Bialetti vs Alessi -->
                <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white; margin-bottom: 1.5rem;">
                    <h3 style="margin-bottom: 1.25rem; color: var(--coffee);">
                        Bialetti vs <a href="../alessi/" style="color: var(--coffee); text-decoration: none;">Alessi</a>
                    </h3>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                        <div>
                            <h4 style="color: var(--text); margin-bottom: 0.75rem; font-size: 1rem;">Bialetti</h4>
                            <ul style="color: var(--text-dim); font-size: 0.85rem; line-height: 1.7; margin: 0; padding-left: 1.25rem;">
                                <li>Prijs: €25-65</li>
                                <li>Design: Klassiek, proven</li>
                                <li>Prioriteit: Functie & Betaalbaarheid</li>
                                <li>Beste voor: Dagelijks gebruik</li>
                                <li>Modellen: 9 varianten</li>
                                <li>Beschikbaarheid: Overal</li>
                                <li>Koffie-kwaliteit: Uitstekend</li>
                            </ul>
                        </div>

                        <div>
                            <h4 style="color: var(--text); margin-bottom: 0.75rem; font-size: 1rem;">Alessi</h4>
                            <ul style="color: var(--text-dim); font-size: 0.85rem; line-height: 1.7; margin: 0; padding-left: 1.25rem;">
                                <li>Prijs: €80-120</li>
                                <li>Design: Award-winning, modern</li>
                                <li>Prioriteit: Design-statement</li>
                                <li>Beste voor: Design-liefhebbers</li>
                                <li>Modellen: 1 hoofdmodel</li>
                                <li>Beschikbaarheid: Beperkt</li>
                                <li>Koffie-kwaliteit: Gelijk aan Bialetti</li>
                            </ul>
                        </div>
                    </div>

                    <div style="background: #f5f0ea; padding: 1rem; border-radius: 0.3rem; margin-top: 1rem;">
                        <p style="margin: 0; color: var(--text-light); font-size: 0.85rem;">
                            <strong>Eindoordeel:</strong> Bialetti als je <strong>koffie + functie</strong> wilt. Alessi als je <strong>design-statement + koffie</strong> wilt en je budget omhoog kan. Beide maken even goede koffie.
                        </p>
                    </div>
                </div>

                <!-- Comparison 2: Bialetti vs Grosche -->
                <div style="border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.5rem; background: white;">
                    <h3 style="margin-bottom: 1.25rem; color: var(--coffee);">
                        Bialetti vs <a href="../grosche/" style="color: var(--coffee); text-decoration: none;">Grosche</a>
                    </h3>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                        <div>
                            <h4 style="color: var(--text); margin-bottom: 0.75rem; font-size: 1rem;">Bialetti</h4>
                            <ul style="color: var(--text-dim); font-size: 0.85rem; line-height: 1.7; margin: 0; padding-left: 1.25rem;">
                                <li>Prijs: €25-65</li>
                                <li>Innovatie: Proven 90+ jaar</li>
                                <li>Prioriteit: Traditie & Authenticiteit</li>
                                <li>Beste voor: Italianen & nostalgici</li>
                                <li>Modellen: 9 varianten</li>
                                <li>Handvat: Basisch</li>
                                <li>Onderdelen: Overal beschikbaar</li>
                            </ul>
                        </div>

                        <div>
                            <h4 style="color: var(--text); margin-bottom: 0.75rem; font-size: 1rem;">Grosche</h4>
                            <ul style="color: var(--text-dim); font-size: 0.85rem; line-height: 1.7; margin: 0; padding-left: 1.25rem;">
                                <li>Prijs: €35-55</li>
                                <li>Innovatie: Modern, safety-focus</li>
                                <li>Prioriteit: Comfort & Features</li>
                                <li>Beste voor: Modernisten</li>
                                <li>Modellen: 2 principale</li>
                                <li>Handvat: Ergonomisch geleid</li>
                                <li>Onderdelen: Beperkt verkrijgbaar</li>
                            </ul>
                        </div>
                    </div>

                    <div style="background: #f5f0ea; padding: 1rem; border-radius: 0.3rem; margin-top: 1rem;">
                        <p style="margin: 0; color: var(--text-light); font-size: 0.85rem;">
                            <strong>Eindoordeel:</strong> Bialetti voor <strong>authenticiteit, keuze en beschikbaarheid</strong>. Grosche voor <strong>ergonomie en moderne features</strong>. Keuze tussen traditioneel vs vernieuwd.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

content = content.replace(section5_old, section5_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sections 4 and 5 rewritten")
