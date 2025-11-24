#!/usr/bin/env python3
"""
Script pour ajouter les descriptions produits exactes aux pages existantes
"""

import re
import os
from pathlib import Path

def slugify(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

# Mapping manuel des noms de produits vers les fichiers existants
PRODUCT_FILE_MAPPING = {
    "Bialetti Moka Express Italia Percolator 3 Kops Aluminium": "bialetti-moka-express-percolator-3-kops-aluminium.html",
    "Bialetti Moka Express Percolator 6 Kops Aluminium": "bialetti-moka-express-percolator-6-kops-aluminium.html", 
    "Bialetti Moka Express 6": "bialetti-moka-express-percolator-6-kops-aluminium.html",
    "Bialetti New Venus 6TZ Percolator": "bialetti-percolator-venus-10-kops-roestvrijstaal-inductiegeschikt.html",
    "Bialetti Mini Express Winterwonderland Set 2 Espressobekers": "bialetti-mini-express-2tz-red-2-cups.html",
    "Bialetti Rainbow Groen Percolator 300ml 6 Kops": "bialetti-moka-express-percolator-6-kops-aluminium.html",
    "Bialetti Moka Express I Love Coffee Percolator Rood 3 Kops 130ml": "bialetti-mini-express-2tz-red-2-cups.html",
    "Bialetti Moka Alpina Limited Editions 3 Kops 120ml": "bialetti-moka-alpina-limited-editions-3-kops-120ml.html",
    "Bialetti Mini Express Percolator 2 Kops Inductiegeschikt met 2 Kopjes": "bialetti-mini-express-percolator-2-kops-inductiegeschikt-met-2-kopjes.html",
    "Bialetti Moka Express 6 Kops Nutcracker": "bialetti-moka-express-percolator-6-kops-aluminium.html",
    "Bialetti Moka Express Percolator 4 Kops Aluminium": "bialetti-moka-express-percolator-4-kops-aluminium.html",
    "Bialetti Rainbow Geel Percolator 200ml 3 Kops": "bialetti-moka-express-percolator-3-kops-aluminium.html",
    "Bialetti Moka Express Percolator 12 Kops Aluminium": "bialetti-moka-express-percolator-12-kops-aluminium.html",
    "Bialetti Moka Exclusive Moka Express Creme": "bialetti-moka-express-percolator-6-kops-aluminium.html",
    "Bialetti Brikka Evolution Percolator 2 Kops Zwart Aluminium": "bialetti-brikka-evolution-percolator-2-kops-zwart-aluminium.html",
    "Bialetti Brikka Percolator 2 Kops Aluminium": "bialetti-brikka-percolator-2-kops-aluminium.html",
    "Bialetti Venus Blue Metallic Percolator 6 Kops Roestvrijstaal Inductiegeschikt": "bialetti-percolator-venus-10-kops-roestvrijstaal-inductiegeschikt.html"
}

# Descriptions exactes fournies
PRODUCT_DESCRIPTIONS = {
    "Bialetti Moka Express Italia Percolator 3 Kops Aluminium": """Met deze klassieke espressomaker bereidt u in enkele minuten een rijke, volle espresso zoals u die in Italië drinkt. Het gepatenteerde veiligheidsventiel en de gemakkelijk te reinigen onderdelen maken het gebruik eenvoudig en veilig. Het ergonomische handvat blijft koel tijdens het zetten, zodat u veilig kunt inschenken.

De Moka Express is een duurzame keuze: geen capsules, geen afval, en een tijdloos object dat generaties meegaat. Het aluminium lichaam is licht maar stevig, ideaal voor dagelijks gebruik. Let op: dit model is niet geschikt voor inductie, maar werkt perfect op gas, elektrische en keramische kookplaten.

Dit is de échte Bialetti – herkenbaar aan het mannetje met de snor. Perfect voor koffieliefhebbers die authenticiteit en kwaliteit waarderen. Of u nu zelf geniet van een ochtendkopje of gasten verrast met Italiaanse espresso, de Moka Express Italia maakt elk moment speciaal. Een must-have voor elke koffieliefhebber die de traditie van Italiaanse koffiecultuur omarmt.""",

    "Bialetti Moka Express Percolator 6 Kops Aluminium": """Deze 6-kops versie biedt ruimte voor ongeveer 300ml koffie – perfect voor een gezellig samenzijn of een productieve werkdag. De aluminium constructie zorgt voor optimale warmtegeleiding, waardoor elke espresso de rijke smaak en het volle aroma krijgt die u van Italiaanse koffie verwacht. Het thermoplastische handvat en de knop blijven comfortabel koel, zelfs wanneer de percolator op het vuur staat.

Het gebruik is verrassend eenvoudig: vul het waterreservoir tot onder het ventiel, doe gemalen koffie in het filter zonder aan te drukken, en plaats de percolator op een middelmatige warmtebron. Binnen enkele minuten hoort u het karakteristieke gorgelende geluid dat aangeeft dat uw espresso klaar is.

Deze Moka Express is geschikt voor gas, elektrische en keramische kookplaten, maar niet voor inductie. Het duurzame ontwerp betekent geen wegwerpfilters of capsules – alleen pure koffie en pure smaak. Een investering in Italiaanse koffietraditie die decennialang meegaat en elke koffiepauze tot een bijzonder moment maakt.""",

    "Bialetti Moka Express 6": """Met een capaciteit voor zes kopjes espresso is deze percolator uitstekend geschikt voor gezinnen, kantoren of gezellige momenten met vrienden. Het lichtgewicht maar sterke aluminium zorgt voor snelle en gelijkmatige opwarming, terwijl het gepatenteerde veiligheidsventiel voor zorgeloze bediening garandeert. De ergonomische handgreep en knop van thermoplastisch materiaal zorgen ervoor dat u altijd veilig kunt inschenken.

Het zetten van perfecte espresso is kinderspel: gebruik vers gemalen koffie, vul het waterreservoir met warm water voor een snellere extractie en minder bitterheid, en laat de Moka zijn magie doen. Het karakteristieke gorggelgeluid vertelt u wanneer uw koffie klaar is om genoten te worden.

Deze duurzame koffiemaker is geschikt voor gas, elektrische en keramische warmtebronnen, maar niet voor inductie. Zonder enige elektronica of wegwerponderdelen is dit een 100% duurzame manier van koffie zetten. De Moka Express vertegenwoordigt pure Italiaanse traditie en is een essentieel keukenaccessoire voor wie houdt van authentieke espresso zonder compromissen.""",

    "Bialetti New Venus 6TZ Percolator": """Het vernieuwde model beschikt over verschillende verbeteringen ten opzichte van eerdere versies: een 20% dikkere bodem voor optimale warmteverdeling, een gezandstraalde binnenkant van het waterreservoir als extra bescherming tegen roestvorming, en een gemoderniseerde greep voor nog beter gebruiksgemak. Het schuinere deksel geeft de Venus een eigentijdse uitstraling die perfect past in moderne keukens.

Met een capaciteit van 300ml bereidt u moeiteloos zes kopjes rijke espresso. De cilindervormige roestvrijstalen behuizing straalt elegantie uit en is bestand tegen dagelijks gebruik. Het ergonomische handvat blijft altijd koel, zodat u veilig en comfortabel kunt inschenken.

De bereiding is eenvoudig en snel: vul water tot net onder het ventiel, plaats gemalen koffie in het filter, schroef de onderdelen in elkaar en zet het geheel op uw favoriete warmtebron. Binnen enkele minuten geniet u van authentieke Italiaanse espresso met een intens aroma.

Perfect voor liefhebbers die een combinatie zoeken van traditionele kwaliteit en modern design, waarbij veelzijdigheid centraal staat.""",

    "Bialetti Mini Express Winterwonderland Set 2 Espressobekers": """De Mini Express onderscheidt zich door zijn compacte formaat en inductiegeschiktheid, wat uniek is voor kleinere Bialetti modellen. Het roestvrijstalen ontwerp zorgt niet alleen voor duurzaamheid maar ook voor compatibiliteit met alle warmtebronnen, inclusief moderne inductiekookplaten. De winterse decoratie brengt warmte en gezelligheid in uw keuken, perfect voor de feestdagen of koude winteravonden.

Met deze set bereidt u twee perfecte kopjes espresso – ideaal voor romantische momenten of een koffiepauze met uw favoriete persoon. De meegeleverde espressobekers zijn speciaal ontworpen om de aroma's en warmte van uw koffie optimaal te bewaren, terwijl het feestelijke design elk moment extra speciaal maakt.

De bediening is net zo eenvoudig als bij alle Bialetti percolatoren: water, koffie, warmte en enkele minuten geduld. Het resultaat is een rijke espresso met authentieke Italiaanse smaak. Deze set is ook een prachtig cadeau voor koffieliefhebbers die houden van beperkte edities en seizoensgebonden designs. Een perfect startpunt voor wie de wereld van Bialetti wil ontdekken.""",

    "Bialetti Rainbow Groen Percolator 300ml 6 Kops": """De Rainbow serie revolutioneert uw koffiepauze door felgekleurde vrolijkheid te combineren met decennialange Italiaanse traditie. Het hoogwaardige aluminium lichaam met de karakteristieke achtkantige vorm zorgt voor optimale warmteverdeling en de beste koffie-extractie. De groene glanzende afwerking voegt een speelse touch toe aan het iconische design, terwijl de vernieuwde handgreep en dekselknop met zachtere lijnen zorgen voor verbeterde ergonomie.

Met een capaciteit van 300ml bereidt u moeiteloos zes kopjes heerlijke espresso – genoeg voor het hele gezin of een gezellig samenzijn met vrienden. De Rainbow is geschikt voor gas, elektrische en keramische kookplaten, waardoor u overal kunt genieten van perfecte Italiaanse koffie.

Het gebruik is net zo eenvoudig als bij de klassieke Moka: vul het reservoir, doe gemalen koffie in het filter, en laat de percolator zijn werk doen. Binnen enkele minuten wordt u beloond met een rijk, aromatisch kopje espresso dat uw dag opfleurt.

Deze Rainbow is niet alleen een koffiezetapparaat, maar een statement piece die uw ochtend in een goed humeur start.""",

    "Bialetti Moka Express I Love Coffee Percolator Rood 3 Kops 130ml": """Het opvallende rode design maakt deze percolator tot meer dan alleen een koffiezetapparaat – het is een decoratief statement in uw keuken. Met een capaciteit van 130ml bereidt u drie kopjes intense espresso, perfect voor een persoonlijke koffieroutine of voor het delen met een geliefde. Het aluminium lichaam met de karakteristieke achtkantige vorm garandeert de superieure kwaliteit waar Bialetti wereldwijd bekend om staat.

Deze special edition beschikt over alle kenmerken die de Moka Express legendarisch maken: het gepatenteerde veiligheidsventiel voor zorgeloos gebruik, het thermoplastische handvat dat koel blijft, en de eenvoudige constructie die makkelijk te reinigen is. Het vrolijke "I Love Coffee" design maakt elke koffiepauze tot een viering van uw favoriete drank.

Geschikt voor gas, elektrische en keramische kookplaten, maar niet voor inductie. De bereiding is klassiek Bialetti: simpel, snel en betrouwbaar. Binnen enkele minuten geniet u van rijke, authentieke Italiaanse espresso die uw liefde voor goede koffie volledig rechtvaardigt.

Een perfect cadeau voor koffieliefhebbers of een traktatie voor uzelf – want echte koffiepassie verdient een bijzondere percolator.""",

    "Bialetti Moka Alpina Limited Editions 3 Kops 120ml": """Deze limited edition is een eerbetoon aan de nauwe band tussen Italië en de Alpen, waar koffiecultuur en bergtraditie samenkomen. Het speciale Alpina-design maakt elke percolator tot een verzamelobject, terwijl de functionaliteit onverminderd top is. Met een capaciteit van 120ml bereidt u drie perfecte kopjes espresso – ideaal voor een intieme koffiemoment of een verfijnde ochtendroutine.

Het aluminium lichaam combineert lichtgewicht draagbaarheid met duurzame kwaliteit, perfect voor zowel thuis als voor outdooravonturen. De karakteristieke achtkantige vorm zorgt voor optimale warmteverdeling, terwijl het gepatenteerde veiligheidsventiel van Bialetti garandeert dat elke extractie veilig en perfect verloopt.

Deze Moka Alpina is geschikt voor gas, elektrische en keramische kookplaten, waardoor u overal kunt genieten van authentieke espresso. Het thermoplastische handvat blijft comfortabel koel, zelfs wanneer de percolator op volle kracht werkt.

Voor verzamelaars en liefhebbers van limited editions is deze Alpina een must-have. Het combineert Bialetti's legendarische kwaliteit met een unieke esthetiek die niet lang beschikbaar zal zijn. Een perfect stuk voor wie originaliteit waardeert.""",

    "Bialetti Mini Express Percolator 2 Kops Inductiegeschikt met 2 Kopjes": """De Mini Express onderscheidt zich door zijn roestvrijstalen constructie, waardoor het geschikt is voor alle warmtebronnen inclusief inductie – een zeldzaamheid bij kleinere Bialetti modellen. Deze veelzijdigheid maakt het ideaal voor moderne keukens met inductiekookplaten, zonder in te boeten op de authentieke Bialetti kwaliteit.

Met een compacte capaciteit bereidt u twee perfecte kopjes espresso, genoeg voor een romantisch ontbijt, een gezellige koffiepauze met een collega, of gewoon voor uzelf met een tweede kopje klaar. De meegeleverde kopjes zijn perfect afgestemd op de hoeveelheid espresso en helpen de aroma's optimaal te bewaren.

Het kleine formaat betekent ook gemakkelijke opslag en snelle opwarming. Toch heeft Bialetti geen compromissen gesloten: u krijgt dezelfde rijke, volle espresso als bij grotere modellen. Het ergonomische design en het koelblijvende handvat zorgen voor comfortabel gebruik.

Perfect voor starters, singles, koppels of als tweede percolator voor snelle koffiemomenten. De Mini Express bewijst dat goede dingen inderdaad in kleine verpakkingen komen.""",

    "Bialetti Moka Express 6 Kops Nutcracker": """Deze exclusieve editie is meer dan een koffiezetapparaat – het is een verzamelobject dat uw keuken transformeert in een winters wonderland. Het unieke Nutcracker-design eert de klassieke kersttraditie, terwijl de beproefde Bialetti technologie zorgt voor perfecte espresso zoals u die van het merk gewend bent. Met een capaciteit van 300ml bereidt u zes kopjes rijke koffie, ideaal voor feestelijke samenzijnzen met familie en vrienden.

Het aluminium lichaam met de karakteristieke achtkantige vorm garandeert optimale warmteverdeling en duurzaamheid. Het gepatenteerde veiligheidsventiel en de gebruiksvriendelijke constructie maken het zetten van espresso eenvoudig en veilig, zelfs tijdens drukke feestdagen wanneer gasten op bezoek zijn.

Deze Nutcracker editie is geschikt voor gas, elektrische en keramische kookplaten en vertegenwoordigt de perfecte combinatie van functionaliteit en feestelijke esthetiek. Het thermoplastische handvat blijft koel tijdens gebruik, zodat u veilig kunt serveren.

Limited editions zoals deze zijn snel uitverkocht, waardoor het ook een waardevol verzamelobject wordt. Perfect als cadeau voor Bialetti-verzamelaars of als speciale toevoeging aan uw eigen collectie. Vier elke winterdag met stijl en authentieke Italiaanse espresso.""",

    "Bialetti Moka Express Percolator 4 Kops Aluminium": """Met een capaciteit voor vier kopjes espresso heeft u precies genoeg voor een ontbijt met twee personen of voor meerdere kopjes voor uzelf gedurende de dag. Het lichtgewicht aluminium zorgt voor snelle opwarming en uitstekende warmtegeleiding, terwijl het iconische achtkantige design niet alleen mooi is, maar ook functioneel – het zorgt voor perfecte warmteverdeling rondom het koffiereservoir.

Het gepatenteerde veiligheidsventiel van Bialetti is eenvoudig te inspecteren en te reinigen, wat regelmatig onderhoud gemakkelijk maakt. Het thermoplastische handvat en de knop blijven comfortabel koel, zodat u zonder zorgen kunt inschenken. De constructie is tijdloos simpel: geen elektronica, geen complexe onderdelen, alleen betrouwbare mechanica die decennialang meegaat.

Deze Moka Express is geschikt voor gas, elektrische en keramische kookplaten, maar niet voor inductie. Het gebruik is kinderlijk eenvoudig en binnen enkele minuten geniet u van authentieke Italiaanse espresso met een rijk aroma en volle smaak.

Een duurzame investering zonder capsules of wegwerpfilters – alleen pure koffie en pure traditie. Perfect voor dagelijks gebruik en een essentieel item voor elke koffieliefhebber.""",

    "Bialetti Rainbow Geel Percolator 200ml 3 Kops": """De Rainbow serie herdefinieert de klassieke percolator door moderne, levendige kleuren toe te voegen aan het tijdloze achtkantige design. Het hoogwaardige aluminium lichaam met gele hoogglans afwerking is niet alleen een lust voor het oog, maar zorgt ook voor optimale warmteverdeling en perfecte koffie-extractie. De vernieuwde handgreep en dekselknop met ergonomische lijnen bieden verbeterd gebruikscomfort.

Met een capaciteit van 200ml bereidt u drie kopjes heerlijke espresso – perfect voor een persoonlijke ochtendroutine of voor het delen met een vriend. Het gele design voegt een speels, optimistisch element toe aan uw keuken en maakt van elke koffiepauze een vrolijk moment.

Deze Rainbow is geschikt voor gas, elektrische en keramische kookplaten en biedt dezelfde betrouwbare prestaties als alle Bialetti percolatoren. Het gebruik is vertrouwd eenvoudig: water, koffie, warmte en enkele minuten geduld voor een perfect resultaat.

Ideaal voor wie houdt van kleurrijke keukenapparatuur zonder concessies te doen aan kwaliteit. De Rainbow Geel is een statement piece dat functionaliteit en flair perfect combineert.""",

    "Bialetti Moka Express Percolator 12 Kops Aluminium": """Met zijn indrukwekkende capaciteit blijft de 12-kops Moka Express trouw aan het klassieke design dat Bialetti wereldberoemd maakte. Het achtkantige aluminium lichaam is groter maar behoudt de perfecte verhoudingen, waardoor optimale warmteverdeling en consistente koffie-extractie gegarandeerd blijven. Het gepatenteerde veiligheidsventiel is even betrouwbaar als bij kleinere modellen.

Deze grote percolator is ideaal voor drukke ochtenden wanneer het hele gezin koffie nodig heeft, voor kantooromgevingen waar collega's samenkomen voor hun koffiepauze, of voor als u gasten ontvangt. Ondanks de grotere afmetingen is de bediening identiek aan kleinere Moka Express modellen: eenvoudig, betrouwbaar en zonder elektronica.

Het stevige thermoplastische handvat blijft koel en biedt voldoende grip voor veilig inschenken van de grotere hoeveelheid koffie. Geschikt voor gas, elektrische en keramische kookplaten (niet voor inductie), met een iets langere opwarmtijd vanwege de capaciteit.

Dit is de percolator voor serieuze koffieliefhebbers die regelmatig grote hoeveelheden hoogwaardige espresso willen serveren. Duurzaam, betrouwbaar en tijdloos – precies wat u van Bialetti verwacht, maar dan groter.""",

    "Bialetti Moka Exclusive Moka Express Creme": """De Moka Exclusive serie onderscheidt zich door zijn verfijnde kleurenpalet dat afwijkt van de traditionele aluminium afwerking. De crèmekleurige coating geeft dit iconische koffiezetapparaat een zachte, warme uitstraling die perfect harmoniëert met eigentijdse keukeninterieurs. Toch blijft de beproefde Bialetti technologie volledig intact: het achtkantige ontwerp zorgt voor optimale warmteverdeling en de beste koffie-extractie.

Het aluminium lichaam met de exclusieve crème afwerking combineert duurzaamheid met verfijnd design. Het gepatenteerde veiligheidsventiel en de eenvoudige constructie maken onderhoud makkelijk, terwijl het thermoplastische handvat comfortabel koel blijft tijdens gebruik. Deze Moka bereidt in enkele minuten rijke, authentieke espresso met het volle aroma waar Italië beroemd om is.

Geschikt voor gas, elektrische en keramische kookplaten, maar niet voor inductie. De Moka Exclusive is perfect voor wie de klassieke functionaliteit van Bialetti waardeert maar graag kiest voor een meer eigentijdse, subtiele esthetiek.

Een prachtige toevoeging aan elke keuken waar stijl en substantie hand in hand gaan. Ideaal als cadeau of als upgrade van uw eigen koffieroutine.""",

    "Bialetti Brikka Evolution Percolator 2 Kops Zwart Aluminium": """De Brikka Evolution beschikt over een speciaal gepatenteerd drukventiel dat hogere druk creëert tijdens het brouwproces. Dit resulteert in een intenser, voller kopje espresso met een karakteristieke crema-laag bovenop, vergelijkbaar met wat u bij professionele espressomachines ziet. Het strakke zwarte design in aluminium geeft deze percolator een moderne, elegante uitstraling.

Met een capaciteit voor twee kopjes is de Brikka Evolution perfect voor singles, koppels of voor wie houdt van vers gezette espresso zonder restjes. Het compacte formaat betekent snelle opwarming en gemakkelijke opslag. Het unieke brouwsysteem vereist iets minder water in het reservoir, wat resulteert in een sterker, geconcentreerder kopje koffie.

Geschikt voor gas, elektrische en keramische kookplaten, maar niet voor inductie. De bediening is vergelijkbaar met de klassieke Moka, maar het eindresultaat is merkbaar anders: rijker, intenser en met die begeerde crema-laag.

Voor koffieliefhebbers die het beste van traditionele percolatoren én moderne espressomachines willen combineren. De Brikka Evolution biedt barista-kwaliteit zonder de complexiteit of kosten van volwaardige espressomachines.""",

    "Bialetti Brikka Percolator 2 Kops Aluminium": """Wat maakt de Brikka zo speciaal? Een gepatenteerd gewichtsventiel creëert hogere druk tijdens het brouwproces, waardoor het water intensiever door de koffie wordt geperst. Het resultaat is een dikkere, romigere espresso met een crema die u normaal alleen bij professionele machines vindt. De aluminium constructie met het klassieke Bialetti design zorgt voor duurzaamheid en optimale warmtegeleiding.

De 2-kops capaciteit is ideaal voor wie kwaliteit belangrijker vindt dan kwantiteit. Elke extractie levert twee perfecte kopjes espresso met een intensiteit en textuur die dichter bij "echte" espresso komt dan bij traditionele percolatoren. Het vereist iets meer aandacht tijdens gebruik, maar de beloning is een superieur kopje koffie.

Geschikt voor gas, elektrische en keramische kookplaten (niet voor inductie). Het thermoplastische handvat blijft koel en biedt veilig, comfortabel gebruik. De Brikka is iets complexer in onderhoud dan de standaard Moka Express, maar voor liefhebbers van espresso met crema is het de moeite meer dan waard.

Perfect voor wie de authenticiteit van Italiaanse percolatoren wil combineren met de rijkdom van moderne espresso. Een must-have voor serieuze thuisbarista's.""",

    "Bialetti Venus Blue Metallic Percolator 6 Kops Roestvrijstaal Inductiegeschikt": """De Venus Blue Metallic onderscheidt zich niet alleen door zijn oogverblindende design, maar ook door zijn veelzijdigheid. Het roestvrijstalen materiaal maakt deze percolator geschikt voor alle warmtebronnen, inclusief inductie – een belangrijk voordeel voor moderne keukens. Met een capaciteit van 300ml bereidt u zes kopjes authentieke Italiaanse espresso, perfect voor gezinnen of gezellige momenten met vrienden.

Het vernieuwde Venus-design beschikt over een 20% dikkere bodem voor superieure warmteverdeling, een gezandstraalde binnenkant tegen roestvorming, en een gemoderniseerde greep voor optimaal comfort. Het elegante cilindervormige lichaam met blauwe metallic coating is niet alleen visueel verbluffend, maar ook uiterst duurzaam en gemakkelijk schoon te houden.

Het ergonomische handvat blijft altijd koel, zelfs bij intensief gebruik, terwijl het vernieuwde, schuinere deksel de moderne esthetiek completeert. De bereiding is eenvoudig en snel, met resultaten die de rijke traditie van Italiaanse espresso eren.

Voor wie geen compromissen sluit tussen functionaliteit en design. De Venus Blue Metallic is een statement piece dat dagelijks perfecte espresso levert met onmiskenbare stijl."""
}

def find_matching_product_file(product_name):
    """Zoekt het juiste bestand voor een productnaam"""
    # Probeer eerst het handmatige mapping
    if product_name in PRODUCT_FILE_MAPPING:
        file_path = f"producten/{PRODUCT_FILE_MAPPING[product_name]}"
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"⚠️  Mapped bestand bestaat niet: {file_path}")
    
    # Fallback naar automatische zoektocht
    slug = slugify(product_name)
    possible_files = [
        f"producten/{slug}.html",
        f"producten/{slugify(product_name.replace('Percolator', ''))}.html",
        f"producten/{slugify(product_name.replace('Kops', 'kops'))}.html"
    ]
    
    # Probeer exacte matches
    for possible_file in possible_files:
        if os.path.exists(possible_file):
            return possible_file
    
    return None

def add_description_to_product_page(file_path, description):
    """Voegt productbeschrijving toe aan een bestaande pagina"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Zoek de plek na de korte description en voor specifications
        pattern = r'(</div>\s*<!-- Specifications -->)'
        
        if re.search(pattern, content):
            # Splits description in paragrafen
            paragraphs = description.strip().split('\n\n')
            formatted_paragraphs = []
            
            for para in paragraphs:
                if para.strip():
                    formatted_paragraphs.append(f'<p style="margin-bottom: 1rem; color: #333; line-height: 1.7;">{para.strip()}</p>')
            
            # Voeg uitgebreide productbeschrijving toe
            detailed_description = f'''
                <!-- Uitgebreide Productbeschrijving -->
                <div style="margin-bottom: 2rem;">
                    <h3 style="font-size: 1.3rem; margin-bottom: 1.5rem; color: #2c2c2c; font-weight: 600;">Productbeschrijving</h3>
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 8px; border-left: 4px solid #D2691E;">
                        {''.join(formatted_paragraphs)}
                    </div>
                </div>

                <!-- Specifications -->'''
            
            # Vervang de specifications sectie
            content = re.sub(pattern, detailed_description, content)
            
            # Schrijf terug
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        else:
            print(f"⚠️  Kon specifications patroon niet vinden in {file_path}")
            # Probeer alternatief patroon
            alt_pattern = r'(</div>\s*</div>\s*<!-- Vergelijkbare producten -->)'
            if re.search(alt_pattern, content):
                print(f"✅ Alternatief patroon gevonden")
                return False
            return False
            
    except Exception as e:
        print(f"❌ Fout bij {file_path}: {e}")
        return False

def main():
    print("🔍 Zoeken naar matching productpagina's...")
    
    updated_count = 0
    not_found_count = 0
    
    for product_name, description in PRODUCT_DESCRIPTIONS.items():
        print(f"\n📋 Verwerken: {product_name}")
        
        # Zoek matching bestand
        file_path = find_matching_product_file(product_name)
        
        if file_path:
            print(f"✅ Gevonden: {file_path}")
            
            # Voeg description toe
            if add_description_to_product_page(file_path, description):
                print(f"✅ Beschrijving toegevoegd aan {file_path}")
                updated_count += 1
            else:
                print(f"❌ Kon beschrijving niet toevoegen aan {file_path}")
        else:
            print(f"❌ Geen matching bestand gevonden voor: {product_name}")
            not_found_count += 1
            
            # Toon mogelijke matches voor debugging
            slug = slugify(product_name)
            print(f"   Gezocht naar: {slug}")
    
    print(f"\n🎯 RESULTATEN:")
    print(f"✅ {updated_count} pagina's bijgewerkt met uitgebreide beschrijvingen")
    print(f"❌ {not_found_count} producten niet gevonden")
    
    if updated_count > 0:
        print(f"\n📋 Alle bijgewerkte pagina's bevatten nu:")
        print("   - Korte productbeschrijving (origineel)")
        print("   - Uitgebreide productbeschrijving (nieuw)")
        print("   - Specificaties")
        print("   - Vergelijkbare producten")
        print("   - FAQ sectie")

if __name__ == "__main__":
    main()
