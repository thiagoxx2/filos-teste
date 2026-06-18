const courses = [
    {
        "slug": "tecnicas-vendas",
        "name": "TÉCNICAS DE VENDAS E NEGOCIAÇÃO",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Técnicas De Vendas E Negociação e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "tecnicas-vendas.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "lei-maria-da-penha",
        "name": "LEI MARIA DA PENHA E PROTEÇÃO À FAMÍLIA",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Lei Maria Da Penha E Proteção À Família e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "lei-maria-da-penha.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "introducao-regularizacao-imoveis",
        "name": "INTRODUÇÃO À REGULARIZAÇÃO DE IMÓVEIS",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Introdução À Regularização De Imóveis e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "introducao-regularizacao-imoveis.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "nocoes-direito-penal",
        "name": "NOÇÕES DE DIREITO PENAL E SEGURANÇA CIDADÃ",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Noções De Direito Penal E Segurança Cidadã e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "nocoes-direito-penal.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "anatomia-seccional",
        "name": "ANATOMIA SECCIONAL (LEITURA BÁSICA)",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Anatomia Seccional (Leitura Básica) e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "anatomia-seccional.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "administracao",
        "name": "ADMINISTRAÇÃO",
        "badge": "Bacharelado",
        "periodo": "Noturno",
        "duracao": "5 anos",
        "description": "Desenvolva competências em gestão, liderança, finanças, marketing e tomada de decisões estratégicas.",
        "price": "299,90",
        "url": "administracao.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "docencia-ensino-superior",
        "name": "DOCÊNCIA NO ENSINO SUPERIOR",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Docência No Ensino Superior e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "docencia-ensino-superior.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "dominio-ias",
        "name": "DOMÍNIO DAS I.AS: CRIAÇÃO DE TEXTOS E IMAGENS",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Domínio Das I.As: Criação De Textos E Imagens e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "dominio-ias.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "controle-qualidade-imagem",
        "name": "CONTROLE DE QUALIDADE DE IMAGEM E ARTEFATOS MÉDICOS",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Controle De Qualidade De Imagem E Artefatos Médicos e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "controle-qualidade-imagem.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "reurb-na-pratica",
        "name": "REURB NA PRÁTICA (LEGALIZAÇÃO)",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Reurb Na Prática (Legalização) e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "reurb-na-pratica.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "ressonancia-magnetica",
        "name": "RESSONÂNCIA MAGNÉTICA",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Ressonância Magnética e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "ressonancia-magnetica.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "direito",
        "name": "DIREITO",
        "badge": "Bacharelado",
        "periodo": "Noturno",
        "duracao": "5 anos",
        "description": "Formação jurídica voltada para atuação profissional, preparação para a OAB e desenvolvimento de análise crítica.",
        "price": "299,90",
        "url": "direito.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "neuropsicopedagogia",
        "name": "NEUROPSICOPEDAGOGIA",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Neuropsicopedagogia e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "neuropsicopedagogia.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "direito-penal",
        "name": "DIREITO PENAL E PROCESSO PENAL",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Aprofunde seus conhecimentos em legislação penal, prática criminal, jurisprudência e estratégias de atuação jurídica.",
        "price": "299,90",
        "url": "direito-penal.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "automacao-pratica",
        "name": "AUTOMAÇÃO PRÁTICA SEM PROGRAMAÇÃO",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Automação Prática Sem Programação e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "automacao-pratica.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "praticas-inclusao",
        "name": "PRÁTICAS DE INCLUSÃO E DIREITOS NA EDUCAÇÃO",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Práticas De Inclusão E Direitos Na Educação e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "praticas-inclusao.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "inteligencia-artificial",
        "name": "INTELIGÊNCIA ARTIFICIAL APLICADA AOS NEGÓCIOS",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Inteligência Artificial Aplicada Aos Negócios e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "inteligencia-artificial.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "pedagogia",
        "name": "PEDAGOGIA",
        "badge": "Licenciatura",
        "periodo": "Noturno",
        "duracao": "4 anos",
        "description": "Formação para atuação na educação, alfabetização, gestão escolar e práticas pedagógicas inclusivas.",
        "price": "299,90",
        "url": "pedagogia.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "gestao-de-operacoes",
        "name": "GESTÃO DE OPERAÇÕES 4.0",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Gestão De Operações 4.0 e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "gestao-de-operacoes.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "vendas-digitais",
        "name": "VENDAS DIGITAIS (REDES SOCIAIS E WHATSAPP)",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Vendas Digitais (Redes Sociais E Whatsapp) e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "vendas-digitais.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "radiologia",
        "name": "RADIOLOGIA",
        "badge": "Tecnólogo",
        "periodo": "Noturno",
        "duracao": "3 anos",
        "description": "Formação voltada para diagnóstico por imagem, tecnologias da saúde e atuação em ambientes clínicos.",
        "price": "299,90",
        "url": "radiologia.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "biosseguranca-ressonancia",
        "name": "BIOSSEGURANÇA EM RESSONÂNCIA",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Biossegurança Em Ressonância e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "biosseguranca-ressonancia.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "direito-imobiliario",
        "name": "DIREITO IMOBILIÁRIO",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Formação voltada para contratos, regularização de imóveis, operações imobiliárias e consultoria jurídica no setor.",
        "price": "299,90",
        "url": "direito-imobiliario.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "oratoria-comunicacao",
        "name": "ORATÓRIA E COMUNICAÇÃO ASSERTIVA",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Oratória E Comunicação Assertiva e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "oratoria-comunicacao.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "excelencia-atendimento",
        "name": "EXCELÊNCIA NO ATENDIMENTO E FIDELIZAÇÃO",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Excelência No Atendimento E Fidelização e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "excelencia-atendimento.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "ferramentas-digitais",
        "name": "FERRAMENTAS DIGITAIS E GAMIFICAÇÃO",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Especialize-se em Ferramentas Digitais E Gamificação e destaque-se no mercado de trabalho com uma formação focada e prática.",
        "price": "299,90",
        "url": "ferramentas-digitais.html",
        "whatsapp": "https://wa.me/5561999061757"
    },
    {
        "slug": "direito-digital",
        "name": "DIREITO DIGITAL",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Conheça os principais fundamentos do Direito Digital, proteção de dados, LGPD e relações jurídicas no ambiente online.",
        "price": "299,90",
        "url": "#contato",
        "whatsapp": "https://wa.me/5561999061757?text=Ol%C3%A1%2C%20tenho%20interesse%20no%20curso%20de%20Direito%20Digital."
    },
    {
        "slug": "gestao-de-pessoas",
        "name": "GESTÃO DE PESSOAS",
        "badge": "Pós-Graduação",
        "periodo": "Noturno",
        "duracao": "6 meses",
        "description": "Desenvolva competências para liderança, desenvolvimento de equipes, comunicação e gestão estratégica de pessoas.",
        "price": "299,90",
        "url": "#contato",
        "whatsapp": "https://wa.me/5561999061757?text=Ol%C3%A1%2C%20tenho%20interesse%20no%20curso%20de%20Gest%C3%A3o%20de%20Pessoas."
    }
];


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
          <div class="courses-pagination-dots" id="related-courses-dots" style="display: flex; justify-content: center; gap: 0.75rem; margin-top: 7.3rem;">
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
