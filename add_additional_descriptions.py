#!/usr/bin/env python3
"""
Script pour ajouter les descriptions supplémentaires aux pages produits
"""

import re
import os
from pathlib import Path

# Mapping des nouvelles descriptions par fichier
ADDITIONAL_DESCRIPTIONS = {
    "bialetti-moka-express-4-kops-carosello-espresso-kop-en-schotel-4-stuks.html": """Het Carosello servies vertelt een uniek verhaal: op elk schoteltje vind je een stap uit het bereidingsproces van perfecte espresso met de Moka Express. Een charmante reis door de tijd die herinneringen oproept en tradities doorgeeft van generatie op generatie. Het witte porselein met het karakteristieke Bialetti-mannetje maakt elke koffiepauze tot een visueel feest.

De 4-kops Moka Express is de perfecte middenweg tussen capaciteit en compactheid. Het aluminium lichaam met het tijdloze achtkantige ontwerp zorgt voor optimale warmteverdeling en authentieke espresso zoals u die in Italië drinkt. Het gepatenteerde veiligheidsventiel en het koelblijvende thermoplastische handvat garanderen veilig en comfortabel gebruik.

Met een capaciteit van ongeveer 200ml bereidt u vier kopjes rijke espresso – precies genoeg voor de meegeleverde kopjes. De elegante porseleinen kopjes met capaciteit van 50ml zijn perfect afgestemd op de hoeveelheid espresso en helpen de aroma's optimaal te bewaren.

Deze complete set is ideaal als cadeau of om uzelf te trakteren op een volledige Italiaanse koffie-ervaring. Geschikt voor gas, elektrische en keramische kookplaten. Pure authenticiteit van koffiebereiding tot serveren.""",

    "bialetti-moka-express-3-kops-nutcracker.html": """Deze verzameledition combineert het iconische Moka Express ontwerp met charmante notenkraker-illustraties die de klassieke kersttraditie eren. Het is meer dan een koffiezetapparaat – het is een decoratief kunstwerk dat uw keuken transformeert in een winters wonderland. Met een capaciteit van ongeveer 120-130ml bereidt u drie kopjes rijke espresso, ideaal voor intieme momenten of een feestelijk ontbijt.

Het aluminium lichaam behoudt alle kwaliteitskenmerken van de klassieke Moka Express: de achtkantige vorm voor optimale warmteverdeling, het gepatenteerde veiligheidsventiel voor zorgeloos gebruik, en het thermoplastische handvat dat comfortabel koel blijft. De bereiding is eenvoudig en binnen enkele minuten geniet u van authentieke Italiaanse espresso.

Geschikt voor gas, elektrische en keramische kookplaten, maar niet voor inductie. Het exclusieve Nutcracker-design maakt deze percolator tot een waardevol verzamelobject dat snel uitverkocht zal zijn. Perfect als uniek cadeau voor Bialetti-verzamelaars of als speciale toevoeging aan uw eigen collectie.

Vier elke winterse ochtend met stijl, traditie en de onweerstaanbare charme van de notenkraker.""",

    "bialetti-moka-express-3-kops-carosello-espresso-kop-en-schotel-4-stuks.html": """Het bijzondere aan het Carosello servies is het educatieve en nostalgische verhaal dat het vertelt. Elk schoteltje toont een stap in het bereidingsproces van espresso met de Moka Express, van water toevoegen tot het inschenken van de perfecte kop koffie. Het witte porselein met het herkenbare Bialetti-mannetje maakt dit servies tot een gespreksstarter en een prachtige manier om de koffietraditie door te geven.

De 3-kops Moka Express is de meest populaire maat – perfect voor singles, koppels of een kleine gezin. Het lichtgewicht aluminium met de karakteristieke achtkantige vorm zorgt voor snelle opwarming en optimale warmtegeleiding. Het gepatenteerde veiligheidsventiel en het ergonomische handvat maken het gebruik eenvoudig en veilig.

De vier meegeleverde espressokopjes hebben elk een capaciteit van 50ml – ideaal voor het genieten van rijke, aromatische espresso. Ze zijn speciaal ontworpen door Bialetti met zachte, harmonieuze lijnen die de smaakervaring versterken.

Geschikt voor gas, elektrische en keramische kookplaten. Een prachtig geschenkset of de perfecte upgrade voor uw eigen koffieroutine – van bereiding tot presentatie volledig Italiaans.""",

    "bialetti-moka-express-2-kops-carosello-espresso-kop-en-schotel-4-stuks.html": """De 2-kops Moka Express is de kleinste variant in de klassieke serie, ideaal wanneer u verse espresso voor één of twee personen wilt zetten zonder verspilling. Het compacte formaat betekent snelle opwarming en gemakkelijke opslag, terwijl de kwaliteit en smaak identiek blijven aan grotere modellen. Het aluminium lichaam met achtkantig design garandeert optimale warmteverdeling en duurzaamheid.

Het Carosello servies voegt een extra dimensie toe aan uw koffie-ervaring. De vier witte porseleinen kopjes en schotels zijn versierd met het complete verhaal van espresso-bereiding met de Moka Express – een visuele reis die nostalgie oproept en tradities deelt. Elk kopje heeft een capaciteit van 50ml, perfect afgestemd op de rijke espresso die de Moka produceert.

Het gepatenteerde veiligheidsventiel en het koelblijvende thermoplastische handvat maken het gebruik veilig en comfortabel. De bereiding is kinderspel: water, koffie, warmte en enkele minuten geduld voor een perfect resultaat.

Geschikt voor gas, elektrische en keramische kookplaten. Deze set is een prachtig cadeau voor startende koffieliefhebbers of een stijlvolle upgrade voor wie houdt van kleine, verfijnde koffiemomenten met authentieke presentatie.""",

    "bialetti-moka-exclusive-moka-express-groen.html": """De Moka Exclusive serie onderscheidt zich door zijn verfijnde kleurenpalet dat verder gaat dan het traditionele aluminium. De groene coating geeft dit iconische koffiezetapparaat een frisse, natuurlijke uitstraling die perfect past in zowel klassieke als eigentijdse keukeninterieurs. Ondanks de moderne esthetiek blijft de beproefde Bialetti-technologie volledig intact.

Het aluminium lichaam met de karakteristieke achtkantige vorm zorgt voor optimale warmteverdeling en perfecte koffie-extractie. Het gepatenteerde veiligheidsventiel garandeert veilig gebruik, terwijl het thermoplastische handvat comfortabel koel blijft tijdens het zetten. Deze percolator bereidt in enkele minuten rijke, authentieke Italiaanse espresso met het volle aroma en de intense smaak waar het land beroemd om is.

De groene afwerking is niet alleen visueel aantrekkelijk maar ook duurzaam, bestand tegen dagelijks gebruik. Geschikt voor gas, elektrische en keramische kookplaten, maar niet voor inductie. De bediening is klassiek Bialetti: eenvoudig, betrouwbaar en zonder onnodige complexiteit.

Perfect voor wie houdt van kleur en persoonlijkheid in de keuken zonder in te boeten op functionaliteit. De Moka Exclusive Groen is een statement piece voor moderne koffieliefhebbers met stijl.""",

    "bialetti-moka-elektrikka-percolator-2-kops-aluminium-elektrisch-230v.html": """De Elektrikka is een elegante fusie van traditie en technologie. Het vertrouwde aluminium lichaam met het iconische Bialetti-design zorgt voor dezelfde rijke, volle espresso als de klassieke stovetop modellen, maar met de eenvoud van een aan/uit-knop. Geen gaspit of kookplaat nodig – alleen een stopcontact en enkele minuten geduld.

Met een capaciteit van ongeveer 90ml bereidt u twee perfecte kopjes espresso, ideaal voor een snelle koffiepauze of een intiem moment. De elektrische basis is gemaakt van duurzaam kunststof met een LED-indicatielampje dat aangeeft wanneer het apparaat actief is. Het gegoten aluminium bovengedeelte garandeert optimale warmtegeleiding en smaakbehoud.

Het gebruik is verrassend eenvoudig: vul water en koffie zoals bij een traditionele Moka, sluit het aan op het stopcontact, en wacht tot uw espresso klaar is. De bereiding is automatisch en betrouwbaar. Reiniging gebeurt handmatig zonder detergenten om de levensduur en smaak te behouden.

Perfect voor wie de authenticiteit van Bialetti waardeert maar meer flexibiliteit wil in waar en hoe ze koffie zetten. Ideaal voor op reis, op kantoor of in student- en hotelkamers.""",

    "bialetti-mini-express-zwart-2-kops.html": """De Mini Express onderscheidt zich door zijn roestvrijstalen constructie, wat niet alleen zorgt voor een luxe, duurzame afwerking maar ook voor geschiktheid op alle warmtebronnen, inclusief inductie. Dit maakt het een veelzijdige keuze voor elke keuken. Het compacte formaat is ideaal voor singles, koppels of als tweede percolator voor snelle koffiemomenten.

Met een capaciteit voor twee kopjes espresso bereidt u precies genoeg voor een romantisch ontbijt, een koffiepauze met een vriend, of gewoon voor uzelf met een tweede kopje klaar. Het zwarte design geeft deze Mini Express een moderne, professionele uitstraling die opvalt zonder opdringerig te zijn.

Het ergonomische handvat blijft comfortabel koel tijdens gebruik, terwijl de eenvoudige bediening identiek is aan alle Bialetti modellen. Binnen enkele minuten geniet u van rijke, authentieke espresso met hetzelfde aroma en dezelfde intensiteit als bij grotere modellen.

Geschikt voor alle warmtebronnen inclusief inductie. Perfect voor wie houdt van minimalistische esthetiek en compacte functionaliteit zonder in te boeten op de kwaliteit van hun espresso. Een stijlvolle toevoeging aan elke moderne keuken.""",

    "bialetti-mini-express-2tz-red-2-cups.html": """De Mini Express in rood is meer dan een koffiezetapparaat – het is een statement piece dat uw aanrecht opheldert. Het roestvrijstalen lichaam met rode afwerking zorgt niet alleen voor een oogverblindende uitstraling, maar maakt deze percolator ook geschikt voor alle warmtebronnen inclusief inductie. Deze veelzijdigheid is bijzonder waardevol in moderne keukens.

Met een capaciteit voor twee kopjes espresso is deze Mini Express ideaal voor singles, koppels of als aanvulling op een grotere percolator voor snelle koffiemomenten. Het compacte formaat betekent snelle opwarming en gemakkelijke opslag, terwijl de kwaliteit en smaak identiek blijven aan grotere Bialetti modellen.

Het ergonomische handvat blijft comfortabel koel tijdens gebruik, en de bediening is klassiek eenvoudig: water, gemalen koffie, warmte en enkele minuten geduld voor perfecte espresso. De rode kleur voegt niet alleen visuele aantrekkingskracht toe, maar maakt dit model ook gemakkelijk herkenbaar in een drukke keuken.

Geschikt voor alle kookplaten inclusief inductie. Perfect voor wie houdt van felle kleuren en compacte functionaliteit zonder in te boeten op authenticiteit en kwaliteit.""",

    "bialetti-inductieplaatje-voor-inductiekooplaat-o13cm.html": """Steeds meer huishoudens stappen over op inductie koken, en nieuwbouwwoningen hebben vaak geen gasaansluiting meer. Dit vormde een uitdaging voor liefhebbers van aluminium percolatoren, maar Bialetti heeft de oplossing gevonden. Dit inductieplaatje wordt zelf verhit door de inductieplaat en geeft vervolgens de warmte door aan uw aluminium percolator.

Met een diameter van 13cm is dit plaatje geschikt voor Bialetti percolatoren tot 6 kopjes. Het is gemaakt van hoogwaardig staal dat perfect reageert op inductie, met een aluminium kern voor optimale warmtegeleiding. Het gebruik is eenvoudig: plaats de adapter op uw inductieplaat, zet uw percolator erop, en geniet van dezelfde perfecte espresso als voorheen.

Let op: gebruik de adapter niet op de boosterfunctie van uw inductieplaat. Kies voor een middelhoge tot lage stand voor de beste resultaten. Het plaatje is handmatig te reinigen, en hoewel vaatwasserbestendig, verdient handwassen de voorkeur om de levensduur te verlengen.

Een kleine investering die uw klassieke percolator een tweede leven geeft in moderne keukens. Perfect voor wie niet wil kiezen tussen inductie en authentieke espresso.""",

    "bialetti-easy-timer-moka-espressomaker-percolator-6-kops-elektrisch-aluminium.html": """De Easy Timer is een game-changer voor drukke ochtenden. Met de programmeerbare timerfunctie stelt u 's avonds het tijdstip in, en de volgende ochtend staat uw espresso klaar wanneer u wakker wordt. Het aluminium lichaam met het klassieke Bialetti-design garandeert dezelfde rijke, volle smaak als stovetop modellen, maar met de toegevoegde luxe van automatische bereiding.

Met een capaciteit voor zes kopjes (ongeveer 300ml) is deze percolator perfect voor gezinnen of voor wie meerdere kopjes gedurende de ochtend drinkt. De elektrische basis elimineert de noodzaak voor een kookplaat – alleen een stopcontact is voldoende. De LED-display en gebruiksvriendelijke knoppen maken programmeren kinderspel.

De automatische uitschakelfunctie zorgt ervoor dat uw koffie warm blijft zonder over te koken, terwijl het veiligheidsventiel zorgeloos gebruik garandeert. Het gegoten aluminium zorgt voor optimale warmtegeleiding en duurzaamheid.

Perfect voor drukke professionals, gezinnen of iedereen die luxe en gemak waardeert. De Easy Timer transformeert uw ochtendroutine van gehaast naar ontspannen, met de garantie van perfecte Italiaanse espresso elke dag.""",

    "bialetti-cafetiere-preziosa-350ml.html": """De Preziosa onderscheidt zich door zijn verfijnde glaswerk omgeven door een beschermende roestvrijstalen behuizing. Dit design zorgt niet alleen voor een luxe uitstraling maar ook voor veiligheid en isolatie. Met 350ml capaciteit bereidt u ongeveer 3 kopjes rijke koffie – perfect voor een ontspannen ochtend of een gezellige middag.

Het Franse pers systeem is ideaal voor het extraheren van volle koffiesmaken en natuurlijke oliën die vaak verloren gaan bij andere zetmethoden. De roestvrij stalen mesh filter scheidt de koffiedik effectief van de vloeistof, terwijl alle aroma's en smaken behouden blijven. Het ergonomische handvat en de gemakkelijk te bedienen pers maken het gebruik comfortabel.

De bereiding is eenvoudig: doe grof gemalen koffie in de kan, giet heet water erover, roer kort, laat vier minuten trekken en druk de pers langzaam naar beneden. Het resultaat is een volle, rijke koffie met diepte en complexiteit.

Perfect voor wie houdt van langzamer koffiezetten en het ritueel waardeert. De Preziosa brengt Bialetti's expertise naar de wereld van Franse persen met onmiskenbare Italiaanse stijl.""",

    "bialetti-brikka-induction-percolator-4-kops-inductiegeschikt.html": """De Brikka Induction is uniek omdat het de enige inductiegeschikte percolator is die een echte crema-laag produceert. Het speciale gewichtsventiel creëert hogere druk tijdens het brouwproces, waardoor uw espresso een rijke, romige textuur krijgt met een verleidelijke crema bovenop. Dit brengt de ervaring dichterbij professionele espressomachines, maar met de eenvoud en authenticiteit van Bialetti.

Met een capaciteit voor vier kopjes is deze percolator ideaal voor kleine gezinnen of koppels die regelmatig gasten ontvangen. Het roestvrijstalen lichaam is niet alleen geschikt voor inductie, maar ook voor alle andere warmtebronnen, waardoor het een veelzijdige keuze is. De robuuste constructie garandeert jarenlang gebruik.

Het gebruik vereist iets meer aandacht dan een standaard Moka: gebruik iets minder water en gemalen koffie dan normaal, en let op de hogere druk tijdens extractie. Het resultaat rechtvaardigt echter de extra zorg: een intense espresso met barista-kwaliteit crema.

Perfect voor serieuze koffieliefhebbers met inductie kookplaten die het beste van beide werelden willen: moderne compatibiliteit en traditionele espresso-excellentie met crema.""",

    "bialetti-brikka-espressopot-aluminium-4-kops-zilver.html": """De Brikka 4 kops onderscheidt zich door zijn unieke vermogen om een echte crema-laag te produceren, iets dat gewone Moka pots niet kunnen. Het speciale gewichtsventiel creëert hogere druk tijdens het brouwproces, waardoor water intensiever door de gemalen koffie wordt geperst. Het resultaat is een dikkere, romigere espresso met de karakteristieke crema die normaal alleen bij professionele machines voorkomt.

Het zilverkleurige aluminium lichaam combineert het klassieke Bialetti design met robuuste functionaliteit. Met een capaciteit voor vier kopjes is deze Brikka ideaal voor gezinnen, kleine kantoren of voor wie regelmatig gasten ontvangt. Elke extractie levert consistente kwaliteit met intensiteit en textuur die dichterbij "echte" espresso komt.

Het gebruik vereist iets meer aandacht dan standaard percolatoren: gebruik iets minder water dan maximaal aangegeven, en let op het karakteristieke gorgelgeluid dat aangeeft dat uw espresso klaar is. De beloning is een superieur kopje koffie met professionele allure.

Geschikt voor gas, elektrische en keramische kookplaten. Perfect voor thuisbarista's die barista-kwaliteit willen zonder de investering in dure espressomachines.""",

    "3x-dparts-rubberen-ringen-en-1-filterplaatje-geschikt-voor-6-kops-bialetti-percolator-series-moka-express-dama-break-moka-timer-rainbow.html": """De rubberen afdichtingsring is een cruciaal onderdeel van elke percolator. Deze zorgt voor een perfecte afsluiting tussen het water- en koffiereservoir, waardoor de druk optimaal opgebouwd kan worden tijdens het brouwproces. Met de tijd slijt deze ring door warmte en gebruik, wat kan leiden tot lekkage en verminderde koffiekwaliteit. Deze set bevat drie ringen, zodat u altijd een reserve heeft.

Het meegeleverde filterplaatje is het fijne zeefje dat onder de koffie ligt en voorkomt dat gemalen koffie in uw espresso terechtkomt. Regelmatige vervanging van dit filter zorgt voor optimale doorstroming en pure, heldere koffie zonder bezinksel.

Deze onderdelen zijn speciaal ontworpen voor 6-kops modellen uit de Bialetti serie: Moka Express, Dama, Break, Moka Timer en Rainbow. Ze garanderen perfecte pasvorm en functionaliteit. Regelmatig onderhoud met verse afdichtingen verlengt de levensduur van uw percolator aanzienlijk.

Een kleine investering die grote impact heeft op de prestaties van uw percolator. Perfect voor wie het maximale uit hun Bialetti wil halen en jarenlang wil blijven genieten van perfecte espresso.""",

    "3x-dparts-rubberen-ringen-en-1-filterplaatje-geschikt-voor-3-en-4-kops-bialetti-percolator-series-moka-express-dama-break-moka-timer-rainbow-alpina.html": """De rubberen afdichtingsring is het hart van de percolator – zonder een goede afdichting kan de benodigde druk niet opgebouwd worden en zal uw espresso zwak en waterig zijn. Deze ringen slijten geleidelijk door herhaalde blootstelling aan hitte en druk. Regelmatige vervanging (aanbevolen elke 6-12 maanden bij dagelijks gebruik) garandeert perfecte afsluiting en optimale extractie.

Het meegeleverde filterplaatje is het fijne zeefje dat ervoor zorgt dat alleen zuivere espresso in het bovenste reservoir komt, terwijl alle koffiedik achterblijft. Een schoon, intact filter is essentieel voor heldere koffie zonder bezinksel. Dit onderdeel kan na verloop van tijd verstopt raken of beschadigen, waardoor vervanging noodzakelijk wordt.

Deze set is compatibel met 3- en 4-kops modellen van diverse Bialetti series, waaronder de populaire Moka Express, Rainbow en Alpina limited editions. De onderdelen garanderen perfecte pasvorm en betrouwbare functionaliteit.

Een verstandige investering in het onderhoud van uw percolator. Met deze set zorgt u ervoor dat elke kop espresso net zo perfect is als de eerste."""
}

def add_description_to_page(file_path, description):
    """Voegt een productbeschrijving toe aan een bestaande pagina"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Controleer of er al een beschrijving is
        if 'Productbeschrijving' in content and 'background: #f8f9fa' in content:
            print(f"⚠️  Beschrijving al aanwezig in {os.path.basename(file_path)}")
            return False
        
        # Splits description in paragrafen
        paragraphs = description.strip().split('\n\n')
        formatted_paragraphs = []
        
        for para in paragraphs:
            if para.strip():
                formatted_paragraphs.append(f'<p style="margin-bottom: 1.5rem; color: #333; line-height: 1.7; font-size: 1rem;">{para.strip()}</p>')
        
        # Creëer de description section
        description_section = f'''
        <!-- Uitgebreide Productbeschrijving - Pleine largeur -->
        <section style="margin: 3rem 0; display: block; clear: both; width: 100%;">
            <div style="max-width: 1000px; margin: 0 auto;">
                <h3 style="font-size: 1.5rem; margin-bottom: 2rem; color: #2c2c2c; font-weight: 600; text-align: center;">Productbeschrijving</h3>
                <div style="background: #f8f9fa; padding: 2.5rem; border-radius: 12px; border-left: 4px solid #D2691E; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                    {''.join(formatted_paragraphs)}
                </div>
            </div>
        </section>
'''
        
        # Insérer avant "Vergelijkbare producten"
        pattern = r'(<!-- Vergelijkbare producten -->)'
        if re.search(pattern, content):
            content = re.sub(pattern, description_section + r'\1', content)
            
            # Écrire le fichier
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        else:
            print(f"⚠️  Pattern 'Vergelijkbare producten' non trouvé dans {os.path.basename(file_path)}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur avec {file_path}: {e}")
        return False

def main():
    print("📝 Ajout des descriptions supplémentaires...")
    
    added_count = 0
    skipped_count = 0
    
    for filename, description in ADDITIONAL_DESCRIPTIONS.items():
        file_path = f"producten/{filename}"
        
        if os.path.exists(file_path):
            print(f"\n📋 Traitement: {filename}")
            
            if add_description_to_page(file_path, description):
                print(f"✅ Description ajoutée: {filename}")
                added_count += 1
            else:
                print(f"⚠️  Ignoré (déjà présent): {filename}")
                skipped_count += 1
        else:
            print(f"❌ Fichier non trouvé: {file_path}")
    
    print(f"\n🎯 RÉSULTATS:")
    print(f"✅ {added_count} nouvelles descriptions ajoutées")
    print(f"⚠️  {skipped_count} pages ignorées (déjà présentes)")
    print(f"\n📋 Structure finale:")
    print("   1. Image + Infos produit (2 colonnes)")
    print("   2. Description détaillée (pleine largeur)")
    print("   3. Vergelijkbare producten")
    print("   4. FAQ section")

if __name__ == "__main__":
    main()
