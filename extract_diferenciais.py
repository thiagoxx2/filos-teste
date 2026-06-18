import re
import os

path = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/cursos/administracao.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Try to extract the inline style block for Diferenciais
match = re.search(r'/\*\s*Seção Diferenciais Acadêmicos\s*\*/.*?(?=</style>)', html, re.DOTALL)
if match:
    css_content = match.group(0)
    print("Found CSS. Lines:", len(css_content.split('\n')))
    
    # Save it to a temporary file to inspect
    with open("temp_diferenciais.css", "w", encoding="utf-8") as out:
        out.write(css_content)
else:
    print("CSS block not found.")
