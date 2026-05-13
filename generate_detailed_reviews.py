#!/usr/bin/env python3
"""Generate detailed review content with comprehensive template"""
import re
from pathlib import Path

# Detailed review data for each product
REVIEW_DATA = {
    'bialetti-moka': {
        'product_name': 'Bialetti Moka Express',
        'product_type': 'Italiaanse percolator',
        'target_group': 'liefhebbers van traditionele Italiaanse koffie',
        'intro': 'De Bialetti Moka Express is een Italiaanse percolator voor liefhebbers van authentieke koffie en traditionele kookmethoden. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Moka Express is vooral interessant voor traditionele koffieliefhebbers die waarde hechten aan authentieke Italiaanse ervaring. Het sterke punt van dit model is de iconische status en authentieke koffiesmaak, terwijl de beperkte inductie-compatibiliteit het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 9.5,
            'Koffiesmaak': 9.3,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.0,
            'Prijs-kwaliteit': 9.5,
            'Traditie': 10.0
        },
        'verdict': 'De Moka Express is de gouden standaard voor traditionele moka-koffie en blijft de beste keuze voor wie zoekt naar authenticiteit boven alles.',
        'pros': [
            'Authentieke Italiaanse koffiesmaak',
            'Iconisch design dat nooit veroudert',
            'Duurzaam aluminium constructie',
            'Geschikt voor alle warmtebronnen (behalve inductie)',
            'Eenvoudig in gebruik en onderhoud',
            'Goede prijs-kwaliteitverhouding',
            'Beschikbaar in verschillende maten (1-12 kops)'
        ],
        'cons': [
            'Niet geschikt voor inductiekookplaten',
            'Vergt wat oefening voor perfecte resultaten',
            'Handgreep kan heet worden',
            'Niet vaatwasserbestendig',
            'Kan lekken als niet goed afgesloten'
        ],
        'suitable_for': [
            'Traditionele koffieliefhebbers die waarde hechten aan authenticiteit',
            'Gebruikers met gas- of elektrische kookplaten',
            'Wie zoekt naar een betaalbaar maar kwalitatief hoogstaand model',
            'Liefhebbers van Italiaanse koffiecultuur',
            'Gebruikers die geen inductiekookplaat hebben'
        ],
        'not_suitable_for': [
            'Gebruikers met inductiekookplaten',
            'Wie zoekt naar volautomatische koffiebereiding',
            'Beginners die geen tijd hebben om de techniek te leren',
            'Wie regelmatig grote groepen koffie wil zetten'
        ],
        'design_p1': 'De Moka Express heeft het iconische achthoekige design dat in 1933 werd geïntroduceerd door Alfonso Bialetti. Gemaakt van hoogwaardig aluminium, straalt dit model traditie en vakmanschap uit. De zilveren kleur en de karakteristieke vorm maken het direct herkenbaar als een Bialetti.',
        'design_p2': 'De constructie is robuust en duurzaam, met een solide handgreep die comfortabel in de hand ligt. De rubberen afdichting zorgt voor een goede sluiting en voorkomt lekkage. Het ontwerp is tijdloos en past in elke keuken, van klassiek tot modern.',
        'koffiesmaak_p1': 'De Moka Express produceert een intense, aromatische koffie die dicht bij de traditionele Italiaanse espresso komt. Het unieke extractieproces zorgt voor een volle body en een rijk crema-achtige schuimlaag. De smaak is authentiek en herkenbaar als "echte" moka-koffie.',
        'koffiesmaak_p2': 'De extractie is afhankelijk van de maalgraad en de temperatuur, maar met de juiste techniek levert dit model consistente resultaten. De aluminium constructie draagt bij aan de karakteristieke smaak die veel koffieliefhebbers waarderen.',
        'usage_steps': [
            'Vul de onderste kamer met koud water tot net onder de veiligheidsklep',
            'Plaats de trechter met gemalen koffie (medium-fijne maling)',
            'Schud lichtjes om de koffie gelijkmatig te verdelen',
            'Schroef de bovenste kamer stevig vast',
            'Zet op middelhoog vuur en verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water en milde zeep',
            'Droog goed af om oxidatie te voorkomen',
            'Vervang de rubberen afdichting regelmatig',
            'Gebruik geen schuurmiddelen of metalen sponsjes'
        ],
        'comparison_table': [
            {'name': 'Bialetti Moka Express', 'usp': 'Authentieke Italiaanse ervaring', 'target': 'Traditionele liefhebbers'},
            {'name': 'Bialetti Venus', 'usp': 'Inductie-compatibel', 'target': 'Inductie-gebruikers'},
            {'name': 'Alessi Moka', 'usp': 'Design-vriendelijk', 'target': 'Design-liefhebbers'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Moka Express geschikt voor inductie?', 'answer': 'Nee, de standaard Moka Express is niet geschikt voor inductiekookplaten. Voor inductie gebruik je de Bialetti Venus of een andere RVS variant.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Venus?', 'answer': 'De Venus is gemaakt van RVS en is inductie-compatibel, terwijl de Moka Express van aluminium is en niet op inductie werkt. De Moka Express is ook goedkoper en produceert een meer traditionele smaak.'},
            {'question': 'Hoe onderhoud je de Bialetti Moka Express het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af om oxidatie te voorkomen. Vervang de rubberen afdichting elke 6-12 maanden.'},
            {'question': 'Is de prijs van de Bialetti Moka Express gerechtvaardigd?', 'answer': 'Ja, absoluut. De Moka Express is betaalbaar, duurzaam en levert consistente kwaliteit. Het is een investering die jaren meegaat.'}
        ],
        'conclusion': 'De Bialetti Moka Express is een goede keuze voor traditionele koffieliefhebbers. Zoek je vooral authenticiteit en Italiaanse traditie, dan is dit model logisch. Zoek je eerder inductie-compatibiliteit of moderne features, dan is een alternatief zoals de Bialetti Venus vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Moka Express',
            'Materiaal': 'Aluminium',
            'Capaciteit': '1-12 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwas aanbevolen'
        }
    },
    'bialetti-venus': {
        'product_name': 'Bialetti Venus',
        'product_type': 'Inductie percolator',
        'target_group': 'gebruikers met inductiekookplaten',
        'intro': 'De Bialetti Venus is een inductie percolator voor moderne keukens met inductiekookplaten. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Venus is vooral interessant voor gebruikers met inductiekookplaten die toch traditionele moka-koffie willen. Het sterke punt van dit model is de inductie-compatibiliteit, terwijl de hogere prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 9.0,
            'Koffiesmaak': 9.0,
            'Gebruiksgemak': 9.0,
            'Onderhoud': 9.0,
            'Prijs-kwaliteit': 8.5,
            'Inductie': 10.0
        },
        'verdict': 'De Venus is de beste keuze voor inductie-gebruikers die niet willen inleveren op de authentieke moka-ervaring.',
        'pros': [
            'Geschikt voor inductiekookplaten',
            'Duurzaam RVS constructie',
            'Houdt warmte langer vast',
            'Vaakwasbestendig (handwas aanbevolen)',
            'Modern en strak design',
            'Geen aluminium smaak in koffie'
        ],
        'cons': [
            'Duurder dan aluminium varianten',
            'Kan warmte minder gelijkmatig verdelen',
            'Langere opwarmtijd',
            'Handgreep kan warm worden'
        ],
        'suitable_for': [
            'Gebruikers met inductiekookplaten',
            'Wie zoekt naar duurzaam RVS materiaal',
            'Moderne keukens met strak design',
            'Wie geen aluminium smaak wil'
        ],
        'not_suitable_for': [
            'Wie zoekt naar de goedkoopste optie',
            'Beginners die snelle resultaten willen',
            'Wie aluminium prefereert voor betere warmtegeleiding'
        ],
        'design_p1': 'De Venus heeft een modern, strak design dat perfect past in hedendaagse keukens. Gemaakt van hoogwaardig roestvrij staal, is het model duurzaam en corrosiebestendig. De zilveren afwerking is tijdloos en elegant.',
        'design_p2': 'De constructie is robuust met een comfortabele handgreep die goed geïsoleerd is. De inductie-bodem is ontworpen voor optimale warmteoverdracht op inductiekookplaten.',
        'koffiesmaak_p1': 'De Venus produceert een koffie die dicht bij de traditionele moka-smaak komt, maar met een subtiele nuance door het RVS materiaal. De smaak is schoon en puur, zonder de metaalachtige ondertoon die soms met aluminium wordt geassocieerd.',
        'koffiesmaak_p2': 'De extractie is consistent en betrouwbaar. De RVS constructie houdt warmte goed vast, wat zorgt voor een stabiele extractietemperatuur en consistente resultaten.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met gemalen koffie',
            'Schroef de bovenste kamer vast',
            'Zet op inductie op middelhoog vermogen',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af om vlekken te voorkomen',
            'Vervang afdichting indien nodig',
            'Vermijd schuurmiddelen'
        ],
        'comparison_table': [
            {'name': 'Bialetti Venus', 'usp': 'Inductie-compatibel', 'target': 'Inductie-gebruikers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Authentieke ervaring', 'target': 'Traditionele liefhebbers'},
            {'name': 'Grosche Milano', 'usp': 'Budget RVS', 'target': 'Budget-kopers'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Venus geschikt voor inductie?', 'answer': 'Ja, de Venus is speciaal ontworpen voor inductiekookplaten en werkt uitstekend op alle inductie-oppervlakken.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Venus is gemaakt van RVS en werkt op inductie, terwijl de Moka Express van aluminium is en niet op inductie werkt. De Venus is ook duurder.'},
            {'question': 'Hoe onderhoud je de Bialetti Venus het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af om vlekken te voorkomen. RVS is duurzamer dan aluminium maar kan wel vlekken vertonen.'},
            {'question': 'Is de prijs van de Bialetti Venus gerechtvaardigd?', 'answer': 'Ja, voor inductie-gebruikers is de prijs gerechtvaardigd. Het is de enige manier om authentieke moka-koffie te maken op inductie.'}
        ],
        'conclusion': 'De Bialetti Venus is een goede keuze voor inductie-gebruikers. Zoek je vooral inductie-compatibiliteit en duurzaamheid, dan is dit model logisch. Zoek je eerder traditionele aluminium smaak, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Venus',
            'Materiaal': 'RVS',
            'Capaciteit': '2-6 kops',
            'Warmtebron': 'Inductie, gas, elektrisch',
            'Onderhoud': 'Handwas aanbevolen'
        }
    },
    'bialetti-brikka': {
        'product_name': 'Bialetti Brikka',
        'product_type': 'Crema percolator',
        'target_group': 'liefhebbers van espresso met crema',
        'intro': 'De Bialetti Brikka is een crema percolator voor liefhebbers van espresso met een echte crema-laag. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Brikka is vooral interessant voor liefhebbers die een echte crema-laag willen. Het sterke punt van dit model is het gepatenteerde klepsysteem voor crema, terwijl de complexiteit het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.5,
            'Koffiesmaak': 9.5,
            'Gebruiksgemak': 7.5,
            'Onderhoud': 7.0,
            'Prijs-kwaliteit': 8.0,
            'Innovatie': 10.0
        },
        'verdict': 'De Brikka is uniek in zijn soort en de beste keuze voor wie zoekt naar een echte crema-laag zonder volautomatisch apparaat.',
        'pros': [
            'Produkt een echte crema-laagje',
            'Uniek gepatenteerd klepsysteem',
            'Dichterbij espresso-ervaring',
            'Authentieke Bialetti kwaliteit',
            'Beschikbaar in verschillende maten'
        ],
        'cons': [
            'Vergt meer precisie in gebruik',
            'Kleppetje vereist onderhoud',
            'Niet voor beginners',
            'Hogere prijs',
            'Kan lastig zijn schoon te maken'
        ],
        'suitable_for': [
            'Liefhebbers van espresso met crema',
            'Gevorderde koffiemakers',
            'Wie zoekt naar innovatie',
            'Bialetti-enthousiasten'
        ],
        'not_suitable_for': [
            'Beginners',
            'Wie zoekt naar eenvoud',
            'Gebruikers met inductiekookplaten',
            'Wie budgetbewust is'
        ],
        'design_p1': 'De Brikka heeft het klassieke Bialetti design met een uniek klepsysteem in de bovenste kamer. Het aluminium constructie is van dezelfde kwaliteit als de Moka Express, met het iconische achthoekige design.',
        'design_p2': 'Het klepsysteem is het onderscheidende kenmerk. Het zorgt voor een verhoogde druk die een crema-laagje produceert. De constructie is robuust maar vereist meer aandacht bij het gebruik.',
        'koffiesmaak_p1': 'De Brikka produceert een koffie met een duidelijke crema-laag, wat uniek is voor een moka-pot. De smaak is intens en dicht bij espresso, met een rijke body en aromatische complexiteit.',
        'koffiesmaak_p2': 'De extractie is afhankelijk van de juiste techniek. Met de juiste maling en temperatuur levert dit model consistente resultaten met een prachtige crema-laag.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met medium-fijne koffie',
            'Schroef de bovenste kamer stevig vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt en het klep opent'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Reinig het kleppetje regelmatig',
            'Droog goed af',
            'Vervang afdichting indien nodig'
        ],
        'comparison_table': [
            {'name': 'Bialetti Brikka', 'usp': 'Crema-functie', 'target': 'Espresso-liefhebbers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Eenvoudig', 'target': 'Traditionele liefhebbers'},
            {'name': 'Bialetti Venus', 'usp': 'Inductie', 'target': 'Inductie-gebruikers'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Brikka geschikt voor beginners?', 'answer': 'Nee, de Brikka vereist meer ervaring en precisie. Beginners zouden beter beginnen met de Moka Express.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Brikka heeft een klepsysteem dat een crema-laagje produceert, terwijl de Moka Express traditionele moka-koffie maakt zonder crema.'},
            {'question': 'Hoe onderhoud je de Bialetti Brikka het best?', 'answer': 'Handwas met warm water. Reinig het kleppetje regelmatig om koffieresten te verwijderen. Vervang de afdichting indien nodig.'},
            {'question': 'Is de prijs van de Bialetti Brikka gerechtvaardigd?', 'answer': 'Voor liefhebbers van espresso met crema is de prijs gerechtvaardigd. Het is uniek in zijn soort en levert resultaten die anders niet mogelijk zijn met een moka-pot.'}
        ],
        'conclusion': 'De Bialetti Brikka is een goede keuze voor espresso-liefhebbers. Zoek je vooral een echte crema-laag, dan is dit model logisch. Zoek je eerder eenvoud en traditionele moka-koffie, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Brikka',
            'Materiaal': 'Aluminium',
            'Capaciteit': '2-4 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'alessi-9090': {
        'product_name': 'Alessi 9090',
        'product_type': 'Design percolator',
        'target_group': 'designliefhebbers en verzamelaars',
        'intro': 'De Alessi 9090 is een design percolator voor designliefhebbers en verzamelaars. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Alessi 9090 is vooral interessant voor designliefhebbers en verzamelaars. Het sterke punt van dit model is het iconische design van Richard Sapper, terwijl de zeer hoge prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 10.0,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Prijs-kwaliteit': 7.0,
            'Design': 10.0
        },
        'verdict': 'De 9090 is een designicoon dat perfect is voor verzamelaars, maar overpriced voor dagelijks gebruik.',
        'pros': [
            'Iconisch design van Richard Sapper',
            'Museumcollectie-waardig',
            'Uitzonderlijke bouwkwaliteit',
            'Unieke afneembare basis',
            'Verzilverd voor betere warmtegeleiding',
            'Geschenkverpakking inbegrepen'
        ],
        'cons': [
            'Zeer hoge prijs',
            'Niet voor dagelijks gebruik',
            'Kwetsbaar design',
            'Beperkte beschikbaarheid',
            'Niet vaatwasserbestendig'
        ],
        'suitable_for': [
            'Designliefhebbers',
            'Verzamelaars',
            'Wie zoekt naar een uniek geschenk',
            'Museum-enthousiasten'
        ],
        'not_suitable_for': [
            'Dagelijks gebruik',
            'Budget-kopers',
            'Wie zoekt naar functionaliteit boven design',
            'Gebruikers met kinderen'
        ],
        'design_p1': 'De 9090 is ontworpen door de legendarische Richard Sapper in 1979. Het conische design met de afneembare basis is uniek en iconisch. Het model is opgenomen in de collecties van vooraanstaande musea over de hele wereld.',
        'design_p2': 'De constructie is van uitzonderlijke kwaliteit, met verzilverde onderdelen voor betere warmtegeleiding. Het model is meer een kunstwerk dan een functioneel koffiezetapparaat.',
        'koffiesmaak_p1': 'De 9090 produceert een goede moka-koffie, vergelijkbaar met andere hoogwaardige percolators. De verzilverde onderdelen dragen bij aan een consistente extractie.',
        'koffiesmaak_p2': 'De smaak is authentiek en van goede kwaliteit, maar niet significant beter dan goedkopere modellen. Het unieke aan dit model is het design, niet de koffiesmaak.',
        'usage_steps': [
            'Verwijder de basis',
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de basis terug vast',
            'Zet op middelhoog vuur'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af om vlekken te voorkomen',
            'Polish regelmatig voor glans',
            'Berg op in de originele verpakking'
        ],
        'comparison_table': [
            {'name': 'Alessi 9090', 'usp': 'Design icon', 'target': 'Verzamelaars'},
            {'name': 'Bialetti Moka Express', 'usp': 'Betaalbaar', 'target': 'Dagelijks gebruik'},
            {'name': 'Alessi La Conica', 'usp': 'Architectonisch', 'target': 'Design-liefhebbers'}
        ],
        'faq': [
            {'question': 'Is de Alessi 9090 geschikt voor dagelijks gebruik?', 'answer': 'Niet echt. De 9090 is meer een designobject dan een functioneel apparaat. Voor dagelijks gebruik is een goedkopere optie beter.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De 9090 is een designicoon van Richard Sapper met een unieke afneembare basis, terwijl de Moka Express een functioneel apparaat is voor dagelijks gebruik.'},
            {'question': 'Hoe onderhoud je de Alessi 9090 het best?', 'answer': 'Handwas met warm water en droog goed af. Polish regelmatig voor de glans. Berg op in de originele verpakking.'},
            {'question': 'Is de prijs van de Alessi 9090 gerechtvaardigd?', 'answer': 'Voor verzamelaars en designliefhebbers is de prijs gerechtvaardigd. Voor dagelijks gebruik is het overpriced.'}
        ],
        'conclusion': 'De Alessi 9090 is een goede keuze voor designliefhebbers en verzamelaars. Zoek je vooral een uniek designobject, dan is dit model logisch. Zoek je eerder functionaliteit voor dagelijks gebruik, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Alessi',
            'Model': '9090',
            'Materiaal': 'RVS met verzilvering',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'bialetti-dama': {
        'product_name': 'Bialetti Dama',
        'product_type': 'Elegante percolator',
        'target_group': 'wie zoekt naar elegantie en stijl',
        'intro': 'De Bialetti Dama is een elegante percolator voor wie zoekt naar elegantie en stijl. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Dama is vooral interessant voor wie zoekt naar elegantie en stijl. Het sterke punt van dit model is het zachte, vrouwelijke design, terwijl de hogere prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 9.0,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.0,
            'Prijs-kwaliteit': 8.0,
            'Esthetiek': 9.5
        },
        'verdict': 'De Dama is een prachtige keuze voor wie stijl en functionaliteit wil combineren.',
        'pros': [
            'Uniek elegant design',
            'Zachte, afgeronde lijnen',
            'Comfortabele handgreep',
            'Authentieke Bialetti kwaliteit',
            'Beschikbaar in verschillende maten',
            'Geschikt voor gas en elektrisch'
        ],
        'cons': [
            'Niet voor inductie',
            'Duurder dan standaard Moka',
            'Beperkte kleuropties',
            'Kan lastiger te vinden zijn'
        ],
        'suitable_for': [
            'Wie zoekt naar elegantie',
            'Stijlbewuste gebruikers',
            'Wie comfortabele handgreep wil',
            'Vrouwelijke koffieliefhebbers'
        ],
        'not_suitable_for': [
            'Inductie-gebruikers',
            'Budget-kopers',
            'Wie zoekt naar traditioneel design',
            'Professionele gebruikers'
        ],
        'design_p1': 'De Dama heeft een zacht, elegant design met afgeronde lijnen. De handgreep is comfortabel en ergonomisch, wat het gebruik aangenaam maakt. Het model is beschikbaar in verschillende kleuren.',
        'design_p2': 'De constructie is van dezelfde kwaliteit als andere Bialetti modellen, met een focus op comfort en esthetiek. Het design is uniek en onderscheidt zich van andere modellen.',
        'koffiesmaak_p1': 'De Dama produceert een authentieke moka-koffie, vergelijkbaar met de Moka Express. De extractie is consistent en betrouwbaar.',
        'koffiesmaak_p2': 'De smaak is traditioneel en authentiek. Het model levert geen betere of slechtere koffie dan andere Bialetti modellen - het verschil is puur esthetisch.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Vervang afdichting indien nodig',
            'Vermijd schuurmiddelen'
        ],
        'comparison_table': [
            {'name': 'Bialetti Dama', 'usp': 'Elegant', 'target': 'Stijlbewuste gebruikers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Klassiek', 'target': 'Traditionele liefhebbers'},
            {'name': 'Bialetti Musa', 'usp': 'Art deco', 'target': 'Design-liefhebbers'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Dama geschikt voor inductie?', 'answer': 'Nee, de Dama is niet geschikt voor inductiekookplaten. Voor inductie gebruik je de Bialetti Venus.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Dama heeft een zacht, elegant design met een comfortabele handgreep, terwijl de Moka Express het klassieke achthoekige design heeft.'},
            {'question': 'Hoe onderhoud je de Bialetti Dama het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af en vervang de afdichting indien nodig.'},
            {'question': 'Is de prijs van de Bialetti Dama gerechtvaardigd?', 'answer': 'Voor wie waarde hecht aan elegantie en comfort is de prijs gerechtvaardigd. Voor wie puur functioneel zoekt, is de Moka Express een betere keuze.'}
        ],
        'conclusion': 'De Bialetti Dama is een goede keuze voor wie zoekt naar elegantie en stijl. Zoek je vooral een comfortabele handgreep en zacht design, dan is dit model logisch. Zoek je eerder traditioneel design, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Dama',
            'Materiaal': 'Aluminium',
            'Capaciteit': '1-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'bialetti-musa': {
        'product_name': 'Bialetti Musa',
        'product_type': 'Art deco percolator',
        'target_group': 'designliefhebbers',
        'intro': 'De Bialetti Musa is een art deco percolator voor designliefhebbers. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Musa is vooral interessant voor designliefhebbers. Het sterke punt van dit model is het art deco design, terwijl de ribbels het belangrijkste aandachtspunt blijven.',
        'specs': {
            'Design & bouwkwaliteit': 9.0,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.0,
            'Prijs-kwaliteit': 8.0,
            'Design': 9.0
        },
        'verdict': 'De Musa is een prachtige keuze voor wie zoekt naar een uniek art deco design.',
        'pros': [
            'Uniek art deco design',
            'Verticale ribbels voor grip',
            'Authentieke Bialetti kwaliteit',
            'Goede warmteverdeling',
            'Beschikbaar in verschillende maten'
        ],
        'cons': [
            'Niet voor inductie',
            'Ribbels kunnen lastig te reinigen zijn',
            'Duurder dan standaard model',
            'Beperkte beschikbaarheid'
        ],
        'suitable_for': [
            'Designliefhebbers',
            'Wie zoekt naar grip',
            'Art deco enthousiasten',
            'Bialetti verzamelaars'
        ],
        'not_suitable_for': [
            'Inductie-gebruikers',
            'Wie zoekt naar eenvoudig onderhoud',
            'Budget-kopers',
            'Wie traditioneel design prefereert'
        ],
        'design_p1': 'De Musa heeft een uniek art deco design met verticale ribbels. Het aluminium constructie is van dezelfde kwaliteit als andere Bialetti modellen, met een focus op esthetiek en functionaliteit.',
        'design_p2': 'De ribbels bieden niet alleen grip, maar ook een uniek visueel element. Het design is geïnspireerd op de gouden eeuw van Italiaanse design.',
        'koffiesmaak_p1': 'De Musa produceert een authentieke moka-koffie, vergelijkbaar met de Moka Express. De extractie is consistent en betrouwbaar.',
        'koffiesmaak_p2': 'De smaak is traditioneel en authentiek. Het model levert geen betere of slechtere koffie dan andere Bialetti modellen.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Reinig ribbels zorgvuldig',
            'Droog goed af',
            'Vervang afdichting indien nodig'
        ],
        'comparison_table': [
            {'name': 'Bialetti Musa', 'usp': 'Art deco', 'target': 'Design-liefhebbers'},
            {'name': 'Bialetti Dama', 'usp': 'Elegant', 'target': 'Stijlbewuste gebruikers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Klassiek', 'target': 'Traditionele liefhebbers'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Musa geschikt voor inductie?', 'answer': 'Nee, de Musa is niet geschikt voor inductiekookplaten. Voor inductie gebruik je de Bialetti Venus.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Musa heeft een uniek art deco design met verticale ribbels, terwijl de Moka Express het klassieke achthoekige design heeft.'},
            {'question': 'Hoe onderhoud je de Bialetti Musa het best?', 'answer': 'Handwas met warm water. Reinig de ribbels zorgvuldig om koffieresten te verwijderen. Droog goed af.'},
            {'question': 'Is de prijs van de Bialetti Musa gerechtvaardigd?', 'answer': 'Voor designliefhebbers is de prijs gerechtvaardigd. Voor wie puur functioneel zoekt, is de Moka Express een betere keuze.'}
        ],
        'conclusion': 'De Bialetti Musa is een goede keuze voor designliefhebbers. Zoek je vooral een uniek art deco design, dan is dit model logisch. Zoek je eerder traditioneel design, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Musa',
            'Materiaal': 'Aluminium',
            'Capaciteit': '2-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'alessi-pulcina': {
        'product_name': 'Alessi Pulcina',
        'product_type': 'Innovatieve percolator',
        'target_group': 'innatieveliefhebbers',
        'intro': 'De Alessi Pulcina is een innovatieve percolator voor liefhebbers van innovatie. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Alessi Pulcina is vooral interessant voor liefhebbers van innovatie. Het sterke punt van dit model is de geoptimaliseerde extractie, terwijl de hoge prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 9.5,
            'Koffiesmaak': 9.0,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Prijs-kwaliteit': 7.5,
            'Innovatie': 9.0
        },
        'verdict': 'De Pulcina is een innovatieve keuze voor wie zoekt naar geoptimaliseerde koffie-extractie.',
        'pros': [
            'Innovatief ontwerp van Michele De Lucchi',
            'Geoptimaliseerde koffie-extractie',
            'Unieke vormgeving',
            'Hoge kwaliteit constructie',
            'Verkrijgbaar in verschillende uitvoeringen'
        ],
        'cons': [
            'Hoge prijs',
            'Vormgeving vergt gewenning',
            'Niet voor inductie',
            'Beperkte maten beschikbaar'
        ],
        'suitable_for': [
            'Innovatie-liefhebbers',
            'Wie zoekt naar optimale extractie',
            'Design-enthousiasten',
            'Alessi fans'
        ],
        'not_suitable_for': [
            'Budget-kopers',
            'Inductie-gebruikers',
            'Wie zoekt naar eenvoud',
            'Beginners'
        ],
        'design_p1': 'De Pulcina heeft een uniek ontwerp van Michele De Lucchi. De vorm is geoptimaliseerd voor een betere koffie-extractie met een speciale tuit die de stroom van koffie controleert.',
        'design_p2': 'De constructie is van hoge kwaliteit met aandacht voor detail. Het model is een perfecte balans tussen vorm en functie.',
        'koffiesmaak_p1': 'De Pulcina produceert een koffie met een geoptimaliseerde extractie dankzij het unieke ontwerp. De smaak is intens en aromatisch.',
        'koffiesmaak_p2': 'De speciale tuit zorgt voor een betere extractie en een consistente smaak. Het model levert resultaten die dicht bij espresso komen.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Reinig de tuit zorgvuldig',
            'Vervang afdichting indien nodig'
        ],
        'comparison_table': [
            {'name': 'Alessi Pulcina', 'usp': 'Innovatie', 'target': 'Innovatie-liefhebbers'},
            {'name': 'Bialetti Brikka', 'usp': 'Crema', 'target': 'Espresso-liefhebbers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Eenvoudig', 'target': 'Traditionele liefhebbers'}
        ],
        'faq': [
            {'question': 'Is de Alessi Pulcina geschikt voor inductie?', 'answer': 'Nee, de Pulcina is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Pulcina heeft een uniek ontwerp met geoptimaliseerde extractie, terwijl de Moka Express traditioneel is.'},
            {'question': 'Hoe onderhoud je de Alessi Pulcina het best?', 'answer': 'Handwas met warm water. Reinig de tuit zorgvuldig en droog goed af.'},
            {'question': 'Is de prijs van de Alessi Pulcina gerechtvaardigd?', 'answer': 'Voor wie zoekt naar innovatie en optimale extractie is de prijs gerechtvaardigd.'}
        ],
        'conclusion': 'De Alessi Pulcina is een goede keuze voor innovatie-liefhebbers. Zoek je vooral geoptimaliseerde extractie, dan is dit model logisch. Zoek je eerder eenvoud, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Alessi',
            'Model': 'Pulcina',
            'Materiaal': 'Aluminium',
            'Capaciteit': '1-3 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'bialetti-fiammetta': {
        'product_name': 'Bialetti Fiammetta',
        'product_type': 'Compacte percolator',
        'target_group': 'singles en kleine huishoudens',
        'intro': 'De Bialetti Fiammetta is een compacte percolator voor singles en kleine huishoudens. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Fiammetta is vooral interessant voor singles en kleine huishoudens. Het sterke punt van dit model is het compacte formaat, terwijl de beperkte capaciteit het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.5,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 9.0,
            'Onderhoud': 9.0,
            'Prijs-kwaliteit': 9.0,
            'Compactheid': 10.0
        },
        'verdict': 'De Fiammetta is de perfecte keuze voor singles en kleine huishoudens.',
        'pros': [
            'Compact formaat',
            'Perfect voor 1-2 kopjes',
            'Goede prijs-kwaliteit',
            'Eenvoudig in gebruik',
            'Snel opgewarmd',
            'Makkelijk op te bergen'
        ],
        'cons': [
            'Niet voor grote groepen',
            'Beperkte capaciteit',
            'Niet voor inductie',
            'Minder varianten beschikbaar'
        ],
        'suitable_for': [
            'Singles',
            'Kleine huishoudens',
            'Wie weinig ruimte heeft',
            'Studenten'
        ],
        'not_suitable_for': [
            'Grote huishoudens',
            'Wie regelmatig voor groepen zet',
            'Inductie-gebruikers',
            'Wie zoekt naar veel varianten'
        ],
        'design_p1': 'De Fiammetta heeft een compact, praktisch design. Het aluminium constructie is van dezelfde kwaliteit als andere Bialetti modellen, maar in een kleiner formaat.',
        'design_p2': 'Het formaat is perfect voor 1-2 kopjes en neemt weinig ruimte in beslag. Het design is eenvoudig maar functioneel.',
        'koffiesmaak_p1': 'De Fiammetta produceert een authentieke moka-koffie, vergelijkbaar met grotere Bialetti modellen. De extractie is consistent en betrouwbaar.',
        'koffiesmaak_p2': 'De smaak is traditioneel en authentiek. Het compacte formaat heeft geen invloed op de koffiekwaliteit.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Vervang afdichting indien nodig',
            'Berg compact op'
        ],
        'comparison_table': [
            {'name': 'Bialetti Fiammetta', 'usp': 'Compact', 'target': 'Singles'},
            {'name': 'Bialetti Mini Express', 'usp': 'Klein', 'target': 'Kleine huishoudens'},
            {'name': 'Bialetti Moka Express 1 kops', 'usp': 'Kleinste', 'target': 'Singles'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Fiammetta geschikt voor inductie?', 'answer': 'Nee, de Fiammetta is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Fiammetta is compacter en geschikt voor 1-2 kopjes, terwijl de Moka Express in verschillende maten beschikbaar is.'},
            {'question': 'Hoe onderhoud je de Bialetti Fiammetta het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af.'},
            {'question': 'Is de prijs van de Bialetti Fiammetta gerechtvaardigd?', 'answer': 'Ja, voor singles en kleine huishoudens is de prijs uitstekend gerechtvaardigd.'}
        ],
        'conclusion': 'De Bialetti Fiammetta is een goede keuze voor singles en kleine huishoudens. Zoek je vooral een compact formaat, dan is dit model logisch. Zoek je eerder grotere capaciteit, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Fiammetta',
            'Materiaal': 'Aluminium',
            'Capaciteit': '1-2 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'cilio-classico-electric': {
        'product_name': 'Cilio Classico Electric',
        'product_type': 'Elektrische percolator',
        'target_group': 'moderne keukens zonder kookplaat',
        'intro': 'De Cilio Classico Electric is een elektrische percolator voor moderne keukens zonder kookplaat. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Cilio Classico Electric is vooral interessant voor moderne keukens zonder kookplaat. Het sterke punt van dit model is de volledige elektrische werking, terwijl de hogere prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.0,
            'Koffiesmaak': 8.0,
            'Gebruiksgemak': 9.5,
            'Onderhoud': 8.5,
            'Prijs-kwaliteit': 7.5,
            'Automatisering': 10.0
        },
        'verdict': 'De Classico Electric is de beste keuze voor wie zoekt naar elektrisch gemak.',
        'pros': [
            'Volledig elektrisch',
            'Geen kookplaat nodig',
            'Automatische uitschakeling',
            'Eenvoudig in gebruik',
            'Geschikt voor elke keuken',
            'Veilig in gebruik'
        ],
        'cons': [
            'Hogere prijs',
            'Minder authentieke ervaring',
            'Elektrisch element kan kapot gaan',
            'Minder draagbaar',
            'Neemt meer ruimte in'
        ],
        'suitable_for': [
            'Moderne keukens zonder kookplaat',
            'Kantoren',
            'Wie zoekt naar gemak',
            'Studenten'
        ],
        'not_suitable_for': [
            'Wie zoekt naar authenticiteit',
            'Budget-kopers',
            'Wie veel reist',
            'Wie minimale ruimte heeft'
        ],
        'design_p1': 'De Classico Electric heeft een modern, strak design met een ingebouwd verwarmingselement. Het aluminium constructie is van goede kwaliteit met een focus op functionaliteit.',
        'design_p2': 'De basis is robuust en stabiel. Het model is ontworpen voor dagelijks gebruik met aandacht voor veiligheid en gebruiksgemak.',
        'koffiesmaak_p1': 'De Classico Electric produceert een goede moka-koffie, vergelijkbaar met traditionele percolators. De automatische temperatuurregeling zorgt voor consistente resultaten.',
        'koffiesmaak_p2': 'De smaak is authentiek maar kan iets minder intens zijn dan met een traditionele percolator op gas. Het verschil is subtiel.',
        'usage_steps': [
            'Vul de onderste kamer met water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Druk op de aan-knop',
            'Wacht tot automatische uitschakeling'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Reinig het verwarmingselement',
            'Droog goed af',
            'Ontkalk regelmatig'
        ],
        'comparison_table': [
            {'name': 'Cilio Classico Electric', 'usp': 'Volledig elektrisch', 'target': 'Moderne keukens'},
            {'name': 'Rommelsbacher EKO366', 'usp': 'Duits kwaliteit', 'target': 'Betrouwbaarheid'},
            {'name': 'Delonghi Alicia', 'usp': 'Timer', 'target': 'Gemak'}
        ],
        'faq': [
            {'question': 'Is de Cilio Classico Electric geschikt voor inductie?', 'answer': 'Nee, dit is een elektrisch model met eigen verwarmingselement, geen inductie.'},
            {'question': 'Wat is het grootste verschil met de Rommelsbacher EKO366?', 'answer': 'Beide zijn elektrisch, maar de Rommelsbacher is Duits en focus op betrouwbaarheid.'},
            {'question': 'Hoe onderhoud je de Cilio Classico Electric het best?', 'answer': 'Handwas met warm water. Reinig het verwarmingselement en ontkalk regelmatig.'},
            {'question': 'Is de prijs van de Cilio Classico Electric gerechtvaardigd?', 'answer': 'Voor wie geen kookplaat heeft is de prijs gerechtvaardigd voor het gemak.'}
        ],
        'conclusion': 'De Cilio Classico Electric is een goede keuze voor moderne keukens zonder kookplaat. Zoek je vooral elektrisch gemak, dan is dit model logisch. Zoek je eerder authenticiteit, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Cilio',
            'Model': 'Classico Electric',
            'Materiaal': 'Aluminium',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Elektrisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'rommelsbacher-eko366': {
        'product_name': 'Rommelsbacher EKO366',
        'product_type': 'Elektrische percolator',
        'target_group': 'wie zoekt naar Duitse kwaliteit',
        'intro': 'De Rommelsbacher EKO366 is een elektrische percolator voor wie zoekt naar Duitse kwaliteit. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Rommelsbacher EKO366 is vooral interessant voor wie zoekt naar Duitse kwaliteit. Het sterke punt van dit model is de betrouwbaarheid, terwijl het minder opvallende design het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.5,
            'Koffiesmaak': 8.0,
            'Gebruiksgemak': 9.0,
            'Onderhoud': 8.5,
            'Prijs-kwaliteit': 8.0,
            'Betrouwbaarheid': 9.5
        },
        'verdict': 'De EKO366 is een uitstekende keuze voor wie zoekt naar Duitse degelijkheid.',
        'pros': [
            'Duitse kwaliteit',
            'Robuuste constructie',
            'Efficiënte werking',
            'Eenvoudig in gebruik',
            'Goede prijs-kwaliteit',
            'Veilig in gebruik'
        ],
        'cons': [
            'Design minder opvallend',
            'Niet voor inductie',
            'Beperkte maten beschikbaar',
            'Minder bekend merk'
        ],
        'suitable_for': [
            'Wie zoekt naar betrouwbaarheid',
            'Duitse kwaliteit fans',
            'Kantoren',
            'Wie zoekt naar degelijkheid'
        ],
        'not_suitable_for': [
            'Design-liefhebbers',
            'Inductie-gebruikers',
            'Wie zoekt naar luxe',
            'Wie premium merk wil'
        ],
        'design_p1': 'De EKO366 heeft een functioneel, no-nonsense design. De constructie is robuust en degelijk, typisch Duits vakmanschap.',
        'design_p2': 'Het model is ontworpen voor duurzaamheid en betrouwbaarheid boven alles. Het design is eenvoudig maar effectief.',
        'koffiesmaak_p1': 'De EKO366 produceert een goede moka-koffie. De extractie is consistent en betrouwbaar dankzij de stabiele temperatuurregeling.',
        'koffiesmaak_p2': 'De smaak is authentiek en van goede kwaliteit. Het model levert consistente resultaten.',
        'usage_steps': [
            'Vul de onderste kamer met water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Druk op de aan-knop',
            'Wacht tot automatische uitschakeling'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Reinig het verwarmingselement',
            'Droog goed af',
            'Ontkalk regelmatig'
        ],
        'comparison_table': [
            {'name': 'Rommelsbacher EKO366', 'usp': 'Duits kwaliteit', 'target': 'Betrouwbaarheid'},
            {'name': 'Cilio Classico Electric', 'usp': 'Volledig elektrisch', 'target': 'Moderne keukens'},
            {'name': 'Delonghi Alicia', 'usp': 'Timer', 'target': 'Gemak'}
        ],
        'faq': [
            {'question': 'Is de Rommelsbacher EKO366 geschikt voor inductie?', 'answer': 'Nee, dit is een elektrisch model met eigen verwarmingselement.'},
            {'question': 'Wat is het grootste verschil met de Cilio Classico Electric?', 'answer': 'De Rommelsbacher is Duits en focus op betrouwbaarheid, de Cilio is meer algemeen.'},
            {'question': 'Hoe onderhoud je de Rommelsbacher EKO366 het best?', 'answer': 'Handwas met warm water. Reinig het verwarmingselement en ontkalk regelmatig.'},
            {'question': 'Is de prijs van de Rommelsbacher EKO366 gerechtvaardigd?', 'answer': 'Ja, voor wie zoekt naar Duitse kwaliteit en betrouwbaarheid is de prijs gerechtvaardigd.'}
        ],
        'conclusion': 'De Rommelsbacher EKO366 is een goede keuze voor wie zoekt naar Duitse kwaliteit. Zoek je vooral betrouwbaarheid, dan is dit model logisch. Zoek je eerder design, dan is een alternatief zoals de Alessi 9090 vaak geschikter.',
        'specs_table': {
            'Merk': 'Rommelsbacher',
            'Model': 'EKO366',
            'Materiaal': 'RVS',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Elektrisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'delonghi-alicia': {
        'product_name': 'DeLonghi Alicia',
        'product_type': 'Elektrische percolator met timer',
        'target_group': 'moderne keukens zonder kookplaat',
        'intro': 'De DeLonghi Alicia is een elektrische percolator met timer voor moderne keukens zonder kookplaat. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De DeLonghi Alicia is vooral interessant voor moderne keukens zonder kookplaat. Het sterke punt van dit model is de timer en warmhoudfunctie, terwijl de hogere prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.0,
            'Koffiesmaak': 8.0,
            'Gebruiksgemak': 9.5,
            'Onderhoud': 8.5,
            'Prijs-kwaliteit': 7.5,
            'Gemak': 9.0
        },
        'verdict': 'De Alicia is een uitstekende keuze voor wie zoekt naar elektrisch gemak met timer.',
        'pros': [
            'Ingebouwde timer',
            'Warmhoudfunctie',
            'Eenvoudig in gebruik',
            'Betrouwbaar merk',
            'Compact formaat',
            'Veilig in gebruik'
        ],
        'cons': [
            'Hogere prijs',
            'Minder authentieke ervaring',
            'Elektronica kan falen',
            'Niet voor inductie',
            'Beperkte capaciteit'
        ],
        'suitable_for': [
            'Moderne keukens zonder kookplaat',
            'Wie zoekt naar gemak',
            'Kantoren',
            'Studenten'
        ],
        'not_suitable_for': [
            'Wie zoekt naar authenticiteit',
            'Budget-kopers',
            'Wie veel reist',
            'Grote huishoudens'
        ],
        'design_p1': 'De Alicia heeft een modern, compact design met een ingebouwde timer en warmhoudfunctie. De constructie is van goede kwaliteit met een focus op functionaliteit.',
        'design_p2': 'Het model is ontworpen voor dagelijks gebruik met aandacht voor gebruiksgemak. De timer en warmhoudfunctie maken het ideaal voor wie koffie wil voorbereiden.',
        'koffiesmaak_p1': 'De Alicia produceert een goede moka-koffie, vergelijkbaar met traditionele percolators. De automatische functies zorgen voor consistente resultaten.',
        'koffiesmaak_p2': 'De smaak is authentiek. De warmhoudfunctie houdt de koffie warm zonder de smaak te beïnvloeden.',
        'usage_steps': [
            'Vul de onderste kamer met water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Stel de timer in',
            'Wacht tot automatische uitschakeling'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Reinig het verwarmingselement',
            'Droog goed af',
            'Ontkalk regelmatig'
        ],
        'comparison_table': [
            {'name': 'DeLonghi Alicia', 'usp': 'Timer', 'target': 'Gemak'},
            {'name': 'Rommelsbacher EKO366', 'usp': 'Duits kwaliteit', 'target': 'Betrouwbaarheid'},
            {'name': 'Cilio Classico Electric', 'usp': 'Volledig elektrisch', 'target': 'Moderne keukens'}
        ],
        'faq': [
            {'question': 'Is de DeLonghi Alicia geschikt voor inductie?', 'answer': 'Nee, dit is een elektrisch model met eigen verwarmingselement.'},
            {'question': 'Wat is het grootste verschil met de Rommelsbacher EKO366?', 'answer': 'De Alicia heeft een timer en warmhoudfunctie, de Rommelsbacher focus meer op betrouwbaarheid.'},
            {'question': 'Hoe onderhoud je de DeLonghi Alicia het best?', 'answer': 'Handwas met warm water. Reinig het verwarmingselement en ontkalk regelmatig.'},
            {'question': 'Is de prijs van de DeLonghi Alicia gerechtvaardigd?', 'answer': 'Voor wie zoekt naar timer en warmhoudfunctie is de prijs gerechtvaardigd.'}
        ],
        'conclusion': 'De DeLonghi Alicia is een goede keuze voor moderne keukens zonder kookplaat. Zoek je vooral timer en warmhoudfunctie, dan is dit model logisch. Zoek je eerder eenvoud, dan is een alternatief zoals de Cilio Classico Electric vaak geschikter.',
        'specs_table': {
            'Merk': 'DeLonghi',
            'Model': 'Alicia',
            'Materiaal': 'Aluminium',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Elektrisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'grosche-milano': {
        'product_name': 'Grosche Milano',
        'product_type': 'Budget percolator',
        'target_group': 'budgetbewuste koffieliefhebbers',
        'intro': 'De Grosche Milano is een budget percolator voor budgetbewuste koffieliefhebbers. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Grosche Milano is vooral interessant voor budgetbewuste koffieliefhebbers. Het sterke punt van dit model is de betaalbare prijs, terwijl de lagere bouwkwaliteit het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 7.5,
            'Koffiesmaak': 7.5,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Prijs-kwaliteit': 9.5,
            'Budget': 10.0
        },
        'verdict': 'De Milano is de beste keuze voor wie zoekt naar een betaalbare maar betrouwbare percolator.',
        'pros': [
            'Zeer betaalbaar',
            'Goede prijs-kwaliteit',
            'Degelijke constructie',
            'Beschikbaar in verschillende maten',
            'Geschikt voor beginners',
            'Vaak beschikbaar'
        ],
        'cons': [
            'Lagere bouwkwaliteit',
            'Minder authentieke smaak',
            'Niet voor inductie',
            'Minder duurzaam',
            'Beperkte designopties'
        ],
        'suitable_for': [
            'Budget-kopers',
            'Beginners',
            'Wie zoekt naar degelijke optie',
            'Studenten'
        ],
        'not_suitable_for': [
            'Wie zoekt naar premium kwaliteit',
            'Inductie-gebruikers',
            'Design-liefhebbers',
            'Professionele gebruikers'
        ],
        'design_p1': 'De Milano heeft een eenvoudig, functioneel design. De constructie is degelijk maar niet van dezelfde kwaliteit als premium merken.',
        'design_p2': 'Het model is ontworpen voor functionaliteit en betaalbaarheid. Het design is eenvoudig maar effectief voor dagelijks gebruik.',
        'koffiesmaak_p1': 'De Milano produceert een acceptabele moka-koffie. De smaak is goed maar minder intens dan premium modellen.',
        'koffiesmaak_p2': 'De extractie is consistent voor een budget model. De smaak is authentiek maar kan minder complex zijn dan duurdere modellen.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Vervang afdichting indien nodig',
            'Vermijd schuurmiddelen'
        ],
        'comparison_table': [
            {'name': 'Grosche Milano', 'usp': 'Budget', 'target': 'Budget-kopers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Origineel', 'target': 'Traditionele liefhebbers'},
            {'name': 'Bialetti Venus', 'usp': 'Inductie', 'target': 'Inductie-gebruikers'}
        ],
        'faq': [
            {'question': 'Is de Grosche Milano geschikt voor inductie?', 'answer': 'Nee, de Milano is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Milano is goedkoper en van lagere kwaliteit, terwijl de Moka Express de originele is.'},
            {'question': 'Hoe onderhoud je de Grosche Milano het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af.'},
            {'question': 'Is de prijs van de Grosche Milano gerechtvaardigd?', 'answer': 'Ja, voor budget-kopers is de prijs uitstekend gerechtvaardigd voor de kwaliteit.'}
        ],
        'conclusion': 'De Grosche Milano is een goede keuze voor budgetbewuste koffieliefhebbers. Zoek je vooral betaalbaarheid, dan is dit model logisch. Zoek je eerder premium kwaliteit, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Grosche',
            'Model': 'Milano',
            'Materiaal': 'Aluminium',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'alessi-moka': {
        'product_name': 'Alessi Moka',
        'product_type': 'Design percolator',
        'target_group': 'designliefhebbers',
        'intro': 'De Alessi Moka is een design percolator voor designliefhebbers. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Alessi Moka is vooral interessant voor designliefhebbers. Het sterke punt van dit model is het kenmerkende Alessi-design, terwijl de hogere prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 9.0,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.5,
            'Prijs-kwaliteit': 7.5,
            'Design': 9.0
        },
        'verdict': 'De Alessi Moka is een prachtige keuze voor wie zoekt naar design en functionaliteit.',
        'pros': [
            'Kenmerkend Alessi-design',
            'Hoge kwaliteit materialen',
            'Goede koffiesmaak',
            'Stijlvolle uitstraling',
            'Beschikbaar in varianten',
            'Geschenkverpakking beschikbaar'
        ],
        'cons': [
            'Hogere prijs',
            'Niet voor inductie',
            'Beperkte beschikbaarheid',
            'Minder traditioneel'
        ],
        'suitable_for': [
            'Designliefhebbers',
            'Wie zoekt naar kwaliteit',
            'Geschenkzoekers',
            'Alessi fans'
        ],
        'not_suitable_for': [
            'Budget-kopers',
            'Inductie-gebruikers',
            'Wie zoekt naar traditioneel',
            'Wie maximale varianten wil'
        ],
        'design_p1': 'De Alessi Moka heeft het kenmerkende Alessi-design met strakke lijnen en hoogwaardige materialen. De constructie is van uitstekende kwaliteit.',
        'design_p2': 'Het model combineert functionaliteit met esthetiek. Het design is tijdloos en past in moderne keukens.',
        'koffiesmaak_p1': 'De Alessi Moka produceert een goede moka-koffie. De extractie is consistent en betrouwbaar.',
        'koffiesmaak_p2': 'De smaak is authentiek en van goede kwaliteit. Het model levert resultaten vergelijkbaar met premium Bialetti modellen.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Vervang afdichting indien nodig',
            'Polish voor glans'
        ],
        'comparison_table': [
            {'name': 'Alessi Moka', 'usp': 'Design', 'target': 'Design-liefhebbers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Origineel', 'target': 'Traditionele liefhebbers'},
            {'name': 'Alessi 9090', 'usp': 'Premium', 'target': 'Verzamelaars'}
        ],
        'faq': [
            {'question': 'Is de Alessi Moka geschikt voor inductie?', 'answer': 'Nee, de Alessi Moka is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Alessi Moka heeft een meer design-georiënteerde uitstraling, terwijl de Moka Express traditioneel is.'},
            {'question': 'Hoe onderhoud je de Alessi Moka het best?', 'answer': 'Handwas met warm water. Droog goed af en polish voor glans.'},
            {'question': 'Is de prijs van de Alessi Moka gerechtvaardigd?', 'answer': 'Voor designliefhebbers is de prijs gerechtvaardigd voor de kwaliteit en esthetiek.'}
        ],
        'conclusion': 'De Alessi Moka is een goede keuze voor designliefhebbers. Zoek je vooral design en kwaliteit, dan is dit model logisch. Zoek je eerder traditioneel, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Alessi',
            'Model': 'Moka',
            'Materiaal': 'Aluminium',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'alessi-la-conica': {
        'product_name': 'Alessi La Conica',
        'product_type': 'Architectonische percolator',
        'target_group': 'architectuur- en designliefhebbers',
        'intro': 'De Alessi La Conica is een architectonische percolator voor architectuur- en designliefhebbers. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Alessi La Conica is vooral interessant voor architectuur- en designliefhebbers. Het sterke punt van dit model is het architectonische design van Aldo Rossi, terwijl de zeer hoge prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 9.5,
            'Koffiesmaak': 8.0,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Prijs-kwaliteit': 7.0,
            'Design': 10.0
        },
        'verdict': 'De La Conica is een meesterwerk voor architectuur- en designliefhebbers.',
        'pros': [
            'Architectonisch design van Aldo Rossi',
            'Tijdloze elegantie',
            'Museumcollectie-waardig',
            'Uitzonderlijke kwaliteit',
            'Unieke uitstraling',
            'Geschenkverpakking inbegrepen'
        ],
        'cons': [
            'Zeer hoge prijs',
            'Niet voor dagelijks gebruik',
            'Kwetsbaar design',
            'Beperkte beschikbaarheid',
            'Niet voor inductie'
        ],
        'suitable_for': [
            'Architectuur-liefhebbers',
            'Design-liefhebbers',
            'Verzamelaars',
            'Geschenkzoekers'
        ],
        'not_suitable_for': [
            'Dagelijks gebruik',
            'Budget-kopers',
            'Wie zoekt naar functionaliteit',
            'Inductie-gebruikers'
        ],
        'design_p1': 'La Conica is een meesterwerk van architect Aldo Rossi. De conische vorm en minimalistische design brengen architecturale elegantie naar de keuken.',
        'design_p2': 'De constructie is van uitzonderlijke kwaliteit. Het model is meer een kunstwerk dan een functioneel apparaat.',
        'koffiesmaak_p1': 'La Conica produceert een goede moka-koffie. De kwaliteit is vergelijkbaar met andere premium Alessi modellen.',
        'koffiesmaak_p2': 'De smaak is authentiek. Het unieke aan dit model is het design, niet de koffiesmaak.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Polish voor glans',
            'Berg in originele verpakking'
        ],
        'comparison_table': [
            {'name': 'Alessi La Conica', 'usp': 'Architectonisch', 'target': 'Architectuur-liefhebbers'},
            {'name': 'Alessi 9090', 'usp': 'Design icon', 'target': 'Verzamelaars'},
            {'name': 'Alessi Moka', 'usp': 'Design', 'target': 'Design-liefhebbers'}
        ],
        'faq': [
            {'question': 'Is de Alessi La Conica geschikt voor inductie?', 'answer': 'Nee, La Conica is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Alessi 9090?', 'answer': 'La Conica heeft een architectonisch design van Aldo Rossi, terwijl de 9090 van Richard Sapper is.'},
            {'question': 'Hoe onderhoud je de Alessi La Conica het best?', 'answer': 'Handwas met warm water. Droog goed af en polish voor glans. Berg in originele verpakking.'},
            {'question': 'Is de prijs van de Alessi La Conica gerechtvaardigd?', 'answer': 'Voor architectuur- en designliefhebbers is de prijs gerechtvaardigd. Voor dagelijks gebruik is het overpriced.'}
        ],
        'conclusion': 'De Alessi La Conica is een goede keuze voor architectuur- en designliefhebbers. Zoek je vooral architectonisch design, dan is dit model logisch. Zoek je eerder functionaliteit, dan is een alternatief zoals de Alessi Moka vaak geschikter.',
        'specs_table': {
            'Merk': 'Alessi',
            'Model': 'La Conica',
            'Materiaal': 'RVS',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'bialetti-mini-express': {
        'product_name': 'Bialetti Mini Express',
        'product_type': 'Compacte percolator',
        'target_group': 'singles en kleine huishoudens',
        'intro': 'De Bialetti Mini Express is een compacte percolator voor singles en kleine huishoudens. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Mini Express is vooral interessant voor singles en kleine huishoudens. Het sterke punt van dit model is het compacte formaat, terwijl de beperkte capaciteit het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.5,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 9.0,
            'Onderhoud': 9.0,
            'Prijs-kwaliteit': 9.0,
            'Compactheid': 10.0
        },
        'verdict': 'De Mini Express is de perfecte keuze voor singles en kleine huishoudens.',
        'pros': [
            'Compact formaat',
            'Perfect voor 1-2 kopjes',
            'Snel opgewarmd',
            'Eenvoudig in gebruik',
            'Makkelijk op te bergen',
            'Goede prijs-kwaliteit'
        ],
        'cons': [
            'Niet voor grote groepen',
            'Beperkte capaciteit',
            'Niet voor inductie',
            'Minder varianten beschikbaar'
        ],
        'suitable_for': [
            'Singles',
            'Kleine huishoudens',
            'Wie weinig ruimte heeft',
            'Studenten'
        ],
        'not_suitable_for': [
            'Grote huishoudens',
            'Wie regelmatig voor groepen zet',
            'Inductie-gebruikers',
            'Wie zoekt naar veel varianten'
        ],
        'design_p1': 'De Mini Express heeft een compact, praktisch design. Het aluminium constructie is van dezelfde kwaliteit als andere Bialetti modellen, maar in een kleiner formaat.',
        'design_p2': 'Het formaat is perfect voor 1-2 kopjes en neemt weinig ruimte in beslag. Het design is eenvoudig maar functioneel.',
        'koffiesmaak_p1': 'De Mini Express produceert een authentieke moka-koffie, vergelijkbaar met grotere Bialetti modellen. De extractie is consistent.',
        'koffiesmaak_p2': 'De smaak is traditioneel en authentiek. Het compacte formaat heeft geen invloed op de koffiekwaliteit.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Vervang afdichting indien nodig',
            'Berg compact op'
        ],
        'comparison_table': [
            {'name': 'Bialetti Mini Express', 'usp': 'Compact', 'target': 'Singles'},
            {'name': 'Bialetti Fiammetta', 'usp': 'Klein', 'target': 'Kleine huishoudens'},
            {'name': 'Bialetti Moka Express 1 kops', 'usp': 'Kleinste', 'target': 'Singles'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Mini Express geschikt voor inductie?', 'answer': 'Nee, de Mini Express is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Mini Express is compacter en geschikt voor 1-2 kopjes, terwijl de Moka Express in verschillende maten beschikbaar is.'},
            {'question': 'Hoe onderhoud je de Bialetti Mini Express het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af.'},
            {'question': 'Is de prijs van de Bialetti Mini Express gerechtvaardigd?', 'answer': 'Ja, voor singles en kleine huishoudens is de prijs uitstekend gerechtvaardigd.'}
        ],
        'conclusion': 'De Bialetti Mini Express is een goede keuze voor singles en kleine huishoudens. Zoek je vooral een compact formaat, dan is dit model logisch. Zoek je eerder grotere capaciteit, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Mini Express',
            'Materiaal': 'Aluminium',
            'Capaciteit': '1-2 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'bialetti-alpina': {
        'product_name': 'Bialetti Alpina',
        'product_type': 'Robuuste percolator',
        'target_group': 'wie zoekt naar degelijkheid',
        'intro': 'De Bialetti Alpina is een robuuste percolator voor wie zoekt naar degelijkheid. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Alpina is vooral interessant voor wie zoekt naar degelijkheid. Het sterke punt van dit model is de robuuste constructie, terwijl de beperkte designopties het belangrijkste aandachtspunt blijven.',
        'specs': {
            'Design & bouwkwaliteit': 8.5,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.5,
            'Prijs-kwaliteit': 8.5,
            'Robuustheid': 9.0
        },
        'verdict': 'De Alpina is een uitstekende keuze voor wie zoekt naar een robuuste, betrouwbare percolator.',
        'pros': [
            'Robuuste constructie',
            'Betrouwbare werking',
            'Goede koffiesmaak',
            'Geschikt voor dagelijks gebruik',
            'Duurzaam materiaal',
            'Goede prijs-kwaliteit'
        ],
        'cons': [
            'Niet voor inductie',
            'Beperkte designopties',
            'Minder bekend model',
            'Beperkte beschikbaarheid'
        ],
        'suitable_for': [
            'Wie zoekt naar degelijkheid',
            'Dagelijks gebruik',
            'Betrouwbaarheidzoekers',
            'Praktische gebruikers'
        ],
        'not_suitable_for': [
            'Inductie-gebruikers',
            'Design-liefhebbers',
            'Wie zoekt naar luxe',
            'Wie uniek design wil'
        ],
        'design_p1': 'De Alpina heeft een robuust, functioneel design geïnspireerd op de Italiaanse bergtraditie. De constructie is duurzaam en betrouwbaar.',
        'design_p2': 'Het model is ontworpen voor dagelijks gebruik met aandacht voor duurzaamheid. Het design is eenvoudig maar effectief.',
        'koffiesmaak_p1': 'De Alpina produceert een goede moka-koffie. De extractie is consistent en betrouwbaar voor dagelijks gebruik.',
        'koffiesmaak_p2': 'De smaak is authentiek en van goede kwaliteit. Het model levert consistente resultaten.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Vervang afdichting indien nodig',
            'Vermijd schuurmiddelen'
        ],
        'comparison_table': [
            {'name': 'Bialetti Alpina', 'usp': 'Robuust', 'target': 'Degelijkheidzoekers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Klassiek', 'target': 'Traditionele liefhebbers'},
            {'name': 'Bialetti Venus', 'usp': 'Inductie', 'target': 'Inductie-gebruikers'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Alpina geschikt voor inductie?', 'answer': 'Nee, de Alpina is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Alpina is robuuster en gericht op dagelijks gebruik, terwijl de Moka Express meer iconisch is.'},
            {'question': 'Hoe onderhoud je de Bialetti Alpina het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af.'},
            {'question': 'Is de prijs van de Bialetti Alpina gerechtvaardigd?', 'answer': 'Ja, voor wie zoekt naar degelijkheid en betrouwbaarheid is de prijs gerechtvaardigd.'}
        ],
        'conclusion': 'De Bialetti Alpina is een goede keuze voor wie zoekt naar degelijkheid. Zoek je vooral robuustheid, dan is dit model logisch. Zoek je eerder design, dan is een alternatief zoals de Bialetti Dama vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Alpina',
            'Materiaal': 'Aluminium',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'bialetti-moka-timer': {
        'product_name': 'Bialetti Moka Timer',
        'product_type': 'Percolator met timer',
        'target_group': 'wie zoekt naar precisie',
        'intro': 'De Bialetti Moka Timer is een percolator met timer voor wie zoekt naar precisie. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Bialetti Moka Timer is vooral interessant voor wie zoekt naar precisie. Het sterke punt van dit model is de timer functie, terwijl de hogere prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.5,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 9.5,
            'Onderhoud': 8.5,
            'Prijs-kwaliteit': 7.5,
            'Precisie': 9.0
        },
        'verdict': 'De Moka Timer is een uitstekende keuze voor wie zoekt naar geautomatiseerde precisie.',
        'pros': [
            'Ingebouwde timer',
            'Automatische functies',
            'Consistente resultaten',
            'Eenvoudig in gebruik',
            'Authentieke Bialetti kwaliteit',
            'Perfect voor beginners'
        ],
        'cons': [
            'Hogere prijs',
            'Elektronica kan falen',
            'Minder authentieke ervaring',
            'Niet voor inductie',
            'Beperkte beschikbaarheid'
        ],
        'suitable_for': [
            'Wie zoekt naar precisie',
            'Beginners',
            'Wie zoekt naar consistentie',
            'Gemakzoekers'
        ],
        'not_suitable_for': [
            'Puristen',
            'Budget-kopers',
            'Inductie-gebruikers',
            'Wie volledig manueel wil'
        ],
        'design_p1': 'De Moka Timer combineert het klassieke Bialetti design met moderne technologie. De constructie is van hoge kwaliteit met ingebouwde timer.',
        'design_p2': 'Het model is ontworpen voor gebruiksgemak en precisie. De timer zorgt voor consistente resultaten zonder constante aandacht.',
        'koffiesmaak_p1': 'De Moka Timer produceert een goede moka-koffie. De automatische functies zorgen voor consistente extractie.',
        'koffiesmaak_p2': 'De smaak is authentiek. De timer helpt om consistente resultaten te bereiken, wat vooral voor beginners nuttig is.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Stel de timer in',
            'Wacht tot automatische uitschakeling'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Reinig de timer',
            'Droog goed af',
            'Vervang batterijen indien nodig'
        ],
        'comparison_table': [
            {'name': 'Bialetti Moka Timer', 'usp': 'Timer', 'target': 'Precisiezoekers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Eenvoudig', 'target': 'Traditionele liefhebbers'},
            {'name': 'Delonghi Alicia', 'usp': 'Timer + warmhoudfunctie', 'target': 'Gemakzoekers'}
        ],
        'faq': [
            {'question': 'Is de Bialetti Moka Timer geschikt voor inductie?', 'answer': 'Nee, de Moka Timer is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Moka Timer heeft een ingebouwde timer voor automatische uitschakeling, terwijl de Moka Express volledig manueel is.'},
            {'question': 'Hoe onderhoud je de Bialetti Moka Timer het best?', 'answer': 'Handwas met warm water. Reinig de timer en vervang batterijen indien nodig.'},
            {'question': 'Is de prijs van de Bialetti Moka Timer gerechtvaardigd?', 'answer': 'Voor wie zoekt naar precisie en consistentie is de prijs gerechtvaardigd.'}
        ],
        'conclusion': 'De Bialetti Moka Timer is een goede keuze voor wie zoekt naar precisie. Zoek je vooral geautomatiseerde functies, dan is dit model logisch. Zoek je eerder eenvoud, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Bialetti',
            'Model': 'Moka Timer',
            'Materiaal': 'Aluminium',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'giannini-giannina': {
        'product_name': 'Giannini Giannina',
        'product_type': 'Traditionele percolator',
        'target_group': 'liefhebbers van Italiaanse traditie',
        'intro': 'De Giannini Giannina is een traditionele percolator voor liefhebbers van Italiaanse traditie. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Giannini Giannina is vooral interessant voor liefhebbers van Italiaanse traditie. Het sterke punt van dit model is het traditionele vakmanschap, terwijl de lagere bekendheid het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.0,
            'Koffiesmaak': 8.5,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Prijs-kwaliteit': 8.5,
            'Traditie': 9.0
        },
        'verdict': 'De Giannina is een uitstekende keuze voor wie zoekt naar authentieke Italiaanse traditie.',
        'pros': [
            'Authentieke Italiaanse traditie',
            'Traditioneel vakmanschap',
            'Goede koffiesmaak',
            'Betaalbaar',
            'Eenvoudig in gebruik',
            'Beschikbaar in varianten'
        ],
        'cons': [
            'Minder bekend merk',
            'Niet voor inductie',
            'Beperkte designopties',
            'Minder duurzaam dan Bialetti'
        ],
        'suitable_for': [
            'Traditionele liefhebbers',
            'Wie zoekt naar authenticiteit',
            'Budget-kopers',
            'Italiaanse koffiecultuur fans'
        ],
        'not_suitable_for': [
            'Inductie-gebruikers',
            'Wie zoekt naar premium',
            'Design-liefhebbers',
            'Wie maximale duurzaamheid wil'
        ],
        'design_p1': 'De Giannina heeft een traditioneel, klassiek design geïnspireerd op de Italiaanse koffietraditie. De constructie is van goede kwaliteit.',
        'design_p2': 'Het model is ontworpen voor traditionele koffiebereiding. Het design is eenvoudig maar authentiek.',
        'koffiesmaak_p1': 'De Giannina produceert een authentieke Italiaanse koffie. De extractie is traditioneel en betrouwbaar.',
        'koffiesmaak_p2': 'De smaak is authentiek en dicht bij traditionele Italiaanse moka. Het model levert goede resultaten.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Vervang afdichting indien nodig',
            'Vermijd schuurmiddelen'
        ],
        'comparison_table': [
            {'name': 'Giannini Giannina', 'usp': 'Traditioneel', 'target': 'Traditionele liefhebbers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Origineel', 'target': 'Puristen'},
            {'name': 'Grosche Milano', 'usp': 'Budget', 'target': 'Budget-kopers'}
        ],
        'faq': [
            {'question': 'Is de Giannini Giannina geschikt voor inductie?', 'answer': 'Nee, de Giannina is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Bialetti Moka Express?', 'answer': 'De Giannina is een minder bekend merk met traditioneel design, terwijl Bialetti het origineel is.'},
            {'question': 'Hoe onderhoud je de Giannini Giannina het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af.'},
            {'question': 'Is de prijs van de Giannini Giannina gerechtvaardigd?', 'answer': 'Ja, voor traditionele liefhebbers is de prijs gerechtvaardigd voor de kwaliteit.'}
        ],
        'conclusion': 'De Giannini Giannina is een goede keuze voor traditionele liefhebbers. Zoek je vooral authenticiteit, dan is dit model logisch. Zoek je eerder premium, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Giannini',
            'Model': 'Giannina',
            'Materiaal': 'Aluminium',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'cloer-5928': {
        'product_name': 'Cloer 5928',
        'product_type': 'Duitse percolator',
        'target_group': 'wie zoekt naar Duitse kwaliteit',
        'intro': 'De Cloer 5928 is een Duitse percolator voor wie zoekt naar Duitse kwaliteit. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Cloer 5928 is vooral interessant voor wie zoekt naar Duitse kwaliteit. Het sterke punt van dit model is de betrouwbaarheid, terwijl het minder opvallende design het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 8.0,
            'Koffiesmaak': 8.0,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.5,
            'Prijs-kwaliteit': 8.5,
            'Betrouwbaarheid': 9.0
        },
        'verdict': 'De Cloer 5928 is een uitstekende keuze voor wie zoekt naar Duitse degelijkheid.',
        'pros': [
            'Duitse kwaliteit',
            'Robuuste constructie',
            'Betrouwbaar in gebruik',
            'Goede prijs-kwaliteit',
            'Eenvoudig te onderhouden',
            'Beschikbaar in varianten'
        ],
        'cons': [
            'Design minder opvallend',
            'Niet voor inductie',
            'Minder bekend merk',
            'Beperkte designopties'
        ],
        'suitable_for': [
            'Wie zoekt naar betrouwbaarheid',
            'Duitse kwaliteit fans',
            'Praktische gebruikers',
            'Degelijkheidzoekers'
        ],
        'not_suitable_for': [
            'Design-liefhebbers',
            'Inductie-gebruikers',
            'Wie zoekt naar luxe',
            'Wie premium merk wil'
        ],
        'design_p1': 'De Cloer 5928 heeft een functioneel, no-nonsense design. De constructie is robuust en degelijk, typisch Duits vakmanschap.',
        'design_p2': 'Het model is ontworpen voor duurzaamheid en betrouwbaarheid. Het design is eenvoudig maar effectief.',
        'koffiesmaak_p1': 'De Cloer 5928 produceert een goede moka-koffie. De extractie is consistent en betrouwbaar.',
        'koffiesmaak_p2': 'De smaak is authentiek en van goede kwaliteit. Het model levert consistente resultaten.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Vermijd schuurmiddelen',
            'Vervang afdichting indien nodig'
        ],
        'comparison_table': [
            {'name': 'Cloer 5928', 'usp': 'Duits kwaliteit', 'target': 'Betrouwbaarheid'},
            {'name': 'Rommelsbacher EKO366', 'usp': 'Duits elektrisch', 'target': 'Elektrische gebruikers'},
            {'name': 'Bialetti Moka Express', 'usp': 'Italiaans', 'target': 'Traditionele liefhebbers'}
        ],
        'faq': [
            {'question': 'Is de Cloer 5928 geschikt voor inductie?', 'answer': 'Nee, de Cloer 5928 is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Rommelsbacher EKO366?', 'answer': 'De Cloer 5928 is niet-elektrisch, terwijl de Rommelsbacher wel elektrisch is.'},
            {'question': 'Hoe onderhoud je de Cloer 5928 het best?', 'answer': 'Handwas met warm water en milde zeep. Droog goed af.'},
            {'question': 'Is de prijs van de Cloer 5928 gerechtvaardigd?', 'answer': 'Ja, voor wie zoekt naar Duitse kwaliteit en betrouwbaarheid is de prijs gerechtvaardigd.'}
        ],
        'conclusion': 'De Cloer 5928 is een goede keuze voor wie zoekt naar Duitse kwaliteit. Zoek je vooral betrouwbaarheid, dan is dit model logisch. Zoek je eerder design, dan is een alternatief zoals de Alessi 9090 vaak geschikter.',
        'specs_table': {
            'Merk': 'Cloer',
            'Model': '5928',
            'Materiaal': 'RVS',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    },
    'stelton-collar': {
        'product_name': 'Stelton Collar',
        'product_type': 'Scandinavische percolator',
        'target_group': 'minimalistische designliefhebbers',
        'intro': 'De Stelton Collar is een Scandinavische percolator voor minimalistische designliefhebbers. In deze review bekijken we design, koffiesmaak, gebruiksgemak, onderhoud en voor welk type gebruiker dit model de beste keuze is.',
        'kort_oordeel': 'De Stelton Collar is vooral interessant voor minimalistische designliefhebbers. Het sterke punt van dit model is het Scandinavische design, terwijl de hogere prijs het belangrijkste aandachtspunt blijft.',
        'specs': {
            'Design & bouwkwaliteit': 9.0,
            'Koffiesmaak': 8.0,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.5,
            'Prijs-kwaliteit': 7.5,
            'Design': 9.5
        },
        'verdict': 'De Collar is een prachtige keuze voor minimalistische designliefhebbers.',
        'pros': [
            'Deens minimalistisch design',
            'Elegante uitstraling',
            'Hoge kwaliteit materialen',
            'Perfect voor moderne keukens',
            'Uniek ontwerp',
            'Geschenkverpakking beschikbaar'
        ],
        'cons': [
            'Hogere prijs',
            'Niet voor inductie',
            'Beperkte beschikbaarheid',
            'Minder traditioneel',
            'Premium positioning'
        ],
        'suitable_for': [
            'Minimalistische designliefhebbers',
            'Scandinavische design fans',
            'Moderne keukens',
            'Geschenkzoekers'
        ],
        'not_suitable_for': [
            'Budget-kopers',
            'Inductie-gebruikers',
            'Traditionele liefhebbers',
            'Wie zoekt naar maximale varianten'
        ],
        'design_p1': 'De Collar heeft een Deens minimalistisch design dat perfect past in moderne, minimalistische keukens. De constructie is van hoge kwaliteit.',
        'design_p2': 'Het model is ontworpen voor esthetiek en functionaliteit. Het design is tijdloos en elegant.',
        'koffiesmaak_p1': 'De Collar produceert een goede moka-koffie. De extractie is consistent en betrouwbaar.',
        'koffiesmaak_p2': 'De smaak is authentiek. Het unieke aan dit model is het design, niet de koffiesmaak.',
        'usage_steps': [
            'Vul de onderste kamer met koud water',
            'Plaats de trechter met koffie',
            'Schroef de bovenste kamer vast',
            'Zet op middelhoog vuur',
            'Verwijder zodra het koffiezoemen stopt'
        ],
        'maintenance_tips': [
            'Handwas met warm water',
            'Droog goed af',
            'Polish voor glans',
            'Vermijd schuurmiddelen'
        ],
        'comparison_table': [
            {'name': 'Stelton Collar', 'usp': 'Scandinavisch', 'target': 'Minimalistische designliefhebbers'},
            {'name': 'Alessi 9090', 'usp': 'Design icon', 'target': 'Verzamelaars'},
            {'name': 'Alessi La Conica', 'usp': 'Architectonisch', 'target': 'Design-liefhebbers'}
        ],
        'faq': [
            {'question': 'Is de Stelton Collar geschikt voor inductie?', 'answer': 'Nee, de Collar is niet geschikt voor inductiekookplaten.'},
            {'question': 'Wat is het grootste verschil met de Alessi 9090?', 'answer': 'De Collar heeft een Deens minimalistisch design, terwijl de 9090 een Italiaans design icon is.'},
            {'question': 'Hoe onderhoud je de Stelton Collar het best?', 'answer': 'Handwas met warm water. Droog goed af en polish voor glans.'},
            {'question': 'Is de prijs van de Stelton Collar gerechtvaardigd?', 'answer': 'Voor minimalistische designliefhebbers is de prijs gerechtvaardigd voor de kwaliteit en esthetiek.'}
        ],
        'conclusion': 'De Stelton Collar is een goede keuze voor minimalistische designliefhebbers. Zoek je vooral Scandinavisch design, dan is dit model logisch. Zoek je eerder functionaliteit, dan is een alternatief zoals de Bialetti Moka Express vaak geschikter.',
        'specs_table': {
            'Merk': 'Stelton',
            'Model': 'Collar',
            'Materiaal': 'RVS',
            'Capaciteit': '3-6 kops',
            'Warmtebron': 'Gas, elektrisch, keramisch',
            'Onderhoud': 'Handwash aanbevolen'
        }
    }
    # Add more products here following the same structure
}

def generate_review_content(review_key, data):
    """Generate HTML content for a review with detailed template"""
    
    # Generate specs list HTML
    specs_list_html = ''
    for label, value in data['specs'].items():
        specs_list_html += f'<li>{label}: {value}/10</li>\n'
    
    # Generate pros HTML
    pros_html = '\n                    <li>'.join(data['pros'])
    
    # Generate cons HTML
    cons_html = '\n                    <li>'.join(data['cons'])
    
    # Generate suitable for HTML
    suitable_for_html = '\n                <li>'.join(data['suitable_for'])
    
    # Generate not suitable for HTML
    not_suitable_for_html = '\n                <li>'.join(data['not_suitable_for'])
    
    # Generate usage steps HTML
    usage_steps_html = '\n                <li>'.join(data['usage_steps'])
    
    # Generate maintenance tips HTML
    maintenance_tips_html = '\n                <li>'.join(data['maintenance_tips'])
    
    # Generate comparison table HTML
    comparison_table_html = ''
    for alt in data['comparison_table']:
        comparison_table_html += f'''
<tr>
<td>{alt['name']}</td>
<td>{alt['usp']}</td>
<td>{alt['target']}</td>
</tr>'''
    
    # Generate FAQ HTML
    faq_html = ''
    for faq in data['faq']:
        faq_html += f'''
<h3>{faq['question']}</h3>
<p>{faq['answer']}</p>'''
    
    # Generate specifications table HTML
    specs_table_html = ''
    for key, value in data['specs_table'].items():
        specs_table_html += f'<tr><th>{key}</th><td>{value}</td></tr>\n'
    
    # Generate full content
    content = f'''    <section class="section-sm">
        <div class="container">
            <div class="article-content">
                <h1>{data['product_name']} review</h1>

                <p>{data['intro']}</p>

                <h2>Kort oordeel</h2>
                <p>{data['kort_oordeel']}</p>

                <h2>Onze beoordeling</h2>
                <ul>
{specs_list_html}
                </ul>

                <p><strong>Verdict:</strong> {data['verdict']}</p>

                <h2>Voordelen en nadelen</h2>
                <h3>Voordelen</h3>
                <ul>
                    <li>{pros_html}</li>
                </ul>

                <h3>Nadelen</h3>
                <ul>
                    <li>{cons_html}</li>
                </ul>

                <h2>Voor wie is de {data['product_name']} geschikt?</h2>
                <ul>
                    <li>{suitable_for_html}</li>
                </ul>

                <h2>Voor wie is de {data['product_name']} minder geschikt?</h2>
                <ul>
                    <li>{not_suitable_for_html}</li>
                </ul>

                <h2>Design en bouwkwaliteit</h2>
                <p>{data['design_p1']}</p>
                <p>{data['design_p2']}</p>

                <h2>Koffiesmaak en extractie</h2>
                <p>{data['koffiesmaak_p1']}</p>
                <p>{data['koffiesmaak_p2']}</p>

                <h2>Gebruiksgemak</h2>
                <p>De {data['product_name']} is eenvoudig in gebruik met een duidelijke werking. Volg deze stappen voor het beste resultaat:</p>
                <ol>
                    <li>{usage_steps_html}</li>
                </ol>

                <h2>Onderhoud en levensduur</h2>
                <p>{data['product_name']} is duurzaam en gaat lang mee met het juiste onderhoud:</p>
                <ul>
                    <li>{maintenance_tips_html}</li>
                </ul>

                <h2>{data['product_name']} vs alternatieven</h2>
                <table>
<thead>
<tr>
<th>Model</th>
<th>Sterk punt</th>
<th>Beste voor</th>
</tr>
</thead>
<tbody>
{comparison_table_html}
</tbody>
</table>

                <h2>Veelgestelde vragen</h2>
{faq_html}

                <h2>Conclusie</h2>
                <p>{data['conclusion']}</p>

                <h2>Specificaties</h2>
                <table>
{specs_table_html}
                </table>
            </div>
        </div>
    </section>

    <section class="section-sm">
        <div class="container">
            <div class="review-cta">
                <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express" target="_blank" rel="sponsored" class="btn btn-primary">
                    Bekijk prijs op Bol.com &rarr;
                </a>
                <a href="categories/percolators.html" class="btn btn-outline">
                    Vergelijk alle percolators
                </a>
            </div>
        </div>
    </section>
'''
    return content

def update_review_file(file_path):
    """Update a review file with generated content"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract review key from filename
    filename = Path(file_path).stem
    review_key = filename.replace('-review', '')
    
    if review_key not in REVIEW_DATA:
        print(f"Skipping {filename}: no data found")
        return False
    
    data = REVIEW_DATA[review_key]
    
    # Update title
    content = re.sub(r'<title>.*?</title>', f'<title>{data["product_name"]} review | Italiaanse Percolator</title>', content)
    
    # Update description
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["intro"]}">', content)
    
    # Update canonical
    content = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://italiaanse-percolator.nl/{filename}.html">', content)
    
    # Update breadcrumbs
    content = re.sub(r'<span>.*?</span>\s*</div>', f'<span>{data["product_name"]} review</span>\n        </div>', content)
    
    # Generate new content from section onwards
    new_content = generate_review_content(review_key, data)
    
    # Replace content from first <section class="section-sm"> onwards
    content = re.sub(r'<section class="section-sm">.*', new_content, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    review_files = [
        'bialetti-moka-review.html',
        'bialetti-venus-review.html',
        'bialetti-brikka-review.html',
        'alessi-9090-review.html',
        'bialetti-dama-review.html',
        'bialetti-musa-review.html',
        'alessi-pulcina-review.html',
        'bialetti-fiammetta-review.html',
        'cilio-classico-electric-review.html',
        'rommelsbacher-eko366-review.html',
        'delonghi-alicia-review.html',
        'grosche-milano-review.html',
        'alessi-moka-review.html',
        'alessi-la-conica-review.html',
        'bialetti-mini-express-review.html',
        'bialetti-alpina-review.html',
        'bialetti-moka-timer-review.html',
        'giannini-giannina-review.html',
        'cloer-5928-review.html',
        'stelton-collar-review.html'
    ]
    
    for file_path in review_files:
        path = Path(file_path)
        if not path.exists():
            print(f"Skipping {file_path}: file not found")
            continue
        
        if update_review_file(path):
            print(f"Updated {file_path}")

if __name__ == '__main__':
    main()
