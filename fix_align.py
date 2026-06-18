import re
import os

path = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/css/pages.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

# Change .matriz-container align-items from center to stretch
css = re.sub(r'(\.matriz-container\s*{[^}]*?align-items:\s*)center(;)', r'\1stretch\2', css)

# Change .matriz-right align-items from center to flex-end
css = re.sub(r'(\.matriz-right\s*{[^}]*?align-items:\s*)center(;)', r'\1flex-end\2', css)

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed alignment in pages.css")
