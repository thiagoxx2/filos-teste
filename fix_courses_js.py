import re
import json
import os

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Extract existing array
match = re.search(r'(const courses = \[.*?\];)', js, re.DOTALL)
if not match:
    print("Could not find courses array!")
    exit(1)

courses_array_str = match.group(1).replace('const courses = ', '').rstrip(';')
courses_array_str = re.sub(r',\s*\]', ']', courses_array_str)

try:
    courses = json.loads(courses_array_str)
except Exception as e:
    print("Error parsing JSON:", e)
    exit(1)

# 2. Extract old prices and categorize
for c in courses:
    slug = c["slug"]
    html_path = f"cursos/{slug}.html"
    
    # Defaults
    c["oldPrice"] = None
    
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Old price
            p_match = re.search(r'<span class="course-price-old">R\$\s*([\d\.,]+)</span>', content)
            if p_match:
                c["oldPrice"] = p_match.group(1)
            
            # Category
            if re.search(r'>\s*Curso de Extensão\s*<', content, re.IGNORECASE) or \
               re.search(r'badge.*?>\s*Extensão\s*<', content, re.IGNORECASE) or \
               "Certificação de Extensão" in content:
                c["badge"] = "Extensão"
            elif "Bacharelado" in content:
                c["badge"] = "Bacharelado"
            elif "Licenciatura" in content:
                c["badge"] = "Licenciatura"
            elif "Tecnólogo" in content:
                c["badge"] = "Tecnólogo"
            else:
                c["badge"] = "Pós-Graduação"
    else:
        # For #contato courses
        pass

# Normalization for data-filter
def normalize_filter(badge):
    if badge == "Bacharelado": return "bacharelado"
    if badge == "Licenciatura": return "licenciatura"
    if badge == "Tecnólogo": return "tecnologo"
    if badge == "Pós-Graduação": return "pos-graduacao"
    if badge == "Extensão": return "extensao"
    return "all"

# 3. Format courses array back to JS string
new_courses_js = "const courses = " + json.dumps(courses, indent=4, ensure_ascii=False) + ";"

# 4. Replace createCourseCard template
new_template = r"""    const createCourseCard = (c) => `
      <div class="course-card-item courses-carousel-item" data-filter="${c.badge.toLowerCase() === 'pós-graduação' ? 'pos-graduacao' : c.badge.toLowerCase() === 'tecnólogo' ? 'tecnologo' : c.badge.toLowerCase() === 'extensão' ? 'extensao' : c.badge.toLowerCase()}" data-course="${c.name}">
        <span class="course-card-item-badge">${c.badge}</span>

        <div class="course-card-item-body">
          <h3>${c.name}</h3>

          <div class="course-card-item-meta">
            <div class="meta-row"><strong>PERÍODO:</strong> ${c.periodo}</div>
            <div class="meta-row"><strong>DURAÇÃO:</strong> ${c.duracao}</div>
          </div>

          <p>${c.description}</p>

          <div class="course-card-price-display">
            ${c.oldPrice ? `
              <p class="course-card-price-from">
                De <span class="course-card-price-old">R$ ${c.oldPrice}</span>
              </p>
            ` : ''}
            
            <p class="course-card-price-current-label">
              por mensalidades a partir de
            </p>
            
            <p class="course-card-price-current">
              R$ ${c.price}<span>*</span>
            </p>
            
            <p class="course-card-price-note">
              *Valor final mediante descontos aplicáveis.
            </p>
          </div>

          <div class="course-card-item-footer">
            <a href="${c.url}" class="course-card-item-saiba">SAIBA MAIS &rarr;</a>
          </div>
        </div>

        <a href="${c.whatsapp}" target="_blank" rel="noopener" class="course-card-item-matricula">
          <i class="fa-brands fa-whatsapp"></i> MATRICULE-SE
        </a>
      </div>
    `;"""

# Rebuild the JS file
js = js.replace(match.group(1), new_courses_js)
js = re.sub(r'const createCourseCard = \(c\) => `.*?</div>\s+`;', new_template, js, flags=re.DOTALL)

with open("js/related-courses.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Updated related-courses.js with oldPrice, correct badges, and new template.")
