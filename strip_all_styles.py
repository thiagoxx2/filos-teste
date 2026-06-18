import re
import glob
import os

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/cursos"
files = glob.glob(os.path.join(repo_dir, "*.html"))

for path in files:
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    match = re.search(r'<style>.*?</style>', content, re.DOTALL)
    if match:
        print(f"Removing inline style from {os.path.basename(path)}")
        content = content.replace(match.group(0), "")
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

