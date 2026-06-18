import os
import re

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE"
files = ["direito.html", "administracao.html", "pedagogia.html"]

for filename in files:
    path = os.path.join(repo_dir, "cursos", filename)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove inline style
    html = re.sub(r'/\* --- ESTILOS SEÇÃO MATRIZ CURRICULAR --- \*/.*?</style>', '</style>', html, flags=re.DOTALL)
    # Remove inline script for accordion
    html = re.sub(r'const headers = document\.querySelectorAll\("\.matriz-accordion-header"\);.*?(?=\s*}\);\s*}\);\s*</script>)', '', html, flags=re.DOTALL)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print("Cleaned inline blocks.")
