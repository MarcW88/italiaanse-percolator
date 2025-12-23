# Plan d'Uniformisation des Articles de Blog

## 🎯 Objectif
Uniformiser le design des 3 nouveaux articles avec le style du site (comme `percolator-vs-espressoapparaat.html`)

## 📋 Changements Nécessaires

### 1. HEAD Section
**Avant:** Styles CSS inline custom
**Après:** 
- Ajouter les Google Fonts
- Garder `<link rel="stylesheet" href="../style.css">`
- Réduire les styles custom au minimum (garder uniquement ceux spécifiques aux articles)

### 2. Navigation
**Avant:**
```html
<nav class="main-nav">
    <div class="container">
        <a href="../index.html" class="logo">Italiaanse-Percolator.nl</a>
        ...
```

**Après:**
```html
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
</nav>
```

### 3. Breadcrumbs (À AJOUTER)
```html
<div class="container" style="padding-top: var(--sp-6);">
    <div class="breadcrumbs">
      <a href="../index.html">Home</a>
      <span>›</span>
      <a href="../koopgids/index.html">Koopgids</a>
      <span>›</span>
      <span>[Titre de l'article]</span>
    </div>
</div>
```

### 4. Structure du Contenu
**Avant:**
```html
<article class="article-content">
    <header class="article-header">...</header>
    [contenu]
</article>
```

**Après:**
```html
<section class="section-sm">
    <div class="container">
      <div class="article-content">
        <header class="article-header">...</header>
        [contenu exact - ne rien supprimer]
      </div>
    </div>
</section>
```

### 5. Variables CSS à Utiliser
Remplacer les valeurs hardcodées par les variables du `style.css`:

**Couleurs:**
- `#D2691E` → `var(--coffee)` ou garder car c'est l'orange signature
- `#f8f9fa` → `var(--surface-soft)`
- `#333` → `var(--text)`
- `#666`, `#555` → `var(--text-dim)`

**Spacing:**
- `2rem` → `var(--sp-8)`
- `1.5rem` → `var(--sp-6)`
- `1rem` → `var(--sp-4)`
- `3rem` → `var(--sp-12)`

**Border Radius:**
- `8px` → `var(--r-lg)`
- `4px` → `var(--r-md)`

**Font Sizes:**
- `2.5rem` → `var(--fs-4xl)` ou garder selon context
- `1.8rem` → `var(--fs-3xl)`
- `1.5rem` → `var(--fs-2xl)`

### 6. Footer
**Avant:** Footer custom inline
**Après:**
```html
<footer style="background: #333; color: white; padding: var(--sp-8); text-align: center; margin-top: var(--sp-16);">
    <p>&copy; 2024 Italiaanse-Percolator.nl | Alle rechten voorbehouden</p>
    <p style="font-size: var(--fs-sm); opacity: 0.8; margin-top: var(--sp-2);">Authentieke Italiaanse koffie thuis</p>
</footer>
```

## 📝 Articles à Modifier

1. ✅ `wat-is-italiaanse-percolator-mokapot.html`
   - Breadcrumb: "Wat is een Italiaanse percolator"
   
2. ✅ `italiaanse-percolator-gebruiken-handleiding.html`
   - Breadcrumb: "Italiaanse percolator gebruiken"
   
3. ✅ `beste-koffiebonen-italiaanse-percolator.html`
   - Breadcrumb: "Welke koffiebonen voor mokapot"

## ⚠️ À NE PAS CHANGER

- ❌ Le contenu texte des articles
- ❌ Les tableaux comparatifs
- ❌ Le bloc auteur
- ❌ La section commentaires
- ❌ Les Schema.org scripts
- ❌ Les JavaScript fonctionnels

## ✅ À GARDER

- Les styles custom pour:
  - `.author-box`
  - `.comments-section`
  - `.comparison-table`
  - `.tip-box`, `.warning-box`, `.highlight-box`
  - Tout ce qui est spécifique aux articles de blog

Mais les adapter pour utiliser les variables CSS du site au lieu des valeurs hardcodées.
