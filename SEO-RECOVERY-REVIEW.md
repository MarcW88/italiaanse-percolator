# SEO Recovery Review — ranking-loss cohort

Scope frozen on 2026-09-06: only the 15 URLs selected from the Search Console ranking-loss analysis.

## Mandatory workflow

The project now uses these layers:

1. `seo-page` / `content-audit` — URL-level decision using available ranking/GSC evidence.
2. `content-refresh` — only when UPDATE is justified.
3. `search-intent`.
4. `affiliate-value` for product/commercial/review pages.
5. `fact-check`.
6. `natural-writing`.
7. `internal-linking-audit`.
8. `seo-technical`.
9. `seo-best-practices`.
10. `seo-drift`-style BEFORE/AFTER regression check.
11. `editorial-qa`.

External skills are stored under `.agents/skills/`. Some upstream skills expect external services (SE Ranking, Firecrawl, Google APIs). Where those services were unavailable in this run, the supplied GSC evidence and repository HTML were used instead; missing API data was not fabricated.

## Preservation gate

For every page in this cohort, the pre-recovery version at commit `8e5056e7f64511907b4d0e1cf2221bc0925df48f` was compared with current `main`.

The following are protected unless an explicit reason is documented:
- visible prices and price ranges;
- affiliate destinations and CTAs;
- images;
- product/specification information;
- canonical;
- H1 and primary intent;
- JSON-LD;
- internal links/breadcrumbs.

Final QA confirmed:
- no unexplained price removal remains;
- no affiliate destination present in the baseline was removed;
- no baseline image was removed by the review;
- all reviewed pages have one H1;
- all reviewed pages have a canonical;
- JSON-LD parses as valid JSON where present;
- no page was unexpectedly truncated.

## Reviewed URLs

| Page | Decision | Content / AI review | Affiliate review | Internal links | Technical / diff QA | Status |
|---|---|---|---|---|---|---|
| `/koopgids/hoe-kies-je-de-juiste-percolator.html` | UPDATE | Fake author/test claims removed; full original useful structure restored | N/A | Reviewed; existing contextual links retained | Prices, image, 2 schema blocks restored/preserved | PASS |
| `/marques/bialetti/` | UPDATE | Brand copy de-hyped; unsupported longevity claims removed | Applied | Existing model/guide links retained | Prices, affiliate links, images, schema preserved | PASS |
| `/beste-italiaanse-percolators.html` | UPDATE | Fake test methodology and unsupported scores removed/neutralised | Applied | Existing review/guide links retained | Full page restored after regression; prices, affiliate links, images, valid schema preserved | PASS |
| `/shop.html` | UPDATE | Rebuilt from empty file as comparison hub | Applied | Links to categories, Bialetti and choice guide | Canonical/H1/meta added; no baseline data existed to lose | PASS |
| `/producten/bialetti-moka-express-percolator-6-kops-aluminium.html` | UPDATE | Merchant-like copy replaced with decision-focused copy | Applied | Product/guide/brand links retained | €28,99 restored; image/schema/canonical retained | PASS |
| `/categories/elektrische-percolators.html` | UPDATE | Salesy intro reduced | Applied | Category links retained | Incorrect page-11 canonical corrected; no protected data lost | PASS |
| `/marques/` | UPDATE | Brand claims made more factual | N/A | Dense brand + guide linking retained | Indicative €15 / €3 context restored; schema/canonical preserved | PASS |
| `/vergelijking/bialetti-vs-alessi.html` | UPDATE | Fake scores/test posture removed; claims made model-dependent | Applied | Brand/review/guide links retained | Price ranges restored/qualified; images/canonical preserved | PASS |
| `/` | UPDATE | Unsupported testing claims removed; selection language made transparent | Applied | Strong hub linking retained | Price guidance and 3 comparison prices preserved; schema valid | PASS |
| `/producten/cafetiere-glas-350-ml-french-press-...html` | KEEP / non-core | Merchant copy replaced; clearly identified as French press, not moka | Applied | Links users back to moka category/guide | Price, affiliate URL, images, schema preserved | PASS |
| `/koopgids/` | UPDATE | Generic AI/promotional phrases reduced; unsupported maintenance absolutes corrected | N/A | Strong guide/hub linking retained | Image/canonical/H1 preserved | PASS |
| `/categories/percolators-aluminium.html` | UPDATE | Material claims nuanced; model-dependent cleaning/induction rules | Applied | Category/guide/brand links retained | Price range/canonical preserved | PASS |
| `/producten/bialetti-moka-inductie-rood-4-kops-150ml-...html` | UPDATE | Escaped merchant copy removed; bundle description clarified | Applied | Product/review links retained | €74,75, affiliate URL, images, schema preserved | PASS |
| `/bialetti-venus-review.html` | UPDATE | Converted to transparent desk review; unsupported taste/superlative claims removed | Applied | Existing guide/brand links retained | Affiliate URL/image/canonical preserved | PASS |
| `/producten/bialetti-rainbow-rood-percolator-200ml-3-kops.html` | UPDATE | Merchant prose replaced by audience/limitation guidance | Applied | Related product links retained | €22,19 and other prices, affiliate URL, images, schema preserved | PASS |

## Internal-linking note

The scoped pages already contain substantial internal linking to relevant guides, brands, categories and reviews. The rule from `internal-linking-audit` was followed: no link was added merely to increase link count, and existing contextual links were preserved. A site-wide orphan analysis is outside this 15-URL scope.

## Natural-writing standard

The review does not classify text as AI-generated. It removes patterns that reduce editorial quality:
- fabricated first-hand experience;
- invented experts/authors or unsupported testing;
- arbitrary numerical ratings;
- generic superlatives;
- repetitive sales language;
- universal claims where instructions are model-dependent;
- overly symmetrical/template prose.

Concrete facts, useful tables, prices, product data and genuine decision information are preserved even when the surrounding prose is rewritten.
