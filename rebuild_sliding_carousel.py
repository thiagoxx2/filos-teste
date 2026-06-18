import re

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

# Extract the courses array
match = re.search(r'(const courses = \[\s*\{.*?\}\s*\];)', js, re.DOTALL)
if not match:
    print("Could not find courses array!")
    exit(1)

courses_array = match.group(1)

# Generate the rest of the JS
new_js = courses_array + """

document.addEventListener('DOMContentLoaded', () => {
    const placeholder = document.querySelector('.related-courses-placeholder');
    if (!placeholder) return;

    const currentCourse = placeholder.getAttribute('data-current-course');

    const filteredCourses = courses.filter(c => c.slug !== currentCourse);
    if (filteredCourses.length === 0) return;

    // Embaralhar
    const shuffled = [...filteredCourses].sort(() => 0.5 - Math.random());
    const selectedCourses = shuffled;

    const createCourseCard = (c) => `
      <div class="course-card-item courses-carousel-item" data-filter="${c.badge.toLowerCase()}" data-course="${c.name}">
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

    const trackHtml = selectedCourses.map(createCourseCard).join('');

    const arrowsHtml = `
      <button class="carousel-nav-btn prev" aria-label="Anterior"><i class="fa-solid fa-chevron-left"></i></button>
      <button class="carousel-nav-btn next" aria-label="Próximo"><i class="fa-solid fa-chevron-right"></i></button>
    `;

    const sectionHtml = `
      <section id="cursos" class="section bg-light section-related-courses" style="--module-bg: #ffffff; z-index: 9;">
        <div class="container-wide">
          <div class="section-header">
            <h2 class="section-title">
              CONHEÇA OUTROS CURSOS DA <strong>FACULDADE FILOS</strong>
            </h2>
            <p class="section-subtitle">
              Explore outras opções de formação da instituição e encontre o curso ideal para o seu momento acadêmico e profissional.
            </p>
          </div>

          <div class="courses-carousel-wrapper">
             <div class="courses-carousel-track" id="related-courses-track">
                 ${trackHtml}
             </div>
             ${arrowsHtml}
          </div>
        </div>
      </section>
    `;

    placeholder.innerHTML = sectionHtml;

    const track = placeholder.querySelector('.courses-carousel-track');
    const prevBtn = placeholder.querySelector('.carousel-nav-btn.prev');
    const nextBtn = placeholder.querySelector('.carousel-nav-btn.next');

    let relatedCoursesInterval = null;

    const scrollNext = () => {
        if (!track) return;
        const itemWidth = track.firstElementChild ? track.firstElementChild.offsetWidth + 24 : 0;
        
        // Se chegou no final, volta para o começo
        if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 10) {
            track.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
            track.scrollBy({ left: itemWidth, behavior: 'smooth' });
        }
    };

    const scrollPrev = () => {
        if (!track) return;
        const itemWidth = track.firstElementChild ? track.firstElementChild.offsetWidth + 24 : 0;
        
        // Se está no começo, vai pro final
        if (track.scrollLeft <= 10) {
            track.scrollTo({ left: track.scrollWidth, behavior: 'smooth' });
        } else {
            track.scrollBy({ left: -itemWidth, behavior: 'smooth' });
        }
    };

    if (prevBtn) prevBtn.addEventListener('click', scrollPrev);
    if (nextBtn) nextBtn.addEventListener('click', scrollNext);

    const startRelatedCoursesAutoplay = () => {
        if (relatedCoursesInterval) return;
        relatedCoursesInterval = setInterval(scrollNext, 2700);
    };

    const stopRelatedCoursesAutoplay = () => {
        if (relatedCoursesInterval) {
            clearInterval(relatedCoursesInterval);
            relatedCoursesInterval = null;
        }
    };

    const wrapper = placeholder.querySelector('.courses-carousel-wrapper');
    if (wrapper) {
        wrapper.addEventListener('mouseenter', stopRelatedCoursesAutoplay);
        wrapper.addEventListener('mouseleave', startRelatedCoursesAutoplay);
        wrapper.addEventListener('touchstart', stopRelatedCoursesAutoplay, {passive: true});
        wrapper.addEventListener('touchend', startRelatedCoursesAutoplay, {passive: true});
    }

    startRelatedCoursesAutoplay();
});
"""

with open("js/related-courses.js", "w", encoding="utf-8") as f:
    f.write(new_js)

print("JS Carousel replaced with sliding track successfully.")
