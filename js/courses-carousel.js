(function () {
  'use strict';

  let cardsData = [];
  const paginated = document.getElementById('courses-paginated');
  const dotsContainer = document.getElementById('courses-pagination-dots');
  const filterCircles = document.querySelectorAll('.filter-circle');

  if (!paginated) return;

  const homeCourses = [
    {
      filter: 'bacharelado',
      badge: 'Bacharelado',
      course: 'Direito',
      title: 'DIREITO',
      href: 'cursos/direito.html',
      duration: '5 anos',
      price: '698,96',
      description: 'Formação jurídica reconhecida pelo MEC, com base prática para atuação no mercado.'
    },
    {
      filter: 'bacharelado',
      badge: 'Bacharelado',
      course: 'Administração',
      title: 'ADMINISTRAÇÃO',
      href: 'cursos/administracao.html',
      duration: '4 anos',
      price: '535,00',
      description: 'Formação em gestão, liderança, finanças e estratégia para atuar em empresas e negócios.'
    },
    {
      filter: 'bacharelado',
      badge: 'Bacharelado',
      course: 'Radiologia',
      title: 'RADIOLOGIA',
      href: 'cursos/radiologia.html',
      duration: '3 anos',
      price: '609,65',
      description: 'Formação reconhecida pelo MEC para atuação técnica e prática na área de radiologia.'
    },
    {
      filter: 'bacharelado',
      badge: 'Bacharelado',
      course: 'Pedagogia',
      title: 'PEDAGOGIA',
      href: 'cursos/pedagogia.html',
      duration: '4 anos',
      price: '475,55',
      description: 'Licenciatura para atuação na docência, coordenação e gestão de espaços escolares.'
    },
    {
      filter: 'pos-graduacao',
      badge: 'Pós-graduação',
      course: 'Direito Penal e Processo Penal',
      title: 'DIREITO PENAL',
      href: 'cursos/direito-penal.html',
      duration: '1 ano',
      price: '249,00',
      description: 'Especialização para aprofundar a atuação em direito penal e processo penal.'
    },
    {
      filter: 'pos-graduacao',
      badge: 'Pós-graduação',
      course: 'Direito Imobiliário',
      title: 'DIREITO IMOBILIÁRIO',
      href: 'cursos/direito-imobiliario.html',
      duration: '1 ano',
      price: '229,00',
      description: 'Especialização voltada à prática jurídica no mercado imobiliário e regularização.'
    },
    {
      filter: 'pos-graduacao',
      badge: 'Pós-graduação',
      course: 'Gestão de Operações 4.0',
      title: 'GESTÃO DE OPERAÇÕES 4.0',
      href: 'cursos/gestao-de-operacoes.html',
      duration: '1 ano',
      price: '299,00',
      description: 'Especialização em processos, tecnologia e melhoria operacional para negócios.'
    },
    {
      filter: 'pos-graduacao',
      badge: 'Pós-graduação',
      course: 'Inteligência Artificial Aplicada aos Negócios',
      title: 'INTELIGÊNCIA ARTIFICIAL',
      href: 'cursos/inteligencia-artificial.html',
      duration: '1 ano',
      price: '349,00',
      description: 'Especialização em IA aplicada a decisões, produtividade e inovação nos negócios.'
    },
    {
      filter: 'pos-graduacao',
      badge: 'Pós-graduação',
      course: 'Docência no Ensino Superior',
      title: 'DOCÊNCIA NO ENSINO SUPERIOR',
      href: 'cursos/docencia-ensino-superior.html',
      duration: '1 ano',
      price: '249,00',
      description: 'Especialização para atuação docente com práticas modernas no ensino superior.'
    },
    {
      filter: 'pos-graduacao',
      badge: 'Pós-graduação',
      course: 'Ressonância Magnética',
      title: 'RESSONÂNCIA MAGNÉTICA',
      href: 'cursos/ressonancia-magnetica.html',
      duration: '1 ano',
      price: '289,00',
      description: 'Especialização para aprofundamento técnico em exames e rotinas de ressonância.'
    },
    {
      filter: 'pos-graduacao',
      badge: 'Pós-graduação',
      course: 'Neuropsicopedagogia',
      title: 'NEUROPSICOPEDAGOGIA',
      href: 'cursos/neuropsicopedagogia.html',
      duration: '1 ano',
      price: '279,00',
      description: 'Especialização para compreensão dos processos de aprendizagem e desenvolvimento.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Controle de Qualidade de Imagem e Artefatos Médicos',
      title: 'CONTROLE DE QUALIDADE',
      href: 'cursos/controle-qualidade-imagem.html',
      duration: '60 horas',
      price: '149,00',
      description: 'Curso prático para aperfeiçoar a análise de qualidade de imagem e artefatos médicos.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Vendas Digitais (Redes Sociais e WhatsApp)',
      title: 'VENDAS DIGITAIS',
      href: 'cursos/vendas-digitais.html',
      duration: '40 horas',
      price: '119,00',
      description: 'Curso prático para vender melhor usando redes sociais, atendimento e WhatsApp.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Excelência no Atendimento e Fidelização',
      title: 'EXCELÊNCIA NO ATENDIMENTO',
      href: 'cursos/excelencia-atendimento.html',
      duration: '40 horas',
      price: '119,00',
      description: 'Curso prático para melhorar atendimento, relacionamento e fidelização de clientes.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Técnicas de Vendas e Negociação',
      title: 'TÉCNICAS DE VENDAS',
      href: 'cursos/tecnicas-vendas.html',
      duration: '40 horas',
      price: '129,00',
      description: 'Curso prático para desenvolver negociação, comunicação e fechamento de vendas.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Domínio das I.As: Criação de Textos e Imagens',
      title: 'DOMÍNIO DAS I.AS',
      href: 'cursos/dominio-ias.html',
      duration: '50 horas',
      price: '159,00',
      description: 'Curso prático para criar textos, imagens e soluções com ferramentas de inteligência artificial.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Automação Prática sem Programação',
      title: 'AUTOMAÇÃO PRÁTICA',
      href: 'cursos/automacao-pratica.html',
      duration: '50 horas',
      price: '149,00',
      description: 'Curso prático para automatizar rotinas e processos sem precisar programar.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Noções de Direito Penal e Segurança Cidadã',
      title: 'NOÇÕES DE DIREITO PENAL',
      href: 'cursos/nocoes-direito-penal.html',
      duration: '60 horas',
      price: '139,00',
      description: 'Curso introdutório sobre fundamentos de direito penal e segurança cidadã.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Lei Maria da Penha e Proteção à Família',
      title: 'LEI MARIA DA PENHA',
      href: 'cursos/lei-maria-da-penha.html',
      duration: '50 horas',
      price: '129,00',
      description: 'Curso prático sobre proteção familiar, direitos e aplicação da Lei Maria da Penha.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Introdução à Regularização de Imóveis',
      title: 'REGULARIZAÇÃO DE IMÓVEIS',
      href: 'cursos/introducao-regularizacao-imoveis.html',
      duration: '60 horas',
      price: '169,00',
      description: 'Curso introdutório para entender processos e bases da regularização imobiliária.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'REURB na Prática (Legalização)',
      title: 'REURB NA PRÁTICA',
      href: 'cursos/reurb-na-pratica.html',
      duration: '60 horas',
      price: '179,00',
      description: 'Curso prático sobre legalização, regularização urbana e aplicação da REURB.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Biossegurança em Ressonância',
      title: 'BIOSSEGURANÇA EM RESSONÂNCIA',
      href: 'cursos/biosseguranca-ressonancia.html',
      duration: '40 horas',
      price: '139,00',
      description: 'Curso prático sobre cuidados, segurança e protocolos em ambientes de ressonância.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Anatomia Seccional (Leitura Básica)',
      title: 'ANATOMIA SECCIONAL',
      href: 'cursos/anatomia-seccional.html',
      duration: '50 horas',
      price: '149,00',
      description: 'Curso básico para leitura e compreensão de anatomia seccional aplicada.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Práticas de Inclusão e Direitos na Educação',
      title: 'PRÁTICAS DE INCLUSÃO',
      href: 'cursos/praticas-inclusao.html',
      duration: '60 horas',
      price: '129,00',
      description: 'Curso prático sobre inclusão, direitos e ações educativas mais acessíveis.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Ferramentas Digitais e Gamificação',
      title: 'FERRAMENTAS DIGITAIS',
      href: 'cursos/ferramentas-digitais.html',
      duration: '40 horas',
      price: '119,00',
      description: 'Curso prático para usar ferramentas digitais e gamificação em experiências de aprendizagem.'
    },
    {
      filter: 'extensao',
      badge: 'Extensão',
      course: 'Oratória e Comunicação Assertiva',
      title: 'ORATÓRIA E COMUNICAÇÃO',
      href: 'cursos/oratoria-comunicacao.html',
      duration: '40 horas',
      price: '129,00',
      description: 'Curso prático para melhorar fala, presença, clareza e comunicação assertiva.'
    }
  ];

  let activeFilter = 'all';
  let currentPage = 0;
  let autoplayTimer = null;
  let isAnimating = false;

  function getItemsPerPage() {
    if (window.innerWidth <= 768) return 1;
    if (window.innerWidth <= 1024) return 2;
    return 6;
  }

  function createWhatsAppHref(courseName) {
    const text = 'Olá, tenho interesse no curso de ' + courseName + ' da Faculdade Filos e gostaria de mais informações sobre matrícula, valores e início das aulas.';
    return 'https://wa.me/5561999061757?text=' + encodeURIComponent(text);
  }

  function createCourseCard(course) {
    const card = document.createElement('div');
    card.className = 'course-card-item';
    card.setAttribute('data-filter', course.filter);
    card.setAttribute('data-course', course.course);
    card.innerHTML =
      '<span class="course-card-item-badge">' + course.badge + '</span>' +
      '<div class="course-card-item-body">' +
        '<h3>' + course.title + '</h3>' +
        '<div class="course-card-item-meta">' +
          '<div class="meta-row"><strong>PERÍODO:</strong> Noturno</div>' +
          '<div class="meta-row"><strong>DURAÇÃO:</strong> ' + course.duration + '</div>' +
        '</div>' +
        '<p>' + course.description + '</p>' +
        '<div class="course-card-item-footer">' +
          '<a href="' + course.href + '" class="course-card-item-saiba">SAIBA MAIS &rarr;</a>' +
          '<div class="course-card-item-price">' + course.price + '</div>' +
        '</div>' +
      '</div>' +
      '<a href="' + createWhatsAppHref(course.course) + '" target="_blank" rel="noopener" class="course-card-item-matricula">' +
        '<i class="fa-brands fa-whatsapp"></i> MATRICULE-SE' +
      '</a>';
    return card;
  }

  // Build cards from the complete course catalog.
  function extractCards() {
    cardsData = homeCourses.map(function (course) {
      return {
        element: createCourseCard(course),
        filter: course.filter
      };
    });
    paginated.innerHTML = '';
  }

  function getFilteredCards() {
    if (activeFilter === 'all') return cardsData.map(c => c.element);
    return cardsData.filter(c => c.filter === activeFilter).map(c => c.element);
  }

  function buildPages() {
    if (cardsData.length === 0) return;
    const filtered = getFilteredCards();
    const itemsPerPage = getItemsPerPage();
    const totalPages = Math.max(1, Math.ceil(filtered.length / itemsPerPage));

    paginated.innerHTML = '';
    if (currentPage >= totalPages) currentPage = 0;

    for (let p = 0; p < totalPages; p++) {
      const page = document.createElement('div');
      const isActive = p === currentPage;
      page.className = 'courses-page' + (isActive ? ' active' : '');

      const start = p * itemsPerPage;
      const end = Math.min(start + itemsPerPage, filtered.length);
      for (let i = start; i < end; i++) {
        page.appendChild(filtered[i].cloneNode(true));
      }

      paginated.appendChild(page);
    }

    buildDots(totalPages);
  }

  function buildDots(count) {
    dotsContainer.innerHTML = '';
    for (let i = 0; i < count; i++) {
      const dot = document.createElement('button');
      dot.className = 'courses-pagination-dot' + (i === currentPage ? ' active' : '');
      dot.setAttribute('aria-label', 'Ir para página ' + (i + 1));
      dot.addEventListener('click', function () {
        goToPage(i);
        restartAutoplay();
      });
      dotsContainer.appendChild(dot);
    }
  }

  function goToPage(index) {
    if (isAnimating) return;
    const pages = paginated.querySelectorAll('.courses-page');
    const total = pages.length;
    if (total === 0) return;

    // Proper modulo for infinite loop (handles negative too)
    const targetIndex = ((index % total) + total) % total;
    if (targetIndex === currentPage) return;

    isAnimating = true;
    const oldPage = pages[currentPage];
    currentPage = targetIndex;
    const newPage = pages[currentPage];

    // Update dots immediately
    dotsContainer.querySelectorAll('.courses-pagination-dot')
      .forEach((d, i) => d.classList.toggle('active', i === currentPage));

    // CSS Grid Stacking handles the crossfade!
    oldPage.classList.remove('active');
    newPage.classList.add('active');

    setTimeout(function () {
      isAnimating = false;
    }, 450);
  }

  // Advance to next page, looping back to 0 after the last
  function nextPage() {
    if (isAnimating) return;
    const pages = paginated.querySelectorAll('.courses-page');
    if (pages.length <= 1) return;
    goToPage((currentPage + 1) % pages.length);
  }

  function startAutoplay() {
    stopAutoplay();
    autoplayTimer = setInterval(nextPage, 2500); // User requested 2.5 seconds
  }

  function stopAutoplay() {
    if (autoplayTimer) {
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
  }

  function restartAutoplay() {
    startAutoplay();
  }

  // Filter circle clicks
  filterCircles.forEach(function (circle) {
    circle.addEventListener('click', function () {
      if (isAnimating) return;
      var filter = circle.getAttribute('data-filter');
      if (filter === activeFilter) return;

      activeFilter = filter;
      filterCircles.forEach(function (c) {
        c.classList.toggle('active', c.getAttribute('data-filter') === filter);
      });

      isAnimating = true;
      var oldPages = paginated.querySelectorAll('.courses-page');
      oldPages.forEach(function (p) { p.classList.remove('active'); });

      setTimeout(function () {
        currentPage = 0;
        buildPages();
        restartAutoplay();
        isAnimating = false;
      }, 380);
    });
  });

  // Pause on hover / touch
  var section = document.getElementById('cursos');
  if (section) {
    section.addEventListener('mouseenter', stopAutoplay);
    section.addEventListener('mouseleave', startAutoplay);
    section.addEventListener('touchstart', stopAutoplay, { passive: true });
    section.addEventListener('touchend', startAutoplay, { passive: true });
  }

  // Rebuild on window resize (debounced)
  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      if (isAnimating) return;
      currentPage = 0;
      buildPages();
    }, 250);
  });

  // Init — guard against script loading before or after DOMContentLoaded
  function init() {
    extractCards();
    buildPages();
    startAutoplay();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
