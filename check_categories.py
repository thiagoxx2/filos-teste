import re
import os

html_files = [f for f in os.listdir("cursos") if f.endswith(".html")]
categories = {}

for file in html_files:
    with open(os.path.join("cursos", file), "r", encoding="utf-8") as f:
        content = f.read()
        
        # Try to find something like <span class="hero-badge">Curso de Extensão</span>
        # or <p class="course-subtitle">... Pós-Graduação ...</p>
        
        # Let's search for "Extensão" or "Extensionista"
        if re.search(r'>\s*Curso de Extensão\s*<', content, re.IGNORECASE) or \
           re.search(r'badge.*?>\s*Extensão\s*<', content, re.IGNORECASE):
            categories[file] = "Extensão"
        elif re.search(r'>\s*Pós-Graduação\s*<', content, re.IGNORECASE) or \
             re.search(r'badge.*?>\s*Pós-Graduação\s*<', content, re.IGNORECASE):
            categories[file] = "Pós-Graduação"
        elif "Bacharelado" in content:
             categories[file] = "Bacharelado"
        elif "Licenciatura" in content:
             categories[file] = "Licenciatura"
        elif "Tecnólogo" in content:
             categories[file] = "Tecnólogo"
        else:
             categories[file] = "Desconhecido"

import json
print(json.dumps(categories, indent=2))
