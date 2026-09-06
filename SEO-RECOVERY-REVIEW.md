# SEO Recovery Review — pages with ranking loss

Scope frozen on 2026-09-06: only the 15 URLs previously selected from Search Console ranking-loss data.

## Review protocol

Every URL below was reviewed against:
1. content-audit
2. content-refresh (when UPDATE was appropriate)
3. search-intent
4. affiliate-value (for commercial/product/review pages)
5. fact-check
6. natural-writing
7. editorial-qa

A skill marked N/A was not relevant to that page type. Final HTML was re-read on `main` after commit. JSON-LD was parsed when present.

| URL/path | Audit decision | Affiliate-value | Final status | Main action |
|---|---|---:|---|---|
| /koopgids/hoe-kies-je-de-juiste-percolator.html | UPDATE | N/A | PASS | Major rewrite around kookplaat, materiaal, maat en onderhoud |
| /marques/bialetti/ | UPDATE | Applied | PASS | Brand page de-hyped; model intent and verifiable claims |
| /beste-italiaanse-percolators.html | UPDATE | Applied | PASS | Fake test methodology/scores removed; selection methodology made transparent |
| /shop.html | UPDATE | Applied | PASS | Empty page rebuilt as comparison hub |
| /producten/bialetti-moka-express-percolator-6-kops-aluminium.html | UPDATE | Applied | PASS | Merchant copy replaced with decision-oriented product content |
| /categories/elektrische-percolators.html?page=11 | UPDATE | Applied | PASS | Canonical fixed to category; salesy copy reduced |
| /marques/ | UPDATE | N/A | PASS | Brand hub claims softened and scope clarified |
| /vergelijking/bialetti-vs-alessi.html | UPDATE | Applied | PASS | Unsupported winners/scores removed; comparison made model-dependent |
| / | UPDATE | Applied | PASS | Unsupported testing/experience claims removed |
| /producten/cafetiere-glas-350-ml-french-press-...html | KEEP / non-core | Applied | PASS | Explicitly identified as French press, not moka; merchant copy removed |
| /koopgids/index.html | UPDATE | N/A | PASS | Generic and unsupported maintenance/selection claims corrected |
| /categories/percolators-aluminium.html | UPDATE | Applied | PASS | Romantic/generalized claims replaced by practical model criteria |
| /producten/bialetti-moka-inductie-rood-4-kops-150ml-...html | UPDATE | Applied | PASS | Escaped merchant copy removed; bundle/capacity inconsistencies clarified |
| /bialetti-venus-review.html | UPDATE | Applied | PASS | Converted to transparent desk review; taste/test claims removed |
| /producten/bialetti-rainbow-rood-percolator-200ml-3-kops.html | UPDATE | Applied | PASS | Merchant copy replaced by audience/limitations/compatibility guidance |

## QA checks

- No remaining known fake-experience markers from the reviewed set (e.g. "50+ modellen getest", "8 jaar ervaring", "onze uitgebreide tests", "we hebben dit model uitgebreid getest").
- JSON-LD currently present on these pages parses as valid JSON after the review.
- Product/review pages do not claim first-hand testing unless evidence exists.
- Existing URLs and primary search intent were preserved unless the page itself was technically broken.
- No additional site pages were included in this pass.
