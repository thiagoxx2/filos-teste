document.addEventListener('DOMContentLoaded', () => {
    const section = document.getElementById('depoimentos');
    if (!section) return;

    const track = section.querySelector('.testimonials-track');
    const indicators = section.querySelector('.testimonials-indicators');

    if (!track || !indicators) return;

    const originalTrackHTML = track.innerHTML;
    const originalTrackClassName = track.className;
    const originalIndicatorsHTML = indicators.innerHTML;

    const allCards = Array.from(track.querySelectorAll('.testimonial-card'));

    const uniqueCards = [];
    const seen = new Set();

    allCards.forEach((card) => {
        const key = card.textContent.trim().replace(/\s+/g, ' ');

        if (!seen.has(key)) {
            seen.add(key);
            uniqueCards.push(card.cloneNode(true));
        }
    });

    if (!uniqueCards.length) return;

    let currentPage = 0;
    let isMobileRendered = false;

    function isMobile() {
        return window.matchMedia('(max-width: 767px)').matches;
    }

    function createPage(cards, pageIndex) {
        const page = document.createElement('div');
        page.className = `testimonials-page${pageIndex === currentPage ? ' active' : ''}`;
        page.dataset.page = String(pageIndex);

        cards.forEach((card) => {
            page.appendChild(card.cloneNode(true));
        });

        return page;
    }

    function renderDots(totalPages) {
        indicators.innerHTML = '';

        if (totalPages <= 1) {
            indicators.style.display = 'none';
            return;
        }

        indicators.style.display = 'flex';

        for (let pageIndex = 0; pageIndex < totalPages; pageIndex++) {
            const button = document.createElement('button');
            button.type = 'button';
            button.className = `testimonials-dot${pageIndex === currentPage ? ' active' : ''}`;
            button.dataset.page = String(pageIndex);
            button.setAttribute('aria-label', `Ver grupo de depoimentos ${pageIndex + 1}`);

            button.addEventListener('click', () => {
                currentPage = pageIndex;
                renderMobile();
            });

            indicators.appendChild(button);
        }
    }

    function renderMobile() {
        const cardsPerPage = 3;
        const totalPages = Math.max(1, Math.ceil(uniqueCards.length / cardsPerPage));

        if (currentPage > totalPages - 1) {
            currentPage = totalPages - 1;
        }

        track.className = 'testimonials-track';
        track.innerHTML = '';

        for (let pageIndex = 0; pageIndex < totalPages; pageIndex++) {
            const start = pageIndex * cardsPerPage;
            const end = start + cardsPerPage;
            const pageCards = uniqueCards.slice(start, end);

            track.appendChild(createPage(pageCards, pageIndex));
        }

        renderDots(totalPages);
        isMobileRendered = true;
    }

    function restoreDesktop() {
        track.className = originalTrackClassName;
        track.innerHTML = originalTrackHTML;
        indicators.innerHTML = originalIndicatorsHTML;
        indicators.style.display = '';

        currentPage = 0;
        isMobileRendered = false;
    }

    function updateLayout() {
        if (isMobile()) {
            renderMobile();
            return;
        }

        if (isMobileRendered) {
            restoreDesktop();
        }
    }

    let resizeTimeout;

    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);

        resizeTimeout = setTimeout(updateLayout, 150);
    });

    updateLayout();
});