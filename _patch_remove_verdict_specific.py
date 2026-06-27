import re

review_files = [
    'bialetti-fiammetta-review.html',
    'bialetti-moka-review.html',
    'bialetti-dama-review.html'
]

for filename in review_files:
    try:
        with open(filename, 'r') as f:
            txt = f.read()

        # Remove Verdict section
        txt = re.sub(
            r'<div style="margin-top: 2rem; padding-top: 2rem; border-top: 1px solid var\(--border\); background: #f5f0ea; border-radius: 0\.5rem; padding: 2rem;">\s*<h3 style="font-family: var\(--font-serif\); font-size: 1\.2rem; font-weight: 400; margin-bottom: 1rem;">Verdict</h3>.*?</div>\s*</div>',
            '</div>',
            txt,
            flags=re.DOTALL
        )

        with open(filename, 'w') as f:
            f.write(txt)

        print(f"Updated {filename}")

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error: {filename}: {e}")

print("\nDone.")
