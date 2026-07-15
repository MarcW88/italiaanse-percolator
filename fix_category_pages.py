#!/usr/bin/env python3
"""
For each of the 6 category pages:
  1. Fix pagination bug: 'categories/percolators-xxx.html' → 'percolators-xxx.html'
  2. Fix <title>: remove "- pagina X"
  3. Fix <link rel="canonical">: remove ?page=X
  4. Inject SEO text (~500 words) + FAQ before <footer>
"""

import re
from pathlib import Path

BASE = Path('/Users/marc/Desktop/italiaanse-percolator/categories')

# ─────────────────────────────────────────────────────────────────────────────
# SEO + FAQ content per page
# ─────────────────────────────────────────────────────────────────────────────

PAGES = {

# ── RVS ──────────────────────────────────────────────────────────────────────
'percolators-rvs.html': {
    'title': 'RVS percolators kopen | Italiaanse Percolator',
    'canonical': 'https://italiaanse-percolator.nl/categories/percolators-rvs.html',
    'baseUrl': 'percolators-rvs.html',
    'seo_h2': 'RVS percolators: duurzaam, inductiegeschikt en makkelijk te onderhouden',
    'seo': [
        'Een <strong>RVS percolator</strong> (roestvrijstaal, ook wel inox of stainless steel) is de moderne keuze voor wie kwaliteit, inductiegeschiktheid en een lange levensduur combineert. In tegenstelling tot aluminium modellen zijn roestvrijstalen percolators geschikt voor <strong>alle kookplaten</strong>, inclusief inductie, en zijn ze bestand tegen krasjes, geurtjes en verkleuring. Dat maakt ze bijzonder populair in keukens met een inductieplaat, maar ook bij mensen die vaker afwassen of meer hygiëne belangrijk vinden.',
        'De meest bekende RVS percolators zijn de <strong>Bialetti Venus</strong> en <strong>Bialetti Musa</strong>, maar ook merken als Pezzetti, G.A.T. Italia, Weis en Alessi brengen hoogwaardige roestvrijstalen modellen op de markt. Prijzen variëren van circa &euro;25 voor instapmodellen tot meer dan &euro;80 voor designmodellen van Alessi of Grosche. Het verschil zit hem doorgaans in de wanddikte van het staal, de kwaliteit van het afdichtingsringetje en de ergonomie van het handvat. Zware, dikwandige RVS modellen geleiden warmte gelijkmatiger, wat de extractie van de koffie ten goede komt.',
        'Wat onderhoud betreft zijn RVS percolators iets vergevingsgezinder dan aluminium: ze zijn minder gevoelig voor vlekken van kalkafzetting en ze lopen niet aan bij langdurig gebruik. Toch geldt ook hier: spoelen met warm water na elk gebruik, en de machine nooit in de afwasmachine zetten. Vervang het siliconen afdichtingsringetje ongeveer jaarlijks, afhankelijk van gebruiksfrequentie. Met dat minimale onderhoud gaat een goede RVS percolator gemakkelijk tien tot twintig jaar mee. Voor inductiebezitters die dagelijks koffie zetten is een RVS percolator dan ook de meest praktische en duurzame keuze op de lange termijn.',
    ],
    'faq': [
        ('Wat is het verschil tussen een RVS en een aluminium percolator?',
         'RVS (roestvrijstaal) is zwaarder, inductiegeschikt en hygiënischer dan aluminium. Aluminium is lichter, goedkoper en heeft een klassiek Italiaans design. Qua koffiesmaak is het verschil minimaal als beide van goede kwaliteit zijn.'),
        ('Zijn alle RVS percolators inductiegeschikt?',
         'De meeste wel, maar controleer altijd de productbeschrijving. Een percolator is inductiegeschikt als de bodem magnetisch is (roestvrijstaal met een ijzerlegering). Zuiver aluminium of bepaalde RVS-legeringen kunnen <em>niet</em> op inductie.'),
        ('Welke RVS percolator is het beste voor beginners?',
         'De Bialetti Venus (2 of 4 kops, circa &euro;35–50) is een solide keuze: bewezen kwaliteit, inductiegeschikt, eenvoudig gebruik en breed verkrijgbaar. Voor een hoger budget is de Alessi 9090 een tijdloos designalternatief.'),
        ('Mag een RVS percolator in de vaatwasser?',
         'Nee, ook RVS percolators worden best met de hand gewassen. De hoge temperatuur en agressieve vaatwastabletten tasten het siliconen afdichtingsringetje aan en kunnen de binnenkant van de pot doen verkleuren.'),
        ('Hoe vaak moet ik het afdichtingsringetje van mijn RVS percolator vervangen?',
         'Bij dagelijks gebruik gemiddeld één keer per jaar. Controleer het ringetje op scheurtjes, verharding of vervorming. Roestvrijstalen percolators gebruiken vaak een siliconen ringetje dat iets langer meegaat dan het rubber equivalent in aluminium modellen.'),
        ('Welke koffie gebruik ik in een RVS percolator?',
         'Gebruik een middelfijne maling, iets grover dan espresso maar fijner dan filterkoffie. Specifieke "moka" of "percolator" maling werkt het best. De filtergrootte kan per model licht verschillen — gebruik altijd de filter die bij het toestel geleverd is.'),
    ],
    'links': [
        ('../categories/percolators-aluminium.html', 'Aluminium percolators'),
        ('../categories/percolators-inductie.html', 'Inductiegeschikte percolators'),
        ('../koopgids/hoe-kies-je-de-juiste-percolator.html', 'Hoe kies je de juiste percolator?'),
        ('../marques/bialetti/', 'Bialetti percolators'),
        ('../vergelijking/index.html', 'Vergelijk alle merken'),
    ],
},

# ── Aluminium ─────────────────────────────────────────────────────────────────
'percolators-aluminium.html': {
    'title': 'Aluminium percolators kopen | Italiaanse Percolator',
    'canonical': 'https://italiaanse-percolator.nl/categories/percolators-aluminium.html',
    'baseUrl': 'percolators-aluminium.html',
    'seo_h2': 'Aluminium percolators: het klassieke Italiaanse koffieritueel',
    'seo': [
        'De <strong>aluminium percolator</strong> is het originele moka-apparaatje zoals miljoenen Italianen het kennen. Uitgevonden door Alfonso Bialetti in 1933, is het achtzijdige aluminium ontwerp al meer dan negentig jaar de standaard voor sterk, aromatisch koffiezetten op het fornuis. Aluminium heeft uitstekende warmtegeleidende eigenschappen, is licht van gewicht en relatief betaalbaar — redenen waarom het materiaal nog altijd de meest verkochte keuze is voor Italiaanse percolators.',
        'De bekendste aluminium percolators zijn de <strong>Bialetti Moka Express</strong>, de Bialetti Brikka (met crema-systeem), de Bialetti Fiammetta en de G.A.T. Italia Tricolore. Naast Bialetti brengen ook Pezzetti, Ilsa en tal van kleinere Italiaanse fabrikanten aluminium moka-potten op de markt. Aluminium modellen zijn er in alle maten, van 1 kops (circa 50 ml) tot 18 kops, en kosten doorgaans <strong>&euro;15 tot &euro;45</strong> voor een kwaliteitsmodel. Dat maakt ze toegankelijk voor iedereen die de Italiaanse koffiecultuur thuis wil brengen zonder een groot budget.',
        'Het enige echte nadeel van aluminium is dat het <strong>niet geschikt is voor inductie</strong>. Heb je een inductieplaat, dan heb je een geschikte roestvrijstalen percolator of een inductieplaatje nodig. Reiniging is eenvoudig: na elk gebruik afspoelen met warm water (geen zeep, geen afwasmachine) en volledig laten drogen. Aluminium patineert licht na verloop van tijd — dit heeft geen invloed op de smaak maar geeft de moka-pot dat typisch gebruikte Italiaanse uiterlijk. Met een jaarlijkse vervanging van het rubber afdichtingsringetje gaat een aluminium percolator decennialang mee.',
    ],
    'faq': [
        ('Is een aluminium percolator veilig om te gebruiken?',
         'Ja. Aluminium percolators worden al meer dan negentig jaar veilig gebruikt. Modernere modellen zijn voorzien van een voedselveilig aluminium legering. De koffie komt in contact met het metaal, maar de hoeveelheid aluminiummigratie bij normaal gebruik is verwaarloosbaar klein en ver onder de veiligheidsdrempel.'),
        ('Kunnen aluminium percolators op inductie?',
         'Nee, niet rechtstreeks. Aluminium is niet magnetisch en werkt dus niet op inductie. Je hebt een roestvrijstalen percolator nodig, of een inductie-adapterplaatje (circa &euro;10–15) dat je tussen de plaat en de percolator legt.'),
        ('Hoe maak ik een aluminium percolator schoon?',
         'Spoel hem na elk gebruik af met warm water, zonder zeep of afwasmiddel. Zeep tast de patina aan die de koffiesmaak beschermt. De vaatwasser is absoluut af te raden. Droog de onderdelen volledig voor je hem opslaat.'),
        ('Wat is het verschil tussen de Bialetti Moka Express en de Brikka?',
         'Beide zijn aluminium percolators. Het verschil: de Brikka heeft een speciale drukklep die een crema-laagje op de koffie produceert, vergelijkbaar met espresso. De Moka Express maakt een krachtige maar crema-loze koffie. De Brikka kost circa &euro;20 meer.'),
        ('Verandert aluminium de smaak van de koffie?',
         'Niet waarneembaar bij een goed onderhouden percolator. Na de eerste paar zetbeurten vormt zich een patina aan de binnenkant van de pot dat de smaak neutraal houdt. Schroob de binnenkant nooit schoon; zo verwijder je die beschermende laag.'),
        ('Welke maat aluminium percolator koop ik het best?',
         'De 3 kops is het populairst voor één persoon die meerdere kopjes wil, of voor twee personen. De 6 kops is ideaal voor een gezin van 3–4 personen. Vergeet niet dat "1 kops" staat voor een Italiaans espressokopje van circa 50 ml, niet een grote mok.'),
    ],
    'links': [
        ('../categories/percolators-rvs.html', 'RVS percolators'),
        ('../categories/percolators-inductie.html', 'Inductiegeschikte percolators'),
        ('../koopgids/hoe-kies-je-de-juiste-percolator.html', 'Hoe kies je de juiste percolator?'),
        ('../koopgids/hoe-onderhoud-je-een-percolator.html', 'Onderhoud en reiniging'),
        ('../marques/bialetti/', 'Bialetti percolators'),
    ],
},

# ── Inductie ──────────────────────────────────────────────────────────────────
'percolators-inductie.html': {
    'title': 'Inductie percolators kopen | Italiaanse Percolator',
    'canonical': 'https://italiaanse-percolator.nl/categories/percolators-inductie.html',
    'baseUrl': 'percolators-inductie.html',
    'seo_h2': 'Inductie-geschikte percolators: Italiaanse koffie op elke kookplaat',
    'seo': [
        'Steeds meer keukens zijn uitgerust met een inductieplaat, en ook koffieliefhebbers willen dan hun Italiaanse moka-koffie kunnen blijven zetten. Een <strong>inductie percolator</strong> werkt via elektromagnetische inductie: de bodem van het apparaat moet magnetisch zijn om warmte te genereren. Dat betekent in de praktijk dat je een percolator nodig hebt met een roestvrijstalen bodem of een volledig stalen behuizing — een zuiver aluminium percolator zal op inductie simpelweg niet werken.',
        'De meest verkochte inductie-geschikte percolators zijn de <strong>Bialetti Venus</strong> (2, 4 en 6 kops), de <strong>Bialetti Moka Induction</strong> en de <strong>Bialetti Musa</strong>. Buiten Bialetti bieden ook G.A.T. Italia, Pezzetti SolidExpress, Weis en Mokavit inductiegeschikte modellen aan. Prijzen beginnen rond de &euro;25 voor instapmodellen en lopen op tot meer dan &euro;90 voor premium designmerken als Alessi. Inductiegeschikte modellen kosten doorgaans &euro;10–20 meer dan vergelijkbare aluminium versies, voornamelijk door de meerprijs van het roestvrijstaal.',
        'Bij de aankoop van een inductie percolator zijn er enkele aandachtspunten. Controleer altijd of de productbeschrijving expliciet vermeldt dat het model voor inductie geschikt is — niet alle RVS percolators zijn dat automatisch. Een handige test: een magneet moet sterk aan de bodem blijven plakken. Qua gebruik en onderhoud verschilt een inductie percolator nauwelijks van zijn aluminium tegenhanger: warm water na elk gebruik, geen vaatwasser en jaarlijkse vervanging van het siliconen afdichtingsringetje. Zo geniet je jarenlang van authentieke moka-koffie, ongeacht je kookplaat.',
    ],
    'faq': [
        ('Hoe weet ik of een percolator geschikt is voor inductie?',
         'Controleer of de bodem magnetisch is: houd een koelkastmagneet ertegenaan. Blijft hij plakken? Dan werkt het op inductie. Kijk ook naar het inductie-symbool (spiraalvormig) op de verpakking. Zuiver aluminium werkt nooit op inductie.'),
        ('Kan ik een aluminium percolator toch op inductie zetten?',
         'Niet rechtstreeks, maar je kunt een <strong>inductie-adapterplaatje</strong> gebruiken (circa &euro;10–15). Dit is een ijzeren of stalen schijf die je op de inductiezone legt en de warmte overdraagt aan de aluminium pot. Werkt redelijk, maar is minder efficiënt dan een native inductiemodel.'),
        ('Welke inductie percolator is het best voor dagelijks gebruik?',
         'De Bialetti Venus 4 kops (circa &euro;45) scoort het best op prijs-kwaliteit: sterk materiaal, goed afdichtend, inductiegeschikt en breed verkrijgbaar. Voor een groter budget is de Bialetti Moka Induction of een model van Alessi een upgrade.'),
        ('Werken alle RVS percolators op inductie?',
         'Niet automatisch. Roestvrijstaal bestaat uit verschillende legeringen, en niet alle zijn magnetisch. Controleer altijd de specificaties. Een percolator die enkel vermeld "RVS" zonder inductie te noemen, is mogelijk niet geschikt.'),
        ('Is er smaaksverschil tussen koffie van een inductie- versus gaspercolator?',
         'Minimaal, als de warmteregeling vergelijkbaar is. Het belangrijkste is de extractietemperatuur: zorg dat het vuur (of de inductiezone) na het pruttelgeluid direct gedoofd wordt. Te lang verhitten geeft een bittere smaak, ongeacht het type kookplaat.'),
        ('Zijn inductie percolators zwaarder dan aluminium?',
         'Ja, doorgaans. Roestvrijstaal is dichter dan aluminium. Een 4-kops RVS percolator weegt circa 400–600 gram, tegenover 200–300 gram voor een aluminium model. Dat maakt weinig verschil in de keuken, maar is een aandachtspunt als je de percolator meeneemt op reis.'),
    ],
    'links': [
        ('../categories/percolators-rvs.html', 'Alle RVS percolators'),
        ('../categories/percolators-aluminium.html', 'Aluminium percolators'),
        ('../koopgids/hoe-kies-je-de-juiste-percolator.html', 'Hoe kies je de juiste percolator?'),
        ('../marques/bialetti/', 'Bialetti percolators'),
        ('../vergelijking/index.html', 'Vergelijk alle merken'),
    ],
},

# ── 1-2 kops ─────────────────────────────────────────────────────────────────
'percolators-1-2-kops.html': {
    'title': '1 en 2 kops percolators kopen | Italiaanse Percolator',
    'canonical': 'https://italiaanse-percolator.nl/categories/percolators-1-2-kops.html',
    'baseUrl': 'percolators-1-2-kops.html',
    'seo_h2': '1 en 2 kops percolators: intens espresso voor één of twee personen',
    'seo': [
        'Een <strong>1 of 2 kops percolator</strong> is de perfecte keuze voor koffieliefhebbers die alleen of in duo genieten van een sterke, aromatische moka-koffie. Let op: "1 kops" en "2 kops" verwijzen naar <strong>Italiaanse espressokopjes van circa 50 ml</strong>, niet naar grote mokken. Een 1-kops percolator maakt dus zo\'n 50 ml koffie; een 2-kops levert circa 100 ml — twee korte, intense espressokopjes. Voor wie gewend is aan lange koffie is dit een aanpassing, maar voor echte espressofans is dit precies de juiste concentratie.',
        'Kleine percolators zijn bijzonder compact en licht, wat ze ideaal maakt voor <strong>reizigers, studenten of mensen met een kleine keuken</strong>. De meest bekende modellen zijn de Bialetti Moka Express 1 kops en 2 kops, de G.A.T. Italia Tricolore 1 kops en de Bialetti La Mokina (1 kops, speciaal ontworpen als het kleinste percolatortje). Prijzen liggen doorgaans tussen &euro;15 en &euro;35 voor aluminium modellen; RVS inductiegeschikte mini-percolators kosten wat meer. Een groot voordeel: ze verwarmen razendsnel, want er is weinig water en koffie nodig.',
        'Een aandachtspunt bij kleine percolators: de verhouding koffie per waterhoeveelheid is gevoeliger dan bij grotere maten. Vul het waterreservoir altijd tot het veiligheidsventiel en gebruik de volledige filtercup met fijngemalen koffie — sla deze stap niet over. Een te weinig gevulde kleine percolator geeft een waterige, lauwe koffie. Met de juiste techniek levert zelfs de kleinste 1-kops percolator een rijke, krachtige espresso die niet onderdoet voor die van een grote machine.',
    ],
    'faq': [
        ('Hoeveel ml koffie maakt een 1 kops percolator?',
         'Een 1-kops percolator maakt circa 50 ml — gelijk aan een klein espressokopje. Een 2-kops maakt circa 100 ml, goed voor twee espresso\'s of één groter kopje sterk gezette koffie.'),
        ('Kan ik in een 2-kops percolator maar 1 kopje zetten?',
         'Niet aan te raden. Percolators werken het best als ze volledig zijn gevuld. Een half gevuld waterreservoir of een halve filtercup geeft een slechtere extractie en kan het veiligheidsventiel overbelasten. Koop liever een 1-kops als je maar één kopje nodig hebt.'),
        ('Welke 1-2 kops percolator is het best voor reizen?',
         'De Bialetti Moka Express 1 kops (aluminium, circa &euro;20) is licht, compact en onbreekbaar genoeg voor reizen. Aluminium modellen zijn lichter dan RVS. Vergeet niet de apart mee te nemen reserve-afdichtring.'),
        ('Zijn kleine percolators ook inductiegeschikt?',
         'Sommige wel. De Bialetti Moka Induction 2 kops is inductiegeschikt. Controleer altijd de productbeschrijving. Kleine RVS modellen van G.A.T. Italia of Pezzetti zijn ook inductiegeschikt beschikbaar.'),
        ('Waarom smaakt mijn kleine percolator bitter?',
         'Mogelijk zet je te lang: haal de percolator van het vuur zodra je het kenmerkende pruttelen hoort en de koffie begint te stromen. Bij kleine volumes gaat dit sneller dan bij grotere maten. Gebruik ook niet te fijn gemalen koffie.'),
    ],
    'links': [
        ('../categories/percolators-3-kops.html', '3 kops percolators'),
        ('../categories/percolators-6-kops.html', '6 kops percolators'),
        ('../koopgids/hoe-kies-je-de-juiste-percolator.html', 'Hoe kies je de juiste percolator?'),
        ('../marques/bialetti/', 'Bialetti percolators'),
    ],
},

# ── 3 kops ────────────────────────────────────────────────────────────────────
'percolators-3-kops.html': {
    'title': '3 kops percolators kopen | Italiaanse Percolator',
    'canonical': 'https://italiaanse-percolator.nl/categories/percolators-3-kops.html',
    'baseUrl': 'percolators-3-kops.html',
    'seo_h2': '3 kops percolators: de meest populaire maat voor thuis',
    'seo': [
        'De <strong>3 kops percolator</strong> is wereldwijd de meest verkochte maat van de Italiaanse moka-pot. Met een inhoud van circa <strong>150 ml</strong> (3 × 50 ml espressokopjes) biedt hij genoeg koffie voor één persoon die twee à drie kopjes wil, of voor twee personen die ieder anderhalve shot nemen. De 3-kops is ook de meest compacte maat waarbij de koffie-waterverhouding consistent genoeg is voor beginners: niet te klein (zoals de 1-kops) en niet te groot (waarbij je snel koffie verspilt als je alleen thuis bent).',
        'De absolute bestseller in deze categorie is de <strong>Bialetti Moka Express 3 kops</strong>, maar ook de Bialetti Fiammetta, de G.A.T. Italia Tricolore 3 kops, de Pezzetti Italexpress en tal van andere merken bieden uitstekende 3-kops modellen. Aluminium 3-kops percolators beginnen al vanaf &euro;15–20; RVS inductiegeschikte modellen zoals de Bialetti Venus 3 kops kosten &euro;35–50. Design-modellen van Alessi of Grosche kunnen oplopen tot &euro;80 of meer, maar het basisprincipe is bij elk model identiek.',
        'Een veelgestelde vraag: kan ik een 3-kops percolator ook maar half vullen voor minder koffie? Technisch gezien niet: de filtercup moet volledig en gelijkmatig gevuld zijn, en het waterreservoir moet tot het veiligheidsventiel gevuld zijn. Anders klinkt de extractie niet goed en kan de koffie waterig of verbrand smaken. Wil je minder koffie, kies dan een kleinere maat. Met de juiste techniek — volledig gevuld, matige warmte en direct van het vuur na het pruttelgeluid — levert de 3-kops percolator keer op keer een perfecte, aromatische moka-koffie.',
    ],
    'faq': [
        ('Hoeveel koffie maakt een 3 kops percolator precies?',
         'Circa 150 ml — dat zijn drie Italiaanse espressokopjes van 50 ml elk. Voor Nederlanders die grotere kopjes gewend zijn: dit is vergelijkbaar met één groot kopje sterke koffie, of twee kleine espresso\'s met wat extra water.'),
        ('Wat is het verschil tussen een 3-kops aluminium en RVS percolator?',
         'Aluminium is lichter, goedkoper (vanaf &euro;15) en klassiek van design, maar werkt niet op inductie. RVS is zwaarder, duurder (vanaf &euro;35) en inductiegeschikt. De koffiesmaak verschilt nauwelijks als beide van goede kwaliteit zijn.'),
        ('Welke 3-kops percolator koopt u het best?',
         'De Bialetti Moka Express 3 kops is de veiligste keuze voor een eerste percolator: bewezen kwaliteit, wijde ondersteuning, reserveonderdelen overal verkrijgbaar. Voor inductie: de Bialetti Venus 3 kops of G.A.T. Italia 3 kops.'),
        ('Kan ik een 3 kops percolator gebruiken voor 2 of 1 kopje?',
         'Nee, dat wordt niet aanbevolen. Vul altijd de volledige filtercup en het waterreservoir. Een halflege percolator geeft een slechte extractie en kan het ventieltje belasten. Voor minder koffie gebruik je beter een kleiner model.'),
        ('Hoe lang duurt het zetten van koffie in een 3-kops percolator?',
         'Op een middelmatig vuur duurt het zetten van koffie in een 3-kops percolator 4 tot 6 minuten. Op inductie of een elektrische plaat iets langer doordat het verwarmen geleidelijker gaat. Houd het vuur laag tot medium voor de beste smaak.'),
        ('Hoe reinig ik een 3-kops percolator?',
         'Spoel na elk gebruik af met warm water. Geen zeep, geen vaatwasser. Demonteer de drie onderdelen (onder, filter, boven), laat alles drogen en bewaar met de deksel open. Vervang het rubber of siliconen afdichtingsringetje jaarlijks.'),
    ],
    'links': [
        ('../categories/percolators-1-2-kops.html', '1 en 2 kops percolators'),
        ('../categories/percolators-6-kops.html', '6 kops percolators'),
        ('../koopgids/hoe-kies-je-de-juiste-percolator.html', 'Hoe kies je de juiste percolator?'),
        ('../marques/bialetti/', 'Bialetti percolators'),
        ('../beste-italiaanse-percolators.html', 'Top 10 beste percolators'),
    ],
},

# ── 6 kops ────────────────────────────────────────────────────────────────────
'percolators-6-kops.html': {
    'title': '6 kops percolators kopen | Italiaanse Percolator',
    'canonical': 'https://italiaanse-percolator.nl/categories/percolators-6-kops.html',
    'baseUrl': 'percolators-6-kops.html',
    'seo_h2': '6 kops percolators: ruime capaciteit voor het gezin of kantoor',
    'seo': [
        'Een <strong>6 kops percolator</strong> maakt circa <strong>300 ml koffie</strong> per zetbeurt — zes Italiaanse espressokopjes van 50 ml elk. Dat is genoeg voor drie à vier personen die ieder twee kopjes willen, of voor één persoon die een langere ochtendroutine heeft. De 6-kops is na de 3-kops de populairste maat, en vrijwel elk merk dat percolators maakt, heeft een 6-kops model in het assortiment. Het is ook de maat waarbij het kostenvoordeel ten opzichte van kleinere modellen het duidelijkst merkbaar is.',
        'In de categorie 6 kops zijn de <strong>Bialetti Moka Express 6 kops</strong>, de <strong>Bialetti Venus 6 kops</strong> en de <strong>Bialetti Moka Induction 6 kops</strong> de meest verkochte modellen. Aluminium versies beginnen vanaf circa &euro;20–25; RVS inductiegeschikte modellen kosten &euro;45–70 afhankelijk van merk en uitvoering. Voor groepen van 6 of meer personen bestaan ook grotere maten (9, 10, 12 of zelfs 18 kops), maar de 6-kops blijft de beste balans tussen capaciteit en hanteerbaarheid voor huishoudelijk gebruik.',
        'Bij een 6-kops percolator is het temmen van het vuur cruciaal. Door het grotere watervolume duurt het verhitten langer, wat het risico op oververhitting vergroot als je het vuur te hoog zet. Gebruik altijd een matig tot laag vuur en laat de koffie rustig omhoogkomen. Hoor je het kenmerkende pruttelen? Zet dan meteen het vuur uit en laat de resterende stoomdruk de koffie verder omhoogperseren. Met die simpele aanpak maakt ook de grootste thuis-percolator een consistente, aromatische moka-koffie die de vergelijking met een espressobar niet hoeft te schuwen.',
    ],
    'faq': [
        ('Hoeveel ml koffie geeft een 6 kops percolator?',
         'Circa 300 ml — zes Italiaanse espressokopjes van 50 ml. Dat is goed voor 2–4 personen afhankelijk van hoe groot hun kopje is. Voor grote mokken van 200 ml geeft een 6-kops percolator dus ongeveer anderhalve mok sterke koffie.'),
        ('Is een 6 kops percolator ook geschikt voor kantoor?',
         'Voor kleine teams van 2–4 personen zeker. Voor grotere groepen zijn er ook 10-, 12- en 18-kops percolators. Overweeg in dat geval een elektrische percolator met warmhoudfunctie voor meer gemak.'),
        ('Welke 6 kops percolator is het best op inductie?',
         'De Bialetti Venus 6 kops en de Bialetti Moka Induction 6 kops zijn de populairste inductiegeschikte keuzes. Ook G.A.T. Italia en Pezzetti bieden goede 6-kops inductiemodellen aan in de prijsklasse &euro;30–60.'),
        ('Kan ik minder dan 6 kopjes zetten in een 6-kops percolator?',
         'Nee, dat is niet aan te raden. Vul altijd het waterreservoir tot het veiligheidsventiel en de filtercup volledig. Een half gevulde 6-kops percolator geeft een slechte extractie. Wil je minder koffie, kies een 3-kops model.'),
        ('Hoe lang duurt koffie zetten in een 6-kops percolator?',
         'Op een matig vuur duurt het 6 tot 9 minuten. Door het grotere watervolume duurt het langer dan bij kleine maten. Zet het vuur niet te hoog: langzamer verwarmen geeft een betere extractie en minder bitterheid.'),
        ('Hoe onderhoud ik een grote percolator?',
         'Net als kleine modellen: na elk gebruik afspoelen met warm water, geen afwasmachine. Bij grote modellen is het extra belangrijk om het veiligheidsventiel regelmatig te controleren op kalkafzetting en het afdichtingsringetje jaarlijks te vervangen.'),
    ],
    'links': [
        ('../categories/percolators-3-kops.html', '3 kops percolators'),
        ('../categories/percolators-1-2-kops.html', '1 en 2 kops percolators'),
        ('../koopgids/hoe-kies-je-de-juiste-percolator.html', 'Hoe kies je de juiste percolator?'),
        ('../marques/bialetti/', 'Bialetti percolators'),
        ('../beste-italiaanse-percolators.html', 'Top 10 beste percolators'),
    ],
},

} # end PAGES


# ─────────────────────────────────────────────────────────────────────────────
# HTML builder helpers
# ─────────────────────────────────────────────────────────────────────────────

def build_seo_faq_block(cfg: dict) -> str:
    paras = ''.join(
        f'\n        <p style="color:var(--text-dim);line-height:1.8;font-size:0.95rem;margin-bottom:1.25rem;">{p}</p>'
        for p in cfg['seo']
    )
    faq_items = ''.join(
        f'''            <details class="faq-item">
                <summary>{q}</summary>
                <p class="text-dim">{a}</p>
            </details>\n'''
        for q, a in cfg['faq']
    )
    links_html = ''.join(
        f'                <a href="{href}">{label}</a>\n'
        for href, label in cfg['links']
    )

    return f'''
    <!-- SEO Content -->
    <section style="background:#fafafa;padding:3rem 0;margin-top:2rem;">
        <div class="container" style="max-width:860px;">
            <h2 style="font-family:var(--font-serif);font-weight:400;font-size:1.6rem;margin-bottom:1.5rem;">{cfg["seo_h2"]}</h2>{paras}
        </div>
    </section>

    <!-- FAQ -->
    <section class="section-sm faq-section" style="padding:3rem 0;">
        <div class="container faq-container" style="max-width:720px;">
            <h2 class="faq-title" style="font-family:var(--font-serif);font-weight:400;font-size:1.8rem;margin-bottom:2rem;">Veelgestelde vragen</h2>
            <div class="faq-list">
{faq_items}            </div>
        </div>
    </section>

    <!-- Links -->
    <section style="padding:2rem 0;">
        <div class="container" style="max-width:720px;">
            <h3 style="font-size:1rem;font-weight:600;margin-bottom:0.5rem;">Meer lezen</h3>
            <div class="brand-links">
{links_html}            </div>
        </div>
    </section>
'''


# ─────────────────────────────────────────────────────────────────────────────
# Process each file
# ─────────────────────────────────────────────────────────────────────────────

for filename, cfg in PAGES.items():
    path = BASE / filename
    html = path.read_text(encoding='utf-8')

    # 1. Fix baseUrl
    html = re.sub(
        r"const baseUrl = '[^']*';",
        f"const baseUrl = '{cfg['baseUrl']}';",
        html
    )

    # 2. Fix <title>
    html = re.sub(r'<title>.*?</title>', f'<title>{cfg["title"]}</title>', html)

    # 3. Fix canonical
    html = re.sub(
        r'<link rel="canonical"[^>]*>',
        f'<link rel="canonical" href="{cfg["canonical"]}">',
        html
    )

    # 4. Remove existing SEO/FAQ if re-running (idempotency)
    html = re.sub(r'\n    <!-- SEO Content -->.*?<!-- Links -->.*?</section>\n', '',
                  html, flags=re.DOTALL)

    # 5. Inject SEO+FAQ block before <footer>
    seo_block = build_seo_faq_block(cfg)
    html = html.replace('\n    <footer', seo_block + '\n    <footer', 1)

    path.write_text(html, encoding='utf-8')
    print(f'  OK: {filename}')

print('\nDone.')
