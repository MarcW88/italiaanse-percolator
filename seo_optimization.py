#!/usr/bin/env python3
"""
Script pour optimiser le SEO des pages HTML :
1. Ajouter self-canonical à chaque page
2. Ajouter hreflang nl-NL
3. Supprimer les emojis des h2 et h3
"""

import os
import re
from pathlib import Path

def get_page_url(file_path, base_url="https://italiaanse-percolator.nl"):
    """Génère l'URL canonique pour une page"""
    # Convertir le chemin de fichier en URL relative
    relative_path = file_path.replace('/Users/marc/Desktop/italiaanse-percolator/', '')
    
    # Remplacer index.html par / pour la racine
    if relative_path == 'index.html':
        return base_url + '/'
    
    # Pour les autres fichiers, construire l'URL complète
    return f"{base_url}/{relative_path}"

def remove_emojis_from_headings(content):
    """Supprime les emojis des balises h2 et h3"""
    # Pattern pour détecter les emojis (caractères Unicode dans les plages d'emojis)
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"  # dingbats
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"  # supplemental symbols
        "]+", 
        flags=re.UNICODE
    )
    
    def clean_heading(match):
        tag_start = match.group(1)  # <h2> ou <h3>
        content = match.group(2)    # contenu entre les balises
        tag_end = match.group(3)    # </h2> ou </h3>
        
        # Supprimer les emojis et nettoyer les espaces
        clean_content = emoji_pattern.sub('', content).strip()
        
        return f"{tag_start}{clean_content}{tag_end}"
    
    # Appliquer le nettoyage aux h2 et h3
    content = re.sub(r'(<h[23][^>]*>)(.*?)(<\/h[23]>)', clean_heading, content, flags=re.DOTALL)
    
    return content

def add_seo_tags(content, canonical_url):
    """Ajoute les balises canonical et hreflang dans le head"""
    
    # Vérifier si canonical existe déjà
    if 'rel="canonical"' not in content:
        canonical_tag = f'  <link rel="canonical" href="{canonical_url}">\n'
        
        # Insérer avant la fermeture du head ou après les autres meta tags
        if '</head>' in content:
            content = content.replace('</head>', f'{canonical_tag}</head>')
        else:
            # Si pas de </head>, insérer après les meta tags existants
            meta_pattern = r'(<meta[^>]*>)'
            matches = list(re.finditer(meta_pattern, content))
            if matches:
                last_meta = matches[-1]
                insert_pos = last_meta.end()
                content = content[:insert_pos] + f'\n{canonical_tag}' + content[insert_pos:]
    
    # Vérifier si hreflang existe déjà
    if 'hreflang=' not in content:
        hreflang_tag = f'  <link rel="alternate" hreflang="nl-NL" href="{canonical_url}">\n'
        
        # Insérer avant la fermeture du head
        if '</head>' in content:
            content = content.replace('</head>', f'{hreflang_tag}</head>')
        else:
            # Insérer après canonical si on vient de l'ajouter
            if 'rel="canonical"' in content:
                content = content.replace(canonical_tag, canonical_tag + hreflang_tag)
    
    return content

def process_html_file(file_path):
    """Traite un fichier HTML pour les optimisations SEO"""
    print(f"Traitement de : {file_path}")
    
    try:
        # Lire le fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Générer l'URL canonique
        canonical_url = get_page_url(file_path)
        
        # Appliquer les optimisations
        content = add_seo_tags(content, canonical_url)
        content = remove_emojis_from_headings(content)
        
        # Sauvegarder le fichier modifié
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Optimisé : {file_path}")
        print(f"   Canonical: {canonical_url}")
        
    except Exception as e:
        print(f"❌ Erreur lors du traitement de {file_path}: {e}")

def main():
    """Fonction principale"""
    base_dir = "/Users/marc/Desktop/italiaanse-percolator"
    
    # Trouver tous les fichiers HTML
    html_files = []
    
    # Fichiers à la racine
    for file in os.listdir(base_dir):
        if file.endswith('.html'):
            html_files.append(os.path.join(base_dir, file))
    
    # Fichiers dans les sous-dossiers
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if file_path not in html_files:  # Éviter les doublons
                    html_files.append(file_path)
    
    print(f"Trouvé {len(html_files)} fichiers HTML à traiter")
    print("=" * 50)
    
    # Traiter chaque fichier
    for file_path in sorted(html_files):
        process_html_file(file_path)
        print()
    
    print("=" * 50)
    print("✅ Optimisation SEO terminée !")

if __name__ == "__main__":
    main()
