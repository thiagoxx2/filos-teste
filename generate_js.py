import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all blocks of course-card-item
cards = re.split(r'<div class="course-card-item"', html)[1:]
courses = []

for card in cards:
    try:
        # url
        url_match = re.search(r'href="([^"]+)"\s*class="course-card-item-saiba"', card)
        if not url_match:
            continue
        url = url_match.group(1)
        if url.startswith('cursos/'):
            url = url.replace('cursos/', '')
        slug = url.replace('.html', '')
        
        # badge
        badge_match = re.search(r'<span class="course-card-item-badge">([^<]+)</span>', card)
        badge = badge_match.group(1) if badge_match else ""
        
        # name
        name_match = re.search(r'<h3>([^<]+)</h3>', card)
        name = name_match.group(1) if name_match else ""
        
        # periodo
        periodo_match = re.search(r'<strong>PERÍODO:</strong>([^<]+)</div>', card)
        periodo = periodo_match.group(1).strip() if periodo_match else "Noturno"
        
        # duracao
        duracao_match = re.search(r'<strong>DURAÇÃO:</strong>([^<]+)</div>', card)
        duracao = duracao_match.group(1).strip() if duracao_match else ""
        
        # description
        desc_match = re.search(r'<p>([^<]+)</p>', card)
        description = desc_match.group(1).strip() if desc_match else ""
        
        # price
        price_match = re.search(r'<div class="course-card-item-price">([^<]+)</div>', card)
        price = price_match.group(1).strip() if price_match else ""
        
        # whatsapp
        wa_match = re.search(r'href="([^"]+)"[^>]*class="course-card-item-matricula"', card)
        whatsapp = wa_match.group(1).strip() if wa_match else ""
        
        courses.append({
            'slug': slug,
            'name': name,
            'badge': badge,
            'periodo': periodo,
            'duracao': duracao,
            'description': description,
            'price': price,
            'url': url,
            'whatsapp': whatsapp
        })
    except Exception as e:
        print('Error parsing card:', e)

js_template = """const courses = __COURSES_JSON__;

document.addEventListener('DOMContentLoaded', () => {
  const placeholder = document.querySelector('.related-courses-placeholder');
  if (!placeholder) return;

  const currentCourse = placeholder.getAttribute('data-current-course');
  
  // Filtrar removendo o curso atual
  const filteredCourses = courses.filter(c => c.slug !== currentCourse);
  
  // Pegar os primeiros 3 cursos embaralhados
  const shuffled = filteredCourses.sort(() => 0.5 - Math.random());
  const selectedCourses = shuffled.slice(0, 3);
  
  if (selectedCourses.length === 0) return;

  let cardsHtml = '';
  selectedCourses.forEach(c => {
    cardsHtml += `
      <div class="course-card-item" data-filter="${c.badge.toLowerCase()}" data-course="${c.name}">
        <span class="course-card-item-badge">${c.badge}</span>

        <div class="course-card-item-body">
          <h3>${c.name}</h3>

          <div class="course-card-item-meta">
            <div class="meta-row"><strong>PERÍODO:</strong> ${c.periodo}</div>
            <div class="meta-row"><strong>DURAÇÃO:</strong> ${c.duracao}</div>
          </div>

          <p>${c.description}</p>

          <div class="course-card-item-footer">
            <a href="${c.url}" class="course-card-item-saiba">SAIBA MAIS &rarr;</a>
            <div class="course-card-item-price">${c.price}</div>
          </div>
        </div>

        <a href="${c.whatsapp}" target="_blank" rel="noopener" class="course-card-item-matricula">
          <i class="fa-brands fa-whatsapp"></i> MATRICULE-SE
        </a>
      </div>
    `;
  });

  const sectionHtml = `
    <section class="section-related-courses">
      <div class="container-wide">
        <div class="section-header">
          <h2 class="section-title">
            CONHEÇA OUTROS CURSOS DA <strong>FACULDADE FILOS</strong>
          </h2>
          <p class="section-subtitle">
            Explore outras opções de formação da instituição e encontre o curso ideal para o seu momento acadêmico e profissional.
          </p>
        </div>

        <div class="related-courses-carousel-wrapper">
          <div class="related-courses-carousel">
            <div class="related-courses-pages">
              <div class="related-courses-page active">
                ${cardsHtml}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  `;

  placeholder.innerHTML = sectionHtml;
});
"""

js_content = js_template.replace("__COURSES_JSON__", json.dumps(courses, indent=2, ensure_ascii=False))

with open('js/related-courses.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f'Generated {len(courses)} courses in related-courses.js')
