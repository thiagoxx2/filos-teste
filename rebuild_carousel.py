import re

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Change selectedCourses to include all
js = re.sub(r'const selectedCourses = shuffled\.slice\(0, 6\);.*?//.*', r'const selectedCourses = shuffled;', js)

# 2. Remove dotsHtml and replace with arrowsHtml
js = re.sub(r'const dotsHtml = .*?:\s*\'\';', r'''
    const arrowsHtml = coursePages.length > 1
        ? `
          <button class="carousel-nav-btn prev" aria-label="Página anterior"><i class="fa-solid fa-chevron-left"></i></button>
          <button class="carousel-nav-btn next" aria-label="Próxima página"><i class="fa-solid fa-chevron-right"></i></button>
        `
        : '';
''', js, flags=re.DOTALL)

# 3. Replace dotsHtml variable inside sectionHtml with arrowsHtml
js = js.replace('${dotsHtml}', '${arrowsHtml}')

# 4. Fix DOM selection for arrows instead of dots
js = re.sub(r'const dots = placeholder\.querySelectorAll\(\'\.courses-pagination-dot\'\);', r'''
    const prevBtn = placeholder.querySelector('.carousel-nav-btn.prev');
    const nextBtn = placeholder.querySelector('.carousel-nav-btn.next');
''', js)

# 5. Fix update function to not toggle dots
js = re.sub(r'dots\.forEach\(\(dot, index\).*?\n\s*\}\);', '', js, flags=re.DOTALL)

# 6. Replace dot event listeners with prev/next event listeners
js = re.sub(r'dots\.forEach\(\(dot, index\).*?\}\);', r'''
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            const nextIndex = (currentPageIndex - 1 + pages.length) % pages.length;
            updateRelatedCoursesPage(nextIndex);
        });
    }
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const nextIndex = (currentPageIndex + 1) % pages.length;
            updateRelatedCoursesPage(nextIndex);
        });
    }
''', js, flags=re.DOTALL)

# 7. Change autoplay to 2700ms
js = re.sub(r'4500\);', r'2700);', js)

with open("js/related-courses.js", "w", encoding="utf-8") as f:
    f.write(js)
