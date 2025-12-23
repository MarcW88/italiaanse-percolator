#!/usr/bin/env python3
"""
Script pour uniformiser le design des articles de blog avec le style.css du site
"""

import re
from pathlib import Path

# Navigation HTML standard du site
STANDARD_NAV = '''  <!-- Navigation -->
  <nav class="navbar">
    <div class="container">
      <div class="nav-container">
        <a href="../index.html" class="nav-brand">Italiaanse Percolator</a>
        <ul class="nav-menu">
          <li><a href="../index.html" class="nav-link">Home</a></li>
          <li><a href="../beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
          <li><a href="../koopgids/index.html" class="nav-link active">Koopgids</a></li>
          <li><a href="../marques/index.html" class="nav-link">Merken</a></li>
          <li><a href="../vergelijking/index.html" class="nav-link">Vergelijking</a></li>
          <li><a href="../over-ons.html" class="nav-link">Over ons</a></li>
          <li><a href="../boutique.html" class="nav-link" style="background: #D2691E; color: white; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600;">Winkel</a></li>
        </ul>
      </div>
    </div>
  </nav>'''

def update_article_structure(filepath, title, breadcrumb_text):
    """Met à jour la structure d'un article pour utiliser le design system du site"""
    
    print(f"\n📝 Traitement de {Path(filepath).name}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sauvegarder l'ancien contenu article
    article_match = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
    if not article_match:
        print("  ⚠️  Balise <article> non trouvée")
        return
    
    article_content = article_match.group(1)
    
    # Extraire le head existant mais enlever les styles custom
    head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
    if head_match:
        head_content = head_match.group(1)
        # Supprimer la balise <style> custom
        head_content = re.sub(r'<style>.*?</style>', '', head_content, flags=re.DOTALL)
    
    # Créer le nouveau head
    new_head = f'''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {re.search(r'<meta name="description"[^>]*>', content).group(0) if re.search(r'<meta name="description"[^>]*>', content) else ''}
    {re.search(r'<meta name="keywords"[^>]*>', content).group(0) if re.search(r'<meta name="keywords"[^>]*>', content) else ''}
    {re.search(r'<meta name="author"[^>]*>', content).group(0) if re.search(r'<meta name="author"[^>]*>', content) else ''}
    {re.search(r'<title>[^<]*</title>', content).group(0) if re.search(r'<title>[^<]*</title>', content) else ''}
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;700&family=DM+Serif+Display:ital,wght@0,400&display=swap" rel="stylesheet">
    
    <!-- Styles -->
    <link rel="stylesheet" href="../style.css">
    
    <style>
        /* Styles spécifiques pour les articles de blog */
        .article-content {{
            max-width: 900px;
            margin: 0 auto;
        }}
        
        .article-header {{
            text-align: center;
            margin-bottom: var(--sp-8);
            padding-bottom: var(--sp-6);
            border-bottom: 3px solid var(--coffee);
        }}
        
        .article-meta {{
            color: var(--text-dim);
            font-size: var(--fs-sm);
            margin-top: var(--sp-4);
        }}
        
        .table-of-contents {{
            background: var(--surface-soft);
            padding: var(--sp-6);
            border-radius: var(--r-lg);
            margin: var(--sp-8) 0;
            border-left: 4px solid var(--coffee);
        }}
        
        .table-of-contents h2 {{
            font-size: var(--fs-2xl);
            margin-bottom: var(--sp-4);
        }}
        
        .table-of-contents ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .table-of-contents li {{
            padding: var(--sp-2) 0;
            padding-left: var(--sp-6);
            position: relative;
        }}
        
        .table-of-contents li:before {{
            content: "→";
            position: absolute;
            left: 0;
            color: var(--coffee);
            font-weight: bold;
        }}
        
        .article-content h2 {{
            font-size: var(--fs-3xl);
            color: var(--text);
            margin-top: var(--sp-12);
            margin-bottom: var(--sp-6);
            padding-bottom: var(--sp-3);
            border-bottom: 2px solid var(--coffee);
        }}
        
        .article-content h3 {{
            font-size: var(--fs-2xl);
            color: var(--text-dim);
            margin-top: var(--sp-8);
            margin-bottom: var(--sp-4);
        }}
        
        .article-content h4 {{
            font-size: var(--fs-xl);
            color: var(--text-dim);
            margin-top: var(--sp-6);
            margin-bottom: var(--sp-3);
        }}
        
        .comparison-table {{
            width: 100%;
            border-collapse: collapse;
            margin: var(--sp-8) 0;
            box-shadow: var(--shadow-md);
            border-radius: var(--r-lg);
            overflow: hidden;
        }}
        
        .comparison-table th {{
            background: var(--coffee);
            color: white;
            padding: var(--sp-4);
            text-align: left;
            font-weight: 600;
        }}
        
        .comparison-table td {{
            padding: var(--sp-4);
            border-bottom: 1px solid var(--surface-soft);
            vertical-align: top;
        }}
        
        .comparison-table tr:hover {{
            background: var(--surface-soft);
        }}
        
        .comparison-table tr:nth-child(even) {{
            background: #fafafa;
        }}
        
        .highlight-box {{
            background: #fff3e0;
            border-left: 4px solid var(--coffee);
            padding: var(--sp-6);
            margin: var(--sp-8) 0;
            border-radius: var(--r-md);
        }}
        
        .tip-box {{
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: var(--sp-6);
            margin: var(--sp-8) 0;
            border-radius: var(--r-md);
        }}
        
        .tip-box:before {{
            content: "💡 PRO TIP: ";
            font-weight: bold;
            color: #2196f3;
        }}
        
        .warning-box {{
            background: #fff3e0;
            border-left: 4px solid #ff9800;
            padding: var(--sp-6);
            margin: var(--sp-8) 0;
            border-radius: var(--r-md);
        }}
        
        .warning-box:before {{
            content: "⚠️ LET OP: ";
            font-weight: bold;
            color: #ff9800;
        }}
        
        .checklist {{
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: var(--sp-6);
            margin: var(--sp-8) 0;
            border-radius: var(--r-md);
        }}
        
        .checklist ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .checklist li:before {{
            content: "✓ ";
            color: #4caf50;
            font-weight: bold;
            margin-right: var(--sp-2);
        }}
        
        .author-box {{
            background: linear-gradient(135deg, #fff9f0 0%, #ffe9d0 100%);
            border-left: 4px solid #4caf50;
            border-radius: var(--r-lg);
            padding: var(--sp-8);
            margin: var(--sp-12) 0;
            display: flex;
            gap: var(--sp-6);
            align-items: flex-start;
        }}
        
        .author-avatar {{
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid var(--coffee);
            flex-shrink: 0;
        }}
        
        .author-info h3 {{
            color: #4caf50;
            font-size: var(--fs-2xl);
            margin: 0 0 var(--sp-2) 0;
        }}
        
        .author-name {{
            font-size: var(--fs-lg);
            font-weight: 600;
            color: var(--text);
            margin-bottom: var(--sp-4);
        }}
        
        .author-bio {{
            color: var(--text-dim);
            line-height: 1.7;
            margin-bottom: var(--sp-4);
        }}
        
        .comments-section {{
            background: var(--surface-soft);
            border-radius: var(--r-lg);
            padding: var(--sp-8);
            margin: var(--sp-12) 0;
        }}
        
        .comments-section h3 {{
            color: var(--coffee);
            font-size: var(--fs-3xl);
            margin-bottom: var(--sp-6);
        }}
        
        .comment-form {{
            background: var(--surface);
            padding: var(--sp-6);
            border-radius: var(--r-lg);
            margin-bottom: var(--sp-8);
            box-shadow: var(--shadow-sm);
        }}
        
        .form-group {{
            margin-bottom: var(--sp-4);
        }}
        
        .form-group label {{
            display: block;
            font-weight: 600;
            margin-bottom: var(--sp-2);
            color: var(--text-dim);
        }}
        
        .form-group input,
        .form-group textarea {{
            width: 100%;
            padding: var(--sp-3);
            border: 1px solid #ddd;
            border-radius: var(--r-md);
            font-family: inherit;
            font-size: var(--fs-base);
        }}
        
        .form-group textarea {{
            min-height: 120px;
            resize: vertical;
        }}
        
        .submit-btn {{
            background: var(--coffee);
            color: white;
            padding: var(--sp-3) var(--sp-8);
            border: none;
            border-radius: var(--r-lg);
            font-size: var(--fs-base);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        
        .submit-btn:hover {{
            background: var(--coffee-light);
            transform: translateY(-1px);
        }}
        
        .comment {{
            background: var(--surface);
            padding: var(--sp-6);
            border-radius: var(--r-lg);
            margin-bottom: var(--sp-4);
            box-shadow: var(--shadow-sm);
        }}
        
        .comment-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: var(--sp-4);
            padding-bottom: var(--sp-3);
            border-bottom: 1px solid var(--surface-soft);
        }}
        
        .comment-author {{
            font-weight: 600;
            color: var(--coffee);
        }}
        
        .comment-date {{
            color: var(--text-light);
            font-size: var(--fs-sm);
        }}
        
        .comment-body {{
            color: var(--text-dim);
            line-height: 1.6;
        }}
        
        @media (max-width: 768px) {{
            .author-box {{
                flex-direction: column;
                text-align: center;
                align-items: center;
            }}
        }}
    </style>
</head>'''
    
    # Créer le breadcrumb
    breadcrumb = f'''
  <!-- Breadcrumbs -->
  <div class="container" style="padding-top: var(--sp-6);">
    <div class="breadcrumbs">
      <a href="../index.html">Home</a>
      <span>›</span>
      <a href="../koopgids/index.html">Koopgids</a>
      <span>›</span>
      <span>{breadcrumb_text}</span>
    </div>
  </div>'''
    
    # Extraire le titre H1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', article_content)
    h1_text = h1_match.group(1) if h1_match else title
    
    # Construire le nouveau document
    new_content = f'''<!DOCTYPE html>
<html lang="nl">
{new_head}
<body>
{STANDARD_NAV}

{breadcrumb}

  <!-- Article Content -->
  <section class="section-sm">
    <div class="container">
      <div class="article-content">
{article_content}
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer style="background: #333; color: white; padding: var(--sp-8); text-align: center; margin-top: var(--sp-16);">
    <p>&copy; 2024 Italiaanse-Percolator.nl | Alle rechten voorbehouden</p>
    <p style="font-size: var(--fs-sm); opacity: 0.8; margin-top: var(--sp-2);">Authentieke Italiaanse koffie thuis</p>
  </footer>

  <!-- Schema.org et Scripts -->
  {re.search(r'<script type="application/ld\+json">.*?</script>', content, re.DOTALL).group(0) if re.search(r'<script type="application/ld\+json">.*?</script>', content, re.DOTALL) else ''}
  {re.search(r'<script>.*?handleCommentSubmit.*?</script>', content, re.DOTALL).group(0) if re.search(r'<script>.*?handleCommentSubmit.*?</script>', content, re.DOTALL) else ''}

</body>
</html>
'''
    
    # Sauvegarder
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✅ Article mis à jour avec le design standard du site")

def main():
    print("🎨 Uniformisation du design des articles de blog...\n")
    
    articles = [
        {
            'file': '/Users/marc/Desktop/italiaanse-percolator/koopgids/wat-is-italiaanse-percolator-mokapot.html',
            'title': 'Wat is een Italiaanse Percolator',
            'breadcrumb': 'Wat is een Italiaanse percolator'
        },
        {
            'file': '/Users/marc/Desktop/italiaanse-percolator/koopgids/italiaanse-percolator-gebruiken-handleiding.html',
            'title': 'Gebruikshandleiding',
            'breadcrumb': 'Italiaanse percolator gebruiken'
        },
        {
            'file': '/Users/marc/Desktop/italiaanse-percolator/koopgids/beste-koffiebonen-italiaanse-percolator.html',
            'title': 'Beste Koffiebonen',
            'breadcrumb': 'Welke koffiebonen voor mokapot'
        }
    ]
    
    for article in articles:
        try:
            update_article_structure(article['file'], article['title'], article['breadcrumb'])
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
    
    print("\n✅ Uniformisation terminée!")

if __name__ == '__main__':
    main()
