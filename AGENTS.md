# Italiaansepercolator.nl — SEO recovery instructions

Deze repository bevat de website italiaanse-percolator.nl. Voor contentherstel en redactionele wijzigingen gelden onderstaande instructies.

## Doel

Herstel pagina's die organische zichtbaarheid verloren hebben door de inhoud aantoonbaar nuttiger, specifieker, betrouwbaarder en natuurlijker te maken. Het doel is niet om teksten alleen "minder AI" te laten klinken.

## Taal en markt

- Schrijf uitsluitend in natuurlijk Nederlands voor Nederland.
- Gebruik Nederlandse zoekterminologie zoals gebruikers die werkelijk gebruiken.
- Behoud relevante termen zoals percolator, mokapot, moka pot, Italiaanse koffie, inductie, aluminium, RVS en elektrische percolator wanneer ze inhoudelijk passen.
- Vermijd onnatuurlijke vertalingen uit het Engels of Frans.

## Sitecontext

Italiaanse-percolator.nl is een affiliatewebsite over Italiaanse percolators, mokapots, koffiezetten, merken, accessoires en productvergelijkingen.

Affiliate monetisatie mag nooit de redactionele conclusie bepalen. Een pagina moet ook nuttig zijn als alle affiliate links worden verwijderd.

## Verplichte workflow voor bestaande pagina's

1. Gebruik `content-audit` om te beslissen: KEEP / UPDATE / MERGE / REDIRECT / REMOVE.
2. Alleen bij UPDATE: gebruik `content-refresh` om te bepalen wat werkelijk moet veranderen.
3. Voor product-, review- en vergelijkingspagina's: gebruik `affiliate-value`.
4. Gebruik `search-intent` om de zoekintentie en paginafunctie te bewaken.
5. Na inhoudelijke wijzigingen: gebruik `fact-check` als aparte verificatiepass.
6. Gebruik daarna `natural-writing` voor een gerichte stilistische revisie.
7. Sluit af met `editorial-qa`. Publiceer of merge pas bij PASS.

## Belangrijkste regels

- Parafraseer geen fabrikant- of winkeltekst enkel om "unieke content" te creëren.
- Verzin nooit een persoonlijke test, ervaring, meting of aankoop.
- Schrijf niet dat "wij getest hebben" tenzij er aantoonbare first-hand testdata in de repo of door de gebruiker aangeleverd is.
- Maak productclaims alleen als ze verifieerbaar zijn.
- Geef bij aanbevelingen ook beperkingen, nadelen en voor wie het product minder geschikt is.
- Voeg geen woorden toe puur voor lengte.
- Behoud historische SEO-waarde: verander URL, hoofdonderwerp of zoekintentie niet zonder expliciete reden.
- Verwijder een pagina niet uitsluitend omdat het verkeer laag is; controleer historische prestaties, overlap en eventuele links.
- Geen automatische keyword-density doelen.
- Geen generieke conclusies of intro's die alleen de titel herhalen.

## Werkwijze

Bij twijfel eerst een auditrapport geven en niet meteen herschrijven. Maak bij een rewrite zo weinig mogelijk wijzigingen aan passages die al goed, specifiek en natuurlijk zijn.


## Preservation contract

This constraint overrides every content/SEO skill.

Before editing an existing page, capture the BEFORE state of:
- visible product prices and old-price/discount values;
- affiliate CTA labels and affiliate destination URLs;
- product images and meaningful content images;
- product specifications, EAN/model/capacity/material fields;
- canonical URL, robots directives and hreflang;
- JSON-LD blocks and schema types;
- H1 and primary page intent;
- contextual internal links and breadcrumbs;
- external review counts/ratings when they are explicitly sourced to a third-party platform;
- availability/shipping information already displayed.

A review is permission to improve editorial content, not permission to remove functional or commercial information.

Rules:
1. Preserve every field above by default.
2. If fact-checking shows a field is wrong, contradictory or unverifiable, FLAG it first. Do not silently delete it.
3. Removing or changing any preserved field requires an explicit reason in the page review log.
4. Prices may be retained even if dynamic. If freshness is uncertain, qualify them as indicative/current-at-check rather than deleting them.
5. Affiliate URLs and CTAs must not be replaced by placeholders such as "#" during editorial review.
6. After editing, compare BEFORE vs AFTER. Any unexplained removal is an automatic editorial-qa FAIL.
7. Validate JSON-LD after every mutation. A page with newly invalid schema is an automatic FAIL.
8. Do not commit a page whose HTML was unexpectedly shortened or whose major sections disappeared.

## Recovery workflow for the ranking-loss cohort

For the 15 pages listed in SEO-RECOVERY-REVIEW.md, run:
1. seo-page / content-audit diagnosis using supplied GSC evidence where available;
2. content-refresh;
3. search-intent;
4. affiliate-value when relevant;
5. fact-check;
6. natural-writing;
7. internal-linking-audit;
8. seo-technical;
9. seo-best-practices;
10. seo-drift-style BEFORE/AFTER comparison;
11. editorial-qa.

The final commit is allowed only after the preservation contract passes.


## Blog editorial finishing pipeline

For every /koopgids/ page that is edited, run this editorial finishing sequence after factual/content changes and before technical QA:

1. humanizer — broad whole-artifact pass; preserve all facts, data, links, tables, headings, prices and technical distinctions.
2. general-writing — final house-style pass using minimum effective edit; review headings, callouts, labels, transitions and whole-page coherence, not only body paragraphs.
3. anti-ai-slop — evidence-based final credibility/specificity review for generic, template-like or AI-smell patterns. Every finding must point to a concrete passage and include a fix.
4. preservation / seo-drift check.
5. seo-technical + seo-best-practices.
6. editorial-qa final status.

For /koopgids/ work, the editorial pass must explicitly detect:
- apparent contradictions between neighboring sentences;
- disclaimers that undermine or repeat the preceding claim;
- stitched-together tone caused by multiple agent edits;
- synthetic authors, invented reader stories, unsupported experience or testing;
- arbitrary ratings, statistics or pseudo-precision;
- repeated template structures and symmetrical section patterns;
- promotional language that is not needed for the reader's task;
- generic recaps and filler transitions;
- claims that are technically true but pragmatically strange or defensive.

A page cannot receive PASS until it has been read from top to bottom in rendered reading order after the final edit.
