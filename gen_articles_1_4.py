"""Generate articles 1-4."""
import sys; sys.path.insert(0, '.')
from article_template import build_page

# ─── Article 1: Maalgraad koffie percolator ──────────────────────────────────
build_page(
  filename='maalgraad-koffie-percolator.html',
  title='De juiste maalgraad voor je percolator',
  meta_desc='Welke maalgraad gebruik je voor een moka pot? Complete gids over te fijn, te grof en de ideale maalgraad, met overzichtstabel en visuele referenties.',
  badge='Koopgids',
  leestijd='7',
  update='jul. 2025',
  intro='De maalgraad is de meest onderschatte variabele bij moka pot koffie. Te fijn geeft bittere over-extractie; te grof levert waterige, zure koffie. Deze gids legt uit waar de ideale zone ligt en hoe je die thuis reproduceert.',
  toc=[
    ('maalgraad-extractie','Maalgraad en extractie'),
    ('ideale-maalgraad','De ideale maalgraad'),
    ('te-fijn','Te fijn gemalen: gevolgen'),
    ('te-grof','Te grof gemalen: gevolgen'),
    ('referentietabel','Overzichtstabel'),
    ('praktische-tips','Praktische tips'),
    ('faq','Veelgestelde vragen'),
  ],
  body="""
<section id="maalgraad-extractie">
<h2>Maalgraad en extractie: waarom elke korrel telt</h2>
<p>Koffie malen is geen triviale handeling. De grootte van de koffiepartikels bepaalt hoe snel en volledig heet water de oplosbare smaakstoffen extraheert. In een moka pot — ook wel Italiaanse percolator of stoompot — werkt heet water onder druk van 1 tot 2 bar omhoog door het koffiebed. Die druk is beduidend lager dan bij een espressomachine (9 bar), maar hoger dan bij een cafetière of filterkoffie. Dit plaatst de moka pot in een bijzondere positie op het spectrum van extractiemethoden: fijner dan filterkoffie vereist, maar grover dan espresso.</p>
<p>Als de maalgraad te fijn is, wordt de weerstand in het koffiebed te groot. Het water vertraagt, de contacttijd verlengt en de extractie wordt te intensief. Daarbij lossen niet alleen de gewenste suikers en fruitige verbindingen op, maar ook bittere polyfenolen en chlorogeenzuren. Omgekeerd: bij een te grove maling schiet het water te snel door het bed, blijft de koffie ondergeëxtraheerd en is het resultaat wrang, zuur en dun. De maalgraad heeft bovendien invloed op de veiligheid: een te fijn koffiebed kan de filter verstoppen, waardoor de druk in het onderreservoir oploopt totdat de veiligheidsklep moet ingrijpen.</p>
</section>

<section id="ideale-maalgraad">
<h2>De ideale maalgraad voor een moka pot</h2>
<p>De optimale maalgraad situeert zich tussen filterkoffie en espresso in — vakjargon spreekt van <em>medium-fijn</em> of kortweg "moka grind". Wrijf je de gemalen koffie tussen duim en wijsvinger, dan voelt het aan als fijn strandzand: een duidelijk schurend gevoel, maar zonder de poederachtige textuur van espressomaling. Je ziet afzonderlijke korreltjes, zij het kleine.</p>
<p>In een speciaalzaak kun je simpelweg vragen om "moka-maling" of "voor een Bialetti" — goede branders begrijpen dit onmiddellijk en stellen hun molen in op 400 tot 600 micron granulometrie, grofweg het dubbele van een standaard espressokorrel. Koop je gemalen koffie in een supermarkt, zoek dan naar "moka" of "espresso medium" op de verpakking en vermijd alles gelabeld "extra fijn" of "ultrafijn", want dat is uitsluitend ontworpen voor 9 bar espressomachines.</p>
<p>Wie thuis maalt met een burr grinder: op de meeste conische burr grinders zit de juiste moka-maalgraad rond het midden van de schaal. Noteer je instelling zodra je de juiste zone hebt gevonden en verander nooit twee variabelen tegelijk — zo begrijp je wat elke wijziging doet.</p>
</section>

<section id="te-fijn">
<h2>Te fijn gemalen: wat er misgaat</h2>
<p>Te fijn gemalen koffie is verreweg de meest voorkomende fout bij een moka pot. Het resultaat is een overwhelmend bittere, donkere en wrange koffie — geen teken van sterkte, maar van over-extractie. Andere signalen: koffieresidu in de bovenste kamer na het zetten, een filter die zwaar aangekoekt zit of een veiligheidsklep die met luid gesis ontlaadt. In dat laatste geval is de druk zo hoog opgelopen dat het apparaat zichzelf moet beveiligen — een situatie die je wil vermijden voor zowel veiligheid als smaak.</p>
</section>

<section id="te-grof">
<h2>Te grof gemalen: dun, zuur en zonder karakter</h2>
<p>Aan het andere uiteinde vind je koffie die te grof gemalen is. Het water passeert het bed te vlot, de contacttijd is te kort en de extractie is voornamelijk oppervlakkig. Het resultaat is een bleek, waterig kopje met een scherpe, éénzijdige zuurheid en vrijwel geen body of afdronk. Dit probleem doet zich regelmatig voor bij mensen die filterkoffiemaling in hun moka pot gebruiken. Filtermaling is ontworpen voor langzame extractie via zwaartekracht — een principe dat fundamenteel verschilt van de drukgestuurde werking van een stoompot.</p>
</section>

<section id="referentietabel">
<h2>Overzichtstabel: maalgraden vergeleken</h2>
<div class="g-table-wrap">
<table class="g-table">
<thead><tr><th>Maalgraad</th><th>Textuur</th><th>Smaakresultaat in moka pot</th><th>Geschikt?</th></tr></thead>
<tbody>
<tr><td>Extra fijn (espresso)</td><td>Poederachtig</td><td>Bitter, wrang, over-geëxtraheerd</td><td>Nee</td></tr>
<tr><td><strong>Medium-fijn (moka)</strong></td><td>Fijn strandzand</td><td>Gebalanceerd, vol, goede body</td><td><strong>Ja &mdash; ideaal</strong></td></tr>
<tr><td>Medium (filterkoffie)</td><td>Grof zand</td><td>Zuur, dun, ondergeëxtraheerd</td><td>Nee</td></tr>
<tr><td>Grof (French press)</td><td>Suikerkorrels</td><td>Waterig, nauwelijks smaak</td><td>Nee</td></tr>
</tbody>
</table>
</div>
</section>

<section id="praktische-tips">
<h2>Praktische tips voor consistente resultaten</h2>
<p>Een propellermolen (mesmolen) maalt onregelmatig en geeft een mix van te fijne en te grove partikels, waardoor consistentie bijna onmogelijk is. Een burr grinder — ook in de goedkopere handmolensegment (Hario, Timemore) — geeft al voor vijftig euro een regelmatig en instelbaar resultaat dat de smaak van je koffie aanzienlijk verbetert.</p>
<ul>
<li>Begin in het midden van de schaal; werk naar fijner (bittere koffie) of grover (zure, dunne koffie) op basis van smaak.</li>
<li>Maal nooit meer dan je direct nodig hebt: gemalen koffie verliest smaak binnen 24 uur na het malen.</li>
<li>Verse koffie (minder dan 4 weken na branding) geeft meer body en minder scherpte dan oude koffie.</li>
</ul>
</section>

<section id="faq">
<h2>Veelgestelde vragen</h2>
<div class="blog-faq">
<details><summary>Kan ik espresso-maling gebruiken in mijn moka pot?</summary><p>Technisch wel, maar het is niet aan te raden. Espresso-maling is ontworpen voor 9 bar druk en geeft in een moka pot (1&ndash;2 bar) vrijwel altijd over-extractie en bitterheid. Bovendien kan de fijne maling de filter verstoppen. Gebruik bij voorkeur een medium-fijne maling specifiek voor moka pots.</p></details>
<details><summary>Hoe weet ik dat mijn maalgraad correct is?</summary><p>De beste indicator is smaak: goed geëxtraheerde moka koffie is rijk en vol met lichte zoetheid, matige zuurheid en weinig bitterheid. Als de percolator meer dan 8 minuten nodig heeft om zijn inhoud naar boven te stuwen, is de maling waarschijnlijk te fijn.</p></details>
<details><summary>Maakt het uit welke koffiebonen ik gebruik?</summary><p>Absoluut. Donker gebrande bonen zijn minder dicht dan licht gebrande en malen bij dezelfde instelling anders. Na een verandering van bonen is het slim om je maalgraad opnieuw te ijken. Over het algemeen werken medium tot medium-donker gebrande espresso-blends het beste.</p></details>
</div>
</section>
""",
)

# ─── Article 2: Camping percolator ───────────────────────────────────────────
build_page(
  filename='camping-percolator.html',
  title='Koffie zetten op de camping: de complete percolator gids',
  meta_desc='Hoe maak je goede koffie op camping met een percolator? Alles over model kiezen, réchaud, transport, bescherming en reinigen met weinig water.',
  badge='Lifestyle',
  leestijd='7',
  update='jul. 2025',
  intro='Een moka pot is het perfecte outdoorgereedschap voor koffieliefhebbers: licht, robuust, geen stroom nodig en toch een kopje espresso-achtige koffie. Deze gids helpt je het juiste model kiezen, correct gebruiken op een réchaud en onderhouden met minimaal water.',
  toc=[
    ('waarom-percolator','Waarom een percolator op camping'),
    ('model-kiezen','Het juiste model kiezen'),
    ('rechaud','Réchaud en warmtebron'),
    ('transport','Transport en bescherming'),
    ('reinigen','Reinigen met weinig water'),
    ('faq','Veelgestelde vragen'),
  ],
  body="""
<section id="waarom-percolator">
<h2>Waarom een moka pot de beste keuze is buiten</h2>
<p>Op de camping of tijdens een trekking heb je geen stopcontact, geen espressomachine en zelden schoon warm water op aanvraag. Toch hoef je het niet te stellen met slechte koffie. Een Italiaanse stoompot is ontworpen voor precies deze omstandigheden: simpele bediening, minimale reiniging en een kopje dat dichter bij espresso ligt dan bij slappe filterkoffie. Het principe is al tientallen jaren onveranderd: water in het onderste reservoir, gemalen koffie in de filter, afsluiten, op het vuur zetten. Geen stroom, geen capsules, geen onderhoudbeurt.</p>
<p>De meeste modellen bestaan uit slechts drie los neembare delen. Dat maakt de moka pot ideaal voor outdoor gebruik: licht, compact en vrijwel onverwoestbaar als je voor het juiste materiaal kiest. Voor camping is aluminium de meest logische keuze als je uitsluitend gas of open vuur gebruikt. RVS biedt meer flexibiliteit als je ook thuis op inductie werkt, maar weegt meer. Een 3-kops Bialetti Moka Express weegt minder dan 250 gram inclusief filter en pakking.</p>
</section>

<section id="model-kiezen">
<h2>Het juiste model kiezen voor outdoor gebruik</h2>
<p>Niet elk model is even geschikt voor buiten. Grote percolators van 9 of 12 kops zijn zwaar, nemen veel ruimte in en hebben meer gas nodig. Modellen met kunststof handvatten of decoratieve onderdelen zijn kwetsbaarder. De ideale campingpercolator is compact, gemaakt van één materiaal en heeft geen uitstekende onderdelen die kunnen breken of haken in je rugzak.</p>
<div class="g-table-wrap">
<table class="g-table">
<thead><tr><th>Model</th><th>Gewicht</th><th>Materiaal</th><th>Camping voordeel</th><th>Nadeel</th></tr></thead>
<tbody>
<tr><td>Bialetti Moka Express 3 kops</td><td>~230 g</td><td>Aluminium</td><td>Lichtgewicht, klassiek, goedkoop</td><td>Niet op inductie</td></tr>
<tr><td>Bialetti Moka Express 6 kops</td><td>~360 g</td><td>Aluminium</td><td>Meer kopjes per ronde, stabiel op vuur</td><td>Groter, minder compact</td></tr>
<tr><td>Bialetti Venus 3 kops</td><td>~310 g</td><td>RVS</td><td>Universeel: ook op inductie thuis</td><td>Iets zwaarder, duurder</td></tr>
</tbody>
</table>
</div>
<p>Voor een solo campingtrip of koppeltje is een 3-kops model de logische keuze. Voor een groep van vier kun je overwegen twee kleinere modellen mee te nemen in plaats van één grote: dat gaart gelijkmatiger en je hebt een reservemodel mochten er onderdelen verloren gaan.</p>
</section>

<section id="rechaud">
<h2>Réchaud en warmtebron</h2>
<p>Een moka pot werkt op elke controleerbare warmtebron. Gas is de beste keuze voor camping: snel, regelbaar en betrouwbaar. Gebruik altijd middelhoog vuur en zorg dat de vlam nooit hoger reikt dan de bodem van de percolator. Zijwaartse verwarming raakt de koffie in de bovenste kamer direct, geeft aangebrand-smakende koffie en versleten afdichtingen.</p>
<p>Op open vuur is meer geduld nodig. Gebruik een rooster of drie stenen om de percolator stabiel te plaatsen en houd de vlam laag zodra je het eerste borrelgeluid hoort. Spiritbranders (alcohol) zijn ultralicht en ideaal voor backpackers, maar trager: reken op vijf tot tien minuten extra ten opzichte van gas. Bij elk vuurtype geldt: zodra de koffie begint te borrelen, haal je hem zo snel mogelijk van de warmtebron om over-extractie te vermijden.</p>
</section>

<section id="transport">
<h2>Transport en bescherming in de rugzak</h2>
<p>Een moka pot in een rugzak is kwetsbaar voor vervorming van de dunne aluminium bodem en beschadiging van het handvat. Wikkel de percolator in een neopreenkoker of stop hem in een oude sok van fleece. Veel campingkooksets hebben een pot die qua diameter past over een 3-kops Moka Express — een elegante oplossing die ruimte bespaart en de percolator beschermt.</p>
<ul>
<li>Bewaar gemalen koffie altijd in een luchtdicht bakje: een gemorste zak ruïneert je volledige rugzak.</li>
<li>Neem een reservepakking mee (weegt vrijwel niks, kost &euro;1&ndash;2) — bij hoge temperaturen verslijten rubberen afdichtingen sneller.</li>
<li>Controleer voor vertrek of de bodem vlak is: een komvormige bodem staat instabiel op een rooster.</li>
</ul>
</section>

<section id="reinigen">
<h2>Reinigen met weinig water</h2>
<p>Op een camping waar water schaars of niet drinkbaar is, wil je zo min mogelijk verspillen aan het reinigen van je percolator. Het goede nieuws: een moka pot hoeft nooit met zeep gewassen te worden. Zeep laat een filmresidu achter dat de volgende kopjes een zeepachtige ondertoon geeft.</p>
<p>De efficiëntste methode is de droge methode: laat de percolator afkoelen, gooi het koffiedik weg, veeg de binnenkant van het onderreservoir en de filter schoon met een droog papieren doekje. Spoel daarna éénmalig met een kleine hoeveelheid warm water en laat alles losgeschroefd drogen in de lucht. Zo voorkom je schimmelvorming bij langere tochten. Na een week intensief outdoor gebruik is een grondige reiniging thuis — met citroenzuur opgelost in warm water — zeker aan te raden.</p>
</section>

<section id="faq">
<h2>Veelgestelde vragen</h2>
<div class="blog-faq">
<details><summary>Kan ik een moka pot gebruiken op een open kampvuur?</summary><p>Ja, maar met voorzichtigheid. Gebruik een rooster en zorg dat vlammen niet hoger reiken dan de bodem. Direct contact met vlammen beschadigt het aluminium en kan het handvat verbranden. Houd het vuur laag zodra je het kenmerkende borrelgeluid hoort.</p></details>
<details><summary>Welke maat is het beste voor een gezin van vier op camping?</summary><p>Een 6-kops model is voor vier personen een betere keuze dan twee 3-kops modellen, tenzij gewicht een absolute prioriteit is. Twee kleine modellen parallel op twee branders zijn iets flexibeler, maar wegen samen meer en nemen meer ruimte in.</p></details>
<details><summary>Hoe lang gaat een moka pot mee bij intensief campinggebruik?</summary><p>Een goed onderhouden aluminium Bialetti gaat tientallen jaren mee, ook bij intensief outdoor gebruik. Het enige onderdeel dat slijt, is de rubberen pakking — neem altijd een reservepakking mee voor lange reizen.</p></details>
</div>
</section>
""",
)

# ─── Article 3: Beste koffie voor Bialetti ───────────────────────────────────
build_page(
  filename='beste-koffie-voor-bialetti.html',
  title='De beste koffie voor een Bialetti: branding, oorsprong en maalgraad',
  meta_desc='Welke koffie gebruik je in een Bialetti moka pot? Gids over branding, oorsprong, intensiteit en maalgraad voor de beste smaak.',
  badge='Koopgids',
  leestijd='6',
  update='jul. 2025',
  intro='De koffie die je kiest is net zo belangrijk als de percolator zelf. Een Bialetti werkt het beste met medium tot medium-donker gebrande blends met voldoende body en lage zuurheid. In deze gids lees je welke brandings, oorsprongen en maalgraden optimaal zijn voor een stoompot.',
  toc=[
    ('geschikt-voor-bialetti','Wat maakt koffie geschikt'),
    ('branding','Branding en smaakprofiel'),
    ('oorsprong','Oorsprong en aroma'),
    ('maalgraad-dosering','Maalgraad en dosering'),
    ('aanbevolen-profielen','Aanbevolen koffieprofielen'),
    ('faq','Veelgestelde vragen'),
  ],
  body="""
<section id="geschikt-voor-bialetti">
<h2>Wat maakt koffie geschikt voor een Bialetti?</h2>
<p>Een Bialetti werkt met stoomdruk van 1 tot 2 bar — veel lager dan een espressomachine (9 bar) maar hoger dan filterkoffie. Dit creëert een extractieprofiel dat voller en intenser is dan filterkoffie, maar minder geconcentreerd dan espresso. De juiste koffie moet goed functioneren in dit middenveld: genoeg oliën en suikers om body te geven bij lage druk, maar niet zo fragiel dat lage-drukextractie een éénzijdig zuur of bitter resultaat geeft.</p>
<p>De drie sleutelvariabelen zijn branding, oorsprong en maalgraad. Te licht gebrande specialty-koffie geeft in een moka pot een scherpzure, onaangename drank. Te donker gebrande robusta-blends leveren een overweldigend bittere, vlakke koffie zonder nuance. Bialetti zelf verkocht jarenlang zijn eigen koffiebrand — een aanwijzing dat het Italiaanse merk goed begreep dat pot en boon onlosmakelijk verbonden zijn.</p>
</section>

<section id="branding">
<h2>Branding: het verschil tussen licht, medium en donker</h2>
<p>Het brandingproces verandert de chemische structuur van de boon radicaal: lichte brandingen bewaren meer zuren en fruitige verbindingen, donkere brandingen ontwikkelen bittere pyrazines en koolachtige verbindingen. Voor een moka pot wil je de zone die de meeste smaakbreedte geeft bij lage extractiedruk.</p>
<div class="g-table-wrap">
<table class="g-table">
<thead><tr><th>Branding</th><th>Kleur boon</th><th>Smaak in moka pot</th><th>Geschikt?</th></tr></thead>
<tbody>
<tr><td>Licht (light roast)</td><td>Lichtbruin, geen olie</td><td>Scherpzuur, fruitig, dun, weinig body</td><td>Niet ideaal</td></tr>
<tr><td>Medium</td><td>Middenbruin, weinig olie</td><td>Gebalanceerd, nootachtig, lichte zoetheid</td><td>Goed</td></tr>
<tr><td><strong>Medium-donker</strong></td><td>Donkerbruin, lichte olieglans</td><td>Rijk, vol, chocolade-ondertonen</td><td><strong>Uitstekend</strong></td></tr>
<tr><td>Donker (Italian/French)</td><td>Bijna zwart, vettig</td><td>Bitter, rookachtig, weinig nuance</td><td>Acceptabel, polariserend</td></tr>
</tbody>
</table>
</div>
<p>De meest veelzijdige keuze is een medium-donkere branding: voldoende oliën voor een volle body, maar genoeg smaakcomplexiteit om interessant te blijven. Het is het profiel dat de meeste traditionele Italiaanse espresso-blends hanteren, en dat is geen toeval.</p>
</section>

<section id="oorsprong">
<h2>Oorsprong en aroma: welke koffies functioneren het beste?</h2>
<p>Braziliaanse bonen (Santos, Cerrado) zijn nootachtig, licht chocoladeachtig en weinig zuur — eigenschappen die goed schalen bij 1 à 2 bar extractie. Ze zijn dan ook de basis van de meeste Italiaanse espresso-blends. Ethiopische bonen (Yirgacheffe, Sidama) voegen fruitige, bloemige noten toe maar zijn uitgesproken zuurder en werken beter als bijdrage in een blend dan als single origin in een moka pot.</p>
<p>Centraal-Amerikaanse koffies (Guatemala, Honduras, Colombia) zijn veelzijdiger: matige zuurheid, caramel en noten, goede body. Ze functioneren prima als single origin in een moka pot, zolang je ze medium tot medium-donker roostert. Aziatische koffies (Sumatra, India) zijn aards en laag in zuurheid — uitstekend als zwaargewicht in een blend. Specialty-bonen met uitgesproken fruitige aciditeit (Kenya, heldere Ethiopiërs) zijn minder geschikt als enige component: ze smaken in een moka pot scherp en éénzijdig.</p>
</section>

<section id="maalgraad-dosering">
<h2>Maalgraad en dosering voor de Bialetti</h2>
<p>Gebruik een medium-fijne maalgraad — tussen filterkoffie en espresso. Vul de filter volledig zonder aan te drukken: een licht, horizontaal gelijkmatig bed. Druk je de koffie aan zoals bij espresso, dan zet je de weerstand te hoog en riskeer je over-extractie of een verstopte filter. Het watervolume staat vast: vul het onderreservoir tot net onder het veiligheidsventiel. Minder water voor "sterkere koffie" geeft oververhitting en een metaalachtige smaak. Sterkte reguleer je via de keuze van de koffie zelf of via een iets fijnere maling.</p>
<ul>
<li>Vul de filter altijd helemaal — een half gevulde filter geeft slechte extractie.</li>
<li>Druk de koffie nooit aan: dat is espresso-techniek, niet voor een moka pot.</li>
<li>Gebruik koffie die minder dan 4 weken geleden geopend is: oude koffie geeft een vlakke, bittere drank.</li>
</ul>
</section>

<section id="aanbevolen-profielen">
<h2>Aanbevolen koffieprofielen</h2>
<p>In plaats van specifieke merken te noemen — want merken en blends veranderen regelmatig — is het nuttiger om profielen te beschrijven. Zoek naar een blend met minimaal 70% arabica, medium tot medium-donker gebrand, met een intensiteitsaanduiding van 5 tot 8 op een schaal van 10. Een aardse, nootachtige of chocoladeachtige smaakbeschrijving past beter dan "bloemig", "fruitig" of "citrusachtig" — die descriptoren horen bij koffies die beter functioneren bij hoge druk of koude extractie.</p>
<p>Wil je experimenteren, maak dan je eigen tweecomponentenblend: 70% Braziliaan (medium-donker, nootachtig) als body-component en 30% Colombiaan (medium, lichte zoetheid) als smaakcomponent. Dit is de methode die de meeste traditionele Italiaanse koffiehuizen hanteren voor hun moka-koffie, en het geeft een consistente, aanpasbare basis.</p>
</section>

<section id="faq">
<h2>Veelgestelde vragen</h2>
<div class="blog-faq">
<details><summary>Kan ik 100% arabica gebruiken in een Bialetti?</summary><p>Ja. Kies een medium tot medium-donker gebrande arabica met lage tot matige aciditeit. Een 100% arabica specialty blend met hoge zuurheid geeft in een moka pot een scherpe, te fruitige koffie. Robusta toevoegen (10&ndash;20%) geeft meer body en een iets meer uitgesproken bitterheid die veel mensen associëren met traditionele Italiaanse espresso.</p></details>
<details><summary>Is verse koffie écht noodzakelijk?</summary><p>Versheid maakt een merkbaar verschil. Koffie die onlangs gebrand is, bevat nog CO&#8322; dat tijdens extractie zorgt voor meer body en complexiteit. Gemalen koffie verliest snel smaak: gebruik binnen 2 weken na het openen van het pakje. In een luchtdicht pakje met ventielklep blijft koffie tot 3 maanden goed na de branddatum.</p></details>
<details><summary>Werken capsulekoffie of pads in een Bialetti?</summary><p>Nee. De maling in capsules is ontworpen voor 9 bar of luchtstoomextractie, niet voor 1&ndash;2 bar. Gebruik altijd losse, vers gemalen koffie voor een optimale Bialetti-ervaring.</p></details>
</div>
</section>
""",
)

# ─── Article 4: Bialetti inductie werkt niet ─────────────────────────────────
build_page(
  filename='bialetti-inductie-werkt-niet.html',
  title='Bialetti werkt niet op inductie: oorzaken en oplossingen',
  meta_desc='Wordt je Bialetti niet herkend door de inductieplaat? Ontdek waarom aluminium niet werkt op inductie, welke Bialetti modellen wél compatibel zijn en wat je kunt doen.',
  badge='Probleemoplossing',
  leestijd='6',
  update='jul. 2025',
  intro='De meest voorkomende frustration met een Bialetti moka pot: hij wordt niet herkend door de inductieplaat. De oorzaak is simpel maar fundamenteel — en de oplossingen zijn concreet. Dit artikel legt uit waarom, welke modellen wél werken en wat je kunt doen met je huidige percolator.',
  toc=[
    ('hoe-inductie-werkt','Hoe inductie werkt'),
    ('waarom-aluminium-niet','Waarom aluminium niet werkt'),
    ('modellen-werken-niet','Bialetti modellen zonder inductie'),
    ('modellen-werken-wel','Bialetti modellen met inductie'),
    ('oplossingen','Oplossingen en alternatieven'),
    ('faq','Veelgestelde vragen'),
  ],
  body="""
<section id="hoe-inductie-werkt">
<h2>Hoe inductie werkt: het magnetische principe</h2>
<p>Een inductieplaat werkt fundamenteel anders dan een gas- of elektrische kookplaat. In plaats van warmte te genereren en over te dragen, creëert inductie een wisselend magnetisch veld onder het glazen oppervlak. Dat veld induceert elektrische stroom in de bodem van de pan — en die stroom produceert warmte. De pan verwarmt zichzelf van binnenuit, niet via contactwarmte van de plaat.</p>
<p>Dit werkt uitsluitend als het materiaal van de bodem <em>ferromagnetisch</em> is: het moet een magneet kunnen aantrekken. De inductieplaat detecteert aanwezigheid en formaat van de pan op basis van dit magnetische veld. Detecteert de plaat niets, dan geeft hij geen energie af — een beveiligingsmechanisme dat ook betekent dat de plaat koud blijft als er een niet-compatibel materiaal op staat.</p>
</section>

<section id="waarom-aluminium-niet">
<h2>Waarom aluminium niet werkt op inductie</h2>
<p>Aluminium is niet ferromagnetisch. Een magneet kleeft niet aan aluminium, en daardoor genereert een inductieplaat geen stroom in een aluminium bodem. De plaat detecteert de pan niet, geeft geen warmte af en de koffie blijft koud. Dit is geen defect aan je Bialetti of aan je kookplaat — het is een fysieke eigenschap van het materiaal die niet omzeild kan worden zonder tussenkomst.</p>
<p>De meest iconische Bialetti-modellen — de Moka Express, Fiammetta, Brikka en de meeste kleurrijke versies — zijn gemaakt van aluminium. Dit is ook de reden waarom ze al tientallen jaren populair zijn: aluminium is lichter, goedkoper en warmt sneller op dan roestvrij staal. Maar op inductie werken ze simpelweg niet.</p>
</section>

<section id="modellen-werken-niet">
<h2>Bialetti modellen die niet op inductie werken</h2>
<div class="g-table-wrap">
<table class="g-table">
<thead><tr><th>Model</th><th>Materiaal</th><th>Inductie?</th><th>Opmerking</th></tr></thead>
<tbody>
<tr><td>Bialetti Moka Express</td><td>Aluminium</td><td>Nee</td><td>Het origineel; de bestseller</td></tr>
<tr><td>Bialetti Fiammetta</td><td>Aluminium</td><td>Nee</td><td>Populair en betaalbaar</td></tr>
<tr><td>Bialetti Brikka</td><td>Aluminium</td><td>Nee</td><td>Heeft crema-klep, maar geen inductiebodem</td></tr>
<tr><td>Alessi Pulcina</td><td>Aluminium</td><td>Nee</td><td>Design-model; niet op inductie</td></tr>
<tr><td>Bialetti Kitty (alu versie)</td><td>Aluminium</td><td>Nee</td><td>Let op: er bestaat ook een RVS versie</td></tr>
</tbody>
</table>
</div>
</section>

<section id="modellen-werken-wel">
<h2>Bialetti modellen die wél op inductie werken</h2>
<p>Bialetti heeft de afgelopen jaren meerdere modellen in roestvrij staal (RVS) gelanceerd, specifiek voor de groeiende markt van inductieküchens. RVS is ferromagnetisch in de versies die Bialetti gebruikt, waardoor de plaat de bodem detecteert en warmte overdraagt. Deze modellen zijn herkenbaar aan hun zilverkleurige, glanzende oppervlak en zijn beschikbaar in 2 tot 10 kops.</p>
<p>De meest verkochte inductie-compatibele Bialetti is de <a href="../bialetti-venus-review.html">Bialetti Venus</a> — een volledig RVS model dat op alle kookplaten werkt: gas, elektrisch, keramisch en inductie. De Bialetti Musa is een modernere variant met een afgeronder design en vergelijkbare eigenschappen.</p>
</section>

<section id="oplossingen">
<h2>Oplossingen als je huidige Bialetti niet werkt</h2>
<p>Als je een aluminium Bialetti hebt en een inductieplaat, zijn er drie praktische opties. De meest toekomstbestendige is simpelweg de percolator vervangen door een RVS model. De investering is beperkt — een Bialetti Venus 3-kops kost tussen de veertig en vijfenvijftig euro — en je hebt daarna een percolator die op alle kookplaten werkt, nu en in de toekomst.</p>
<p>De tweede optie is een inductie-adapter: een ronde ijzeren of RVS schijf die tussen inductieplaat en percolator wordt geplaatst. De schijf absorbeert de inductie-energie en geeft die als warmte af via geleiding. Dit werkt, maar met beperkingen: de opwarmtijd verlengt met twee tot vier minuten, de warmteverdeling is minder uniform en de maximale temperatuur die de percolatorbodem bereikt is lager dan bij directe inductie. Kies voor een adapter van minimaal 3 mm dikte met een diameter gelijk aan of groter dan de percolatorbodem.</p>
<ul>
<li>Optie 1: RVS Bialetti Venus of Musa — aanbevolen voor dagelijks gebruik op inductie.</li>
<li>Optie 2: Inductie-adapter schijf — bruikbare tijdelijke oplossing, minder consistente resultaten.</li>
<li>Optie 3: Campinggas réchaud naast de inductieplaat — noodoplossing voor incidenteel gebruik.</li>
</ul>
</section>

<section id="faq">
<h2>Veelgestelde vragen</h2>
<div class="blog-faq">
<details><summary>Hoe test ik snel of mijn percolator op inductie werkt?</summary><p>De magneettest: houd een koelkastmagneet tegen de bodem van de percolator. Kleeft de magneet? Dan is het materiaal ferromagnetisch en werkt het op inductie. Laat de magneet los? Dan is de bodem aluminium of koper en werkt het niet. Deze test is 100% betrouwbaar en duurt twee seconden.</p></details>
<details><summary>Mijn percolator staat gelabeld als "inductiegeschikt" maar werkt niet. Wat nu?</summary><p>Controleer of de bodem schoon en volledig vlak is — inductie detecteert geen komvormige bodems. Controleer ook of de diameter groot genoeg is: sommige inductieplaatjes vereisen een minimale pandiameter van 12 cm. Doe de magneettest om het materiaal te bevestigen.</p></details>
<details><summary>Is er een Bialetti Brikka die op inductie werkt?</summary><p>De klassieke Brikka is van aluminium en werkt niet op inductie. Bialetti heeft recentelijk de Brikka 4-kops ook in een RVS-inductie versie uitgebracht in sommige markten — check de productspecificaties zorgvuldig voor je koopt en doe de magneettest bij ontvangst.</p></details>
<details><summary>Verliest mijn koffie smaak als ik een inductie-adapter gebruik?</summary><p>De smaak verandert marginaal. Een adapter geeft minder uniforme warmte en een langere opwarmtijd, wat de extractie iets minder consistent maakt. Voor dagelijks gebruik op inductie is een RVS model aanzienlijk beter.</p></details>
</div>
</section>
""",
)

print('All 4 articles generated.')
