from pathlib import Path
PROTECTED = [
  "producten/bialetti-inductieplaatje-voor-inductiekooplaat-o13cm.html",
  "producten/g-a-t-italia-filterplaatje-siliconringen-1-en-2-kops.html",
  "producten/bialetti-moka-express-percolator-6-kops-aluminium.html",
  "producten/bialetti-moka-express-filterplaatje-en-drie-rubber-ringen-3-4-kops.html",
  "producten/bialetti-moka-induction-percolator-rood-6-kops.html",
  "producten/bialetti-moka-induction-percolator-zwart-6-kops.html",
  "producten/italiaans-koffiezetapparaat-pezzetti-italexpress-aluminium-3-kopjes-blauw.html",
  "producten/cafetiere-glas-350-ml-french-press-koffiezetapparaat-koffiemaker-koffie-koffiepo.html",
  "producten/bialetti-percolator-venus-10-kops-roestvrijstaal-inductiegeschikt.html",
  "producten/bialetti-moka-express-percolator-4-kops-aluminium.html",
  "producten/klausberg-kb-serie-espressomaker-600ml-aluminium-12-kopjes.html",
  "producten/ibili-express-inox-moka-koffiezetapparaat-italiaans-4-bekers-zilver.html",
  "producten/bialetti-venus-copper-percolator-4-kops-roestvrijstaal-inductiegeschikt.html",
  "producten/bialetti-moka-alpina-limited-editions-3-kops-120ml.html",
  "producten/3x-dparts-rubberen-ringen-en-1-filterplaatje-geschikt-voor-6-kops-bialetti-percolator-series-moka-express-dama-break-moka-timer-rainbow.html",
  "producten/bialetti-moka-express-italia-percolator-3-kops-aluminium.html",
  "producten/bialetti-rainbow-rood-percolator-200ml-3-kops.html",
  "producten/bialetti-moka-express-6-kops-nutcracker.html",
  "producten/espresso-maker-voor-6-kopjes-10oz-handmatige-moka-pot-voor-italiaanse-koffie-alu.html",
  "producten/perculator-300ml-percolator-percolator-koffiepercolator-keukenpercolator-percola.html",
  "producten/alessi-aldo-cafetiere-3-kops.html",
  "producten/koffie-en-theepers-0-60l-transparant.html",
  "producten/adore-maison-barista-koffie-verdeler-donkerbruin-espresso-distributeur-espresso-.html",
  "producten/bialetti-moka-express-percolator-2-kops-aluminium.html",
  "producten/bialetti-rainbow-groen-percolator-200ml-3-kops.html",
  "producten/bialetti-brikka-evolution-percolator-2-kops-zwart-aluminium.html",
  "producten/koffie-percolator-6-kopjes-300ml.html",
  "producten/bialetti-moka-express-6-kops-carosello-espresso-kop-en-schotel-4-stuks.html",
  "producten/leopold-vienna-percolator-tivoli-6-kops-aluminium.html",
  "producten/bialetti-brikka-espressopot-aluminium-4-kops-zilver.html",
  "producten/bialetti-mini-express-zwart-2-kops.html",
  "producten/bialetti-moka-express-i-love-coffee-percolator-rood-3-kops-130ml.html",
  "producten/bialetti-moka-aluminium-filterplaatje-3-rubber-ringen-1-kops.html",
  "producten/bialetti-moka-express-percolator-6-kops-aluminium-zwart.html",
  "producten/bialetti-moka-inductie-rood-4-kops-150ml-bialetti-koffie-proefpakket-3-x-250gr.html",
  "producten/bialetti-moka-induction-percolator-zwart-4-kops.html",
  "producten/imperial-kitchen-cafetiere-6-kops-aluminium.html",
  "producten/bialetti-brikka-induction-percolator-4-kops-inductiegeschikt.html",
  "producten/bialetti-venus-copper-percolator-2-kops-roestvrijstaal.html",
  "producten/thomas-sunny-day-geel-koffiekan-met-deksel-6-personen.html",
  "producten/bialetti-mini-express-percolator-2-kops-inductiegeschikt-met-2-kopjes.html",
  "producten/bialetti-moka-exclusive-moka-express-creme.html",
  "producten/alessandro-percolator-italiaans-koffiezetapparaat-1-kopje-aluminium-zilver-60-ml.html",
  "producten/alessi-aldo-cafetiere-8-kops.html",
  "producten/bialetti-moka-exclusive-moka-express-groen.html",
  "producten/bialetti-moka-express-4-kops-carosello-espresso-kop-en-schotel-4-stuks.html",
  "producten/bialetti-mini-express-kandinsky-bialetti-koffiepakket-3-x-250gr.html",
  "producten/bialetti-moka-express-percolator-3-kops-aluminium-rood.html",
  "producten/alessi-sapper-espresso-koffiezetter-9090-m-10-kops.html",
  "producten/thermoskan-1-l-roestvrij-staal-304-theepot-thermoskan-koffiekan-dubbelwandige-th.html"
]
protected = set(PROTECTED)
files = sorted(Path("producten").glob("*.html"))
changed = 0
already = 0
for p in files:
    rel = p.as_posix()
    if rel in protected:
        continue
    s = p.read_text(encoding="utf-8")
    if 'name="robots"' in s.lower() or "name='robots'" in s.lower():
        if "noindex" in s.lower():
            already += 1
            continue
        raise SystemExit(f"Existing robots directive needs manual review: {rel}")
    marker = "<head>"
    if marker not in s:
        raise SystemExit(f"No <head> found: {rel}")
    s = s.replace(marker, marker + '\n<meta name="robots" content="noindex,follow">', 1)
    p.write_text(s, encoding="utf-8")
    changed += 1
print(f"Product HTML files: {len(files)}; protected: {len(protected)}; changed: {changed}; already noindex: {already}")
if changed + already != 790:
    raise SystemExit(f"Safety check failed: expected 790 noindex candidates, got {changed + already}")
