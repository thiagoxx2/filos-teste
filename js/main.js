/**
 * main.js - Core layout initialization and interactive bindings
 * Faculdade Filos
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  // --- MENU: item ativo (negrito) por clique / página / hash ---
  const NAV_STORAGE_KEY = 'filos-active-nav';

  /** Mapeie novas páginas aqui ao desenvolver (ex.: blog.html → 'blog') */
  const PAGE_PATH_NAV = [
    { match: /\/cursos\//i, navId: 'cursos' },
    { match: /\/blog\.html$/i, navId: 'blog' },
    { match: /\/vestibular\.html$/i, navId: 'vestibular' },
    { match: /\/institucional\.html$/i, navId: 'institucional' },
    { match: /\/sobre\.html$/i, navId: 'sobre' },
  ];

  const HASH_NAV = {
    cursos: 'cursos',
    contato: 'contato',
    depoimentos: 'sobre',
    galeria: 'sobre',
    faq: 'contato',
  };

  function setActiveNav(navId) {
    const navMenu = document.getElementById('nav-menu');
    if (!navMenu || !navId) return;

    const mobileLabelTarget = document.querySelector('.header-nav .header-row__center');
    const labels = {
      home: 'HOME',
      cursos: 'CURSOS',
      vestibular: 'VESTIBULAR',
      institucional: 'INSTITUCIONAL',
      sobre: 'SOBRE',
      blog: 'BLOG',
      contato: 'CONTATO'
    };

    if (mobileLabelTarget) {
      mobileLabelTarget.dataset.mobilePageLabel = labels[navId] || 'HOME';
    }

    navMenu.querySelectorAll('.nav-link').forEach((link) => {
      link.classList.toggle('active', link.dataset.nav === navId);
    });
  }

  function resolveNavIdFromContext() {
    const bodyNav = document.body.dataset.pageNav;
    if (bodyNav) return bodyNav;

    const pathNav = PAGE_PATH_NAV.find((entry) => entry.match.test(window.location.pathname));
    if (pathNav) return pathNav.navId;

    const stored = sessionStorage.getItem(NAV_STORAGE_KEY);
    if (stored) return stored;

    const hash = window.location.hash.replace('#', '');
    if (hash && HASH_NAV[hash]) return HASH_NAV[hash];
    if (hash === 'inicio') return 'home';
    if (hash === 'quem-somos') return 'institucional';

    const htmlActive = document.querySelector('.nav-menu .nav-link.active');
    return htmlActive?.dataset.nav || 'home';
  }

  function initNavActiveState() {
    const navMenu = document.getElementById('nav-menu');
    if (!navMenu) return;

    setActiveNav(resolveNavIdFromContext());

    let isScrollingFromClick = false;
    let clickScrollTimeout;

    navMenu.querySelectorAll('.nav-link').forEach((link) => {
      link.addEventListener('click', (e) => {
        const navId = link.dataset.nav;
        if (!navId) return;

        isScrollingFromClick = true;
        sessionStorage.setItem(NAV_STORAGE_KEY, navId);
        setActiveNav(navId);

        if (link.getAttribute('href') === '#') {
          e.preventDefault();
        }
      });
    });

    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '');
      if (HASH_NAV[hash]) {
        sessionStorage.setItem(NAV_STORAGE_KEY, HASH_NAV[hash]);
        setActiveNav(HASH_NAV[hash]);
      } else if (hash === 'inicio') {
        const stored = sessionStorage.getItem(NAV_STORAGE_KEY);
        if (stored === 'vestibular' || stored === 'home') {
          setActiveNav(stored);
        } else {
          sessionStorage.setItem(NAV_STORAGE_KEY, 'home');
          setActiveNav('home');
        }
      } else if (hash === 'quem-somos') {
        const stored = sessionStorage.getItem(NAV_STORAGE_KEY);
        if (stored === 'sobre' || stored === 'institucional') {
          setActiveNav(stored);
        } else {
          sessionStorage.setItem(NAV_STORAGE_KEY, 'institucional');
          setActiveNav('institucional');
        }
      }
    });

    // --- ScrollSpy: Menu ativo dinâmico por rolagem ---
    const sections = [
      { id: 'inicio', navIds: ['home', 'vestibular'] },
      { id: 'cursos', navIds: ['cursos'] },
      { id: 'quem-somos', navIds: ['institucional', 'sobre'] },
      { id: 'contato', navIds: ['contato'] }
    ];

    function getActiveNavForSection(sectionId) {
      const stored = sessionStorage.getItem(NAV_STORAGE_KEY);
      if (sectionId === 'inicio') {
        return (stored === 'vestibular') ? 'vestibular' : 'home';
      }
      if (sectionId === 'quem-somos') {
        return (stored === 'sobre') ? 'sobre' : 'institucional';
      }
      if (sectionId === 'cursos') return 'cursos';
      if (sectionId === 'contato') return 'contato';
      return null;
    }

    function handleScrollSpy() {
      const onCoursePage = /\/cursos\//i.test(window.location.pathname);
      if (onCoursePage) return;

      const headerOffset = document.getElementById('site-header')?.offsetHeight || 148;
      const scrollPos = window.scrollY + headerOffset + 80; // Buffer de 80px para suavizar transição

      let activeSectionId = null;

      // Se estiver no topo da página
      if (window.scrollY < 50) {
        activeSectionId = 'inicio';
      } else if ((window.innerHeight + window.scrollY) >= document.documentElement.scrollHeight - 50) {
        // Se estiver no fim da página
        activeSectionId = 'contato';
      } else {
        // Encontrar seção ativa
        for (const section of sections) {
          const el = document.getElementById(section.id);
          if (el) {
            const top = el.getBoundingClientRect().top + window.scrollY;
            const height = el.offsetHeight;
            if (scrollPos >= top && scrollPos < top + height) {
              activeSectionId = section.id;
              break;
            }
          }
        }
      }

      if (activeSectionId) {
        const targetNavId = getActiveNavForSection(activeSectionId);
        if (targetNavId) {
          const currentActive = sessionStorage.getItem(NAV_STORAGE_KEY);
          if (currentActive !== targetNavId) {
            sessionStorage.setItem(NAV_STORAGE_KEY, targetNavId);
            setActiveNav(targetNavId);
          }
        }
      }
    }

    window.addEventListener('scroll', () => {
      if (isScrollingFromClick) {
        clearTimeout(clickScrollTimeout);
        clickScrollTimeout = setTimeout(() => {
          isScrollingFromClick = false;
        }, 150); // 150ms após cessar movimento, reabilita scrollspy
      } else {
        handleScrollSpy();
      }
    }, { passive: true });
  }

  initNavActiveState();

  // --- COURSE PRICE TOGGLES ---
  function initCoursePriceToggles() {
    document.querySelectorAll('[data-price-card]').forEach((card) => {
      const output = card.querySelector('[data-price-output]');
      const toggles = Array.from(card.querySelectorAll('[data-price-toggle]'));
      if (!output || !toggles.length) return;

      let note = card.querySelector('[data-price-note]') || card.querySelector('.sidebar-price-period');
      if (!note) {
        note = document.createElement('p');
        note.className = 'price-mode-note';
        note.dataset.priceNote = '';
        output.insertAdjacentElement('afterend', note);
      } else {
        note.dataset.priceNote = '';
        note.classList.add('price-mode-note');
      }

      const format = output.dataset.priceFormat || 'plain';
      const defaultPrice = card.dataset.priceDefault || output.textContent.trim();

      const renderPrice = (value) => {
        if (!value) return;
        if (format === 'sidebar') {
          output.innerHTML = `<span>R$</span> ${value}`;
          return;
        }
        output.textContent = value;
      };

      const getToggleLabel = (toggle) => (
        toggle?.dataset.priceLabel ||
        toggle?.closest('.course-price-toggle, .toggle-switch')?.querySelector('span')?.textContent.trim() ||
        ''
      );

      const syncPrice = (activeToggle) => {
        const selected = activeToggle || toggles.find((toggle) => toggle.checked);
        renderPrice(selected?.dataset.price || defaultPrice);
        const label = getToggleLabel(selected);
        if (label) {
          note.textContent = `Valor referente à modalidade: ${label}.`;
        }
      };

      toggles.forEach((toggle) => {
        toggle.addEventListener('change', () => {
          if (toggle.checked) {
            toggles.forEach((other) => {
              if (other !== toggle) other.checked = false;
            });
            syncPrice(toggle);
          } else {
            const fallback = toggles.find((other) => other.checked);
            if (!fallback) {
              toggle.checked = true;
              syncPrice(toggle);
              return;
            }
            syncPrice(fallback);
          }
        });
      });

      syncPrice();
    });
  }

  initCoursePriceToggles();

  // --- FLOATING SIDEBAR LEFT (links conforme a página) ---
  const floatingLocation = document.querySelector('[data-floating-location]');
  if (floatingLocation) {
    floatingLocation.href = 'https://www.google.com/maps/dir/?api=1&destination=Faculdade+Filos,+Avenida+Tiradentes,+%C3%81guas+Lindas+de+Goi%C3%A1s';
    floatingLocation.target = '_blank';
    floatingLocation.rel = 'noopener noreferrer';
  }

  const floatingSearch = document.querySelector('[data-floating-search]');
  if (floatingSearch) {
    floatingSearch.addEventListener('click', (e) => {
      e.preventDefault();
      const onCoursePage = /\/cursos\//i.test(window.location.pathname);
      const cursosSection = document.getElementById('cursos');

      if (cursosSection && !onCoursePage) {
        const headerOffset = document.getElementById('site-header')?.offsetHeight || 148;
        const top = cursosSection.getBoundingClientRect().top + window.pageYOffset - headerOffset;
        window.scrollTo({ top, behavior: 'smooth' });
        return;
      }

      window.location.href = onCoursePage ? '../index.html#cursos' : 'index.html#cursos';
    });
  }

  // --- LOGIN / CADASTRAR DROPDOWN MENU ---
  const loginToggle = document.getElementById('login-menu-toggle');
  const loginDropdown = document.getElementById('login-dropdown');

  if (loginToggle && loginDropdown) {
    const loginContainer = loginToggle.closest('.header-login-container');
    let loginCloseTimer;

    const openLoginDropdown = () => {
      clearTimeout(loginCloseTimer);
      loginToggle.setAttribute('aria-expanded', 'true');
      loginDropdown.classList.add('active');
    };

    const closeLoginDropdown = () => {
      clearTimeout(loginCloseTimer);
      loginToggle.setAttribute('aria-expanded', 'false');
      loginDropdown.classList.remove('active');
    };

    const scheduleLoginDropdownClose = () => {
      clearTimeout(loginCloseTimer);
      loginCloseTimer = setTimeout(closeLoginDropdown, 160);
    };

    loginToggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const isExpanded = loginToggle.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closeLoginDropdown();
      } else {
        openLoginDropdown();
      }
    });

    if (loginContainer) {
      loginContainer.addEventListener('mouseenter', openLoginDropdown);
      loginContainer.addEventListener('mouseleave', scheduleLoginDropdownClose);
      loginContainer.addEventListener('focusin', openLoginDropdown);
      loginContainer.addEventListener('focusout', (e) => {
        if (!loginContainer.contains(e.relatedTarget)) {
          scheduleLoginDropdownClose();
        }
      });
    }

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!loginContainer || !loginContainer.contains(e.target)) {
        closeLoginDropdown();
      }
    });

    // Close when pressing Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeLoginDropdown();
      }
    });
  }

  // --- MOBILE MENU HAMBURGER ---
  const mobileMenuHost = document.querySelector('.header-nav .header-row__side--end');
  const mobileMenuButton = document.getElementById('menu-toggle');

  if (mobileMenuHost && mobileMenuButton && mobileMenuButton.parentElement !== mobileMenuHost) {
    mobileMenuHost.appendChild(mobileMenuButton);
  }

  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');

  if (menuToggle && navMenu) {
    const closeMobileCourseMenu = initMobileCourseMenu(navMenu, menuToggle);
    ensureMobileLoginLink(navMenu);
    const closeMobileInstitutionalMenu = initMobileLinkPanel(navMenu, menuToggle, {
      triggerSelector: '[data-nav="institucional"]',
      sourceSelector: '.dropdown-menu-institucional',
      itemSelector: '.dropdown-item-vertical'
    });
    const closeMobileContactMenu = initMobileLinkPanel(navMenu, menuToggle, {
      triggerSelector: '[data-nav="contato"]',
      sourceSelector: '.dropdown-menu-contato',
      itemSelector: '.dropdown-item-vertical'
    });
    const closeMobileLoginMenu = initMobileLinkPanel(navMenu, menuToggle, {
      triggerSelector: '.mobile-login-link',
      sourceSelector: '#login-dropdown',
      itemSelector: '.login-dropdown-item'
    });

    const closeMobilePanels = () => {
      [
        closeMobileCourseMenu,
        closeMobileInstitutionalMenu,
        closeMobileContactMenu,
        closeMobileLoginMenu
      ].forEach((closePanel) => {
        if (typeof closePanel === 'function') closePanel();
      });
    };

    menuToggle.addEventListener('click', (e) => {
      e.preventDefault();
      menuToggle.classList.toggle('active');
      navMenu.classList.toggle('active');
      menuToggle.setAttribute('aria-expanded', navMenu.classList.contains('active') ? 'true' : 'false');
      
      // Stop background scrolling when mobile menu is open
      if (navMenu.classList.contains('active')) {
        document.body.style.overflow = 'hidden';
      } else {
        closeMobilePanels();
        document.body.style.overflow = '';
      }
    });

    // Close menu when clicking links
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        navMenu.classList.remove('active');
        closeMobilePanels();
        menuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }


  function ensureMobileLoginLink(navMenu) {
    if (navMenu.querySelector('.mobile-login-item')) return;

    const loginItem = document.createElement('div');
    loginItem.className = 'nav-item-dropdown mobile-login-item';

    const loginLink = document.createElement('a');
    loginLink.className = 'nav-link mobile-login-link';
    loginLink.href = '#';
    loginLink.textContent = 'Login / Cadastrar';
    loginItem.appendChild(loginLink);
    navMenu.appendChild(loginItem);
  }

  function initMobileLinkPanel(navMenu, menuToggle, config) {
    const trigger = navMenu.querySelector(config.triggerSelector);
    const source = document.querySelector(config.sourceSelector) || navMenu.querySelector(config.sourceSelector);
    if (!trigger || !source) return;

    const mobileQuery = window.matchMedia('(max-width: 1023px)');
    const triggerItem = trigger.closest('.nav-item, .nav-item-dropdown') || trigger.parentElement;
    if (!triggerItem || triggerItem.querySelector('.mobile-submenu-panel')) return;

    const panel = document.createElement('div');
    panel.className = 'mobile-submenu-panel';
    panel.setAttribute('aria-hidden', 'true');

    Array.from(source.querySelectorAll(config.itemSelector)).forEach((item) => {
      const link = document.createElement('a');
      link.className = 'mobile-submenu-link';
      link.href = item.getAttribute('href') || '#';
      link.textContent = item.textContent.trim();

      ['target', 'rel'].forEach((attr) => {
        const value = item.getAttribute(attr);
        if (value) link.setAttribute(attr, value);
      });

      panel.appendChild(link);
    });

    triggerItem.appendChild(panel);
    trigger.setAttribute('aria-haspopup', 'true');
    trigger.setAttribute('aria-expanded', 'false');

    const closePanel = () => {
      panel.classList.remove('is-active');
      panel.setAttribute('aria-hidden', 'true');
      trigger.classList.remove('is-mobile-submenu-open');
      trigger.setAttribute('aria-expanded', 'false');
    };

    const openPanel = () => {
      navMenu.dispatchEvent(new CustomEvent('mobile-submenu-open', { detail: panel }));
      panel.classList.add('is-active');
      panel.setAttribute('aria-hidden', 'false');
      trigger.classList.add('is-mobile-submenu-open');
      trigger.setAttribute('aria-expanded', 'true');
    };

    trigger.addEventListener('click', (e) => {
      if (!mobileQuery.matches) return;
      e.preventDefault();
      e.stopImmediatePropagation();
      const shouldOpen = !panel.classList.contains('is-active');
      closePanel();
      if (shouldOpen) openPanel();
    });

    panel.addEventListener('click', (e) => {
      const link = e.target.closest('.mobile-submenu-link');
      if (!link) return;

      menuToggle.classList.remove('active');
      navMenu.classList.remove('active');
      closePanel();
      menuToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });

    navMenu.addEventListener('mobile-submenu-open', (e) => {
      if (e.detail !== panel) closePanel();
    });

    window.addEventListener('resize', () => {
      if (!mobileQuery.matches) closePanel();
    });

    return closePanel;
  }

  // --- MOBILE COURSE MENU: course list below Cursos ---
  function initMobileCourseMenu(navMenu, menuToggle) {
    const coursesLink = navMenu.querySelector('[data-nav="cursos"]');
    const coursesDropdown = navMenu.querySelector('.dropdown-menu-cursos');
    if (!coursesLink || !coursesDropdown || navMenu.querySelector('.mobile-course-panel')) return;

    const mobileQuery = window.matchMedia('(max-width: 1023px)');
    const columns = Array.from(coursesDropdown.querySelectorAll('.dropdown-column'));
    const coursesItem = coursesLink.closest('.nav-item, .nav-item-dropdown') || coursesLink.parentElement;
    if (!columns.length || !coursesItem) return;

    const panel = document.createElement('div');
    panel.className = 'mobile-course-panel';
    panel.setAttribute('aria-hidden', 'true');

    const courseList = document.createElement('div');
    courseList.className = 'mobile-course-list is-active';

    const items = columns
      .flatMap((column) => Array.from(column.querySelectorAll('.dropdown-item')))
      .slice(0, 15);

    items.forEach((item) => {
      const link = document.createElement('a');
      link.className = 'mobile-course-link';
      link.href = item.getAttribute('href') || '#';
      link.textContent = item.textContent.trim();
      courseList.appendChild(link);
    });

    const seeAll = document.createElement('a');
    seeAll.className = 'mobile-course-link mobile-course-link--all';
    seeAll.href = 'index.html#cursos';
    seeAll.textContent = 'Ver todos';
    courseList.appendChild(seeAll);
    panel.appendChild(courseList);

    coursesItem.appendChild(panel);

    const openPanel = () => {
      navMenu.dispatchEvent(new CustomEvent('mobile-submenu-open', { detail: panel }));
      panel.classList.add('is-active');
      panel.setAttribute('aria-hidden', 'false');
      coursesLink.classList.add('is-mobile-courses-open');
      coursesLink.setAttribute('aria-expanded', 'true');
    };

    const closePanel = () => {
      panel.classList.remove('is-active');
      panel.setAttribute('aria-hidden', 'true');
      coursesLink.classList.remove('is-mobile-courses-open');
      coursesLink.setAttribute('aria-expanded', 'false');
    };

    coursesLink.setAttribute('aria-haspopup', 'true');
    coursesLink.setAttribute('aria-expanded', 'false');

    coursesLink.addEventListener('click', (e) => {
      if (!mobileQuery.matches) return;
      e.preventDefault();
      e.stopImmediatePropagation();
      sessionStorage.setItem(NAV_STORAGE_KEY, 'cursos');
      setActiveNav('cursos');
      if (panel.classList.contains('is-active')) closePanel();
      else openPanel();
    });

    panel.addEventListener('click', (e) => {
      const courseLink = e.target.closest('.mobile-course-link');
      if (courseLink) {
        menuToggle.classList.remove('active');
        navMenu.classList.remove('active');
        closePanel();
        menuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });

    window.addEventListener('resize', () => {
      if (!mobileQuery.matches) closePanel();
    });

    navMenu.addEventListener('mobile-submenu-open', (e) => {
      if (e.detail !== panel) closePanel();
    });

    return closePanel;
  }

  // --- LAZY MAP EMBED LOAD (LGPD & PERFORMANCE) ---
  const mapPlaceholder = document.getElementById('map-placeholder');
  const mapIframe = document.getElementById('map-iframe');

  if (mapPlaceholder && mapIframe) {
    const loadMap = () => {
      // Get source from data-src or load standard Google Maps embed for Faculdade Filos address
      const mapSrc = mapIframe.getAttribute('data-src') || "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3840.404285885233!2d-48.2483864!3d-15.7825227!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x935bc9f187a55097%3A0xe54e6fe4ef0f968!2sAv.%20Tiradentes%20-%20Jardim%20P%C3%A9rola%2C%20%C3%81guas%20Lindas%20de%20Goi%C3%A1s%20-%20GO%2C%2072911-262!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr";
      
      mapIframe.src = mapSrc;
      mapIframe.classList.add('loaded');
      
      // Fade out placeholder
      mapPlaceholder.style.opacity = '0';
      setTimeout(() => {
        mapPlaceholder.style.display = 'none';
      }, 300);
    };

    // Load map on user interaction click
    mapPlaceholder.addEventListener('click', loadMap);

    // Also auto-load if cookies consent allows everything
    document.addEventListener('cookieConsentChanged', (e) => {
      const consent = e.detail;
      if (consent && consent.marketing) {
        loadMap();
      }
    });
  }


  // --- STICKY HEADER ACCENTS ---
  const siteHeader = document.querySelector('.site-header');
  if (siteHeader) {
    window.addEventListener('scroll', () => {
      siteHeader.classList.toggle('is-scrolled', window.scrollY > 24);
    }, { passive: true });
  }


  // --- SMOOTH SCROLL FOR INTERNAL LINKS ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        
        // Offset for sticky header
        const headerOffset = document.getElementById('site-header')?.offsetHeight || 148;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // --- DINAMIZAR E REPETIR ITENS DA MARQUEE SUPERIOR ---
  function initDynamicMarquee() {
    const marqueeTrack = document.querySelector('.top-marquee .marquee-track');
    if (!marqueeTrack) return;

    // 1. Obter todos os cards de graduação (bacharelado) na página
    const graduationCards = Array.from(document.querySelectorAll('.course-card-item[data-filter="bacharelado"]'));
    
    // Se não houver cards (ex: em páginas secundárias se não tiverem os cards na DOM), 
    // ou se quisermos manter fallback estático caso nada seja encontrado.
    if (graduationCards.length === 0) {
      const contents = marqueeTrack.querySelectorAll('.marquee-content');
      if (contents.length > 0) {
        const baseContent = contents[0].innerHTML;
        const repeatedHTML = Array(5).fill(baseContent).join('');
        
        marqueeTrack.innerHTML = `
          <div class="marquee-content">${repeatedHTML}</div>
          <div class="marquee-content" aria-hidden="true">${repeatedHTML}</div>
        `;
      }
      return;
    }

    // 2. Extrair dados dos cursos
    const coursesData = graduationCards.map(card => {
      const courseName = card.getAttribute('data-course') || '';
      const saibaLink = card.querySelector('.course-card-item-saiba');
      const courseHref = saibaLink ? saibaLink.getAttribute('href') : '#';
      return {
        name: courseName.toUpperCase(),
        href: courseHref
      };
    });

    // 3. Montar a sequência base de itens da marquee
    const buildSequenceHTML = () => {
      let html = '';
      coursesData.forEach(course => {
        html += `<a href="${course.href}">${course.name}</a>`;
      });
      return html;
    };

    const baseSequenceHTML = buildSequenceHTML();

    // 4. Repetir a sequência base (5 vezes) para garantir que preencha toda a tela sem espaços vazios
    const repetitions = 5;
    const fullContentHTML = Array(repetitions).fill(baseSequenceHTML).join('');

    // 5. Inserir a estrutura duplicada na track para o scroll infinito
    marqueeTrack.innerHTML = `
      <div class="marquee-content">${fullContentHTML}</div>
      <div class="marquee-content" aria-hidden="true">${fullContentHTML}</div>
    `;
  }

  initDynamicMarquee();

});
