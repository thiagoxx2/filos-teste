import re
import json

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Add whitelist at the top
whitelist_code = """const pricedCourseSlugs = new Set([
  'direito',
  'pedagogia',
  'administracao',
  'radiologia'
]);

"""

if "const pricedCourseSlugs" not in js:
    js = whitelist_code + js

# 2. Extract and update the courses array
match = re.search(r'(const courses = \[.*?\];)', js, re.DOTALL)
if match:
    courses_array_str = match.group(1).replace('const courses = ', '').rstrip(';')
    courses_array_str = re.sub(r',\s*\]', ']', courses_array_str)
    try:
        courses = json.loads(courses_array_str)
        
        whitelist = ['direito', 'pedagogia', 'administracao', 'radiologia']
        for c in courses:
            if c["slug"] not in whitelist:
                c["price"] = None
                c["oldPrice"] = None
        
        # Serialize back
        new_courses_str = "const courses = [\n"
        for i, c in enumerate(courses):
            new_courses_str += "    {\n"
            for k, v in c.items():
                if v is None:
                    new_courses_str += f'        "{k}": null,\n'
                else:
                    new_courses_str += f'        "{k}": "{v}",\n'
            new_courses_str = new_courses_str.rstrip(",\n") + "\n    }"
            if i < len(courses) - 1:
                new_courses_str += ",\n"
            else:
                new_courses_str += "\n];"
        
        js = js.replace(match.group(1), new_courses_str)
    except Exception as e:
        print("Error parsing courses JSON:", e)

# 3. Replace createCourseCard and add helpers
new_functions = """const normalizeCategory = (badge) => {
  const normalized = badge.toLowerCase();

  if (normalized === 'pós-graduação') return 'pos-graduacao';
  if (normalized === 'tecnólogo') return 'tecnologo';
  if (normalized === 'extensão') return 'extensao';

  return normalized;
};

const createPriceBlock = (c) => {
  const hasPrice = pricedCourseSlugs.has(c.slug) && c.price && c.oldPrice;

  if (!hasPrice) return '';

  return `
    <div class="course-card-price-display">
      <p class="course-card-price-from">
        De <span class="course-card-price-old">R$ ${c.oldPrice}</span>
      </p>

      <p class="course-card-price-current-label">
        mensalidades a partir de
      </p>

      <p class="course-card-price-current">
        <span class="course-card-price-currency">R$</span>
        <strong>${c.price}</strong>
        <span class="course-card-price-asterisk">*</span>
      </p>

      <p class="course-card-price-note">
        *Valor final mediante descontos aplicáveis.
      </p>
    </div>
  `;
};

    const createCourseCard = (c) => `
  <div class="course-card-item courses-carousel-item" data-filter="${normalizeCategory(c.badge)}" data-course="${c.name}">
    <span class="course-card-item-badge">${c.badge}</span>

    <div class="course-card-item-body">
      <h3>${c.name}</h3>

      <div class="course-card-item-meta">
        <div class="meta-row"><strong>PERÍODO:</strong> ${c.periodo}</div>
        <div class="meta-row"><strong>DURAÇÃO:</strong> ${c.duracao}</div>
      </div>

      <p>${c.description}</p>

      ${createPriceBlock(c)}

      <div class="course-card-item-footer">
        <a href="${c.url}" class="course-card-item-saiba">SAIBA MAIS &rarr;</a>
      </div>
    </div>

    <a href="${c.whatsapp}" target="_blank" rel="noopener" class="course-card-item-matricula">
      <i class="fa-brands fa-whatsapp"></i> MATRICULE-SE
    </a>
  </div>
`;"""

js = re.sub(r'const createCourseCard = \(c\) => `.*?`;', new_functions, js, flags=re.DOTALL)

with open("js/related-courses.js", "w", encoding="utf-8") as f:
    f.write(js)

print("js/related-courses.js updated.")
