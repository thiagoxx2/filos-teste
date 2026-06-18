import re
import os

path = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/css/pages.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace min-width: 350px; with padding: 0 4rem; max-width: 100%;
css = re.sub(r'min-width:\s*350px;', 'padding: 0 3.5rem;\n  max-width: 100%;', css)

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed button width")
