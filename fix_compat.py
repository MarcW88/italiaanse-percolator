from pathlib import Path

f = Path('koopgids/hoe-kies-je-de-juiste-percolator.html')
html = f.read_text(encoding='utf-8')

# Find the exact block to replace
start_marker = '<p><strong>Veelgemaakte fout:</strong>'
end_marker = '<div class="blog-callout blog-callout-neutral">\n<p><strong>Heb je inductie?</strong>'

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

assert idx_start != -1, 'start not found'
assert idx_end != -1, 'end not found'

# Go back to find the opening <div class="blog-callout"> before the start
open_div = html.rfind('<div class="blog-callout">', 0, idx_start)
assert open_div != -1, 'opening div not found'

old_block = html[open_div:idx_end]
print('OLD block (last 80 chars):', repr(old_block[-80:]))
print('Length:', len(old_block))

new_block = (
    '<div class="blog-callout">\n'
    '<p><strong>Veelgemaakte fout:</strong> \u201eIk kocht een mooie aluminium percolator, maar hij werkt niet op mijn inductiekookplaat!\u201d \u2014 veelgehoorde klacht in onze inbox.</p>\n'
    '</div>\n'
    '<table class="compat-table">\n'
    '<thead>\n'
    '<tr><th>Kookplaat</th><th>Aluminium</th><th>RVS</th><th>Opmerking</th></tr>\n'
    '</thead>\n'
    '<tbody>\n'
    '<tr><td>Gas</td><td class="compat-ok">Ja</td><td class="compat-ok">Ja</td><td>Alle percolators werken. Aluminium warmt sneller op.</td></tr>\n'
    '<tr><td>Elektrisch</td><td class="compat-ok">Ja</td><td class="compat-ok">Ja</td><td>Let op vlakke bodem voor goed contact.</td></tr>\n'
    '<tr><td>Keramisch</td><td class="compat-ok">Ja</td><td class="compat-ok">Ja</td><td>Zorg voor schone bodem om krassen te vermijden.</td></tr>\n'
    '<tr><td>Inductie</td><td class="compat-no">Nee</td><td class="compat-ok">Ja</td><td>Alleen RVS met magnetische bodem. Test met magneet.</td></tr>\n'
    '</tbody>\n'
    '</table>\n'
    '<p style="font-size:.82rem;color:var(--text-dim);">Snelle test: houd een magneet tegen de bodem. Plakt hij? Dan werkt het op inductie.</p>\n'
)

html = html[:open_div] + new_block + html[idx_end:]
f.write_text(html, encoding='utf-8')
print('OK: compat section replaced')
