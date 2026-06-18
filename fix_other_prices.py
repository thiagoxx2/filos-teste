import re
import os

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/cursos"
skip_files = ["direito.html", "pedagogia.html", "administracao.html", "radiologia.html"]

pattern = re.compile(
    r'<div class="inscription-card-price" data-price-output="">\s*(.*?)\s*</div>',
    re.DOTALL
)

for root, dirs, files in os.walk(repo_dir):
    for filename in files:
        if filename.endswith(".html") and filename not in skip_files:
            filepath = os.path.join(root, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            def replacer(match):
                old_val = match.group(1).strip()
                # If there's no old value, use a placeholder
                if not old_val:
                    old_val = "0,00"
                    
                return (
                    '<div class="course-price-display" style="display: none;">\n'
                    '  <p class="course-price-from">\n'
                    f'    De <span class="course-price-old">R$ {old_val}</span>\n'
                    '  </p>\n'
                    '  <p class="course-price-current">\n'
                    '    por mensalidades a partir de\n'
                    f'    <strong>R$ {old_val}*</strong>\n'
                    '  </p>\n'
                    '  <p class="course-price-note">\n'
                    '    *Valor final mediante descontos aplicáveis.\n'
                    '  </p>\n'
                    '</div>'
                )
            
            new_content, count = pattern.subn(replacer, content)
            
            if count > 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

print("Done")
