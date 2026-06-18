import re
import json

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

match = re.search(r'(const courses = \[.*?\];)', js, re.DOTALL)
courses_array_str = match.group(1).replace('const courses = ', '').rstrip(';')
courses_array_str = re.sub(r',\s*\]', ']', courses_array_str)
courses = json.loads(courses_array_str)

whitelist = ['direito', 'pedagogia', 'administracao', 'radiologia']

html_cards = []
for c in courses:
    url = c["url"]
    if url.endswith(".html") and not url.startswith("cursos/") and url != "#contato":
        url = "cursos/" + url
        
    badge_lower = c["badge"].lower()
    filter_val = "all"
    if badge_lower == 'pós-graduação':
        filter_val = 'pos-graduacao'
    elif badge_lower == 'tecnólogo':
        filter_val = 'tecnologo'
    elif badge_lower == 'extensão':
        filter_val = 'extensao'
    else:
        filter_val = badge_lower
        
    price_block = ""
    if c["slug"] in whitelist and c.get("price") and c.get("oldPrice"):
        price_block = f'''
              <div class="course-card-price-display">
                <p class="course-card-price-from">
                  De <span class="course-card-price-old">R$ {c["oldPrice"]}</span>
                </p>
                <p class="course-card-price-current-label">
                  mensalidades a partir de
                </p>
                <p class="course-card-price-current">
                  <span class="course-card-price-currency">R$</span>
                  <strong>{c["price"]}</strong>
                  <span class="course-card-price-asterisk">*</span>
                </p>
                <p class="course-card-price-note">
                  *Valor final mediante descontos aplicáveis.
                </p>
              </div>'''
              
    card_html = f'''          <div class="course-card-item" data-filter="{filter_val}" data-course="{c["name"]}">
            <span class="course-card-item-badge">{c["badge"]}</span>
            <div class="course-card-item-body">
              <h3>{c["name"]}</h3>
              <div class="course-card-item-meta">
                <div class="meta-row"><strong>PERÍODO:</strong> {c["periodo"]}</div>
                <div class="meta-row"><strong>DURAÇÃO:</strong> {c["duracao"]}</div>
              </div>
              <p>{c["description"]}</p>{price_block}
              <div class="course-card-item-footer">
                <a href="{url}" class="course-card-item-saiba">SAIBA MAIS &rarr;</a>
              </div>
            </div>
            <a href="{c["whatsapp"]}" target="_blank" rel="noopener" class="course-card-item-matricula">
              <i class="fa-brands fa-whatsapp"></i> MATRICULE-SE
            </a>
          </div>'''
    html_cards.append(card_html)

full_html = "\n".join(html_cards)

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

pattern = r'(<div class="courses-paginated" id="courses-paginated">).*?(<div class="courses-pagination-dots" id="courses-pagination-dots">)'
replacement = r'\1\n' + full_html.replace('\\', '\\\\') + r'\n      </div>\n\n      \2'
new_index = re.sub(pattern, replacement, index_content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_index)

print("index.html updated.")
