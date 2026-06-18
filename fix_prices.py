import re
import os

prices = {
    "direito.html": ("2.184,25", "698,96"),
    "pedagogia.html": ("951,11", "475,55"),
    "administracao.html": ("1.188,89", "535,00"),
    "radiologia.html": ("1.354,78", "609,65")
}

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/cursos"

# We want to match:
# <div class="inscription-card-price" data-price-output="">
#    698,96
# </div>

pattern = re.compile(
    r'<div class="inscription-card-price" data-price-output="">\s*(.*?)\s*</div>',
    re.DOTALL
)

for filename, (old_val, new_val) in prices.items():
    filepath = os.path.join(repo_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    replacement = (
        '<div class="course-price-display">\n'
        '  <p class="course-price-from">\n'
        f'    De <span class="course-price-old">R$ {old_val}</span>\n'
        '  </p>\n'
        '  <p class="course-price-current">\n'
        '    por mensalidades a partir de\n'
        f'    <strong>R$ {new_val}*</strong>\n'
        '  </p>\n'
        '  <p class="course-price-note">\n'
        '    *Valor final mediante descontos aplicáveis.\n'
        '  </p>\n'
        '</div>'
    )
    
    new_content, count = pattern.subn(replacement, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No match found in {filename}")

