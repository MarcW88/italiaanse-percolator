# 🚀 Utilisation Rapide - Générateur d'Articles

## ✅ Configuration Terminée !

Ta clé API OpenAI est **déjà configurée** dans le fichier `.env`

---

## 📝 Générer un Article (2 étapes)

### Étape 1: Installer les dépendances (1 fois)

```bash
cd /Users/marc/Desktop/italiaanse-percolator
pip3 install -r requirements_blog.txt
```

### Étape 2: Lancer le générateur

**Option A: Version Simple** (recommandé pour commencer)
```bash
python3 blog_generator.py
```

**Option B: Version Avancée** (meilleure qualité)
```bash
python3 blog_generator_advanced.py
```

---

## 🎯 Les Scripts Font Quoi?

### `blog_generator.py` - Version Simple
- ✅ **Pas besoin de taper la clé API** (déjà dans .env)
- ⚡ Rapide: 3-5 minutes
- 📝 Génère 1000-1500 mots
- 💰 Coût: ~$0.10 par article

### `blog_generator_advanced.py` - Version Avancée  
- ✅ **Pas besoin de taper la clé API** (déjà dans .env)
- 🔍 Analyse les concurrents sur Google
- 📊 Identifie les gaps de contenu
- 📝 Génère 1500-2000 mots optimisés SEO
- ⏱️ Plus lent: 10-15 minutes
- 💰 Coût: ~$0.30 par article

---

## 📋 Workflow Simple

```bash
# 1. Installer (1 seule fois)
pip3 install -r requirements_blog.txt

# 2. Générer un article
python3 blog_generator_advanced.py

# 3. Suivre les instructions à l'écran
# - Choisis Mode 2 (sans scraping, plus rapide)
# - Choisis un mot-clé (ex: choix 1)
# - Attends 5-10 minutes

# 4. Article prêt dans le dossier blog/
```

---

## 🎯 Mots-clés Suggérés

Quand le script demande un mot-clé, **tape le numéro** :

1. **italiaanse percolator reinigen** ← COMMENCE ICI
2. beste italiaanse percolator 2024
3. bialetti moka pot gebruiksaanwijzing
4. verschil percolator en espresso
5. koffie malen voor percolator
6. aluminium of rvs percolator
7. percolator op inductie
8. italiaanse koffie thuis maken
9. moka pot onderhoud tips
10. geschiedenis italiaanse percolator

**Ou tape ton propre mot-clé !**

---

## 📂 Où Trouver les Articles?

Les articles générés sont dans:
```
/Users/marc/Desktop/italiaanse-percolator/blog/
```

Format: `nom-du-mot-cle-20241223-1430.html`

---

## 💰 Coûts

**Avec ta clé API actuelle:**
- 1 article simple: ~$0.10
- 1 article avancé: ~$0.30
- 10 articles: ~$2-3
- 50 articles: ~$10-15

💡 **Astuce:** Commence avec 5 articles pour tester

---

## 🆘 Problèmes?

### "Module 'openai' not found"
```bash
pip3 install --upgrade openai requests beautifulsoup4 python-dotenv
```

### "Rate limit exceeded"
- Attendre 1 minute
- Ton compte OpenAI a peut-être besoin de crédit
- Vérifier: https://platform.openai.com/account/billing

### Article de mauvaise qualité
- Essayer un mot-clé plus spécifique
- Utiliser la version avancée
- Régénérer (résultat différent à chaque fois)

---

## 🔒 Sécurité

✅ Ta clé API est dans `.env`
✅ `.env` est protégé par `.gitignore`
✅ Elle ne sera JAMAIS commitée sur Git

**Ne partage JAMAIS ta clé API !**

---

## ✨ Exemple d'Utilisation

```bash
$ python3 blog_generator_advanced.py

╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   GÉNÉRATEUR D'ARTICLES BLOG AVANCÉ - Italiaanse Percolator      ║
║   Version: 2.0 - Avec Scraping & Analyse Concurrentielle         ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

✅ Clé API OpenAI chargée depuis .env

📋 Mode de génération:
  1. Avec scraping Google (complet mais lent)
  2. Sans scraping (rapide, moins optimisé)

Choix (1 ou 2): 2

📚 Mots-clés suggérés:
   1. italiaanse percolator reinigen
   2. beste italiaanse percolator 2024
   ...

✏️  Choix (numéro) ou entre un mot-clé: 1

🚀 GÉNÉRATION AVANCÉE D'ARTICLE: italiaanse percolator reinigen
...
✅ ARTICLE GÉNÉRÉ AVEC SUCCÈS!
📂 Fichier: blog/italiaanse-percolator-reinigen-20241223-1430.html
```

---

## 📖 Plus d'Infos

- **Guide complet:** `README_BLOG_GENERATOR.md`
- **50 mots-clés:** `keywords_blog.txt`
- **Guide rapide:** `QUICKSTART_BLOG.md`

---

**C'est tout ! Tu es prêt à générer des articles ! 🎉**

```bash
python3 blog_generator_advanced.py
```
