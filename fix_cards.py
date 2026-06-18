import re
import os

files_to_update = [
    "anatomia-seccional.html",
    "biosseguranca-ressonancia.html",
    "ferramentas-digitais.html",
    "introducao-regularizacao-imoveis.html",
    "neuropsicopedagogia.html",
    "oratoria-comunicacao.html",
    "praticas-inclusao.html",
    "reurb-na-pratica.html"
]

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/cursos"

pattern = re.compile(
    r'<div class="diferencial-card-content">\s*'
    r'<h3 class="diferencial-card-title">(.*?)</h3>\s*'
    r'<p class="diferencial-card-desc">(.*?)</p>\s*'
    r'</div>',
    re.DOTALL
)

for filename in files_to_update:
    filepath = os.path.join(repo_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replacer(match):
        title = match.group(1).strip()
        desc = match.group(2).strip()
        
        if desc and desc[0].isupper():
            desc = desc[0].lower() + desc[1:]
            
        return (
            '<div class="diferencial-card-content diferencial-card-content--centered">\n'
            f'<p class="diferencial-card-desc" style="margin-top: 0;"><strong>{title}</strong> {desc}</p>\n'
            '</div>'
        )
    
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No match found in {filename}")
