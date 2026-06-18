import re
import os

path = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/css/pages.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace translate(-50px, 90px) with translate(-50px, 50px)
css = re.sub(r'transform:\s*translate\(-50px,\s*90px\);', 'transform: translate(-50px, 50px);', css)
# Replace margin-bottom: -90px; with margin-bottom: -50px; 
css = re.sub(r'margin-bottom:\s*-90px;', 'margin-bottom: -50px;', css)

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed image positioning in pages.css")
