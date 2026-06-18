import re
import json

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

# Extract the courses array
match = re.search(r'(const courses = \[.*?\];)', js, re.DOTALL)
if not match:
    print("Could not find courses array!")
    exit(1)

courses_array_str = match.group(1).replace('const courses = ', '').rstrip(';')
# Since it's valid JS/JSON (except for maybe trailing commas), we can parse it.
# Actually, let's just use Python's ast or json
# We might need to clean it up for json.loads
courses_array_str = re.sub(r',\s*\]', ']', courses_array_str) # remove trailing comma
try:
    courses = json.loads(courses_array_str)
except Exception as e:
    print("Error parsing JSON:", e)
    exit(1)

html_cards = []
for c in courses:
    # URL adjustment for index.html
    url = c["url"]
    if url.endswith(".html") and not url.startswith("cursos/"):
        url = "cursos/" + url
        
    # Badge formatting for data-filter
    # badge is 'Bacharelado', 'Pós-Graduação', 'Curso de Extensão'
    # in index.html, filters are 'bacharelado', 'pos', 'extensao'
    # We need to map them!
    badge = c["badge"]
    filter_val = ""
    if badge == "Bacharelado":
        filter_val = "bacharelado"
    elif badge == "Pós-Graduação":
        filter_val = "pos"
    else:
        filter_val = "extensao"
        
    card_html = f'''          <div class="course-card-item" data-filter="{filter_val}" data-course="{c["name"]}">
            <span class="course-card-item-badge">{c["badge"]}</span>
            <div class="course-card-item-body">
              <h3>{c["name"]}</h3>
              <div class="course-card-item-meta">
                <div class="meta-row"><strong>PERÍODO:</strong> {c["periodo"]}</div>
                <div class="meta-row"><strong>DURAÇÃO:</strong> {c["duracao"]}</div>
              </div>
              <p>{c["description"]}</p>
              <div class="course-card-item-footer">
                <a href="{url}" class="course-card-item-saiba">SAIBA MAIS &rarr;</a>
                <div class="course-card-item-price">R$ {c["price"]}</div>
              </div>
            </div>
            <a href="{c["whatsapp"]}" target="_blank" rel="noopener" class="course-card-item-matricula">
              <i class="fa-brands fa-whatsapp"></i> MATRICULE-SE
            </a>
          </div>'''
    html_cards.append(card_html)

full_html = "\n".join(html_cards)

# Now inject it into index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

# We need to replace everything inside <div class="courses-paginated" id="courses-paginated">
# up to the closing </div> (before <div class="courses-pagination-dots" id="courses-pagination-dots">)
pattern = r'(<div class="courses-paginated" id="courses-paginated">).*?(<div class="courses-pagination-dots" id="courses-pagination-dots">)'
replacement = r'\1\n' + full_html.replace('\\', '\\\\') + r'\n      </div>\n\n      \2'

new_index = re.sub(pattern, replacement, index_content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_index)

print("index.html updated successfully with 28 courses.")
