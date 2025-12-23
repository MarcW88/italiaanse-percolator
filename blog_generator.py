#!/usr/bin/env python3
"""
Script de génération d'articles de blog pour italiaanse-percolator.nl
Génère des articles de 1000-1500 mots optimisés SEO via ChatGPT API
"""

import os
import json
import time
import requests
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Configuration
SERP_API_KEY = os.getenv('SERP_API_KEY', '')  # Optionnel: SerpAPI key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')  # Chargé depuis .env
OUTPUT_DIR = 'blog'

class BlogGenerator:
    def __init__(self, openai_api_key):
        """Initialise le générateur avec la clé API OpenAI"""
        self.client = OpenAI(api_key=openai_api_key)
        self.ensure_output_dir()
    
    def ensure_output_dir(self):
        """Crée le dossier de sortie s'il n'existe pas"""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
            print(f"✅ Dossier '{OUTPUT_DIR}' créé")
    
    def search_serp_competitors(self, keyword):
        """
        Recherche les concurrents sur les SERPs pour un mot-clé
        Alternative simple sans API payante
        """
        print(f"\n🔍 Analyse des SERPs pour: '{keyword}'")
        
        # Simulation d'analyse de concurrents (à remplacer par vraie recherche si API disponible)
        competitors = [
            {
                'title': f'Complete gids voor {keyword}',
                'url': 'https://example.com/guide',
                'topics': ['geschiedenis', 'soorten', 'gebruik', 'onderhoud', 'tips']
            },
            {
                'title': f'Beste {keyword} kopen in 2024',
                'url': 'https://example.com/kopen',
                'topics': ['merken', 'prijzen', 'vergelijking', 'koopadvies']
            },
            {
                'title': f'Hoe werkt een {keyword}?',
                'url': 'https://example.com/werking',
                'topics': ['mechanisme', 'techniek', 'stap-voor-stap', 'problemen']
            }
        ]
        
        print(f"  📊 {len(competitors)} concurrenten geanalyseerd")
        return competitors
    
    def analyze_topic(self, keyword, competitors):
        """Analyse approfondie du sujet via ChatGPT"""
        print(f"\n🧠 Analyse approfondie du sujet...")
        
        competitors_info = "\n".join([
            f"- {c['title']}: {', '.join(c['topics'])}"
            for c in competitors
        ])
        
        analysis_prompt = f"""Analyseer het onderwerp '{keyword}' voor een Nederlandse blog over Italiaanse percolatoren.

Concurrenten behandelen:
{competitors_info}

Geef een gedetailleerde analyse met:
1. Hoofdthema's om te behandelen (uniek en uitgebreid)
2. Belangrijke vragen van gebruikers
3. SEO opportuniteiten
4. Unieke invalshoek ten opzichte van concurrenten
5. Suggesties voor structuur

Antwoord in JSON formaat."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Je bent een SEO expert en content strategist gespecialiseerd in Italiaanse koffiecultuur."},
                    {"role": "user", "content": analysis_prompt}
                ],
                temperature=0.7
            )
            
            analysis = response.choices[0].message.content
            print(f"  ✅ Analyse compleet")
            return analysis
            
        except Exception as e:
            print(f"  ❌ Erreur lors de l'analyse: {e}")
            return None
    
    def generate_article_outline(self, keyword, analysis):
        """Génère un plan détaillé de l'article"""
        print(f"\n📝 Génération du plan de l'article...")
        
        outline_prompt = f"""Créer un plan détaillé pour un article de blog en néerlandais sur '{keyword}'.

Analyse précédente:
{analysis}

Exigences:
- Article de 1500-2000 mots
- Introduction captivante (150-200 mots)
- 5-7 sections principales avec sous-sections
- Chaque section: 200-300 mots
- Conclusion avec call-to-action (150 mots)
- Ton: informatif, expert mais accessible
- Inclure: conseils pratiques, exemples concrets, données

Format du plan:
# Titre principal (H1)
## Introduction
## Section 1: [Titre] (H2)
### Sous-section 1.1 (H3)
### Sous-section 1.2 (H3)
## Section 2: [Titre] (H2)
...
## Conclusion

Réponds uniquement avec le plan en markdown."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Je bent een professionele content writer voor Nederlandse koffieblogs."},
                    {"role": "user", "content": outline_prompt}
                ],
                temperature=0.7
            )
            
            outline = response.choices[0].message.content
            print(f"  ✅ Plan généré")
            return outline
            
        except Exception as e:
            print(f"  ❌ Erreur lors de la génération du plan: {e}")
            return None
    
    def generate_article_section(self, keyword, section_title, section_context, word_count=300):
        """Génère une section spécifique de l'article"""
        
        section_prompt = f"""Schrijf een gedetailleerde sectie voor een blogartikel over '{keyword}'.

Sectie titel: {section_title}
Context: {section_context}
Gewenste lengte: {word_count} woorden

Vereisten:
- Schrijf in perfecte, natuurlijke Nederlandse taal
- Gebruik concrete voorbeelden en praktische tips
- Integreer het keyword '{keyword}' natuurlijk (1-2x per 100 woorden)
- Schrijf informatief maar toegankelijk
- Gebruik korte paragrafen (2-4 zinnen)
- Voeg subkoppen toe waar relevant (###)
- Maak het boeiend en leesbaar

Schrijf alleen de content van deze sectie, geen meta-informatie."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Je bent een ervaren Nederlandse copywriter gespecialiseerd in koffie en Italiaanse percolatoren."},
                    {"role": "user", "content": section_prompt}
                ],
                temperature=0.8,
                max_tokens=800
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"  ❌ Erreur section: {e}")
            return None
    
    def generate_full_article(self, keyword, outline):
        """Génère l'article complet section par section"""
        print(f"\n✍️  Génération de l'article complet...")
        
        # Extraire les sections du plan
        sections = self.parse_outline(outline)
        
        full_content = []
        total_sections = len(sections)
        
        for idx, section in enumerate(sections, 1):
            print(f"  📄 Section {idx}/{total_sections}: {section['title']}")
            
            content = self.generate_article_section(
                keyword=keyword,
                section_title=section['title'],
                section_context=section.get('context', ''),
                word_count=section.get('word_count', 300)
            )
            
            if content:
                full_content.append({
                    'level': section['level'],
                    'title': section['title'],
                    'content': content
                })
                time.sleep(2)  # Rate limiting
            else:
                print(f"    ⚠️  Échec de génération de la section")
        
        print(f"  ✅ Article généré ({len(full_content)} sections)")
        return full_content
    
    def parse_outline(self, outline):
        """Parse le plan markdown en sections structurées"""
        sections = []
        lines = outline.split('\n')
        
        current_h2_context = ""
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith('# '):
                # H1 - Titre principal
                sections.append({
                    'level': 'h1',
                    'title': line[2:],
                    'word_count': 0
                })
            elif line.startswith('## '):
                # H2 - Section principale
                title = line[3:]
                current_h2_context = title
                word_count = 250 if 'introduction' in title.lower() else 300
                sections.append({
                    'level': 'h2',
                    'title': title,
                    'context': current_h2_context,
                    'word_count': word_count
                })
            elif line.startswith('### '):
                # H3 - Sous-section
                sections.append({
                    'level': 'h3',
                    'title': line[4:],
                    'context': current_h2_context,
                    'word_count': 200
                })
        
        return sections
    
    def format_to_html(self, sections, keyword):
        """Formate le contenu en HTML"""
        print(f"\n🎨 Formatage en HTML...")
        
        html_parts = []
        
        # Header
        html_parts.append(f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Uitgebreide gids over {keyword} - Alles wat je moet weten">
    <title>{sections[0]['title'] if sections else keyword}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="container">
        <article class="blog-post">
""")
        
        # Content
        for section in sections:
            level = section['level']
            title = section['title']
            content = section.get('content', '')
            
            if level == 'h1':
                html_parts.append(f'            <h1>{title}</h1>\n')
            elif level == 'h2':
                html_parts.append(f'            <h2>{title}</h2>\n')
                if content:
                    html_parts.append(f'            <div class="section-content">\n')
                    html_parts.append(f'                {self.markdown_to_html(content)}\n')
                    html_parts.append(f'            </div>\n')
            elif level == 'h3':
                html_parts.append(f'            <h3>{title}</h3>\n')
                if content:
                    html_parts.append(f'            <div class="subsection-content">\n')
                    html_parts.append(f'                {self.markdown_to_html(content)}\n')
                    html_parts.append(f'            </div>\n')
        
        # Footer
        html_parts.append("""        </article>
    </div>
</body>
</html>""")
        
        return ''.join(html_parts)
    
    def markdown_to_html(self, text):
        """Convertit le markdown simple en HTML"""
        # Paragraphes
        paragraphs = text.split('\n\n')
        html_paragraphs = [f'<p>{p.strip()}</p>' for p in paragraphs if p.strip()]
        
        html = '\n                '.join(html_paragraphs)
        
        # Listes
        html = html.replace('- ', '<li>').replace('<p><li>', '<ul>\n<li>').replace('</li></p>', '</li>\n</ul>')
        
        # Gras
        html = html.replace('**', '<strong>').replace('</strong><strong>', '</strong>')
        
        return html
    
    def save_article(self, html_content, keyword):
        """Sauvegarde l'article en HTML"""
        slug = keyword.lower().replace(' ', '-').replace('/', '-')
        filename = f"{slug}-{datetime.now().strftime('%Y%m%d')}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\n💾 Article sauvegardé: {filepath}")
        return filepath
    
    def generate(self, keyword):
        """Pipeline complet de génération d'article"""
        print(f"\n{'='*60}")
        print(f"🚀 GÉNÉRATION D'ARTICLE: {keyword}")
        print(f"{'='*60}")
        
        # 1. Recherche concurrents
        competitors = self.search_serp_competitors(keyword)
        
        # 2. Analyse du sujet
        analysis = self.analyze_topic(keyword, competitors)
        if not analysis:
            print("❌ Échec de l'analyse")
            return None
        
        # 3. Génération du plan
        outline = self.generate_article_outline(keyword, analysis)
        if not outline:
            print("❌ Échec de la génération du plan")
            return None
        
        print(f"\n📋 Plan de l'article:")
        print(outline)
        
        # 4. Génération de l'article complet
        sections = self.generate_full_article(keyword, outline)
        if not sections:
            print("❌ Échec de la génération de l'article")
            return None
        
        # 5. Formatage en HTML
        html_content = self.format_to_html(sections, keyword)
        
        # 6. Sauvegarde
        filepath = self.save_article(html_content, keyword)
        
        print(f"\n{'='*60}")
        print(f"✅ ARTICLE GÉNÉRÉ AVEC SUCCÈS!")
        print(f"{'='*60}")
        
        return filepath


def main():
    """Fonction principale"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     GÉNÉRATEUR D'ARTICLES BLOG - Italiaanse Percolator   ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Configuration de la clé API depuis .env
    api_key = OPENAI_API_KEY
    
    if not api_key:
        print("❌ Clé API OpenAI manquante!")
        print("💡 Créer un fichier .env avec: OPENAI_API_KEY=ta-clé")
        return
    
    print("✅ Clé API OpenAI chargée depuis .env")
    
    # Initialisation du générateur
    generator = BlogGenerator(api_key)
    
    # Mots-clés suggérés
    suggested_keywords = [
        "italiaanse percolator reinigen",
        "beste italiaanse percolator kopen",
        "verschil moka pot en espresso",
        "italiaanse koffie maken thuis",
        "bialetti percolator gebruiken",
        "percolator onderhoud tips",
        "aluminium vs rvs percolator",
        "italiaanse koffiecultuur",
        "moka pot inductie",
        "percolator maling kiezen"
    ]
    
    print("\n📚 Mots-clés suggérés:")
    for i, kw in enumerate(suggested_keywords, 1):
        print(f"  {i}. {kw}")
    
    # Sélection du mot-clé
    choice = input("\n✏️  Entre un mot-clé ou le numéro (1-10): ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(suggested_keywords):
        keyword = suggested_keywords[int(choice) - 1]
    else:
        keyword = choice
    
    if not keyword:
        print("❌ Mot-clé requis!")
        return
    
    # Génération
    try:
        filepath = generator.generate(keyword)
        
        if filepath:
            print(f"\n🎉 Article prêt à publier!")
            print(f"📂 Fichier: {filepath}")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
