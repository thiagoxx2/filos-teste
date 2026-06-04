import os
import re

ROOT_DIR = "/Users/shayenefreita/FACULDADE FILOS"

# Regex para casar components.css com qualquer parâmetro de versão (ex: components.css?v=5.16, components.css?v=5.17)
CSS_REGEX = re.compile(r"components\.css\?v=[0-9.]+")
NEW_CSS_STRING = "components.css?v=5.18"

count = 0

for root, dirs, files in os.walk(ROOT_DIR):
    # Ignorar pastas ocultas ou virtuais
    if ".git" in root or ".venv" in root:
        continue
        
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                
            if CSS_REGEX.search(content):
                new_content = CSS_REGEX.sub(NEW_CSS_STRING, content)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Atualizado: {os.path.relpath(file_path, ROOT_DIR)}")
                count += 1

print(f"\nTotal de arquivos HTML atualizados: {count}")
