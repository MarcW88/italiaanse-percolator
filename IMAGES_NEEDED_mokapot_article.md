# 📸 Images et Schémas Nécessaires pour l'Article Mokapot

## 🎨 3 Visuels à Créer

### 1. PHOTO: Mokapot en 3 parties (Priorité HAUTE)

**Emplacement:** Section 1 - "Wat is een Italiaanse percolator"

**Spécifications:**
- Photo d'une mokapot démontée en 3 parties
- Vue aérienne ou légèrement en angle
- Les 3 parties bien séparées et alignées

**Annotations nécessaires:**
```
┌─────────────────────────────────────┐
│                                     │
│   [Bovenste kan]                    │ ← Label: "Opvangkan"
│                                     │    (waar koffie komt)
│                                     │
├─────────────────────────────────────┤
│                                     │
│   [Filterbakje]                     │ ← Label: "Filterbakje"
│   (trechter vorm)                   │    (voor gemalen koffie)
│                                     │
├─────────────────────────────────────┤
│                                     │
│   [Onderste reservoir]              │ ← Label: "Waterreservoir"
│   (met veiligheidsventiel)          │    (vul tot ventiel)
│                                     │
└─────────────────────────────────────┘
```

**Pijltjes toevoegen die wijzen naar:**
- Veiligheidsventiel (op onderste deel)
- Rubberen ring (tussen onder en filter)
- Centraal pijpje (in bovenste kan)

**Suggestie:**
- Gebruik Photoshop/Canva om pijlen en labels toe te voegen
- Kleuren: Pijlen in oranje (#D2691E), labels in wit op semi-transparante achtergrond

---

### 2. SCHEMA: Doorsnede Mokapot - Hoe Water Stroomt (Priorité HAUTE)

**Emplacement:** Section 2 - "Hoe werkt een mokapot"

**Type:** Simpele technische illustratie / infographic

**Elementen:**
```
     ╔═══════════════════════╗
     ║   KOFFIE ☕           ║  ← Bovenste kamer (leeg aan begin)
     ║                       ║
     ║        ↑ ↑ ↑          ║  ← Koffie komt hier uit pijpje
     ╠═══════════════════════╣
     ║  ███████████████████  ║  ← Gemalen koffie (bruin)
     ║  ▓▓▓▓▓ FILTER ▓▓▓▓▓  ║  ← Filter met gaatjes
     ╠═══════════════════════╣
     ║   ~~~~~ WATER ~~~~~   ║  ← Water (blauw)
     ║   ~~~~~ HOT   ~~~~~   ║  
     ║ [●] ← veiligheidsventiel
     ╚═══════════════════════╝
           🔥 VUUR
```

**Pijlen toevoegen:**
1. **Blauwe pijl** van water omhoog door filter
2. **Bruine pijl** van koffie naar pijpje
3. **Bruine pijl** van pijpje naar bovenste kamer
4. **Rode golven** onder = warmte

**Kleuren:**
- Water: Lichtblauw (#4FC3F7)
- Koffie/gemalen: Bruin (#6F4E37)
- Filter: Grijs (#999)
- Vuur: Oranje/rood gradient
- Pijlen: #D2691E (oranje)

**Software suggesties:**
- Canva (templates voor infographics)
- Adobe Illustrator
- Figma (gratis)
- PowerPoint/Keynote (simpel maar effectief)

---

### 3. SCHEMA: De 6 Stappen Visueel (Priorité MOYENNE)

**Emplacement:** Section 2 - na de stap-voor-stap tekst

**Type:** Horizontale timeline met 6 illustraties

**Format:**
```
[1] → [2] → [3] → [4] → [5] → [6]
```

**Elk nummer toont:**

**Stap 1:** Waterkan met water + pijl omlaag naar mokapot
**Stap 2:** Filterbakje + koffiebonen + schepje
**Stap 3:** Mokapot in elkaar gedraaid (handen symbool)
**Stap 4:** Mokapot op gasvlam
**Stap 5:** Mokapot met pruttelsymbool (♪ noten) + stoom
**Stap 6:** Kopje koffie met checkmark ✓

**Stijl:**
- Flat design / line art
- Kleuren: Oranje (#D2691E), bruin, zwart, wit
- Minimalistisch maar duidelijk

---

## 🎨 Alternatieve Oplossingen (als je geen tijd hebt)

### Plan A: Gebruik Stockfoto's + Annotaties
1. Koop stockfoto's op:
   - Shutterstock
   - iStock
   - Adobe Stock
   - Unsplash (gratis maar beperkt)

2. Zoektermen:
   - "moka pot parts"
   - "moka pot exploded view"
   - "italian coffee maker diagram"

3. Bewerk met Canva:
   - Upload foto
   - Voeg pijlen toe
   - Voeg labels toe

### Plan B: AI Image Generation
Gebruik tools zoals:
- **Midjourney:** "technical diagram of moka pot cross section, labeled parts, flat design, educational"
- **DALL-E 3:** "infographic showing how moka pot works, water flow arrows, simple illustration"
- **Stable Diffusion:** Met prompt engineering

### Plan C: Vraag het aan een Designer
Platforms:
- **Fiverr:** €10-50 voor simpele infographics
- **99designs:** Design contest
- **Upwork:** Freelance designers

---

## 📐 Specificaties Techniques

### Afmetingen:
- **Breedte:** 800-1200px (responsive)
- **Hoogte:** Variabel, maar max 800px
- **Format:** JPG ou PNG
- **Kwaliteit:** 72-150 DPI (web optimalisé)
- **Bestandsgrootte:** Max 200KB per image

### Où Placer les Images:

```
/Images/
├── mokapot-3-delen-labeled.jpg         (Image 1)
├── mokapot-doorsnede-schema.png        (Schema 1)
└── mokapot-6-stappen-timeline.png      (Schema 2)
```

### Code HTML pour insérer:

**Image 1 (remplacer le placeholder):**
```html
<img src="../Images/mokapot-3-delen-labeled.jpg" 
     alt="Italiaanse mokapot in 3 delen: waterreservoir, filterbakje en opvangkan"
     style="width: 100%; max-width: 800px; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
```

**Schema 1:**
```html
<img src="../Images/mokapot-doorsnede-schema.png" 
     alt="Schema doorsnede mokapot met waterstroming"
     style="width: 100%; max-width: 700px; height: auto; margin: 2rem auto; display: block;">
```

**Schema 2:**
```html
<img src="../Images/mokapot-6-stappen-timeline.png" 
     alt="6 stappen mokapot koffie zetten visueel"
     style="width: 100%; max-width: 900px; height: auto;">
```

---

## ✅ Checklist

- [ ] Créer ou trouver Image 1 (mokapot 3 delen)
- [ ] Ajouter annotations/labels à Image 1
- [ ] Créer Schema 1 (doorsnede)
- [ ] Créer Schema 2 (6 stappen) - optionnel
- [ ] Optimiser toutes les images pour le web (compression)
- [ ] Upload dans dossier /Images/
- [ ] Remplacer les placeholders dans le HTML
- [ ] Tester sur mobile et desktop
- [ ] Vérifier temps de chargement

---

## 🎯 Priorités

**PRIORITÉ 1 (MUST HAVE):**
- Image 1: Mokapot en 3 parties avec labels

**PRIORITÉ 2 (SHOULD HAVE):**
- Schema 1: Doorsnede avec waterstroming

**PRIORITÉ 3 (NICE TO HAVE):**
- Schema 2: Timeline 6 stappen

**Tu peux publier l'article SANS les images,** les placeholders sont stylés et expliquent ce qui manque.

---

## 💡 Conseil Final

Si tu veux publier rapidement:
1. Cherche une bonne stockfoto de mokapot
2. Utilise Canva (gratuit) pour ajouter pijlen en labels
3. Export en PNG
4. Upload et remplace le placeholder
5. **Total temps: 30 minutes**

Les schémas techniques peuvent venir plus tard dans une v2 de l'article.
