const pricedCourseSlugs = new Set([
  'direito',
  'pedagogia',
  'administracao',
  'radiologia'
]);

const courses = [
    {
        "slug": "tecnicas-vendas",
        "name": "TÉCNICAS DE VENDAS E NEGOCIAÇÃO",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Técnicas De Vendas E Negociação e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "tecnicas-vendas.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "lei-maria-da-penha",
        "name": "LEI MARIA DA PENHA E PROTEÇÃO À FAMÍLIA",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Lei Maria Da Penha E Proteção À Família e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "lei-maria-da-penha.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "introducao-regularizacao-imoveis",
        "name": "INTRODUÇÃO À REGULARIZAÇÃO DE IMÓVEIS",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Introdução À Regularização De Imóveis e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "introducao-regularizacao-imoveis.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "nocoes-direito-penal",
        "name": "NOÇÕES DE DIREITO PENAL E SEGURANÇA CIDADÃ",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Noções De Direito Penal E Segurança Cidadã e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "nocoes-direito-penal.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "anatomia-seccional",
        "name": "ANATOMIA SECCIONAL (LEITURA BÁSICA)",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Anatomia Seccional (Leitura Básica) e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "anatomia-seccional.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "administracao",
        "name": "ADMINISTRAÇÃO",
        "badge": "Graduação",
        "periodo": "Noturno",
        "duracao": "5 anos",
        "description": "Desenvolva competências em gestão, liderança, finanças, marketing e tomada de decisões estratégicas.",
        "price": "535,00",
        "url": "administracao.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": "1.188,89"
    },
    {
        "slug": "docencia-ensino-superior",
        "name": "DOCÊNCIA NO ENSINO SUPERIOR",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Docência No Ensino Superior e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "docencia-ensino-superior.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "dominio-ias",
        "name": "DOMÍNIO DAS I.AS: CRIAÇÃO DE TEXTOS E IMAGENS",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Domínio Das I.As: Criação De Textos E Imagens e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "dominio-ias.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "controle-qualidade-imagem",
        "name": "CONTROLE DE QUALIDADE DE IMAGEM E ARTEFATOS MÉDICOS",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Controle De Qualidade De Imagem E Artefatos Médicos e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "controle-qualidade-imagem.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "reurb-na-pratica",
        "name": "REURB NA PRÁTICA (LEGALIZAÇÃO)",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Reurb Na Prática (Legalização) e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "reurb-na-pratica.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "ressonancia-magnetica",
        "name": "RESSONÂNCIA MAGNÉTICA",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Ressonância Magnética e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "ressonancia-magnetica.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "direito",
        "name": "DIREITO",
        "badge": "Graduação",
        "periodo": "Noturno",
        "duracao": "5 anos",
        "description": "Formação jurídica voltada para atuação profissional, preparação para a OAB e desenvolvimento de análise crítica.",
        "price": "698,96",
        "url": "direito.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": "2.184,25"
    },
    {
        "slug": "neuropsicopedagogia",
        "name": "NEUROPSICOPEDAGOGIA",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Neuropsicopedagogia e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "neuropsicopedagogia.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "direito-penal",
        "name": "DIREITO PENAL E PROCESSO PENAL",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Aprofunde seus conhecimentos em legislação penal, prática criminal, jurisprudência e estratégias de atuação jurídica.",
        "price": null,
        "url": "direito-penal.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "automacao-pratica",
        "name": "AUTOMAÇÃO PRÁTICA SEM PROGRAMAÇÃO",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Automação Prática Sem Programação e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "automacao-pratica.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "praticas-inclusao",
        "name": "PRÁTICAS DE INCLUSÃO E DIREITOS NA EDUCAÇÃO",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Práticas De Inclusão E Direitos Na Educação e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "praticas-inclusao.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "inteligencia-artificial",
        "name": "INTELIGÊNCIA ARTIFICIAL APLICADA AOS NEGÓCIOS",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Inteligência Artificial Aplicada Aos Negócios e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "inteligencia-artificial.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "pedagogia",
        "name": "PEDAGOGIA",
        "badge": "Licenciatura",
        "periodo": "Noturno",
        "duracao": "4 anos",
        "description": "Formação para atuação na educação, alfabetização, gestão escolar e práticas pedagógicas inclusivas.",
        "price": "475,55",
        "url": "pedagogia.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": "951,11"
    },
    {
        "slug": "gestao-de-operacoes",
        "name": "GESTÃO DE OPERAÇÕES 4.0",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Gestão De Operações 4.0 e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "gestao-de-operacoes.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "vendas-digitais",
        "name": "VENDAS DIGITAIS (REDES SOCIAIS E WHATSAPP)",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Vendas Digitais (Redes Sociais E Whatsapp) e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "vendas-digitais.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "radiologia",
        "name": "RADIOLOGIA",
        "badge": "Tecnólogo",
        "periodo": "Noturno",
        "duracao": "3 anos",
        "description": "Formação voltada para diagnóstico por imagem, tecnologias da saúde e atuação em ambientes clínicos.",
        "price": "609,65",
        "url": "radiologia.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": "1.354,78"
    },
    {
        "slug": "biosseguranca-ressonancia",
        "name": "BIOSSEGURANÇA EM RESSONÂNCIA",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Biossegurança Em Ressonância e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "biosseguranca-ressonancia.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "direito-imobiliario",
        "name": "DIREITO IMOBILIÁRIO",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Formação voltada para contratos, regularização de imóveis, operações imobiliárias e consultoria jurídica no setor.",
        "price": null,
        "url": "direito-imobiliario.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "oratoria-comunicacao",
        "name": "ORATÓRIA E COMUNICAÇÃO ASSERTIVA",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Oratória E Comunicação Assertiva e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "oratoria-comunicacao.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "excelencia-atendimento",
        "name": "EXCELÊNCIA NO ATENDIMENTO E FIDELIZAÇÃO",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Excelência No Atendimento E Fidelização e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "excelencia-atendimento.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "ferramentas-digitais",
        "name": "FERRAMENTAS DIGITAIS E GAMIFICAÇÃO",
        "badge": "Extensão",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Ferramentas Digitais E Gamificação e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": null,
        "url": "ferramentas-digitais.html",
        "whatsapp": "https://wa.me/5561999061757",
        "oldPrice": null
    },
    {
        "slug": "direito-digital",
        "name": "DIREITO DIGITAL",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Conheça os principais fundamentos do Direito Digital, proteção de dados, LGPD e relações jurídicas no ambiente online.",
        "price": null,
        "url": "#contato",
        "whatsapp": "https://wa.me/5561999061757?text=Ol%C3%A1%2C%20tenho%20interesse%20no%20curso%20de%20Direito%20Digital.",
        "oldPrice": null
    },
    {
        "slug": "gestao-de-pessoas",
        "name": "GESTÃO DE PESSOAS",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Desenvolva competências para liderança, desenvolvimento de equipes, comunicação e gestão estratégica de pessoas.",
        "price": null,
        "url": "#contato",
        "whatsapp": "https://wa.me/5561999061757?text=Ol%C3%A1%2C%20tenho%20interesse%20no%20curso%20de%20Gest%C3%A3o%20de%20Pessoas.",
        "oldPrice": null
    }
];

document.addEventListener('DOMContentLoaded', () => {
    const placeholder = document.querySelector('.related-courses-placeholder');
    if (!placeholder) return;

    const currentCourse = placeholder.getAttribute('data-current-course');

    const filteredCourses = courses.filter(c => c.slug !== currentCourse);
    if (filteredCourses.length === 0) return;

    // Embaralhar
    const shuffled = [...filteredCourses].sort(() => 0.5 - Math.random());
    const selectedCourses = shuffled;

        const normalizeCategory = (badge) => {
  const normalized = badge.toLowerCase();

  if (normalized === 'graduação') return 'graduacao';
  if (normalized === 'pós-graduação') return 'pos-graduacao';
  if (normalized === 'tecnólogo') return 'graduacao';
  if (normalized === 'licenciatura') return 'graduacao';
  if (normalized === 'extensão') return 'extensao';

  return normalized;
};

const createPriceBlock = (c) => {
  const hasPrice = pricedCourseSlugs.has(c.slug) && c.price && c.oldPrice;

  if (!hasPrice) return '';

  return `
    <div class="course-card-price-display">
      <p class="course-card-price-from">
        De <span class="course-card-price-old">R$ ${c.oldPrice}</span>
      </p>

      <p class="course-card-price-current-label">
        mensalidades a partir de
      </p>

      <p class="course-card-price-current">
        <span class="course-card-price-currency">R$</span>
        <strong>${c.price}</strong>
        <span class="course-card-price-asterisk">*</span>
      </p>

      <p class="course-card-price-note">
        *Valor final mediante descontos aplicáveis.
      </p>
    </div>
  `;
};

    const createCourseCard = (c) => `
  <div class="course-card-item courses-carousel-item" data-filter="${normalizeCategory(c.badge)}" data-course="${c.name}">
    <span class="course-card-item-badge">${c.badge}</span>

    <div class="course-card-item-body">
      <h3>${c.name}</h3>

      <div class="course-card-item-meta">
        <div class="meta-row"><strong>PERÍODO:</strong> ${c.periodo}</div>
        <div class="meta-row"><strong>DURAÇÃO:</strong> ${c.duracao}</div>
      </div>

      <p>${c.description}</p>

      ${createPriceBlock(c)}

      <div class="course-card-item-footer">
        <a href="${c.url}" class="course-card-item-saiba">SAIBA MAIS &rarr;</a>
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
