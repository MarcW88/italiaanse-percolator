from pathlib import Path

f = Path('vergelijking/index.html')
html = f.read_text(encoding='utf-8')

CSS = """<style>
.v-hero{background:#f5f0ea;padding:3rem 0 2.5rem;border-bottom:1px solid var(--border);}
.v-hero h1{font-family:var(--font-serif);font-size:clamp(1.8rem,3vw,2.4rem);font-weight:400;margin:0 0 .75rem;}
.v-lead{color:var(--text-dim);font-size:1rem;max-width:640px;margin:0;}
.v-breadcrumb{font-size:.77rem;color:var(--text-light);margin-bottom:.9rem;}
.v-breadcrumb a{color:var(--text-light);text-decoration:none;}
.v-breadcrumb a:hover{color:var(--coffee);}
.v-breadcrumb span{margin:0 .3rem;}
.v-section{padding:3rem 0;}
.v-section-alt{background:#fafafa;border-top:1px solid var(--border);border-bottom:1px solid var(--border);}
.v-section h2{font-family:var(--font-serif);font-size:clamp(1.25rem,2.2vw,1.65rem);font-weight:400;margin:0 0 .4rem;}
.v-section-intro{color:var(--text-dim);font-size:.95rem;margin:0 0 2rem;max-width:720px;}
.v-grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;}
.v-grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:1.5rem;}
.v-card{border:1px solid var(--border);border-radius:.5rem;padding:1.5rem;background:white;}
.v-card h3{font-size:1rem;font-weight:700;margin:0 0 .55rem;color:var(--text);}
.v-card p{font-size:.88rem;color:var(--text-dim);line-height:1.65;margin-bottom:.5rem;}
.v-card .v-tip{font-size:.8rem;color:var(--text-light);margin-bottom:1rem;}
.v-card a{font-size:.85rem;color:var(--coffee);text-decoration:none;font-weight:600;}
.v-card a:hover{text-decoration:underline;}
.v-method-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin:1.5rem 0;}
.v-method-block h3{font-size:.9rem;font-weight:700;color:var(--text);margin:0 0 .5rem;}
.v-method-block ul{padding-left:1.25rem;margin:0;}
.v-method-block li{font-size:.85rem;color:var(--text-dim);margin-bottom:.3rem;line-height:1.5;}
.v-method-note{font-size:.85rem;color:var(--text-dim);line-height:1.7;margin:.75rem 0 0;border-top:1px solid var(--border);padding-top:.75rem;}
.v-comparison-block{border:1px solid var(--border);border-radius:.5rem;padding:2rem;margin-bottom:1.5rem;background:white;}
.v-comparison-block.v-muted{opacity:.65;}
.v-brand-vs{display:flex;align-items:center;gap:2rem;margin-bottom:1.5rem;flex-wrap:wrap;}
.v-brand-item{text-align:center;min-width:90px;}
.v-brand-item img{width:68px;height:68px;object-fit:cover;border-radius:.4rem;display:block;margin:0 auto .4rem;}
.v-brand-item strong{display:block;font-size:.88rem;font-weight:700;color:var(--text);}
.v-brand-item small{font-size:.74rem;color:var(--text-light);}
.v-vs-sep{font-size:1.1rem;font-weight:700;color:var(--text-light);padding:0 .5rem;}
.v-choose-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.25rem 0;}
.v-choose-col{background:#fafafa;border:1px solid var(--border);border-radius:.4rem;padding:1rem;}
.v-choose-col h4{font-size:.85rem;font-weight:700;margin:0 0 .5rem;color:var(--text);}
.v-choose-col ul{padding-left:1.25rem;margin:0;}
.v-choose-col li{font-size:.84rem;color:var(--text-dim);margin-bottom:.3rem;line-height:1.5;}
.v-scores{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.25rem 0;}
.v-score-item{padding:.75rem;border:1px solid var(--border);border-radius:.4rem;text-align:center;background:#fafafa;}
.v-score-num{font-size:1.3rem;font-weight:700;color:var(--coffee);}
.v-score-label{font-size:.74rem;color:var(--text-dim);margin-top:.1rem;}
.v-table-wrap{overflow-x:auto;margin:1.25rem 0;}
.v-table{width:100%;border-collapse:collapse;font-size:.87rem;}
.v-table th{background:#f5f0ea;padding:.6rem .9rem;text-align:left;font-weight:600;color:var(--text);border-bottom:2px solid var(--border);}
.v-table td{padding:.6rem .9rem;border-bottom:1px solid var(--border);color:var(--text-dim);}
.v-table tr:last-child td{border-bottom:none;}
.v-table tr:hover td{background:#fafafa;}
.v-table a{color:var(--coffee);text-decoration:none;font-weight:600;}
.v-table td:nth-child(5){font-weight:700;color:var(--text);}
.v-material-card{border:1px solid var(--border);border-radius:.5rem;padding:1.5rem;background:white;}
.v-material-card h3{font-size:1rem;font-weight:700;margin:0 0 .5rem;color:var(--text);}
.v-material-card p{font-size:.88rem;color:var(--text-dim);line-height:1.65;margin-bottom:.5rem;}
.v-material-card .v-summary{font-size:.79rem;color:var(--text-light);margin-bottom:1rem;}
.v-material-card a{font-size:.85rem;color:var(--coffee);text-decoration:none;font-weight:600;}
.v-cat-card{border:1px solid var(--border);border-radius:.5rem;padding:1.5rem;background:white;}
.v-cat-card h4{font-size:1rem;font-weight:700;margin:0 0 .5rem;color:var(--text);}
.v-cat-card>p{font-size:.88rem;color:var(--text-dim);margin-bottom:.75rem;}
.v-cat-card .v-cat-items p{font-size:.83rem;color:var(--text-dim);margin-bottom:.3rem;line-height:1.55;}
.v-decision-wrap{max-width:860px;margin:0 auto;}
.v-decision-grid{display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;margin-top:1.5rem;}
.v-decision-col h3{font-size:.95rem;font-weight:700;margin:0 0 .5rem;color:var(--text);}
.v-decision-col>p{font-size:.88rem;color:var(--text-dim);margin-bottom:.75rem;}
.v-decision-col ul{padding-left:1.25rem;margin-bottom:.75rem;}
.v-decision-col li{font-size:.85rem;color:var(--text-dim);margin-bottom:.35rem;line-height:1.5;}
.v-decision-col a{color:var(--coffee);text-decoration:none;}
.v-decision-col a:hover{text-decoration:underline;}
.v-faq-wrap{max-width:800px;margin:0 auto;}
.v-faq details{border-bottom:1px solid var(--border);padding:.8rem 0;}
.v-faq summary{font-size:.95rem;font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem;}
.v-faq summary::-webkit-details-marker{display:none;}
.v-faq summary::after{content:'+';font-size:1.1rem;color:var(--coffee);flex-shrink:0;}
.v-faq details[open] summary::after{content:'\2212';}
.v-faq details p{font-size:.88rem;color:var(--text-dim);line-height:1.7;margin:.7rem 0 .2rem;}
.v-cta-section{background:#f5f0ea;border-top:1px solid var(--border);padding:3rem 0;text-align:center;}
.v-cta-section h2{font-family:var(--font-serif);font-size:clamp(1.3rem,2vw,1.6rem);font-weight:400;margin:0 0 .5rem;}
.v-cta-section p{color:var(--text-dim);margin:0 0 1.5rem;}
.v-cta-inner{max-width:600px;margin:0 auto;}
.v-btn-group{display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;}
.v-coming-soon-tag{display:inline-block;font-size:.72rem;font-weight:600;color:var(--text-light);border:1px solid var(--border);border-radius:2rem;padding:.2rem .7rem;margin-bottom:1rem;}
@media(max-width:768px){
  .v-grid-3,.v-grid-2,.v-method-grid,.v-choose-grid,.v-scores,.v-decision-grid{grid-template-columns:1fr;}
  .v-comparison-block{padding:1.25rem;}
}
</style>
"""

NEW_BODY = """\
<section class="v-hero">
<div class="container">
<nav class="v-breadcrumb"><a href="../index.html">Home</a><span>/</span>Percolators Vergelijken</nav>
<h1>Vergelijk de beste percolators</h1>
<p class="v-lead">Vergelijk merken, materialen, modellen en maten op basis van praktijktests, smaak, gebruiksgemak en prijs-kwaliteit.</p>
</div>
</section>

<section class="v-section">
<div class="container">
<h2>Populaire vergelijkingen</h2>
<p class="v-section-intro">Dit zijn de vergelijkingen waar onze lezers het vaakst mee starten. Gebruik ze als snelkoppeling naar de belangrijkste keuzes.</p>
<div class="v-grid-3">
<div class="v-card">
<h3>Fiammetta vs Moka Express</h3>
<p>Twee Bialetti-iconen met nauwelijks smaakverschil, maar wel een andere look en prijs. Perfect als je twijfelt tussen klassiek en iets moderner.</p>
<p class="v-tip">Moka is budgetvriendelijker; Fiammetta heeft een frisse uitstraling.</p>
<a href="../beste-italiaanse-percolators.html#bialetti-fiammetta">Bekijk onze beoordeling</a>
</div>
<div class="v-card">
<h3>Fiammetta vs Venus</h3>
<p>De keuze tussen aluminium en RVS in de praktijk: Fiammetta voor gas/elektrisch, Venus als je inductie hebt of RVS mooier vindt.</p>
<p class="v-tip">Als je ooit naar inductie overstapt, is Venus de veiligere keuze.</p>
<a href="../beste-italiaanse-percolators.html#bialetti-venus">Bekijk onze beoordeling</a>
</div>
<div class="v-card">
<h3>Percolator vs Espressoapparaat</h3>
<p>Twijfel je nog tussen een percolator en een volautomaat of espressomachine? Onze vergelijking zet smaak, kosten en onderhoud helder naast elkaar.</p>
<p class="v-tip">Percolators winnen bijna altijd op prijs en eenvoud; espressomachines op cappuccino-mogelijkheden.</p>
<a href="../koopgids/percolator-vs-espressoapparaat.html">Lees volledige vergelijking</a>
</div>
</div>
</div>
</section>

<section class="v-section v-section-alt">
<div class="container">
<h2>Hoe vergelijken wij percolators?</h2>
<p class="v-section-intro">Onze vergelijkingen zijn niet gebaseerd op productfiches of korte eerste indrukken. Elk model dat we vergelijken wordt minimaal 3 maanden in de praktijk gebruikt en direct naast alternatieven getest.</p>
<div class="v-method-grid">
<div class="v-method-block">
<h3>Fase 1: Eerste indruk</h3>
<ul>
<li>Unboxing en bouwkwaliteit controleren</li>
<li>Comfort, balans en handvat beoordelen</li>
<li>1&ndash;2 weken dagelijks gebruik</li>
</ul>
</div>
<div class="v-method-block">
<h3>Fase 2: Intensieve test</h3>
<ul>
<li>Verschillende maling- en bonencombinaties</li>
<li>Vergelijking op verschillende kookplaten</li>
<li>Onderhoudsfrequentie en schoonmaak testen</li>
</ul>
</div>
<div class="v-method-block">
<h3>Fase 3: Lange termijn</h3>
<ul>
<li>Slijtage na 3+ maanden observeren</li>
<li>Stabiliteit van smaak en prestaties</li>
<li>Beschikbaarheid van onderdelen controleren</li>
</ul>
</div>
</div>
<p class="v-method-note"><strong>Scores:</strong> we scoren elk model op koffiesmaak (30%), bouwkwaliteit (20%), gebruiksgemak (15%), onderhoud (15%), prijs-kwaliteit (10%) en duurzaamheid (10%). Waar persoonlijke smaakvoorkeur meespeelt, benoemen we dat expliciet.</p>
</div>
</section>

<section class="v-section" id="bialetti-vs-alessi">
<div class="container">
<h2>Merkvergelijkingen</h2>
<div class="v-comparison-block">
<div class="v-brand-vs">
<div class="v-brand-item">
<img alt="Bialetti percolator" src="../Images/italiaanse-percolator.png"/>
<strong>Bialetti</strong>
<small>Traditie &amp; functionaliteit</small>
</div>
<span class="v-vs-sep">vs</span>
<div class="v-brand-item">
<img alt="Alessi percolator" src="../Images/italiaanse-percolator-3.png"/>
<strong>Alessi</strong>
<small>Design &amp; exclusiviteit</small>
</div>
</div>
<h3>Bialetti vs Alessi: welk merk past bij jou?</h3>
<p>Bialetti is de uitvinder van de moka pot (sinds 1933) en focust op traditie, gebruiksgemak en betaalbaarheid. Alessi is de design-innovator met award-winnende percolators zoals de Pulcina &mdash; duurder, maar met een uitgesproken uitstraling en premium afwerking.</p>
<div class="v-choose-grid">
<div class="v-choose-col">
<h4>Kies Bialetti als&hellip;</h4>
<ul>
<li>Budget en prijs-kwaliteit belangrijk zijn (&plusmn; &euro;25&ndash;50).</li>
<li>Je klassieke Italiaanse look waardeert (Moka, Fiammetta).</li>
<li>Je een bewezen merk wilt met makkelijk verkrijgbare onderdelen.</li>
</ul>
</div>
<div class="v-choose-col">
<h4>Kies Alessi als&hellip;</h4>
<ul>
<li>Design en uitstraling je hoogste prioriteit zijn (&plusmn; &euro;80&ndash;120).</li>
<li>Je een percolator wilt die ook als designobject in de keuken staat.</li>
<li>Je bereid bent extra te betalen voor afwerking en merkstatus.</li>
</ul>
</div>
</div>
<div class="v-scores">
<div class="v-score-item">
<div class="v-score-num">8.9/10</div>
<div class="v-score-label">Bialetti gemiddeld &mdash; beste prijs-kwaliteit</div>
</div>
<div class="v-score-item">
<div class="v-score-num">8.5/10</div>
<div class="v-score-label">Alessi gemiddeld &mdash; beste design</div>
</div>
</div>
<div class="v-table-wrap">
<table class="v-table">
<thead><tr><th>Criterium</th><th>Bialetti</th><th>Alessi</th></tr></thead>
<tbody>
<tr><td>Gemiddelde prijs</td><td>&euro;25&ndash;50</td><td>&euro;80&ndash;120</td></tr>
<tr><td>Koffiesmaak</td><td>8.5/10</td><td>8.6/10</td></tr>
<tr><td>Bouwkwaliteit</td><td>8.7/10</td><td>9.2/10</td></tr>
<tr><td>Design</td><td>Klassiek</td><td>Award-winnend</td></tr>
<tr><td>Prijs-kwaliteit</td><td>9.5/10</td><td>7.0/10</td></tr>
</tbody>
</table>
</div>
<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:.5rem;">Bialetti wint op rationele gronden (waarde voor je geld), Alessi op design en uitstraling. De koffiesmaak ligt vrijwel gelijk.</p>
<p style="font-size:.88rem;color:var(--text-dim);margin-bottom:1.25rem;"><strong>Voor wie welke?</strong> Kies Bialetti als je een betrouwbare daily driver zoekt met uitstekende prijs-kwaliteit. Kies Alessi als je percolator ook een designstatement moet zijn.</p>
<a class="btn btn-primary" href="../vergelijking/bialetti-vs-alessi.html">Lees volledige Bialetti vs Alessi vergelijking &rarr;</a>
</div>
<div class="v-comparison-block v-muted" id="bialetti-vs-grosche">
<h3>Bialetti vs Grosche</h3>
<p>Een gevestigde Italiaanse klassieker tegenover een jonger merk dat inzet op modern design en sociale impact. In deze vergelijking kijken we naar smaak, bouwkwaliteit, prijs-kwaliteit en beschikbaarheid van onderdelen.</p>
<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1rem;">Bialetti wint doorgaans op lange termijn betrouwbaarheid en onderdelen, terwijl Grosche interessant kan zijn als je bewust buiten de klassieke merken wilt kiezen.</p>
<span class="v-coming-soon-tag">Binnenkort beschikbaar</span>
</div>
</div>
</section>

<section class="v-section v-section-alt" id="materiaal-vergelijkingen">
<div class="container">
<h2>Materiaalkeuze</h2>
<p class="v-section-intro">De drie meest gevraagde vergelijkingen op het vlak van materiaal en kookplaat.</p>
<div class="v-grid-3">
<div class="v-material-card">
<h3>Aluminium vs RVS</h3>
<p>De meest fundamentele keuze: lichter en goedkoper aluminium, of duurzamer en inductiegeschikt RVS. In onze tests blijkt de koffiesmaak vrijwel identiek; het echte verschil zit in kookplaat-compatibiliteit, onderhoud en uitstraling.</p>
<p class="v-summary">Geen inductie? Aluminium is prima en goedkoper. Wel inductie of minimale onderhoudswens? RVS.</p>
<a href="../koopgids/hoe-kies-je-de-juiste-percolator.html#materiaal">Lees meer &rarr;</a>
</div>
<div class="v-material-card">
<h3>Inductie vs Gas</h3>
<p>Op gas werken alle percolators perfect en warmen ze snel op. Op inductie heb je een RVS-model nodig met magnetische bodem, maar profiteer je van veiligheid en energie-effici&euml;ntie.</p>
<p class="v-summary">Onze vergelijking laat zien welke kookplaat het beste past bij jouw koffie- en kookstijl.</p>
<a href="../koopgids/hoe-kies-je-de-juiste-percolator.html#compatibiliteit">Lees meer &rarr;</a>
</div>
<div class="v-material-card">
<h3>3 vs 6 kopjes</h3>
<p>3-kops percolators zijn perfect voor 1&ndash;2 personen, maar bieden weinig marge als je bezoek hebt. 6-kops modellen zijn veelzijdiger: genoeg voor een gezin, maar nog bruikbaar voor twee personen.</p>
<p class="v-summary">Onze gids helpt je kiezen tussen compact, flexibel of familie-formaat, met concrete aanbevelingen.</p>
<a href="../koopgids/hoe-kies-je-de-juiste-percolator.html#grootte">Lees meer &rarr;</a>
</div>
</div>
</div>
</section>

<section class="v-section" id="top-modellen">
<div class="container">
<h2>Productvergelijking</h2>
<p class="v-section-intro">Onze experts hebben alle populaire percolators getest. Deze tabel helpt je snel de juiste keuze maken.</p>
<div class="v-table-wrap">
<table class="v-table">
<thead><tr><th>Model</th><th>Materiaal</th><th>Inductie</th><th>Prijs</th><th>Score</th><th>Best voor</th></tr></thead>
<tbody>
<tr><td><a href="../bialetti-fiammetta-review.html">Bialetti Fiammetta</a></td><td>Aluminium</td><td>Nee</td><td>&euro;34,95</td><td>9.2/10</td><td>Algehele winnaar</td></tr>
<tr><td><a href="../bialetti-venus-review.html">Bialetti Venus</a></td><td>RVS</td><td>Ja</td><td>&euro;42,50</td><td>8.8/10</td><td>Inductie gebruikers</td></tr>
<tr><td><a href="../alessi-pulcina-review.html">Alessi Pulcina</a></td><td>Aluminium</td><td>Nee</td><td>&euro;89,00</td><td>8.5/10</td><td>Design liefhebbers</td></tr>
<tr><td><a href="../bialetti-brikka-review.html">Bialetti Brikka</a></td><td>Aluminium</td><td>Nee</td><td>&euro;45,99</td><td>8.6/10</td><td>Crema liefhebbers</td></tr>
</tbody>
</table>
</div>
<p style="font-size:.88rem;color:var(--text-dim);max-width:800px;margin:0 0 1.5rem;">De <strong>Fiammetta</strong> wint op totale prijs-prestatie. De <strong>Venus</strong> is de logische keuze voor inductie. De <strong>Pulcina</strong> koop je voor design en uitstraling. De <strong>Brikka</strong> is de keuze als je crema en een espresso-achtige ervaring wilt.</p>
<a class="btn btn-primary" href="../beste-italiaanse-percolators.html">Bekijk volledige top 10 &rarr;</a>
</div>
</section>

<section class="v-section v-section-alt" id="snelle-keuze">
<div class="container">
<h2>Vergelijk op categorie</h2>
<p class="v-section-intro">Wil je direct filteren op budget of gezinsgrootte?</p>
<div class="v-grid-2">
<div class="v-cat-card">
<h4>Budget</h4>
<p>Kies op basis van wat je realistisch wilt uitgeven en wat je daarvoor terugkrijgt.</p>
<div class="v-cat-items">
<p><strong>&euro;20&ndash;40:</strong> Bialetti Moka Express of Fiammetta &mdash; perfecte koffie zonder franje.</p>
<p><strong>&euro;40&ndash;70:</strong> Bialetti Venus of Brikka &mdash; RVS of crema-functie, hogere afwerking.</p>
<p><strong>&euro;70+:</strong> Alessi Pulcina &mdash; je betaalt voor design en merkbeleving.</p>
</div>
</div>
<div class="v-cat-card">
<h4>Gezinsgrootte</h4>
<p>De juiste maat bepaalt of je percolator praktisch is of frustrerend in gebruik.</p>
<div class="v-cat-items">
<p><strong>1&ndash;2 personen:</strong> 3-kops model (bijv. Fiammetta) &mdash; ideaal voor dagelijks gebruik.</p>
<p><strong>3&ndash;4 personen:</strong> 6-kops model (bijv. Venus of Musa) &mdash; gezin en bezoek in &eacute;&eacute;n keer bedienen.</p>
<p><strong>5+ personen / kantoor:</strong> 9&ndash;12-kops model, of twee 6-kops voor meer flexibiliteit.</p>
</div>
</div>
</div>
</div>
</section>

<section class="v-section">
<div class="container">
<div class="v-decision-wrap">
<h2>Vergelijkingshulp</h2>
<div class="v-decision-grid">
<div class="v-decision-col">
<h3>Snel zelf vergelijken</h3>
<p>Wil je eerst zelf ori&euml;nteren? Deze drie pagina's geven je in korte tijd een volledig beeld.</p>
<ul>
<li><a href="../koopgids/hoe-kies-je-de-juiste-percolator.html">Complete koopgids: alle keuzecriteria op een rij</a></li>
<li><a href="../koopgids/percolator-vs-espressoapparaat.html">Percolator vs espressoapparaat: smaak, kosten, onderhoud</a></li>
<li><a href="../beste-italiaanse-percolators.html">Top 10 percolators: onze best geteste modellen</a></li>
</ul>
</div>
<div class="v-decision-col">
<h3>Laat ons met je meedenken</h3>
<p>Twijfel je nog tussen twee of drie modellen? Stuur ons een bericht en we denken actief met je mee.</p>
<ul>
<li>De modellen waar je tussen twijfelt</li>
<li>Je kookplaat (gas, inductie, elektrisch, keramisch)</li>
<li>Je budget en huishouden (aantal personen)</li>
<li>Wat voor jou belangrijk is (prijs, design, prestatie, onderhoud)</li>
</ul>
<p style="font-size:.85rem;color:var(--text-dim);">Je krijgt terug: een eerlijke aanbeveling op basis van onze tests, de belangrijkste voor- en nadelen per model en links naar relevante reviews.</p>
<a class="btn btn-primary btn-sm" href="../contact.html">Vraag persoonlijk advies &rarr;</a>
</div>
</div>
</div>
</div>
</section>

<section class="v-section v-section-alt" id="faq-vergelijkingen">
<div class="container">
<div class="v-faq-wrap">
<h2>Veelgestelde vragen</h2>
<div class="v-faq">
<details><summary>Wat is het belangrijkste verschil tussen Bialetti en Alessi?</summary><p>Bialetti focust op traditie, gebruiksgemak en betaalbaarheid; Alessi op design en premium afwerking. In blinde smaaktests liggen de scores dicht bij elkaar, maar Bialetti wint meestal op prijs-kwaliteit, terwijl Alessi uitblinkt in uitstraling en bouwkwaliteit. Voor de meeste mensen is Bialetti de logische keuze; Alessi is ideaal als je percolator ook een designobject moet zijn.</p></details>
<details><summary>Maakt een dure percolator echt betere koffie dan een goedkope?</summary><p>Niet per se. Een &euro;25 Bialetti Moka Express kan vrijwel dezelfde koffiesmaak geven als een &euro;90 Alessi Pulcina. Duurdere modellen scoren vooral beter op afwerking, design en soms duurzaamheid. De grootste smaakverschillen komen van de koffiebonen, maling en zetmethode &mdash; niet van de prijs van de percolator.</p></details>
<details><summary>Hoe kies ik tussen aluminium en RVS percolators?</summary><p>Heb je inductie, dan is RVS verplicht. Op gas of elektrisch is aluminium vaak de beste prijs-kwaliteitkeuze: lichter, goedkoper en klassiek van uitstraling. Qua smaak is het verschil minimaal. RVS wint als je minder onderhoud wilt, een moderne look zoekt of maximale kookplaatflexibiliteit wilt.</p></details>
<details><summary>Welke maat percolator is het meest veelzijdig?</summary><p>In de praktijk is een 6-kops percolator het meest veelzijdig: groot genoeg voor een gezin of bezoek, maar nog bruikbaar voor twee personen als je hem niet volledig vult. 3-kops is ideaal voor solo of koppels, 9+ kopjes vooral voor grote gezinnen of kantoor.</p></details>
<details><summary>Welke vergelijking moet ik eerst lezen als ik helemaal vastzit?</summary><p>Begin met de vergelijking die jouw grootste twijfel oplost: materiaal (Aluminium vs RVS), kookplaat (Inductie vs gas), of merk (Bialetti vs Alessi). Als je nog niet weet welk type of budget bij je past, start dan met de koopgids en kom daarna terug naar de specifieke vergelijkingen.</p></details>
<details><summary>Werkt een RVS percolator ook op gas?</summary><p>Ja. Een RVS percolator werkt op alle kookplaten: inductie, gas, elektrisch en keramisch, zolang de bodem vlak is. Op gas heb je geen voordeel ten opzichte van aluminium, maar je behoudt de flexibiliteit om later naar inductie over te stappen zonder een nieuwe percolator te kopen.</p></details>
<details><summary>Welke percolator maakt de beste koffie?</summary><p>Het smaakverschil tussen goede percolators is kleiner dan veel mensen denken. Een degelijk basismodel van rond de &euro;25&ndash;40 kan bijna dezelfde koffie maken als een veel duurder designmodel. Uitzondering is de Bialetti Brikka, die dankzij de speciale klep een vollere, meer espresso-achtige koffie met crema maakt.</p></details>
<details><summary>Kan ik jullie om persoonlijk vergelijkingsadvies vragen?</summary><p>Ja. Als je twijfelt tussen twee of drie concrete modellen kun je ons een bericht sturen met jouw situatie (kookplaat, budget, huishouden, ervaring en prioriteiten). Op basis van onze praktijktests geven we een eerlijke aanbeveling met voor- en nadelen per optie en een duidelijke voorkeur.</p></details>
</div>
</div>
</div>
</section>

<section class="v-cta-section">
<div class="container">
<div class="v-cta-inner">
<h2>Wat is je volgende stap?</h2>
<p>Je hebt nu alle belangrijke vergelijkingen gezien. Kies de stap die het beste bij je past.</p>
<div class="v-btn-group">
<a class="btn btn-primary btn-lg" href="../beste-italiaanse-percolators.html">Bekijk onze Top 10 &rarr;</a>
<a class="btn btn-outline btn-lg" href="../koopgids/hoe-kies-je-de-juiste-percolator.html">Lees de complete koopgids &rarr;</a>
<a class="btn btn-ghost btn-lg" href="../contact.html">Vraag persoonlijk advies &rarr;</a>
</div>
</div>
</div>
</section>
"""

# ── Apply changes ─────────────────────────────────────────────────────────────

# 1. Inject CSS before </head>
assert '</head>' in html, 'Missing </head>'
html = html.replace('</head>', CSS + '</head>', 1)

# 2. Replace body content between overlay div and footer
ANCHOR_START = '<div class="mobile-menu-overlay"></div>'
ANCHOR_END = '<footer class="footer">'
idx_start = html.find(ANCHOR_START)
idx_end = html.find(ANCHOR_END)
assert idx_start != -1 and idx_end != -1, 'Anchors not found'
html = html[:idx_start + len(ANCHOR_START)] + '\n' + NEW_BODY + '\n' + html[idx_end:]

f.write_text(html, encoding='utf-8')
print('OK: vergelijking/index.html rewritten')
