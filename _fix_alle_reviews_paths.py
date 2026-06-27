#!/usr/bin/env python3
import re

with open('alle-reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix image paths that don't have Images/ prefix
# Match img src with just filename (no path) and add ../Images/ prefix
content = re.sub(r'src="([^/]+\.jpg)"', r'src="../Images/\1"', content)
content = re.sub(r'src="([^/]+\.png)"', r'src="../Images/\1"', content)
content = re.sub(r'src="([^/]+\.webp)"', r'src="../Images/\1"', content)

# Also fix paths that have Images/ but not ../Images/
content = re.sub(r'src="Images/', r'src="../Images/', content)

with open('alle-reviews.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Fixed image paths in alle-reviews.html")
