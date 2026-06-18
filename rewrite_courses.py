import glob
import os
import re
import json

html_files = glob.glob('cursos/*.html')

courses = []

desc_map = {
    "direito": "Formação jurídica voltada para atuação profissional, preparação para a OAB e desenvolvimento de análise crítica.",
    "administracao": "Desenvolva competências em gestão, liderança, finanças, marketing e tomada de decisões estratégicas.",
    "radiologia": "Formação voltada para diagnóstico por imagem, tecnologias da saúde e atuação em ambientes clínicos.",
    "pedagogia": "Formação para atuação na educação, alfabetização, gestão escolar e práticas pedagógicas inclusivas.",
    "direito-penal": "Aprofunde seus conhecimentos em legislação penal, prática criminal, jurisprudência e estratégias de atuação jurídica.",
    "direito-imobiliario": "Formação voltada para contratos, regularização de imóveis, operações imobiliárias e consultoria jurídica no setor.",
    "direito-digital": "Conheça os principais fundamentos do Direito Digital, proteção de dados, LGPD e relações jurídicas no ambiente online.",
    "gestao-de-pessoas": "Desenvolva competências para liderança, desenvolvimento de equipes, comunicação e gestão estratégica de pessoas."
}

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    slug = os.path.basename(file_path).replace('.html', '')
    url = f"{slug}.html"
    
    name_match = re.search(r'<h1 class="hero-new-title">([^<]+)</h1>', html)
    name = name_match.group(1).strip() if name_match else slug.upper().replace('-', ' ')
    
    badge_match = re.search(r'<span class="course-badge">([^<]+)</span>', html)
    badge = badge_match.group(1).strip() if badge_match else "Pós-Graduação"
    
    duracao = ""
    duracao_match = re.search(r'<strong>Duração:\s*</strong>\s*([^<]+)</p>', html, re.IGNORECASE)
    if duracao_match:
        duracao = duracao_match.group(1).strip()
    else:
        d_match = re.search(r'Duração:\s*</strong>\s*([^<]+)</p>', html, re.IGNORECASE)
        if d_match:
            duracao = d_match.group(1).strip()

    if not duracao and badge == "Pós-Graduação":
        duracao = "6 meses"
            
    periodo = "Noturno"
    price = "299,90"
    
    # Try to find whatsapp link properly. Note: text might be URL encoded.
    wa_match = re.search(r'href="(https://wa\.me/5561999061757[^"]*)"', html)
    whatsapp = wa_match.group(1).replace('&amp;', '&') if wa_match else f"https://wa.me/5561999061757?text=Ol%C3%A1%2C%20tenho%20interesse%20no%20curso%20de%20{name}%20da%20Faculdade%20Filos."
    
    # Hardcoded fixes from user
    if slug == "pedagogia":
        badge = "Licenciatura"
        duracao = "4 anos"
    elif slug == "direito":
        badge = "Bacharelado"
        duracao = "5 anos"
    elif slug == "administracao":
        badge = "Bacharelado"
        duracao = "5 anos"
    elif slug == "radiologia":
        badge = "Tecnólogo"
        duracao = "3 anos"
        
    description = desc_map.get(slug, f"Especialize-se em {name.title()} e destaque-se no mercado de trabalho com uma formação focada e prática.")
    
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

if "direito-digital" not in [c['slug'] for c in courses]:
    courses.append({
        'slug': 'direito-digital',
        'name': 'DIREITO DIGITAL',
        'badge': 'Pós-Graduação',
        'periodo': 'Noturno',
        'duracao': '6 meses',
        'description': desc_map['direito-digital'],
        'price': '299,90',
        'url': '#contato',
        'whatsapp': "https://wa.me/5561999061757?text=Ol%C3%A1%2C%20tenho%20interesse%20no%20curso%20de%20Direito%20Digital."
    })
    
if "gestao-de-pessoas" not in [c['slug'] for c in courses]:
    courses.append({
        'slug': 'gestao-de-pessoas',
        'name': 'GESTÃO DE PESSOAS',
        'badge': 'Pós-Graduação',
        'periodo': 'Noturno',
        'duracao': '6 meses',
        'description': desc_map['gestao-de-pessoas'],
        'price': '299,90',
        'url': '#contato',
        'whatsapp': "https://wa.me/5561999061757?text=Ol%C3%A1%2C%20tenho%20interesse%20no%20curso%20de%20Gest%C3%A3o%20de%20Pessoas."
    })

js_template = """const courses = __COURSES_JSON__;

document.addEventListener('DOMContentLoaded', () => {
  const placeholder = document.querySelector('.related-courses-placeholder');
  if (!placeholder) return;

  const currentCourse = placeholder.getAttribute('data-current-course');
  
  // Filtrar removendo o curso atual
  const filteredCourses = courses.filter(c => c.slug !== currentCourse);
  
  // Embaralhar usando uma cópia do array
  const shuffled = [...filteredCourses].sort(() => 0.5 - Math.random());
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

for c in courses:
    c['description'] = c['description'].replace('\n', ' ').strip()
    c['description'] = re.sub(r'\s+', ' ', c['description'])

js_content = js_template.replace("__COURSES_JSON__", json.dumps(courses, indent=2, ensure_ascii=False))

with open('js/related-courses.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
