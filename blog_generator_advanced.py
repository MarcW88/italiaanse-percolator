#!/usr/bin/env python3
"""
VERSION AVANCÉE: Générateur d'articles avec scraping réel des SERPs
Inclut scraping Google, analyse de contenu concurrent, et génération optimisée
"""

import os
import json
import time
import re
import requests
from datetime import datetime
from openai import OpenAI
from bs4 import BeautifulSoup
from urllib.parse import quote_plus, urlparse
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

OUTPUT_DIR = 'blog'

class AdvancedBlogGenerator:
    def __init__(self, openai_api_key):
        """Initialise le générateur"""
        self.client = OpenAI(api_key=openai_api_key)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.ensure_output_dir()
    
    def ensure_output_dir(self):
        """Crée le dossier de sortie"""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    
    def scrape_google_serps(self, keyword, num_results=10):
        """
        Scrape les résultats Google pour un mot-clé
        ATTENTION: Respecter les Terms of Service de Google
        Pour production, utiliser plutôt une API comme SerpAPI
        """
        print(f"\n🔍 Scraping Google SERPs pour: '{keyword}'")
        
        try:
            # URL de recherche Google
            search_url = f"https://www.google.nl/search?q={quote_plus(keyword)}&hl=nl"
            
            # Requête
            response = self.session.get(search_url, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extraire les résultats
            results = []
            search_results = soup.find_all('div', class_='g')
            
            for idx, result in enumerate(search_results[:num_results], 1):
                try:
                    # Titre
                    title_elem = result.find('h3')
                    title = title_elem.text if title_elem else ''
                    
                    # URL
                    link_elem = result.find('a')
                    url = link_elem['href'] if link_elem and 'href' in link_elem.attrs else ''
                    
                    # Snippet
                    snippet_elem = result.find('div', class_=['VwiC3b', 'yXK7lf'])
                    snippet = snippet_elem.text if snippet_elem else ''
                    
                    if title and url:
                        results.append({
                            'position': idx,
                            'title': title,
                            'url': url,
                            'snippet': snippet
                        })
                        print(f"  {idx}. {title[:60]}...")
                
                except Exception as e:
                    continue
            
            print(f"  ✅ {len(results)} résultats trouvés")
            return results
            
        except Exception as e:
            print(f"  ⚠️  Erreur scraping: {e}")
            print(f"  💡 Conseil: Utiliser SerpAPI pour un scraping fiable")
            return []
    
    def scrape_page_content(self, url):
        """Scrape le contenu d'une page"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Retirer scripts et styles
            for script in soup(['script', 'style', 'nav', 'footer', 'header']):
                script.decompose()
            
            # Extraire le texte
            text = soup.get_text()
            
            # Nettoyer
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            # Limiter la longueur
            return text[:3000]
            
        except Exception as e:
            return None
    
    def analyze_competitors_content(self, keyword, serp_results):
        """Analyse approfondie du contenu des concurrents"""
        print(f"\n🧪 Analyse approfondie des concurrents...")
        
        competitor_analysis = []
        
        for idx, result in enumerate(serp_results[:5], 1):
            print(f"  📄 Analyse page {idx}/5: {result['title'][:50]}...")
            
            content = self.scrape_page_content(result['url'])
            
            if content:
                # Extraire les topics via ChatGPT
                topics = self.extract_topics_from_content(content, keyword)
                
                competitor_analysis.append({
                    'position': result['position'],
                    'title': result['title'],
                    'url': result['url'],
                    'snippet': result['snippet'],
                    'topics': topics,
                    'word_count': len(content.split())
                })
                
                time.sleep(2)  # Rate limiting
        
        print(f"  ✅ {len(competitor_analysis)} concurrents analysés")
        return competitor_analysis
    
    def extract_topics_from_content(self, content, keyword):
        """Extrait les principaux topics d'un contenu via ChatGPT"""
        prompt = f"""Analyseer deze content over '{keyword}' en extraheer de 5-7 belangrijkste onderwerpen/topics.

Content (eerste 1000 woorden):
{content[:4000]}

Geef alleen een lijst van topics, gescheiden door komma's."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Je bent een content analist."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=200
            )
            
            topics_text = response.choices[0].message.content
            topics = [t.strip() for t in topics_text.split(',')]
            return topics[:7]
            
        except Exception as e:
            return []
    
    def create_content_gap_analysis(self, keyword, competitor_analysis):
        """Identifie les gaps de contenu vs concurrents"""
        print(f"\n🎯 Analyse des gaps de contenu...")
        
        # Compiler tous les topics des concurrents
        all_topics = []
        for comp in competitor_analysis:
            all_topics.extend(comp.get('topics', []))
        
        # Créer le prompt d'analyse
        competitors_summary = "\n".join([
            f"Position {c['position']}: {c['title']}\n  Topics: {', '.join(c.get('topics', []))}\n  Mots: {c.get('word_count', 0)}"
            for c in competitor_analysis
        ])
        
        gap_analysis_prompt = f"""Analyseer de top 5 concurrenten voor '{keyword}' en identificeer content gaps.

Concurrenten analyse:
{competitors_summary}

Geef:
1. Veelbehandelde onderwerpen (wat concurrenten allemaal behandelen)
2. Content gaps (wat ontbreekt of oppervlakkig behandeld wordt)
3. Unieke invalshoek voor ons artikel
4. Optimale lengte (gebaseerd op concurrenten)
5. Must-have topics voor ranking

Antwoord in gestructureerd formaat."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Je bent een SEO content strategist expert."},
                    {"role": "user", "content": gap_analysis_prompt}
                ],
                temperature=0.7
            )
            
            gap_analysis = response.choices[0].message.content
            print(f"  ✅ Gap analysis compleet")
            return gap_analysis
            
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
            return None
    
    def generate_seo_optimized_outline(self, keyword, gap_analysis, target_length=1500):
        """Génère un plan optimisé SEO basé sur la gap analysis"""
        print(f"\n📐 Génération du plan optimisé SEO...")
        
        outline_prompt = f"""Creëer een SEO-geoptimaliseerd artikel plan voor '{keyword}'.

Gap Analysis:
{gap_analysis}

Vereisten:
- Target lengte: {target_length} woorden
- Behandel ALLE belangrijke topics die concurrenten missen
- Voeg unieke waarde toe
- Structuur: H1 → H2 (5-7 secties) → H3 (sub-secties)
- Elke sectie: praktisch, actionable, met voorbeelden
- SEO-vriendelijke subkoppen met keyword variaties

Format het plan als:
# [SEO-geoptimaliseerde H1 titel met keyword]
## Introductie (200 woorden)
[Korte beschrijving wat intro moet bevatten]

## [H2 Sectie 1] (300 woorden)
### [H3 Sub-sectie 1.1] (150 woorden)
[Wat deze sub-sectie moet behandelen]
### [H3 Sub-sectie 1.2] (150 woorden)

## [H2 Sectie 2] (300 woorden)
...

## Conclusie (200 woorden)
[Wat conclusie moet bevatten]

Geef een volledig, gedetailleerd plan."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Je bent een SEO copywriter expert."},
                    {"role": "user", "content": outline_prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            outline = response.choices[0].message.content
            print(f"  ✅ Plan SEO généré")
            return outline
            
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
            return None
    
    def generate_section_content(self, keyword, section_info):
        """Génère le contenu d'une section avec instructions détaillées"""
        
        section_prompt = f"""Schrijf een uitgebreide sectie voor een blogartikel over '{keyword}'.

SECTIE INFORMATIE:
Titel: {section_info['title']}
Level: {section_info['level']}
Target lengte: {section_info['word_count']} woorden
Context/Instructies: {section_info.get('instructions', '')}

SCHRIJFRICHTLIJNEN:
✅ Schrijf natuurlijk Nederlands (geen AI-toon)
✅ Gebruik concrete voorbeelden en praktische tips
✅ Voeg cijfers, data, feiten toe waar mogelijk
✅ Maak paragrafen kort (2-4 zinnen max)
✅ Gebruik transitiewoorden (echter, daarom, bovendien, etc.)
✅ Integreer keyword natuurlijk (maar niet geforceerd)
✅ Schrijf informatief maar toegankelijk
✅ Vermijd clichés en generieke frases
✅ Maak het actionable (lezer kan er iets mee)

FORMAAT:
- Gebruik ## voor H2, ### voor H3
- Gebruik * voor lijsten
- Gebruik **vet** voor belangrijke termen
- Schrijf in duidelijke paragrafen

Schrijf ALLEEN de content van deze sectie. Geen intro/outro."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Je bent een professionele Nederlandse copywriter met expertise in koffie en Italiaanse culinaire cultuur. Je schrijft boeiende, praktische content die lezers écht helpt."},
                    {"role": "user", "content": section_prompt}
                ],
                temperature=0.85,  # Plus créatif
                max_tokens=1000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"    ❌ Erreur: {e}")
            return None
    
    def parse_detailed_outline(self, outline):
        """Parse le plan détaillé avec instructions"""
        sections = []
        lines = outline.split('\n')
        
        current_section = None
        current_instructions = []
        
        for line in lines:
            line_stripped = line.strip()
            
            if line_stripped.startswith('# '):
                # H1
                sections.append({
                    'level': 'h1',
                    'title': line_stripped[2:],
                    'word_count': 0,
                    'instructions': ''
                })
            
            elif line_stripped.startswith('## '):
                # H2 - Sauvegarder la section précédente
                if current_section:
                    current_section['instructions'] = ' '.join(current_instructions)
                    sections.append(current_section)
                
                # Nouvelle section H2
                title = line_stripped[3:]
                word_count_match = re.search(r'\((\d+)\s*woorden?\)', title)
                word_count = int(word_count_match.group(1)) if word_count_match else 300
                title = re.sub(r'\s*\(\d+\s*woorden?\)', '', title).strip()
                
                current_section = {
                    'level': 'h2',
                    'title': title,
                    'word_count': word_count,
                    'instructions': ''
                }
                current_instructions = []
            
            elif line_stripped.startswith('### '):
                # H3
                title = line_stripped[4:]
                word_count_match = re.search(r'\((\d+)\s*woorden?\)', title)
                word_count = int(word_count_match.group(1)) if word_count_match else 200
                title = re.sub(r'\s*\(\d+\s*woorden?\)', '', title).strip()
                
                sections.append({
                    'level': 'h3',
                    'title': title,
                    'word_count': word_count,
                    'instructions': ' '.join(current_instructions)
                })
                current_instructions = []
            
            elif line_stripped.startswith('[') and current_section:
                # Instructions pour la section
                instruction = line_stripped.strip('[]')
                current_instructions.append(instruction)
        
        # Sauvegarder la dernière section
        if current_section:
            current_section['instructions'] = ' '.join(current_instructions)
            sections.append(current_section)
        
        return sections
    
    def generate_complete_article(self, keyword, outline):
        """Génère l'article complet avec toutes les sections"""
        print(f"\n✍️  Génération de l'article complet...")
        
        sections = self.parse_detailed_outline(outline)
        
        generated_content = []
        total_sections = sum(1 for s in sections if s['level'] in ['h2', 'h3'])
        current = 0
        
        for section in sections:
            if section['level'] == 'h1':
                generated_content.append(section)
                continue
            
            if section['level'] in ['h2', 'h3']:
                current += 1
                print(f"  📝 Section {current}/{total_sections}: {section['title'][:50]}...")
                
                content = self.generate_section_content(keyword, section)
                
                if content:
                    section['content'] = content
                    generated_content.append(section)
                    
                    # Afficher un aperçu
                    preview = content[:150].replace('\n', ' ')
                    print(f"    ✅ Généré ({len(content.split())} mots): {preview}...")
                    
                    time.sleep(3)  # Rate limiting important
                else:
                    print(f"    ⚠️  Échec")
        
        print(f"\n  ✅ Article complet: {sum(len(s.get('content', '').split()) for s in generated_content)} mots")
        return generated_content
    
    def create_html_article(self, sections, keyword, metadata):
        """Crée l'article HTML final avec SEO"""
        
        title = sections[0]['title'] if sections else keyword
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower())
        
        html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Uitgebreide gids over {keyword}. Leer alles over {keyword} met praktische tips en expert advies.">
    <meta name="keywords" content="{keyword}, italiaanse percolator, koffie, gids">
    <title>{title} | Italiaanse-Percolator.nl</title>
    <link rel="stylesheet" href="../style.css">
    <style>
        .blog-post {{ max-width: 800px; margin: 0 auto; padding: 2rem; }}
        .blog-post h1 {{ font-size: 2.5rem; margin-bottom: 1rem; color: #D2691E; }}
        .blog-post h2 {{ font-size: 2rem; margin-top: 2rem; margin-bottom: 1rem; color: #333; border-bottom: 2px solid #D2691E; padding-bottom: 0.5rem; }}
        .blog-post h3 {{ font-size: 1.5rem; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #555; }}
        .blog-post p {{ line-height: 1.8; margin-bottom: 1rem; color: #444; }}
        .blog-post ul, .blog-post ol {{ margin: 1rem 0; padding-left: 2rem; }}
        .blog-post li {{ margin-bottom: 0.5rem; line-height: 1.6; }}
        .blog-post strong {{ color: #D2691E; }}
        .meta-info {{ color: #666; font-size: 0.9rem; margin-bottom: 2rem; }}
    </style>
</head>
<body>
    <div class="container">
        <article class="blog-post">
            <div class="meta-info">
                📅 Gepubliceerd: {datetime.now().strftime('%d %B %Y')} | 
                ⏱️ Leestijd: {metadata.get('reading_time', 8)} minuten |
                📝 {metadata.get('word_count', 0)} woorden
            </div>
"""
        
        for section in sections:
            level = section['level']
            title = section['title']
            content = section.get('content', '')
            
            if level == 'h1':
                html += f'            <h1>{title}</h1>\n'
            elif level == 'h2':
                html += f'\n            <h2>{title}</h2>\n'
                if content:
                    html += self.format_content_to_html(content)
            elif level == 'h3':
                html += f'            <h3>{title}</h3>\n'
                if content:
                    html += self.format_content_to_html(content)
        
        html += """
        </article>
    </div>
</body>
</html>"""
        
        return html
    
    def format_content_to_html(self, content):
        """Formate le markdown en HTML propre"""
        html_parts = []
        
        # Séparer en paragraphes
        blocks = content.split('\n\n')
        
        for block in blocks:
            block = block.strip()
            if not block:
                continue
            
            # Listes
            if block.startswith('* ') or block.startswith('- '):
                items = block.split('\n')
                html_parts.append('            <ul>')
                for item in items:
                    item_text = item.lstrip('*- ').strip()
                    if item_text:
                        html_parts.append(f'                <li>{self.format_inline(item_text)}</li>')
                html_parts.append('            </ul>')
            
            # Paragraphes
            else:
                html_parts.append(f'            <p>{self.format_inline(block)}</p>')
        
        return '\n'.join(html_parts) + '\n'
    
    def format_inline(self, text):
        """Formate les éléments inline (gras, italique)"""
        # Gras
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        # Italique
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        return text
    
    def save_article(self, html, keyword):
        """Sauvegarde l'article"""
        slug = re.sub(r'[^a-z0-9]+', '-', keyword.lower())
        timestamp = datetime.now().strftime('%Y%m%d-%H%M')
        filename = f"{slug}-{timestamp}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"\n💾 Article sauvegardé: {filepath}")
        
        # Statistiques
        word_count = len(html.split())
        print(f"📊 Statistiques:")
        print(f"   • Mots: {word_count}")
        print(f"   • Taille: {len(html)} caractères")
        
        return filepath
    
    def generate_full_pipeline(self, keyword, scrape_serps=True):
        """Pipeline complet avec scraping et analyse"""
        print(f"\n{'='*70}")
        print(f"🚀 GÉNÉRATION AVANCÉE D'ARTICLE: {keyword}")
        print(f"{'='*70}")
        
        # 1. Scraper les SERPs
        if scrape_serps:
            serp_results = self.scrape_google_serps(keyword)
            time.sleep(3)
        else:
            serp_results = []
        
        # 2. Analyser les concurrents
        if serp_results:
            competitor_analysis = self.analyze_competitors_content(keyword, serp_results)
        else:
            print("  ⚠️  Pas de scraping - génération sans analyse concurrents")
            competitor_analysis = []
        
        # 3. Gap analysis
        if competitor_analysis:
            gap_analysis = self.create_content_gap_analysis(keyword, competitor_analysis)
        else:
            gap_analysis = f"Créer un article complet et approfondi sur '{keyword}'"
        
        # 4. Générer plan optimisé
        outline = self.generate_seo_optimized_outline(keyword, gap_analysis, target_length=1500)
        
        if not outline:
            print("❌ Échec génération du plan")
            return None
        
        print(f"\n📋 PLAN DE L'ARTICLE:")
        print("─" * 70)
        print(outline)
        print("─" * 70)
        
        # 5. Générer l'article complet
        sections = self.generate_complete_article(keyword, outline)
        
        if not sections:
            print("❌ Échec génération de l'article")
            return None
        
        # 6. Créer HTML
        word_count = sum(len(s.get('content', '').split()) for s in sections)
        reading_time = max(1, word_count // 200)
        
        metadata = {
            'word_count': word_count,
            'reading_time': reading_time
        }
        
        html = self.create_html_article(sections, keyword, metadata)
        
        # 7. Sauvegarder
        filepath = self.save_article(html, keyword)
        
        print(f"\n{'='*70}")
        print(f"✅ ARTICLE GÉNÉRÉ AVEC SUCCÈS!")
        print(f"{'='*70}")
        print(f"\n📂 Fichier: {filepath}")
        print(f"📊 {word_count} mots • ⏱️ {reading_time} min de lecture")
        
        return filepath


def main():
    """Main function"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   GÉNÉRATEUR D'ARTICLES BLOG AVANCÉ - Italiaanse Percolator      ║
║   Version: 2.0 - Avec Scraping & Analyse Concurrentielle         ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    # Clé API chargée depuis .env
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Clé API OpenAI manquante!")
        print("💡 Créer un fichier .env avec: OPENAI_API_KEY=ta-clé")
        return
    
    print("✅ Clé API OpenAI chargée depuis .env")
    
    
    # Mode
    print("\n📋 Mode de génération:")
    print("  1. Avec scraping Google (complet mais lent)")
    print("  2. Sans scraping (rapide, moins optimisé)")
    
    mode = input("\nChoix (1 ou 2): ").strip()
    scrape_serps = (mode == '1')
    
    # Générateur
    generator = AdvancedBlogGenerator(api_key)
    
    # Mots-clés
    keywords = [
        "italiaanse percolator reinigen",
        "beste italiaanse percolator 2024",
        "bialetti moka pot gebruiksaanwijzing",
        "verschil percolator en espresso",
        "koffie malen voor percolator",
        "aluminium of rvs percolator",
        "percolator op inductie",
        "italiaanse koffie thuis maken",
        "moka pot onderhoud tips",
        "geschiedenis italiaanse percolator"
    ]
    
    print("\n📚 Mots-clés suggérés:")
    for i, kw in enumerate(keywords, 1):
        print(f"  {i:2d}. {kw}")
    
    choice = input("\n✏️  Choix (numéro) ou entre un mot-clé: ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(keywords):
        keyword = keywords[int(choice) - 1]
    else:
        keyword = choice
    
    if not keyword:
        print("❌ Mot-clé requis!")
        return
    
    # Génération
    try:
        filepath = generator.generate_full_pipeline(keyword, scrape_serps=scrape_serps)
        
        if filepath:
            print(f"\n🎉 Article prêt à publier!")
            print(f"📁 Ouvrir: {filepath}")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Génération interrompue")
    
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
