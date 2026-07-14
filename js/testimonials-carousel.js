document.addEventListener('DOMContentLoaded', () => {
  const track = document.querySelector('#depoimentos .testimonials-track');
  const indicators = document.querySelector('#depoimentos .testimonials-indicators');

  if (!track) return;

  const originalCards = Array.from(track.querySelectorAll('.testimonial-card'));
  if (originalCards.length === 0) return;

  let currentPage = 0;
  let autoplayTimer = null;
  const AUTOPLAY_MS = 6000;

  function getCardsPerPage() {
    if (window.matchMedia('(max-width: 767px)').matches) return 1;
    if (window.matchMedia('(max-width: 1023px)').matches) return 2;
    if (window.matchMedia('(max-width: 1279px)').matches) return 3;
    return 4;
  }

  function getTotalPages() {
    return Math.max(1, Math.ceil(originalCards.length / getCardsPerPage()));
  }

  function createPage(cards, pageIndex) {
    const page = document.createElement('div');
    page.className = `testimonials-page${pageIndex === currentPage ? ' active' : ''}`;
    page.dataset.page = String(pageIndex);

    cards.forEach((card) => {
      page.appendChild(card);
    });

    return page;
  }

  function renderIndicators(totalPages) {
    if (!indicators) return;

    indicators.innerHTML = '';

    if (totalPages <= 1) {
      indicators.style.display = 'none';
      return;
    }

    indicators.style.display = 'flex';

    for (let i = 0; i < totalPages; i += 1) {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.className = `testimonials-dot${i === currentPage ? ' active' : ''}`;
      dot.setAttribute('aria-label', `Ver depoimentos ${i + 1}`);
      dot.dataset.page = String(i);

      dot.addEventListener('click', () => {
        currentPage = i;
        render();
        restartAutoplay();
      });

      indicators.appendChild(dot);
    }
  }

  function render() {
    const cardsPerPage = getCardsPerPage();
    const totalPages = getTotalPages();

    if (currentPage > totalPages - 1) {
      currentPage = totalPages - 1;
    }

    track.innerHTML = '';

    for (let pageIndex = 0; pageIndex < totalPages; pageIndex += 1) {
      const start = pageIndex * cardsPerPage;
      const end = start + cardsPerPage;
      const pageCards = originalCards.slice(start, end);
      track.appendChild(createPage(pageCards, pageIndex));
    }

    track.classList.add('is-initialized');
    renderIndicators(totalPages);
  }

  function stopAutoplay() {
    if (autoplayTimer) {
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
  }

  function startAutoplay() {
    stopAutoplay();

    if (getTotalPages() <= 1) return;

    autoplayTimer = setInterval(() => {
      currentPage = (currentPage + 1) % getTotalPages();
      render();
    }, AUTOPLAY_MS);
  }

  function restartAutoplay() {
    stopAutoplay();
    startAutoplay();
  }

  const carousel = document.querySelector('#depoimentos .testimonials-carousel');
  if (carousel) {
    carousel.addEventListener('mouseenter', stopAutoplay);
    carousel.addEventListener('mouseleave', startAutoplay);
  }

  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      currentPage = 0;
      render();
      restartAutoplay();
    }, 150);
  });

  render();
  startAutoplay();
});
