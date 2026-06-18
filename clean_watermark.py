import re

css_file = "css/pages.css"
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# Pattern to match .matriz-watermark { ... } and .matriz-watermark::before { ... }
# Handling nested braces for media queries is complex with simple regex, but the first two are not in media queries.
# Let's remove them directly via regex
css = re.sub(r'\.matriz-watermark\s*\{[^}]*\}', '', css)
css = re.sub(r'\.matriz-watermark::before\s*\{[^}]*\}', '', css)

# The one inside the media query might be empty or have display:none
css = re.sub(r'\s*\.matriz-watermark\s*\{\s*display:\s*none;\s*\}', '', css)

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS watermark rules removed.")
