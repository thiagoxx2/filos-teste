import re
with open("js/related-courses.js", "r") as f:
    js = f.read()

# The user wants to perfectly mimic the home page course section without duplicating logic.
# However, the JS logic for the carousel needs to work for the related courses independently.

# Let's replace the JS DOM generation part
new_js = re.sub(
    r'const getRelatedCoursesPageSize.*',
    """
const getRelatedCoursesPageSize = () => {
    if (window.matchMedia('(max-width: 767px)').matches) return 1;
    if (window.matchMedia('(max-width: 1024px)').matches) return 2;
    return 3;
};

document.addEventListener('DOMContentLoaded', () => {
    const placeholder = document.querySelector('.related-courses-placeholder');
    if (!placeholder) return;

    const currentCourse = placeholder.getAttribute('data-current-course');

    const filteredCourses = courses.filter(c => c.slug !== currentCourse);
    if (filteredCourses.length === 0) return;

    // Embaralhar
    const shuffled = [...filteredCourses].sort(() => 0.5 - Math.random());
    const selectedCourses = shuffled.slice(0, 6); // Pegar até 6 pra ter 2 páginas no desktop

    const pageSize = getRelatedCoursesPageSize();
    const coursePages = [];

    for (let i = 0; i < selectedCourses.length; i += pageSize) {
        coursePages.push(selectedCourses.slice(i, i + pageSize));
    }

    const createCourseCard = (c) => `
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

    const pagesHtml = coursePages.map((page, index) => `
      <div class="courses-page ${index === 0 ? 'active' : ''}">
        ${page.map(createCourseCard).join('')}
      </div>
    `).join('');

    const dotsHtml = coursePages.length > 1
        ? `
          <div class="courses-pagination-dots" id="related-courses-dots" style="display: flex;">
            ${Array.from({ length: coursePages.length }).map((_, index) => `
              <button 
                class="courses-pagination-dot ${index === 0 ? 'active' : ''}" 
                type="button" 
                aria-label="Grupo ${index + 1} de cursos">
              </button>
            `).join('')}
          </div>
        `
        : '';

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

          <div class="courses-paginated" id="related-courses-paginated">
             ${pagesHtml}
          </div>
          
          ${dotsHtml}
        </div>
      </section>
    `;

    placeholder.innerHTML = sectionHtml;

    const pages = placeholder.querySelectorAll('.courses-page');
    const dots = placeholder.querySelectorAll('.courses-pagination-dot');

    let currentPageIndex = 0;
    let relatedCoursesInterval = null;

    const updateRelatedCoursesPage = (newIndex) => {
        if (!pages.length) return;

        currentPageIndex = newIndex;

        pages.forEach((page, index) => {
            page.classList.toggle('active', index === currentPageIndex);
        });

        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentPageIndex);
        });
    };

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            updateRelatedCoursesPage(index);
        });
    });

    const startRelatedCoursesAutoplay = () => {
        if (pages.length <= 1 || relatedCoursesInterval) return;

        relatedCoursesInterval = setInterval(() => {
            const nextIndex = (currentPageIndex + 1) % pages.length;
            updateRelatedCoursesPage(nextIndex);
        }, 4500);
    };

    const stopRelatedCoursesAutoplay = () => {
        if (relatedCoursesInterval) {
            clearInterval(relatedCoursesInterval);
            relatedCoursesInterval = null;
        }
    };

    const relatedCarousel = placeholder.querySelector('.section-related-courses');
    if (relatedCarousel) {
        relatedCarousel.addEventListener('mouseenter', stopRelatedCoursesAutoplay);
        relatedCarousel.addEventListener('mouseleave', startRelatedCoursesAutoplay);
    }

    startRelatedCoursesAutoplay();
});
""", js, flags=re.DOTALL)

with open("js/related-courses.js", "w") as f:
    f.write(new_js)
