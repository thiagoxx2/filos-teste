import re
import os

path = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/css/pages.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

# Change min-height: 63px to min-height: 48px
css = re.sub(r'min-height:\s*63px;', 'min-height: 48px;', css)
# Change width: min(330px, calc(100vw - 4rem)); to width: max-content; padding: 0 2rem; min-width: 350px;
css = re.sub(r'width:\s*min\(330px,\s*calc\(100vw\s*-\s*4rem\)\);', 'width: max-content;\n  min-width: 350px;\n  white-space: nowrap;', css)

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed button CSS")
