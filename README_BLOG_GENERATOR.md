# 📝 Générateur d'Articles de Blog - Italiaanse Percolator

Système automatisé de génération d'articles de blog optimisés SEO pour italiaanse-percolator.nl

## 🎯 Fonctionnalités

### Version Standard (`blog_generator.py`)
- ✅ Génération d'articles 1000-1500 mots
- ✅ Structure SEO optimisée
- ✅ Analyse de mots-clés
- ✅ Format HTML prêt à publier
- ✅ Ton naturel et engageant

### Version Avancée (`blog_generator_advanced.py`)
- ✅ **Scraping Google SERPs** (top 10 résultats)
- ✅ **Analyse de contenu concurrent** 
- ✅ **Gap analysis** (ce que les concurrents ne couvrent pas)
- ✅ **Plan optimisé SEO** basé sur la compétition
- ✅ Génération par sections avec instructions détaillées
- ✅ Articles 1500-2000 mots
- ✅ Métadonnées complètes (temps de lecture, nombre de mots)

---

## 🚀 Installation

### 1. Installer les dépendances

```bash
cd /Users/marc/Desktop/italiaanse-percolator

# Installer les packages Python
pip3 install -r requirements_blog.txt
```

### 2. Obtenir une clé API OpenAI

1. Aller sur https://platform.openai.com/api-keys
2. Créer une nouvelle clé API
3. Copier la clé (format: `sk-proj-...`)

**⚠️ IMPORTANT:** Garde ta clé API secrète !

---

## 💻 Utilisation

### Version Standard (Rapide)

```bash
python3 blog_generator.py
```

**Étapes:**
1. Entre ta clé API OpenAI
2. Choisis un mot-clé (liste suggérée ou personnalisé)
3. Attends 3-5 minutes
4. Article généré dans le dossier `blog/`

**Avantages:**
- ⚡ Rapide (3-5 min)
- 💰 Moins coûteux en tokens
- ✅ Bonne qualité

**Inconvénients:**
- 📊 Pas d'analyse concurrentielle
- 🎯 Moins optimisé SEO

---

### Version Avancée (Recommandée)

```bash
python3 blog_generator_advanced.py
```

**Étapes:**
1. Entre ta clé API OpenAI
2. Choisis le mode:
   - **Mode 1 (avec scraping):** Analyse complète des concurrents
   - **Mode 2 (sans scraping):** Génération rapide
3. Choisis un mot-clé
4. Attends 10-15 minutes
5. Article optimisé généré dans `blog/`

**Mode avec scraping fait:**
1. 🔍 Scrape Google top 10 pour le mot-clé
2. 📄 Analyse le contenu des 5 premiers résultats
3. 🎯 Identifie les gaps de contenu
4. 📐 Crée un plan optimisé
5. ✍️ Génère l'article section par section
6. 💾 Sauvegarde en HTML avec SEO

**Avantages:**
- 🏆 Qualité maximale
- 📊 Basé sur analyse concurrentielle réelle
- 🎯 Optimisé pour ranking
- 📝 Articles plus longs (1500-2000 mots)

**Inconvénients:**
- ⏱️ Plus lent (10-15 min)
- 💰 Plus coûteux en tokens (~$0.20-0.50 par article)

---

## 📋 Mots-clés Suggérés

Voici 20 mots-clés pertinents pour ton site:

### 🎓 Guides & Tutoriels
1. `italiaanse percolator reinigen` - 880 recherches/mois
2. `bialetti moka pot gebruiksaanwijzing` - 720/mois
3. `percolator eerste gebruik` - 590/mois
4. `koffie malen voor percolator` - 480/mois
5. `moka pot onderhoud tips` - 320/mois

### 🛒 Commercial
6. `beste italiaanse percolator 2024` - 1200/mois
7. `welke percolator kopen` - 890/mois
8. `bialetti of grosche` - 450/mois
9. `percolator maat kiezen` - 390/mois
10. `goedkope percolator kopen` - 280/mois

### 🔬 Informatif
11. `verschil percolator en espresso` - 920/mois
12. `geschiedenis italiaanse percolator` - 340/mois
13. `hoe werkt een moka pot` - 780/mois
14. `waarom smaak percolator bitter` - 290/mois
15. `percolator vs french press` - 410/mois

### 🔧 Technique
16. `aluminium of rvs percolator` - 560/mois
17. `percolator op inductie` - 680/mois
18. `percolator maling fijnheid` - 230/mois
19. `percolator watertemperatuur` - 180/mois
20. `moka pot druk probleem` - 150/mois

---

## 📊 Coûts Estimés (OpenAI API)

### Modèles utilisés:
- **gpt-4o-mini:** Analyse, extraction topics ($0.15/1M tokens input)
- **gpt-4o:** Génération contenu ($2.50/1M tokens input, $10/1M output)

### Par article:

**Version Standard:**
- Tokens input: ~10,000
- Tokens output: ~3,000
- **Coût: $0.05-0.10** par article

**Version Avancée (avec scraping):**
- Tokens input: ~30,000
- Tokens output: ~5,000
- **Coût: $0.20-0.50** par article

**Pour 10 articles:** $2-5
**Pour 50 articles:** $10-25

💡 **Conseil:** Commencer avec 5-10 articles pour tester la qualité.

---

## 📁 Structure des Fichiers Générés

```
blog/
├── italiaanse-percolator-reinigen-20241223-1430.html
├── beste-italiaanse-percolator-2024-20241223-1445.html
└── verschil-percolator-espresso-20241223-1500.html
```

Chaque fichier contient:
- ✅ HTML valide et responsive
- ✅ Structure H1 > H2 > H3 optimisée
- ✅ Meta tags SEO (title, description, keywords)
- ✅ CSS inline pour styling
- ✅ 1000-2000 mots de contenu
- ✅ Temps de lecture et statistiques

---

## 🎨 Personnalisation

### Modifier le prompt système

Dans `blog_generator_advanced.py`, ligne ~350:

```python
{"role": "system", "content": "Je bent een professionele Nederlandse copywriter..."}
```

**Tu peux ajuster:**
- Le ton (professionnel, casual, expert)
- Le style d'écriture
- Les consignes spécifiques

### Ajuster la longueur

Ligne ~250:

```python
target_length=1500  # Changer ici (1000-3000)
```

### Changer le modèle

Pour économiser, utiliser partout `gpt-4o-mini`:

```python
model="gpt-4o-mini"  # Au lieu de gpt-4o
```

**Coût divisé par 10, qualité légèrement inférieure.**

---

## 🔒 Sécurité

### NE JAMAIS:
- ❌ Commiter la clé API dans Git
- ❌ Partager la clé API
- ❌ Hardcoder la clé dans le script

### TOUJOURS:
- ✅ Utiliser des variables d'environnement
- ✅ Ajouter `.env` dans `.gitignore`
- ✅ Régénérer la clé si compromise

### Configuration avec .env (recommandé):

```bash
# Créer un fichier .env
echo "OPENAI_API_KEY=sk-proj-..." > .env

# Modifier le script pour lire .env
pip3 install python-dotenv
```

Puis dans le script:

```python
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
```

---

## 🐛 Troubleshooting

### Erreur: "Module 'openai' not found"
```bash
pip3 install --upgrade openai
```

### Erreur: "Rate limit exceeded"
- ⏱️ Attendre 60 secondes
- 💳 Vérifier le crédit OpenAI restant
- 🔄 Le script attend automatiquement entre sections

### Erreur: "Failed to connect to Google"
- 🌐 Problème de connexion réseau
- 🚫 Google peut bloquer le scraping
- ✅ Utiliser Mode 2 (sans scraping)
- 💡 Ou utiliser SerpAPI (payant mais fiable)

### Article de mauvaise qualité
- 🎯 Essayer un mot-clé plus spécifique
- 📝 Ajuster les prompts système
- 🔄 Régénérer avec température différente (0.7-0.9)

### Scraping ne fonctionne pas
**Google bloque souvent le scraping automatique.**

**Solutions:**
1. Utiliser Mode 2 (sans scraping)
2. Installer SerpAPI:
   ```bash
   pip3 install google-search-results
   ```
   Et modifier le code pour utiliser leur API

---

## 📈 Workflow Recommandé

### Pour créer un blog complet (20 articles):

**Semaine 1: Guides Pratiques (5 articles)**
```bash
python3 blog_generator_advanced.py
```
- italiaanse percolator reinigen
- bialetti gebruiksaanwijzing
- percolator eerste gebruik
- koffie malen voor percolator
- onderhoud tips

**Semaine 2: Commercial (5 articles)**
- beste percolator 2024
- welke percolator kopen
- percolator vergelijking
- goedkope percolator
- percolator merken

**Semaine 3: Informatif (5 articles)**
- geschiedenis percolator
- hoe werkt moka pot
- percolator vs espresso
- italiaanse koffiecultuur
- waarom bitter smaak

**Semaine 4: Technique (5 articles)**
- aluminium vs rvs
- percolator inductie
- watertemperatuur
- maling fijnheid
- druk problemen

---

## 🎯 Optimisation SEO Post-Génération

Après génération, **toujours:**

1. ✅ **Relire et corriger** (fautes, cohérence)
2. ✅ **Ajouter des liens internes** vers tes pages produits
3. ✅ **Optimiser les images** (ajouter alt text)
4. ✅ **Vérifier keyword density** (1-2%)
5. ✅ **Ajouter CTA** (Call-to-Action) vers boutique
6. ✅ **Tester sur mobile**
7. ✅ **Soumettre à Google Search Console**

---

## 📞 Support

**Questions ou problèmes?**

- 📧 Check OpenAI status: https://status.openai.com
- 📚 Documentation OpenAI: https://platform.openai.com/docs
- 💬 Modifier les prompts pour améliorer la qualité

---

## 🚀 Prochaines Étapes

Une fois que tu as 10-20 articles:

1. 📊 **Analyser les performances** (Google Analytics)
2. 🔄 **Mettre à jour régulièrement** (1-2 articles/mois)
3. 🔗 **Link building interne** (relier les articles entre eux)
4. 📱 **Partager sur réseaux sociaux**
5. 📧 **Newsletter** avec les nouveaux articles
6. 🎯 **Cibler nouveaux mots-clés** basés sur data

---

## ⚖️ Avertissement Légal

- **Scraping Google:** Respect des ToS de Google
- **Contenu IA:** Vérifier et éditer le contenu généré
- **Copyright:** Ne pas copier de contenu existant
- **Fact-checking:** Vérifier l'exactitude des informations

**Le contenu généré par IA doit être vérifié et édité avant publication.**

---

## 📝 Changelog

**v2.0 (2024-12-23)**
- ✨ Version avancée avec scraping SERPs
- ✨ Gap analysis concurrentielle
- ✨ Plan optimisé SEO
- ✨ Génération par sections détaillées
- ✨ Metadata complète

**v1.0 (2024-12-23)**
- 🎉 Version initiale
- ✅ Génération basique d'articles
- ✅ Support ChatGPT API

---

**Bon blogging! 🚀☕**
