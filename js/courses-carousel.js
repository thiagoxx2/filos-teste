document.addEventListener('DOMContentLoaded', () => {
  const coursesRoot = document.getElementById('courses-paginated');
  const dotsRoot = document.getElementById('courses-pagination-dots');
  const filterButtons = document.querySelectorAll('.filter-circle[data-filter]');

  if (!coursesRoot || !dotsRoot) return;

  const originalCards = Array.from(coursesRoot.querySelectorAll('.course-card-item'));

  let currentFilter = 'all';
  let currentPage = 0;

  function getCardsPerPage() {
    return window.matchMedia('(max-width: 767px)').matches ? 3 : 6;
  }

  function getFilteredCards() {
    if (currentFilter === 'all') return originalCards;
    return originalCards.filter((card) => card.dataset.filter === currentFilter);
  }

  function createPage(cards, pageIndex) {
    const page = document.createElement('div');
    page.className = `courses-page${pageIndex === currentPage ? ' active' : ''}`;
    page.dataset.page = String(pageIndex);

    cards.forEach((card) => {
      page.appendChild(card);
    });

    return page;
  }

  function renderDots(totalPages) {
    dotsRoot.innerHTML = '';

    if (totalPages <= 1) {
      dotsRoot.style.display = 'none';
      return;
    }

    dotsRoot.style.display = 'flex';

    const maxVisibleDots = 5;
    const visibleDots = Math.min(totalPages, maxVisibleDots);

    let startPage = 0;

    if (totalPages > maxVisibleDots) {
      startPage = Math.min(
        Math.max(currentPage - 2, 0),
        totalPages - maxVisibleDots
      );
    }

    for (let i = 0; i < visibleDots; i++) {
      const pageIndex = startPage + i;

      const button = document.createElement('button');
      button.type = 'button';
      button.className = `courses-pagination-dot${pageIndex === currentPage ? ' active' : ''}`;
      button.setAttribute('aria-label', `Ver grupo de cursos ${pageIndex + 1}`);
      button.dataset.page = String(pageIndex);

      button.addEventListener('click', () => {
        currentPage = pageIndex;
        renderCourses();
      });

      dotsRoot.appendChild(button);
    }
  }

  function renderCourses() {
    const cardsPerPage = getCardsPerPage();
    const filteredCards = getFilteredCards();
    const totalPages = Math.max(1, Math.ceil(filteredCards.length / cardsPerPage));

    if (currentPage > totalPages - 1) {
      currentPage = totalPages - 1;
    }

    coursesRoot.innerHTML = '';

    for (let pageIndex = 0; pageIndex < totalPages; pageIndex++) {
      const start = pageIndex * cardsPerPage;
      const end = start + cardsPerPage;
      const pageCards = filteredCards.slice(start, end);

      coursesRoot.appendChild(createPage(pageCards, pageIndex));
    }

    renderDots(totalPages);
  }

  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      filterButtons.forEach((item) => item.classList.remove('active'));
      button.classList.add('active');

      currentFilter = button.dataset.filter || 'all';
      currentPage = 0;

      renderCourses();
    });
  });

  let resizeTimeout;

  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);

    resizeTimeout = setTimeout(() => {
      currentPage = 0;
      renderCourses();
    }, 150);
  });

  renderCourses();
});