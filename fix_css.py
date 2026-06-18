import re
import os

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE"

# 1. Extract CSS from administracao.html
with open(os.path.join(repo_dir, "cursos/administracao.html"), "r", encoding="utf-8") as f:
    admin_html = f.read()

# Find the CSS block
css_match = re.search(r'(/\* --- ESTILOS SEÇÃO MATRIZ CURRICULAR --- \*/.*?</style>)', admin_html, re.DOTALL)
if css_match:
    matriz_css_block = css_match.group(1).replace("</style>", "").strip()
else:
    print("Could not find CSS block in administracao.html")
    matriz_css_block = ""

# 2. Inject CSS into radiologia.html
rad_path = os.path.join(repo_dir, "cursos/radiologia.html")
with open(rad_path, "r", encoding="utf-8") as f:
    rad_html = f.read()

if "section-matriz-admin" not in rad_html[:rad_html.find("</head>")]:
    style_tag = f"\n<style>\n{matriz_css_block}\n</style>\n</head>"
    rad_html = rad_html.replace("</head>", style_tag)

with open(rad_path, "w", encoding="utf-8") as f:
    f.write(rad_html)

print("Injected CSS into radiologia.html successfully.")
