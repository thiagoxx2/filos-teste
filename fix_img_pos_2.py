import re
import os

path = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/css/pages.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace translate(-50px, 50px) with translate(-50px, -10px)
css = re.sub(r'transform:\s*translate\(-50px,\s*50px\);', 'transform: translate(-50px, -10px);', css)
# Replace margin-bottom: -50px; with margin-bottom: 10px; 
css = re.sub(r'margin-bottom:\s*-50px;', 'margin-bottom: 10px;', css)

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed image positioning in pages.css")
