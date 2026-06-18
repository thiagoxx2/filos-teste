import re
import os

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE"
files = ["cursos/administracao.html", "cursos/direito.html", "cursos/pedagogia.html", "cursos/radiologia.html"]

for f in files:
    path = os.path.join(repo_dir, f)
    if not os.path.exists(path): continue
    
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Check if there is an inline style tag before the body tag
    match = re.search(r'<style>.*?</style>', content, re.DOTALL)
    if match:
        print(f"Removing inline style from {f}")
        content = content.replace(match.group(0), "")
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

