---
name: content-audit
description: Beslis voor bestaande pagina's op italiaanse-percolator.nl of ze KEEP, UPDATE, MERGE, REDIRECT of REMOVE zijn voordat er herschreven wordt.
license: MIT
---

# Content audit — italiaanse-percolator.nl

Gebruik deze skill als eerste stap bij SEO-herstel.

## Doel

Niet elke zwakke pagina moet herschreven worden. Bepaal eerst of de URL nog een duidelijke functie en herstelpotentieel heeft.

## Vereiste informatie

Gebruik zoveel mogelijk:
- huidige URL en inhoud;
- historische en recente GSC-data;
- belangrijkste queries en vroegere posities;
- organische clicks en impressies vóór en na de daling;
- eventuele backlinks of interne links;
- overlap met andere pagina's in de repo;
- paginatype: product, merk, categorie, vergelijking, gids of FAQ.

Ontbreekt data, vermeld dat expliciet. Vul niets in op basis van aannames.

## Beslissingen

### KEEP
Gebruik wanneer de pagina inhoudelijk sterk, actueel en uniek is en nog een duidelijke zoekintentie bedient. Kleine taalcorrecties zijn toegestaan, maar geen volledige rewrite.

### UPDATE
Gebruik wanneer de URL historisch potentieel toont of een nuttige functie heeft, maar inhoud mist, verouderd is, te generiek is of onvoldoende beslissingswaarde biedt.

### MERGE
Gebruik wanneer twee of meer URL's vrijwel dezelfde intentie bedienen en afzonderlijk weinig onderscheid hebben. Kies de sterkste canonieke bestemming op basis van historische prestaties, links, relevantie en URL-logica.

### REDIRECT
Gebruik wanneer de specifieke pagina geen zelfstandige reden van bestaan meer heeft, maar een relevante opvolger bestaat. Geef de voorgestelde doel-URL.

### REMOVE
Alleen wanneer de pagina geen relevante intentie, historische waarde, links of unieke functie heeft en niet logisch te consolideren is.

## Extra risico's voor deze site

Flag:
- productbeschrijvingen die hoofdzakelijk fabrikant-/merchantinformatie herhalen;
- honderden pagina's met hetzelfde template en weinig unieke beslissingswaarde;
- bijna identieke vergelijkingen;
- generieke AI-intro's en conclusies;
- pagina's waarvan alleen merk/model verschilt;
- verouderde producten of prijzen die als actueel worden voorgesteld;
- pagina's zonder duidelijk antwoord op "voor wie is dit product geschikt?".

## Output

Geef:
1. **Decision:** KEEP / UPDATE / MERGE / REDIRECT / REMOVE
2. **Confidence:** high / medium / low
3. **Evidence:** concrete signalen
4. **Main problem:** één kernprobleem
5. **Recovery potential:** waarom herstel wel/niet zinvol is
6. **Next skill:** welke stap hierna moet volgen

Herschrijf de pagina niet tijdens deze audit.
