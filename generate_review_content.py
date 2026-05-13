#!/usr/bin/env python3
"""Generate optimized review content with wonenmetlef-inspired structure"""
import re
from pathlib import Path

# Review content database based on product names
REVIEW_DATA = {
    'bialetti-moka': {
        'title': 'Bialetti Moka Express Review 2025: De Klassieke Referentie',
        'subtitle': 'Tijdloze klassieker',
        'description': 'Het origineel sinds 1933',
        'intro': 'Sinds 1933 is de Moka Express het symbool van de Italiaanse koffiecultuur. Iconisch achthoekig design, aluminiumconstructie en authentieke moka-smaak. We testen dit model uitgebreid en vergelijken het met moderne alternatieven.',
        'specs': {
            'Koffiesmaak': 9.3,
            'Design & Kwaliteit': 9.5,
            'Prijs/Waarde': 9.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.0,
            'Traditie': 10.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Venus', 'reason': 'Inductie-variant met RVS'},
            {'name': 'Alessi Moka', 'reason': 'Design-vriendelijke alternatief'},
            {'name': 'Grosche Milano', 'reason': 'Budgetvriendelijke optie'}
        ]
    },
    'bialetti-venus': {
        'title': 'Bialetti Venus Review 2025: De Inductie-Klassieker',
        'subtitle': 'Voor inductiekookplaten',
        'description': 'RVS variant met inductie-compatibiliteit',
        'intro': 'De Venus brengt de klassieke Bialetti-ervaring naar moderne keukens met inductiekookplaten. Gemaakt van hoogwaardig roestvrij staal, combineert deze percolator traditioneel vakmanschap met hedendaagse functionaliteit.',
        'specs': {
            'Koffiesmaak': 9.0,
            'Design & Kwaliteit': 9.0,
            'Prijs/Waarde': 8.5,
            'Gebruiksgemak': 9.0,
            'Onderhoud': 9.0,
            'Inductie': 10.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Klassieke aluminium variant'},
            {'name': 'Bialetti Brikka', 'reason': 'Met crema-functie'},
            {'name': 'Grosche Milano', 'reason': 'Budget RVS optie'}
        ]
    },
    'bialetti-brikka': {
        'title': 'Bialetti Brikka Review 2025: De Crema-Revolutie',
        'subtitle': 'Met echte crema',
        'description': 'Innovatief ontwerp voor crema-laagje',
        'intro': 'De Brikka is uniek in het Bialetti-assortiment dankzij het gepatenteerde klepsysteem dat een echte crema-laagje produceert. Een must voor liefhebbers die de espresso-ervaring zo dicht mogelijk bij het origineel willen brengen.',
        'specs': {
            'Koffiesmaak': 9.5,
            'Design & Kwaliteit': 8.5,
            'Prijs/Waarde': 8.0,
            'Gebruiksgemak': 7.5,
            'Onderhoud': 7.0,
            'Innovatie': 10.0
        },
        'pros': [
            'Produkt een echte crema-laagje',
            'Uniek gepatenteerd systeem',
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Eenvoudiger alternatief'},
            {'name': 'Bialetti Venus', 'reason': 'Inductie-variant'},
            {'name': 'Alessi 9090', 'reason': 'Design alternatief'}
        ]
    },
    'alessi-9090': {
        'title': 'Alessi 9090 Review 2025: Designicoon van Sapper',
        'subtitle': 'Design-meesterwerk',
        'description': 'Iconisch ontwerp van Richard Sapper',
        'intro': 'De Alessi 9090 is meer dan een koffiezetapparaat - het is een kunstwerk. Ontworpen door de legendarische Richard Sapper in 1979, combineert dit model functionaliteit met tijdloos design dat in musea over de hele wereld te vinden is.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 10.0,
            'Prijs/Waarde': 7.0,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Design': 10.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Betaalbaar alternatief'},
            {'name': 'Alessi Moka', 'reason': 'Betaalbaarder Alessi'},
            {'name': 'Bialetti Venus', 'reason': 'Functionele variant'}
        ]
    },
    'bialetti-dama': {
        'title': 'Bialetti Dama Review 2025: Elegance in de Keuken',
        'subtitle': 'Vrouwelijk en elegant',
        'description': 'Zacht ontwerp met afgeronde lijnen',
        'intro': 'De Dama brengt een verfijnde, vrouwelijke touch aan de klassieke Bialetti-ervaring. Met zachte, afgeronde lijnen en een elegante handgreep is dit model perfect voor wie stijl en functionaliteit wil combineren.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 9.0,
            'Prijs/Waarde': 8.0,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.0,
            'Esthetiek': 9.5
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Klassieke variant'},
            {'name': 'Bialetti Musa', 'reason': 'Art deco design'},
            {'name': 'Alessi La Conica', 'reason': 'Design alternatief'}
        ]
    },
    'bialetti-musa': {
        'title': 'Bialetti Musa Review 2025: Art Deco Revival',
        'subtitle': 'Art deco stijl',
        'description': 'Geïnspireerd op art deco architectuur',
        'intro': 'De Musa viert de gouden eeuw van Italiaanse design met zijn art deco geïnspireerde lijnen. De verticale ribbels en geometrische vormen maken dit model een eyecatcher in elke keuken.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 9.0,
            'Prijs/Waarde': 8.0,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.0,
            'Design': 9.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Dama', 'reason': 'Elegant alternatief'},
            {'name': 'Bialetti Moka Express', 'reason': 'Klassieke variant'},
            {'name': 'Alessi Moka', 'reason': 'Design optie'}
        ]
    },
    'alessi-pulcina': {
        'title': 'Alessi Pulcina Review 2025: De Innovatieve Espresso',
        'subtitle': 'Ontworpen door Michele De Lucchi',
        'description': 'Innovatief ontwerp met optimale extractie',
        'intro': 'De Pulcina is het resultaat van jarenlange research naar de perfecte koffie-extractie. Ontworpen door Michele De Lucchi, combineert dit model innovatieve technologie met het vertrouwde moka-systeem voor een nog betere smaakbeleving.',
        'specs': {
            'Koffiesmaak': 9.0,
            'Design & Kwaliteit': 9.5,
            'Prijs/Waarde': 7.5,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Innovatie': 9.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Brikka', 'reason': 'Crema-functie'},
            {'name': 'Bialetti Moka Express', 'reason': 'Klassieke variant'},
            {'name': 'Alessi 9090', 'reason': 'Design icon'}
        ]
    },
    'bialetti-fiammetta': {
        'title': 'Bialetti Fiammetta Review 2025: De Vlammenjager',
        'subtitle': 'Compact en krachtig',
        'description': 'Ideaal voor kleine keukens',
        'intro': 'De Fiammetta is ontworpen voor wie weinig ruimte heeft maar niet wil inleveren op kwaliteit. Met zijn compacte formaat en efficiënte werking is dit model perfect voor singles, studenten en kleine huishoudens.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 8.5,
            'Prijs/Waarde': 9.0,
            'Gebruiksgemak': 9.0,
            'Onderhoud': 9.0,
            'Compactheid': 10.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Mini Express', 'reason': 'Vergelijkbaar formaat'},
            {'name': 'Bialetti Moka Express 1 kops', 'reason': 'Kleinste variant'},
            {'name': 'Grosche Milano', 'reason': 'Budget optie'}
        ]
    },
    'cilio-classico-electric': {
        'title': 'Cilio Classico Electric Review 2025: Elektrisch Gemak',
        'subtitle': 'Volledig elektrisch',
        'description': 'Geen kookplaat nodig',
        'intro': 'De Cilio Classico Electric brengt het gemak van elektrisch koffiezetten naar de traditionele moka-pot. Met ingebouw verwarmingselement en automatische uitschakeling is dit model perfect voor moderne keukens.',
        'specs': {
            'Koffiesmaak': 8.0,
            'Design & Kwaliteit': 8.0,
            'Prijs/Waarde': 7.5,
            'Gebruiksgemak': 9.5,
            'Onderhoud': 8.5,
            'Automatisering': 10.0
        },
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
        'alternatives': [
            {'name': 'Rommelsbacher EKO366', 'reason': 'Vergelijkbaar elektrisch'},
            {'name': 'Delonghi Alicia', 'reason': 'Elektrisch alternatief'},
            {'name': 'Bialetti Moka Express', 'reason': 'Niet-elektrisch variant'}
        ]
    },
    'rommelsbacher-eko366': {
        'title': 'Rommelsbacher EKO366 Review 2025: Duitse Degelijkheid',
        'subtitle': 'Robuust elektrisch model',
        'description': 'Duitse kwaliteit en betrouwbaarheid',
        'intro': 'De EKO366 staat voor Duitse degelijkheid en betrouwbaarheid. Met zijn robuuste constructie en efficiënte werking is dit model een uitstekende keuze voor wie zoekt naar een duurzame elektrische percolator.',
        'specs': {
            'Koffiesmaak': 8.0,
            'Design & Kwaliteit': 8.5,
            'Prijs/Waarde': 8.0,
            'Gebruiksgemak': 9.0,
            'Onderhoud': 8.5,
            'Betrouwbaarheid': 9.5
        },
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
        'alternatives': [
            {'name': 'Cilio Classico Electric', 'reason': 'Vergelijkbaar elektrisch'},
            {'name': 'Delonghi Alicia', 'reason': 'Italiaans alternatief'},
            {'name': 'Bialetti Venus', 'reason': 'Niet-elektrisch variant'}
        ]
    },
    'delonghi-alicia': {
        'title': 'DeLonghi Alicia Review 2025: Italiaans Elektrisch',
        'subtitle': 'Elektrisch met timer',
        'description': 'Met timer en warmhoudfunctie',
        'intro': 'De Alicia combineert Italiaanse traditie met moderne technologie. Met ingebouwde timer en warmhoudfunctie biedt dit model het gemak van een volautomatisch apparaat met de authentieke smaak van een moka-pot.',
        'specs': {
            'Koffiesmaak': 8.0,
            'Design & Kwaliteit': 8.0,
            'Prijs/Waarde': 7.5,
            'Gebruiksgemak': 9.5,
            'Onderhoud': 8.5,
            'Gemak': 9.0
        },
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
        'alternatives': [
            {'name': 'Rommelsbacher EKO366', 'reason': 'Duits alternatief'},
            {'name': 'Cilio Classico Electric', 'reason': 'Vergelijkbaar'},
            {'name': 'Bialetti Moka Express', 'reason': 'Niet-elektrisch variant'}
        ]
    },
    'grosche-milano': {
        'title': 'Grosche Milano Review 2025: Budgetvriendelijke Kwaliteit',
        'subtitle': 'Goede prijs-kwaliteit',
        'description': 'Betaalbaar en betrouwbaar',
        'intro': 'De Milano bewijst dat kwaliteit niet duur hoeft te zijn. Met zijn betaalbare prijs en degelijke constructie is dit model een uitstekende keuze voor beginners en wie zoekt naar een goedkope maar betrouwbare percolator.',
        'specs': {
            'Koffiesmaak': 7.5,
            'Design & Kwaliteit': 7.5,
            'Prijs/Waarde': 9.5,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Budget': 10.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Originele variant'},
            {'name': 'Bialetti Venus', 'reason': 'Inductie optie'},
            {'name': 'Alessi Moka', 'reason': 'Design optie'}
        ]
    },
    'alessi-moka': {
        'title': 'Alessi Moka Review 2025: Design & Functionaliteit',
        'subtitle': 'Italiaans design',
        'description': 'Balans tussen design en gebruik',
        'intro': 'De Alessi Moka combineert het vertrouwde moka-systeem met het kenmerkende Alessi-design. Met strakke lijnen en hoogwaardige materialen is dit model perfect voor wie stijl en functionaliteit wil combineren.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 9.0,
            'Prijs/Waarde': 7.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.5,
            'Design': 9.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Originele variant'},
            {'name': 'Alessi 9090', 'reason': 'Premium variant'},
            {'name': 'Bialetti Venus', 'reason': 'Inductie optie'}
        ]
    },
    'alessi-la-conica': {
        'title': 'Alessi La Conica Review 2025: Tijdloze Elegantie',
        'subtitle': 'Ontworpen door Aldo Rossi',
        'description': 'Architectonisch design',
        'intro': 'La Conica is een meesterwerk van architect Aldo Rossi. Met zijn conische vorm en minimalistische design brengt dit model architecturale elegantie naar de keuken. Een must voor designliefhebbers.',
        'specs': {
            'Koffiesmaak': 8.0,
            'Design & Kwaliteit': 9.5,
            'Prijs/Waarde': 7.0,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Design': 10.0
        },
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
        'alternatives': [
            {'name': 'Alessi 9090', 'reason': 'Vergelijkbaar design'},
            {'name': 'Bialetti Dama', 'reason': 'Elegant alternatief'},
            {'name': 'Alessi Moka', 'reason': 'Betaalbaarder optie'}
        ]
    },
    'bialetti-mini-express': {
        'title': 'Bialetti Mini Express Review 2025: Compacte Perfectie',
        'subtitle': 'Ideaal voor 1-2 kopjes',
        'description': 'Klein maar krachtig',
        'intro': 'De Mini Express is perfect voor wie alleen of met z\'n tweeën koffie drinkt. Met zijn compacte formaat en snelle werking levert dit model in no time een perfecte kop espresso.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 8.5,
            'Prijs/Waarde': 9.0,
            'Gebruiksgemak': 9.0,
            'Onderhoud': 9.0,
            'Compactheid': 10.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Fiammetta', 'reason': 'Vergelijkbaar formaat'},
            {'name': 'Bialetti Moka Express 1 kops', 'reason': 'Kleinste variant'},
            {'name': 'Grosche Milano', 'reason': 'Budget optie'}
        ]
    },
    'bialetti-alpina': {
        'title': 'Bialetti Alpina Review 2025: Bergvrijheid',
        'subtitle': 'Robuust en betrouwbaar',
        'description': 'Geïnspireerd op de Alpen',
        'intro': 'De Alpina viert de Italiaanse bergtraditie met zijn robuuste constructie en betrouwbare werking. Dit model is ontworpen voor wie zoekt naar een percolator die tegen een stootje kan.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 8.5,
            'Prijs/Waarde': 8.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.5,
            'Robuustheid': 9.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Klassieke variant'},
            {'name': 'Bialetti Venus', 'reason': 'Inductie optie'},
            {'name': 'Grosche Milano', 'reason': 'Budget optie'}
        ]
    },
    'bialetti-moka-timer': {
        'title': 'Bialetti Moka Timer Review 2025: Precisie Koffie',
        'subtitle': 'Met timer functie',
        'description': 'Geprogrammeerde perfectie',
        'intro': 'De Moka Timer combineert traditionele koffiebereiding met moderne precisie. Met ingebouwde timer en automatische functies levert dit model telkens weer perfecte resultaten.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 8.5,
            'Prijs/Waarde': 7.5,
            'Gebruiksgemak': 9.5,
            'Onderhoud': 8.5,
            'Precisie': 9.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Niet-elektrisch variant'},
            {'name': 'Delonghi Alicia', 'reason': 'Vergelijkbaar elektrisch'},
            {'name': 'Cilio Classico Electric', 'reason': 'Elektrisch alternatief'}
        ]
    },
    'giannini-giannina': {
        'title': 'Giannini Giannina Review 2025: Italiaanse Traditie',
        'subtitle': 'Klassiek Italiaans',
        'description': 'Traditioneel vakmanschap',
        'intro': 'De Giannina viert de rijke Italiaanse koffietraditie. Met zijn klassieke ontwerp en traditionele werking brengt dit model de authentieke Italiaanse koffie-ervaring naar jouw keuken.',
        'specs': {
            'Koffiesmaak': 8.5,
            'Design & Kwaliteit': 8.0,
            'Prijs/Waarde': 8.5,
            'Gebruiksgemak': 8.0,
            'Onderhoud': 8.0,
            'Traditie': 9.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Originele variant'},
            {'name': 'Grosche Milano', 'reason': 'Budget optie'},
            {'name': 'Alessi Moka', 'reason': 'Design optie'}
        ]
    },
    'cloer-5928': {
        'title': 'Cloer 5928 Review 2025: Duitse Kwaliteit',
        'subtitle': 'Robuust en betrouwbaar',
        'description': 'Duitse degelijkheid',
        'intro': 'De Cloer 5928 staat voor Duitse kwaliteit en betrouwbaarheid. Met zijn robuuste constructie en efficiënte werking is dit model een uitstekende keuze voor wie zoekt naar een duurzame percolator.',
        'specs': {
            'Koffiesmaak': 8.0,
            'Design & Kwaliteit': 8.0,
            'Prijs/Waarde': 8.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.5,
            'Betrouwbaarheid': 9.0
        },
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
        'alternatives': [
            {'name': 'Bialetti Moka Express', 'reason': 'Italiaanse variant'},
            {'name': 'Rommelsbacher EKO366', 'reason': 'Duits elektrisch'},
            {'name': 'Grosche Milano', 'reason': 'Budget optie'}
        ]
    },
    'stelton-collar': {
        'title': 'Stelton Collar Review 2025: Deens Design',
        'subtitle': 'Minimalistisch en elegant',
        'description': 'Scandinavisch design',
        'intro': 'De Collar brengt Deens minimalisme naar de wereld van percolators. Met zijn strakke lijnen en elegante uitstraling is dit model perfect voor moderne, minimalistische keukens.',
        'specs': {
            'Koffiesmaak': 8.0,
            'Design & Kwaliteit': 9.0,
            'Prijs/Waarde': 7.5,
            'Gebruiksgemak': 8.5,
            'Onderhoud': 8.5,
            'Design': 9.5
        },
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
        'alternatives': [
            {'name': 'Alessi 9090', 'reason': 'Vergelijkbaar design'},
            {'name': 'Alessi La Conica', 'reason': 'Design optie'},
            {'name': 'Bialetti Venus', 'reason': 'Functionele variant'}
        ]
    }
}

def generate_review_content(review_key, data):
    """Generate HTML content for a review with wonenmetlef-inspired structure"""
    
    # Generate specs HTML
    specs_html = ''
    for label, value in data['specs'].items():
        specs_html += f'''
  <div class="review-spec-item">
    <div class="review-spec-label">{label}</div>
    <div class="review-spec-bar">
      <div class="review-spec-bar-bg">
        <div class="review-spec-bar-fill" style="width: {int(value * 10)}%"></div>
      </div>
      <div class="review-spec-value">{value}/10</div>
    </div>
  </div>'''
    
    # Generate pros HTML
    pros_html = '\n                        '.join([f'<li>{pro}</li>' for pro in data['pros']])
    
    # Generate cons HTML
    cons_html = '\n                        '.join([f'<li>{con}</li>' for con in data['cons']])
    
    # Generate alternatives HTML
    alternatives_html = ''
    for alt in data['alternatives']:
        alternatives_html += f'''
                <div class="alternative-card">
                    <h3>{alt['name']}</h3>
                    <p class="text-dim">{alt['reason']}</p>
                    <a href="{alt['name'].lower().replace(' ', '-')}-review.html" class="btn btn-outline">Bekijk review</a>
                </div>'''
    
    # Generate full content
    content = f'''    <section class="section-sm">
        <div class="container">
            <div class="review-hero">
                <div class="review-hero-content">
                    <h1 class="display-title">{data['title']}</h1>
                    <p class="lead">{data['intro']}</p>
                </div>
                <div class="review-hero-sidebar">
                    <div class="card">
                        <div class="rating-badge">9.0/10{data['subtitle']}{data['description']}</div>
                        <h3>{data['subtitle']}</h3>
                        <p class="text-dim">{data['description']}</p>
                        <div class="review-specs">
                            <div class="review-specs">
{specs_html}
</div>
                        </div>
                        <div class="review-cta">
                            <a href="https://partner.bol.com/click/click?p=2&t=url&s=1519207&f=TXL&url=https%3A%2F%2Fwww.bol.com%2Fnl%2Fnl%2Fp%2Fbialetti-moka-express-percolator-6-kops-aluminium%2F9200000038446313%2F&name=Bialetti%20Moka%20Express%20-%20Percolator%206%20kops%20-%20Aluminium%20-%20270ml%20inhoud" target="_blank" rel="sponsored" class="btn btn-primary">
                                Bekijk prijs op Bol.com &rarr;
                            </a>
                            <a href="categories/percolators.html" class="btn btn-outline">
                                Vergelijk alle percolators
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section-sm">
        <div class="container">
            <h2 class="section-title">Plus- en minpunten</h2>
            <div class="pros-cons">
                <div class="pros">
                    <h3>Pluspunten</h3>
                    <ul>
                        {pros_html}
                    </ul>
                </div>
                <div class="cons">
                    <h3>Minpunten</h3>
                    <ul>
                        {cons_html}
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="section-sm">
        <div class="container">
            <h2 class="section-title">Alternatieven</h2>
            <div class="alternative-card-grid">
{alternatives_html}
            </div>
        </div>
    </section>

    <!-- More sections as needed -->
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
    content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} | Italiaanse Percolator</title>', content)
    
    # Update description
    content = re.sub(r'<meta name="description" content="DESCRIPTION_HERE">', f'<meta name="description" content="{data["intro"]}">', content)
    
    # Update canonical
    content = re.sub(r'<link rel="canonical" href="https://italiaanse-percolator.nl/REVIEW_URL_HERE">', f'<link rel="canonical" href="https://italiaanse-percolator.nl/{filename}.html">', content)
    
    # Update hero title
    content = re.sub(r'<h1 class="display-title">.*?</h1>', f'<h1 class="display-title">{data["title"]}</h1>', content)
    
    # Update hero lead
    content = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">{data["intro"]}</p>', content)
    
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
