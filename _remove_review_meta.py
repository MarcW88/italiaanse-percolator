#!/usr/bin/env python3
import re

with open('alle-reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all <div class="review-meta">...</div> tags
content = re.sub(r'<div class="review-meta">.*?</div>', '', content, flags=re.DOTALL)

with open('alle-reviews.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Removed all review-meta divs.")
