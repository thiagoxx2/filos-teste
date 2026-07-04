/**
 * carousel.js - Banner and page carousels
 * Faculdade Filos
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  // --- BANNER CAROUSEL ---
  const bannerSlides = document.querySelectorAll('.carousel-slide');
  const bannerIndicators = document.querySelectorAll('.carousel-indicator');
  let bannerInterval = null;
  let currentBannerIndex = 0;
  const BANNER_TIMEOUT = 5000; // 5 seconds autoplay

  function showBanner(index) {
    if (bannerSlides.length === 0) return;
    
    // Clean states
    bannerSlides.forEach(slide => slide.classList.remove('active'));
    bannerIndicators.forEach(ind => ind.classList.remove('active'));
    
    // Set active
    currentBannerIndex = (index + bannerSlides.length) % bannerSlides.length;
    bannerSlides[currentBannerIndex].classList.add('active');
    
    if (bannerIndicators[currentBannerIndex]) {
      bannerIndicators[currentBannerIndex].classList.add('active');
    }
  }

  function nextBanner() {
    showBanner(currentBannerIndex + 1);
  }

  function startBannerAutoplay() {
    stopBannerAutoplay();
    bannerInterval = setInterval(nextBanner, BANNER_TIMEOUT);
  }

  function stopBannerAutoplay() {
    if (bannerInterval) {
      clearInterval(bannerInterval);
      bannerInterval = null;
    }
  }

  // Setup Banner indicators click
  bannerIndicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
      stopBannerAutoplay();
      showBanner(index);
      startBannerAutoplay(); // Restart timer on click
    });
  });

  // Start banner slider if elements exist
  if (bannerSlides.length > 0) {
    showBanner(0);
    startBannerAutoplay();
    
    // Stop autoplay when mouse is hovering the hero area to improve UX
    const heroCarousel = document.querySelector('.hero-carousel');
    if (heroCarousel) {
      heroCarousel.addEventListener('mouseenter', stopBannerAutoplay);
      heroCarousel.addEventListener('mouseleave', startBannerAutoplay);
    }
  }

  // --- MINI GALERIA CAROUSEL ---
  const galeriaTrack = document.querySelector('.mini-galeria-track');
  const galeriaOriginalSlides = Array.from(document.querySelectorAll('.mini-galeria-slide'));
  const galeriaDots = document.querySelectorAll('.mini-galeria-dot');
  const galeriaTabs = document.querySelectorAll('.mini-galeria-tab');
  const galeriaPagination = document.querySelector('.mini-galeria-pagination');

  let currentGaleriaIndex = 0;
  let galeriaInterval = null;
  const GALERIA_TIMEOUT = 5000;

  function isGaleriaMobile() {
    return window.innerWidth <= 768;
  }

  // ---- DESKTOP: slides por categoria ----
  function showGaleriaSlide(index) {
    if (!galeriaTrack || galeriaOriginalSlides.length === 0) return;

    currentGaleriaIndex = ((index % galeriaOriginalSlides.length) + galeriaOriginalSlides.length) % galeriaOriginalSlides.length;

    const offset = -currentGaleriaIndex * 100;
    galeriaTrack.style.transform = `translateX(${offset}%)`;

    // Atualiza dots (re-consultando os elementos dinâmicos do DOM)
    const activeDots = document.querySelectorAll('.mini-galeria-pagination .mini-galeria-dot');
    activeDots.forEach((dot, i) => dot.classList.toggle('active', i === currentGaleriaIndex));

    // Atualiza tabs
    galeriaTabs.forEach((tab, i) => {
      if (tab) tab.classList.toggle('active', i === currentGaleriaIndex);
    });
  }

  function nextGaleriaSlide() {
    showGaleriaSlide(currentGaleriaIndex + 1);
  }

  function startGaleriaAutoplay() {
    stopGaleriaAutoplay();
    galeriaInterval = setInterval(nextGaleriaSlide, GALERIA_TIMEOUT);
  }

  function stopGaleriaAutoplay() {
    if (galeriaInterval) { clearInterval(galeriaInterval); galeriaInterval = null; }
  }

  // ---- MOBILE: 1 item por vez ----
  // Mapa: itemIndex → slideIndex (para sincronizar tabs)
  let mobileItems = []; // { element, slideIndex }
  let mobileGaleriaIndex = 0;
  let mobilePaginationEl = null;

  function buildMobileGaleria() {
    if (!galeriaTrack) return;

    // Coleta todos os itens de todos os slides, na ordem
    mobileItems = [];
    galeriaOriginalSlides.forEach((slide, slideIdx) => {
      const items = slide.querySelectorAll('.mini-galeria-item');
      items.forEach(item => {
        mobileItems.push({ element: item.cloneNode(true), slideIndex: slideIdx });
      });
    });

    // Reconstrói o track: 1 slide por item
    galeriaTrack.innerHTML = '';
    galeriaTrack.style.transition = 'transform 0.45s ease';

    mobileItems.forEach(({ element }) => {
      const slide = document.createElement('div');
      slide.className = 'mini-galeria-slide mini-galeria-slide--mobile';
      slide.style.cssText = 'min-width:100%;flex-shrink:0;';

      // Grid com 1 item
      const grid = document.createElement('div');
      grid.className = 'mini-galeria-grid';
      grid.style.gridTemplateColumns = '1fr';
      grid.appendChild(element);
      slide.appendChild(grid);
      galeriaTrack.appendChild(slide);
    });

    // Cria paginação mobile (substitui os dots estáticos do HTML)
    if (galeriaPagination) {
      galeriaPagination.innerHTML = '';
      mobileItems.forEach((_, i) => {
        const dot = document.createElement('span');
        dot.className = 'mini-galeria-dot' + (i === 0 ? ' active' : '');
        dot.addEventListener('click', () => {
          goToMobileGaleriaItem(i);
          stopGaleriaAutoplay();
          startGaleriaAutoplay();
        });
        galeriaPagination.appendChild(dot);
      });
    }

    mobileGaleriaIndex = 0;
    goToMobileGaleriaItem(0);
  }

  function goToMobileGaleriaItem(index) {
    if (mobileItems.length === 0) return;
    mobileGaleriaIndex = ((index % mobileItems.length) + mobileItems.length) % mobileItems.length;

    galeriaTrack.style.transform = `translateX(${-mobileGaleriaIndex * 100}%)`;

    // Atualiza dots
    if (galeriaPagination) {
      Array.from(galeriaPagination.children).forEach((dot, i) => {
        dot.classList.toggle('active', i === mobileGaleriaIndex);
      });
    }

    // Sincroniza a tab com a categoria do item atual
    const slideIdx = mobileItems[mobileGaleriaIndex].slideIndex;
    galeriaTabs.forEach((tab, i) => tab.classList.toggle('active', i === slideIdx));
  }

  function nextMobileGaleriaItem() {
    goToMobileGaleriaItem(mobileGaleriaIndex + 1);
  }

  function startMobileGaleriaAutoplay() {
    stopGaleriaAutoplay();
    galeriaInterval = setInterval(nextMobileGaleriaItem, GALERIA_TIMEOUT);
  }

  // ---- INIT e RESIZE ----
  function resetDesktopGaleria() {
    if (!galeriaTrack) return;
    // Restaura os slides originais
    galeriaTrack.innerHTML = '';
    galeriaOriginalSlides.forEach(slide => galeriaTrack.appendChild(slide));
    galeriaTrack.style.transition = 'transform 0.5s ease';
    galeriaTrack.style.transform = 'translateX(0)';
    
    // Determina qual aba está ativa por padrão no HTML
    const activeTabIdx = Array.from(galeriaTabs).findIndex(tab => tab.classList.contains('active'));
    const initialIndex = activeTabIdx >= 0 ? activeTabIdx : 0;
    currentGaleriaIndex = initialIndex;

    // Restaura dots estáticos
    if (galeriaPagination) {
      galeriaPagination.innerHTML = '';
      galeriaOriginalSlides.forEach((_, i) => {
        const dot = document.createElement('span');
        dot.className = 'mini-galeria-dot' + (i === initialIndex ? ' active' : '');
        dot.addEventListener('click', () => {
          stopGaleriaAutoplay();
          showGaleriaSlide(i);
          startGaleriaAutoplay();
        });
        galeriaPagination.appendChild(dot);
      });
    }

    // Reconecta tabs ao desktop mode
    galeriaTabs.forEach((tab, i) => {
      tab.onclick = () => {
        stopGaleriaAutoplay();
        showGaleriaSlide(i);
        startGaleriaAutoplay();
      };
    });

    showGaleriaSlide(initialIndex);
    startGaleriaAutoplay();
  }

    function initGaleriaForMode() {
    stopGaleriaAutoplay();
    resetDesktopGaleria();
  }

  if (galeriaTrack) {
    initGaleriaForMode();

    // Pausa ao hover / touch
    galeriaTrack.parentElement.addEventListener('mouseenter', stopGaleriaAutoplay);
    galeriaTrack.parentElement.addEventListener('mouseleave', () => {
      if (isGaleriaMobile()) startMobileGaleriaAutoplay(); else startGaleriaAutoplay();
    });
    galeriaTrack.parentElement.addEventListener('touchstart', stopGaleriaAutoplay, { passive: true });
    galeriaTrack.parentElement.addEventListener('touchend', () => {
      if (isGaleriaMobile()) startMobileGaleriaAutoplay(); else startGaleriaAutoplay();
    }, { passive: true });

    // Resize
    let lastGaleriaMobile = isGaleriaMobile();
    let galeriaResizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(galeriaResizeTimer);
      galeriaResizeTimer = setTimeout(() => {
        const nowMobile = isGaleriaMobile();
        if (nowMobile !== lastGaleriaMobile) {
          lastGaleriaMobile = nowMobile;
          initGaleriaForMode();
        }
      }, 200);
    });
  }

  // --- ALUNOS DESTAQUES CAROUSEL ---
  const destaquesSlides = document.querySelectorAll('.destaques-slide');
  const destaquesDots = document.querySelectorAll('.destaques-pagination .destaques-dot');
  let destaquesInterval = null;
  let currentDestaquesIndex = 0;
  const DESTAQUES_TIMEOUT = 5000; // 5 segundos autoplay

  function showDestaque(index) {
    if (destaquesSlides.length === 0) return;

    destaquesSlides.forEach(slide => slide.classList.remove('active'));
    destaquesDots.forEach(dot => dot.classList.remove('active'));

    currentDestaquesIndex = (index + destaquesSlides.length) % destaquesSlides.length;
    destaquesSlides[currentDestaquesIndex].classList.add('active');
    
    if (destaquesDots[currentDestaquesIndex]) {
      destaquesDots[currentDestaquesIndex].classList.add('active');
    }
  }

  function nextDestaque() {
    showDestaque(currentDestaquesIndex + 1);
  }

  function startDestaquesAutoplay() {
    stopDestaquesAutoplay();
    destaquesInterval = setInterval(nextDestaque, DESTAQUES_TIMEOUT);
  }

  function stopDestaquesAutoplay() {
    if (destaquesInterval) {
      clearInterval(destaquesInterval);
      destaquesInterval = null;
    }
  }

  destaquesDots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      stopDestaquesAutoplay();
      showDestaque(index);
      startDestaquesAutoplay();
    });
  });

  if (destaquesSlides.length > 0) {
    showDestaque(0);
    startDestaquesAutoplay();

    // Pausar autoplay ao passar o mouse por cima
    const destaquesContainer = document.querySelector('.destaques-container');
    if (destaquesContainer) {
      destaquesContainer.addEventListener('mouseenter', stopDestaquesAutoplay);
      destaquesContainer.addEventListener('mouseleave', startDestaquesAutoplay);
    }
  }

  // --- ACORDEÃO SUAVE DE LOCALIZAÇÃO (FAQ) ---
  document.querySelectorAll('.new-location-faq-item').forEach(details => {
    const summary = details.querySelector('summary');
    
    summary.addEventListener('click', (e) => {
      e.preventDefault();
      
      if (details.hasAttribute('open')) {
        // Altura inicial (aberto)
        const startHeight = details.offsetHeight;
        // Altura final (somente summary)
        const endHeight = summary.offsetHeight;
        
        details.style.height = `${startHeight}px`;
        details.style.overflow = 'hidden';
        
        // Forçar renderização
        details.offsetHeight;
        
        const animation = details.animate({
          height: [`${startHeight}px`, `${endHeight}px`]
        }, {
          duration: 320,
          easing: 'cubic-bezier(0.25, 1, 0.50, 1)'
        });
        
        animation.onfinish = () => {
          details.removeAttribute('open');
          details.style.height = '';
          details.style.overflow = '';
        };
      } else {
        // Abre temporariamente sem animar para calcular o scrollHeight real
        details.setAttribute('open', '');
        const endHeight = details.scrollHeight;
        details.removeAttribute('open');
        
        const startHeight = summary.offsetHeight;
        
        details.setAttribute('open', '');
        details.style.height = `${startHeight}px`;
        details.style.overflow = 'hidden';
        
        // Forçar renderização
        details.offsetHeight;
        
        const animation = details.animate({
          height: [`${startHeight}px`, `${endHeight}px`]
        }, {
          duration: 320,
          easing: 'cubic-bezier(0.25, 1, 0.50, 1)'
        });
        
        animation.onfinish = () => {
          details.style.height = '';
          details.style.overflow = '';
        };
      }
    });
  });

});
