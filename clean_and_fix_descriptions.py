#!/usr/bin/env python3
"""
Script pour nettoyer les descriptions dupliquées et les repositionner correctement
"""

import re
import os
from pathlib import Path

# Mapping des descriptions correctes par produit
CORRECT_DESCRIPTIONS = {
    "bialetti-moka-alpina-limited-editions-3-kops-120ml.html": """Deze limited edition is een eerbetoon aan de nauwe band tussen Italië en de Alpen, waar koffiecultuur en bergtraditie samenkomen. Het speciale Alpina-design maakt elke percolator tot een verzamelobject, terwijl de functionaliteit onverminderd top is. Met een capaciteit van 120ml bereidt u drie perfecte kopjes espresso – ideaal voor een intieme koffiemoment of een verfijnde ochtendroutine.

Het aluminium lichaam combineert lichtgewicht draagbaarheid met duurzame kwaliteit, perfect voor zowel thuis als voor outdooravonturen. De karakteristieke achtkantige vorm zorgt voor optimale warmteverdeling, terwijl het gepatenteerde veiligheidsventiel van Bialetti garandeert dat elke extractie veilig en perfect verloopt.

Deze Moka Alpina is geschikt voor gas, elektrische en keramische kookplaten, waardoor u overal kunt genieten van authentieke espresso. Het thermoplastische handvat blijft comfortabel koel, zelfs wanneer de percolator op volle kracht werkt.

Voor verzamelaars en liefhebbers van limited editions is deze Alpina een must-have. Het combineert Bialetti's legendarische kwaliteit met een unieke esthetiek die niet lang beschikbaar zal zijn. Een perfect stuk voor wie originaliteit waardeert.""",

    "bialetti-moka-express-percolator-3-kops-aluminium.html": """Met deze klassieke espressomaker bereidt u in enkele minuten een rijke, volle espresso zoals u die in Italië drinkt. Het gepatenteerde veiligheidsventiel en de gemakkelijk te reinigen onderdelen maken het gebruik eenvoudig en veilig. Het ergonomische handvat blijft koel tijdens het zetten, zodat u veilig kunt inschenken.

De Moka Express is een duurzame keuze: geen capsules, geen afval, en een tijdloos object dat generaties meegaat. Het aluminium lichaam is licht maar stevig, ideaal voor dagelijks gebruik. Let op: dit model is niet geschikt voor inductie, maar werkt perfect op gas, elektrische en keramische kookplaten.

Dit is de échte Bialetti – herkenbaar aan het mannetje met de snor. Perfect voor koffieliefhebbers die authenticiteit en kwaliteit waarderen. Of u nu zelf geniet van een ochtendkopje of gasten verrast met Italiaanse espresso, de Moka Express Italia maakt elk moment speciaal. Een must-have voor elke koffieliefhebber die de traditie van Italiaanse koffiecultuur omarmt.""",

    "bialetti-moka-express-percolator-6-kops-aluminium.html": """Deze 6-kops versie biedt ruimte voor ongeveer 300ml koffie – perfect voor een gezellig samenzijn of een productieve werkdag. De aluminium constructie zorgt voor optimale warmtegeleiding, waardoor elke espresso de rijke smaak en het volle aroma krijgt die u van Italiaanse koffie verwacht. Het thermoplastische handvat en de knop blijven comfortabel koel, zelfs wanneer de percolator op het vuur staat.

Het gebruik is verrassend eenvoudig: vul het waterreservoir tot onder het ventiel, doe gemalen koffie in het filter zonder aan te drukken, en plaats de percolator op een middelmatige warmtebron. Binnen enkele minuten hoort u het karakteristieke gorgelende geluid dat aangeeft dat uw espresso klaar is.

Deze Moka Express is geschikt voor gas, elektrische en keramische kookplaten, maar niet voor inductie. Het duurzame ontwerp betekent geen wegwerpfilters of capsules – alleen pure koffie en pure smaak. Een investering in Italiaanse koffietraditie die decennialang meegaat en elke koffiepauze tot een bijzonder moment maakt."""
}

def clean_and_fix_page(file_path):
    """Nettoie une page et remet la bonne description"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Supprimer toutes les descriptions existantes
        content = re.sub(
            r'<!-- Uitgebreide Productbeschrijving.*?</div>\s*</div>',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Supprimer les sections orphelines
        content = re.sub(
            r'<section style="margin: 3rem 0;">.*?</section>',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Vérifier si on a une description pour ce fichier
        if filename in CORRECT_DESCRIPTIONS:
            description = CORRECT_DESCRIPTIONS[filename]
            
            # Formater la description en paragraphes
            paragraphs = description.strip().split('\n\n')
            formatted_paragraphs = []
            
            for para in paragraphs:
                if para.strip():
                    formatted_paragraphs.append(f'<p style="margin-bottom: 1.5rem; color: #333; line-height: 1.7; font-size: 1rem;">{para.strip()}</p>')
            
            # Créer la section description
            description_section = f'''
        <!-- Uitgebreide Productbeschrijving - Pleine largeur -->
        <section style="margin: 3rem 0;">
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
                print(f"⚠️  Pattern 'Vergelijkbare producten' non trouvé dans {filename}")
                return False
        else:
            print(f"⚠️  Pas de description définie pour {filename}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur avec {file_path}: {e}")
        return False

def main():
    print("🧹 Nettoyage et correction des descriptions produits...")
    
    fixed_count = 0
    
    for filename, description in CORRECT_DESCRIPTIONS.items():
        file_path = f"producten/{filename}"
        
        if os.path.exists(file_path):
            print(f"\n📋 Traitement: {filename}")
            
            if clean_and_fix_page(file_path):
                print(f"✅ Page nettoyée et corrigée: {filename}")
                fixed_count += 1
            else:
                print(f"❌ Échec pour: {filename}")
        else:
            print(f"⚠️  Fichier non trouvé: {file_path}")
    
    print(f"\n🎯 RÉSULTATS:")
    print(f"✅ {fixed_count} pages nettoyées et corrigées")
    print(f"\n📋 Structure finale:")
    print("   1. Image + Infos produit (2 colonnes)")
    print("   2. Description détaillée (pleine largeur, une seule)")
    print("   3. Vergelijkbare producten")
    print("   4. FAQ section")

if __name__ == "__main__":
    main()
