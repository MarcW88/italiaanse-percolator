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


## Review Recovery Workflow

Use this workflow for individual product review pages (for example `*-review.html`). It extends the existing recovery stack; it does not replace the existing skills.

### Pre-edit diagnosis

1. **Performance / recovery diagnostic** — use supplied GSC evidence where available; distinguish loss of clicks, impressions and average position.
2. **content-audit + spam-risk** — decide KEEP / LIGHT REFRESH / MEDIUM REFRESH / DEEP REFRESH before editing.
3. **search-intent** — preserve the individual-review intent and avoid turning the page into a generic buying guide.
4. **affiliate-value** — the page must remain useful if affiliate links are removed.
5. **evidence-based-reviews** — mandatory core review gate. Classify the evidence behind material claims and never imply hands-on testing without documented first-hand evidence.
6. **Product facts / source verification** — verify important specifications against the exact model/variant where possible. Flag uncertain facts rather than silently deleting them.
7. **Review methodology / evidence tier** — make the factual basis of the review transparent. Do not create arbitrary numeric ratings.
8. **Strengths / drawbacks / use-case fit** — explain who the product suits, who it does not suit, and meaningful trade-offs.
9. **comparison-tool-design** — use when the review compares the reviewed product with alternatives or makes relative/best-choice claims.
10. **fact-check** — separate verification pass after substantive edits.
11. **internal-linking-audit** — link naturally to relevant comparison, koopgids, maintenance/use guides and genuine alternatives without creating a templated link block.
12. **Schema judgment** — use Review/rating markup only when the page has a defensible documented review/rating basis. Otherwise prefer honest Article/Product markup appropriate to the visible content.

### Editorial finishing sequence

After factual/content changes and before technical QA, run the same finishing stack already used for /koopgids/:

1. **humanizer**
2. **general-writing**
3. **anti-ai-slop**
4. **preservation / seo-drift BEFORE vs AFTER**
5. **seo-technical + seo-best-practices**
6. **editorial-qa**
7. **whole-page final read in rendered reading order**

### Review-specific preservation gate

In addition to the global Preservation contract, preserve by default:
- exact product/model name and variant;
- visible price, old price and discount values;
- affiliate CTA labels and destination URLs;
- product images;
- material, capacity/ml, cup count, dimensions, weight, compatibility and other technical specifications;
- pros/cons that remain factually supported;
- contextual links to the product's comparison and relevant guides;
- availability/shipping information;
- existing Product/Offer fields that remain accurate.

Do not silently remove a preserved commercial or technical field. If it is wrong, contradictory or unverifiable, flag it in the review log and change it only with an explicit reason.

### Automatic FAIL conditions

A review cannot receive PASS when:
- it claims or implies first-hand testing without documented evidence;
- it retains an unexplained numeric score or rating presented as objective;
- a recommendation is stronger than its evidence;
- material product facts disappeared during rewriting;
- affiliate URLs or prices were unintentionally removed;
- schema claims a Review/rating that the visible methodology cannot support;
- the final page contains stitched-agent contradictions, synthetic expertise, unsupported performance claims or generic AI-style filler.


## Product Page Recovery Workflow

Use this workflow for individual affiliate/e-commerce product pages under `/producten/`. It extends the existing recovery stack and reuses installed skills.

### Pre-edit diagnosis
1. Performance / recovery diagnostic from supplied GSC evidence.
2. content-audit + spam-risk: KEEP / LIGHT / MEDIUM / DEEP REFRESH.
3. search-intent: preserve exact product/model intent.
4. Thin-affiliate / merchant-copy audit: identify copied manufacturer/merchant language and require useful original decision support.
5. seo-ecommerce: mandatory product-data and e-commerce SEO gate. Audit visible product facts, Product/Offer markup, price, currency, availability, brand, SKU/GTIN/MPN where present, images, metadata and HTML ↔ structured-data consistency.
6. evidence-based-reviews: apply to performance, quality, durability, recommendation, comparison or experience claims. Never imply hands-on testing without documented evidence.
7. fact-check: verify material claims and exact variant/model facts; flag uncertainty instead of inventing or silently deleting.
8. internal-linking-audit: connect naturally to parent category, relevant koopgids, comparison/review and genuine alternatives.
9. Schema judgment: Product/Offer data must reflect visible, supportable information. Do not fabricate ratings/reviews.

### Editorial finishing sequence
1. humanizer
2. general-writing
3. anti-ai-slop
4. preservation / seo-drift BEFORE vs AFTER
5. seo-technical + seo-best-practices
6. editorial-qa
7. whole-page final read in rendered reading order

### Product preservation contract
Preserve by default:
- exact product/model/variant name;
- current price, old price, discount and currency;
- affiliate CTA text and destination URL;
- availability/shipping information;
- images and image destinations;
- brand, material, capacity/ml, cup count, dimensions, weight, color and compatibility;
- SKU, GTIN, MPN or other identifiers when present;
- Product/Offer structured-data fields that remain accurate;
- factual pros/cons;
- category, guide, comparison and review links.

The seo-ecommerce skill is an audit/optimization gate, not permission to delete or invent product data. Any contradiction or unverifiable preserved field must be flagged and changed only for an explicit documented reason.

### Product editorial language guard

During the whole-page final read, flag and rewrite defensive/internal-process language that exposes editorial mechanics instead of helping the reader. Examples include:
- explaining what "this page is intended to do";
- telling readers that the page "is not responsible for" current commercial information;
- disclaimers that repeat obvious uncertainty about price/availability in bureaucratic language;
- phrases such as "we do not claim...", "this page is meant to...", "use the seller for commercial information" when a simpler reader-facing sentence would do.

Prefer direct reader language, e.g. "Prijs en beschikbaarheid kunnen veranderen. Bekijk de actuele informatie bij de verkooppartner."

### Automatic FAIL conditions
A product page cannot PASS when:
- a preserved price, affiliate URL, image, specification or identifier disappeared unintentionally;
- visible price/currency/availability conflicts with Product/Offer markup;
- merchant/manufacturer copy remains substantially duplicated without meaningful added value;
- unsupported testing, performance, durability, taste or quality claims remain;
- a rating/review is fabricated or unsupported;
- the page is mostly generic template text that could apply unchanged to another model;
- schema contains unsupported commercial data;
- final rendered reading order contains contradictions, stitched-agent artifacts or AI-style filler;
- defensive or meta-editorial wording remains where a simpler reader-facing formulation is possible.
