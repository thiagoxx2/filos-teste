const fs = require('fs');

const cssContent = `/* responsive.css - Sistema de Responsividade Consistente (Mobile-First)
   Faculdade Filos
   ========================================================================== */

/* ==========================================================================
   1. VARIÁVEIS FLUIDAS E BASE DE SEGURANÇA (BASELINE MOBILE)
   Aplica-se a todas as telas por padrão (Mobile-First) e é aprimorado progressivamente.
   ========================================================================== */
:root {
  /* Tipografia Fluida (Mobile) */
  --h1-size: clamp(1.8rem, 6vw, 2.5rem);
  --h2-size: clamp(1.5rem, 5vw, 2.1rem);
  --h3-size: clamp(1.25rem, 4vw, 1.6rem);
  --h4-size: clamp(1.1rem, 3vw, 1.35rem);
  --h5-size: clamp(1rem, 2.5vw, 1.15rem);
  --h6-size: clamp(0.9rem, 2vw, 1rem);

  /* Espaçamentos e Gaps Fluidos (Mobile) */
  --page-gutter: clamp(16px, 4vw, 24px);
  --section-padding: clamp(3.5rem, 8vh, 4.5rem);
  --gap-sm: 0.75rem;
  --gap-md: 1rem;
  --gap-lg: 1.5rem;
  --gap-xl: 2rem;
}

/* Proteção global robusta contra overflow horizontal */
html, body {
  overflow-x: hidden;
  width: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}

/* Ajuste dos containers de layout para serem fluidos */
.container {
  width: min(100% - 2 * var(--page-gutter), var(--container));
  margin-inline: auto;
}

.container-wide {
  width: min(100% - 2 * var(--page-gutter), var(--container-wide));
  margin-inline: auto;
}

/* ==========================================================================
   2. ESTILOS BASE MOBILE (PADRÃO PARA LARGURA < 768px)
   Redefine o layout desktop nativo para um comportamento mobile limpo.
   ========================================================================== */

/* --- SITE HEADER MOBILE --- */
.header-nav {
  display: none !important; /* Esconde a linha do menu e botão coração no mobile */
}

.menu-toggle {
  display: flex !important; /* Mostra o botão hambúrguer */
}

.nav-menu {
  position: fixed;
  top: 0;
  right: 0;
  width: 100%;
  height: 100vh;
  background-color: var(--topbar-bg);
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  transform: translateX(100%);
  transition: transform var(--transition-normal);
  z-index: 110;
}

.nav-menu.active {
  transform: translateX(0);
}

.nav-link {
  font-size: 1.25rem;
  color: var(--text-white) !important; /* Garante visibilidade no fundo escuro do mobile */
  width: 100%;
  max-width: 280px;
  text-align: center;
  padding: 0.5rem 0;
  white-space: normal;
}

.nav-link:hover,
.nav-link.active {
  color: var(--cta-green) !important;
  font-weight: 800 !important;
}

.site-logo-img,
.logo-svg {
  height: clamp(52px, 12vw, 64px);
  width: auto;
}

.header-login {
  font-size: 0.9rem;
}

/* --- HERO CAROUSEL MOBILE --- */
.hero-carousel-container {
  padding-left: 0;
  padding-right: 0;
}

.hero-carousel-container::before,
.hero-carousel-container::after {
  display: none !important; /* Oculta blocos laterais flutuantes no mobile */
}

.hero-carousel--new {
  border-radius: 20px;
  overflow: visible;
}

.carousel-track-container {
  height: 540px !important; /* Altura fixa robusta para mobile */
}

.carousel-slide--new {
  display: flex !important;
  flex-direction: column-reverse;
  align-items: center;
  justify-content: center;
  padding: 2.5rem 1.5rem 6.5rem 1.5rem; /* Espaço para o botão e dots */
  gap: 1rem;
  text-align: center;
}

.slide-student-image {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 0.25rem;
}

.slide-student-image img {
  width: 130px;
  height: 150px;
  border-radius: 0;
  object-fit: cover;
  box-shadow: none;
}

.slide-content-new {
  align-items: center;
  text-align: center;
  max-width: 100%;
  gap: 0.35rem;
}

.slide-content-new h2 {
  font-size: clamp(1.3rem, 5.5vw, 1.7rem);
  line-height: 1.25;
  text-align: center;
}

.slide-content-new p {
  font-size: 0.85rem;
  text-align: center;
}

.slide-phi-logo {
  display: none !important; /* Oculta decoração de logo phi no mobile */
}

/* Botão Matricule-se e dots flutuantes no mobile (Centralizados, sem overlap) */
.btn-matricule-float {
  bottom: 2.75rem !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  padding: 0.75rem 1.5rem;
  font-size: 0.85rem;
  width: auto;
  white-space: nowrap;
  box-shadow: var(--shadow-lg);
  z-index: 10;
}

.carousel-indicators--new {
  bottom: 1.25rem !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  gap: 0.6rem;
  z-index: 10 !important;
}

.carousel-socials {
  display: none !important;
}

/* --- SEÇÃO DE CURSOS MOBILE (CARROSSEL COM 1 CARD) --- */
.courses-page {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  min-height: 410px;
}

.courses-paginated {
  min-height: 410px;
}

/* Cards menores, mais compactos e proporcionais */
.course-card-item {
  border-radius: 28px;
  padding: 1.75rem 1.5rem 3.5rem 1.5rem;
  width: 100%;
  box-shadow: var(--shadow-md);
}

.course-card-item-badge {
  font-size: 0.8rem;
  padding: 0.3rem 0.75rem;
  margin-bottom: 1.25rem;
}

.course-card-item-body {
  gap: 0.75rem;
}

.course-card-item-body h3 {
  font-size: 1.25rem;
  line-height: 1.15;
}

.course-card-item-meta {
  font-size: 1rem;
  gap: 0.25rem;
}

.course-card-item-body p {
  font-size: 1.05rem;
  line-height: 1.45;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.course-card-item-footer {
  flex-wrap: wrap;
  gap: 0.5rem;
  padding-top: 0.5rem;
}

.course-card-item-price {
  font-size: 1.75rem;
}

.course-card-item-saiba {
  font-size: 0.9rem;
}

.course-card-item-matricula {
  padding: 0.75rem 1.5rem;
  font-size: 0.9rem;
}

/* --- DEPOIMENTOS MOBILE (CARROSSEL INDIVIDUAL) --- */
.testimonials-track-container {
  overflow: hidden;
}

.testimonials-track.testimonials-marquee {
  animation: none !important; /* Desativa a animação de rolagem contínua */
  display: flex;
  gap: 0;
}

.testimonial-card {
  width: calc(100vw - 2 * var(--page-gutter) - 1rem);
  flex: 0 0 calc(100vw - 2 * var(--page-gutter) - 1rem);
  padding: 1.75rem 1.25rem 1.25rem 1.25rem;
  border-radius: 28px;
  gap: 0.75rem;
}

.testimonial-avatar {
  width: 48px;
  height: 48px;
}

.testimonial-name {
  font-size: 0.85rem;
}

.testimonial-course {
  font-size: 0.7rem;
}

.testimonial-user {
  margin-bottom: 0.75rem;
  gap: 0.5rem;
}

.testimonial-text {
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 0.75rem;
}

.testimonial-rating {
  font-size: 0.75rem;
  gap: 0.15rem;
.testimonials-indicators {
  display: flex !important;
  justify-content: center;
  margin-top: 1.5rem;
  gap: 0.5rem;
}

/* --- OUTRAS SEÇÕES MOBILE --- */
/* FAQ */
.faq-panel {
  padding: 2rem 1.25rem;
  border-radius: 32px;
  width: 100%;
  left: auto;
  transform: none;
}

.faq-panel-header {
  flex-direction: column;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 2rem;
}

.faq-logo {
  display: none !important;
}

.faq-grid {
  grid-template-columns: 1fr !important;
  gap: 0;
}

/* Destaques (Seção Faculdade Filos) */
.destaques-section {
  padding: 4.5rem 0 3rem 0;
}

.destaques-subtitle {
  font-size: 1.35rem;
}

.quote-mark-left {
  left: -0.25rem;
}

}

.quote-mark-right {
  right: -0.25rem;
/* Mini Galeria */
.gallery-grid {
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 0.75rem;
}

.mini-galeria-grid {
  grid-template-columns: 1fr !important;
  gap: 0;
}

.mini-galeria-item {
  aspect-ratio: 4/3;
  border-radius: 20px;
  width: 100%;
}

.mini-galeria-tabs {
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
}

.mini-galeria-tab {
  padding: 0.4rem 0.75rem;
  font-size: 0.8rem;
}

/* Localização */
.new-location-grid {
  grid-template-columns: 1fr !important;
.new-location-grid {
}

.new-location-map-container {
  height: 260px;
}

.location-floating-logo {
  display: none !important;
}

.new-location-address {
  margin-top: 1.5rem;
  padding-left: 0;
  flex-direction: column;
  gap: 0.75rem;
  text-align: center;
}

.new-location-address p {
  text-align: center;
}

/* Footer */
.new-footer {
  padding-top: 3rem;
}

.new-footer-grid {
  grid-template-columns: 1fr !important;
  gap: 2.5rem;
  text-align: center;
}

.new-footer-location {
  justify-content: center;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.new-footer-title {
  justify-content: center;
}

.new-footer-socials {
  justify-content: center;
}

.footer-legal-links {
.footer-legal-links {
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
}

/* Menu de cookies */
.cookies-banner {
  left: 10px;
  bottom: 10px;
  width: calc(100vw - 20px);
  padding: 1.25rem;
  border-radius: 16px;
}

.cookies-buttons-row {
  flex-direction: column;
  gap: 0.5rem;
}

.cookies-modal-content {
  padding: 1.5rem 1rem;
}

.cookies-preference-item {
  padding: 0.75rem;
  flex-direction: column;
  gap: 0.75rem;
}

.cookies-switch {
  align-self: flex-end;
}

/* Formulários */
.form-container,
.course-sidebar-card {
  padding: 2rem 1.25rem;
  border-radius: 28px;
}

/* Páginas Individuais de Cursos */
.course-hero {
  padding: 3rem 0;
  text-align: center;
}

.course-hero-container {
  grid-template-columns: 1fr !important;
  gap: 2rem;
}

.course-hero-content {
  align-items: center;
}

.course-hero-title {
  font-size: clamp(1.8rem, 6vw, 2.5rem);
  text-align: center;
}

.course-hero-meta {
  flex-direction: column;
  gap: 0.5rem;
  align-items: center;
}

.course-layout-container {
  grid-template-columns: 1fr !important;
  gap: 2rem;
}

.course-grade-grid {
  grid-template-columns: 1fr !important;
}

/* Ícones Flutuantes Mobile (WhatsApp e Voltar ao topo) */
.floating-sidebar-left {
  display: none !important; /* Oculta botões flutuantes secundários no mobile */
}

.floating-buttons {
  bottom: 1.25rem;
  right: 1.25rem;
  gap: 0.5rem;
}

.btn-float {
  width: 44px;
  height: 44px;
  font-size: 1.1rem;
}

.btn-float-whatsapp,
.btn-whatsapp {
  width: 50px;
  height: 50px;
  font-size: 1.35rem;
}
}

/* ==========================================================================
   3. PROGRESSIVE ENHANCEMENT: MOBILE GRANDE (min-width: 480px)
   ========================================================================== */
@media (min-width: 480px) {
  :root {
    --page-gutter: 24px;
  }
  
  .carousel-slide--new {
    padding-bottom: 6rem;
  }
  
  .course-card-item {
    padding: 2.25rem 2rem 3.75rem 2rem;
  }
  
  .course-card-item-body h3 {
    font-size: 1.35rem;
  }

  .testimonial-card {
    width: calc(100vw - 2 * var(--page-gutter) - 2rem);
    flex: 0 0 calc(100vw - 2 * var(--page-gutter) - 2rem);
    padding: 2rem 1.5rem;
  }
  
  .new-location-map-container {
    height: 300px;
  }
  .floating-sidebar-left {
    left: 0.25rem;
    gap: 0.3rem;
  }
}

/* ==========================================================================
   BREAKPOINT 360px — CELULAR PEQUENO
   ========================================================================== */
@media (max-width: 360px) {
  .hero-carousel--new .carousel-track-container {
    min-height: 400px;
  }

  /* --- HEADER DESKTOP --- */
  .site-logo-img,
  .logo-svg {
    height: clamp(80px, 6vw, 100px) !important; /* Logo grande e marcante como na referência */
  }

  .header-nav-wrapper {
    background-color: var(--header-bar-bg) !important;
  }

  .header-nav {
    display: grid !important;
    padding: 1rem 0 0 !important; /* Alinha a aba à base */
  }

  .menu-toggle {
    display: none !important;
  }

  .nav-menu {
    position: static;
    width: auto;
    height: auto;
    background-color: transparent;
    flex-direction: row;
    transform: none;
    gap: var(--header-nav-gap);
    z-index: auto;
    align-items: flex-end !important; /* Alinha os itens na base */
  }

  .nav-link {
    font-size: clamp(1rem, 1.25vw, 1.2rem) !important;
    color: var(--gray-blue) !important;
    font-weight: 500 !important;
    width: auto;
    max-width: none;
    text-align: left;
    padding: 0.6rem 1.25rem !important;
    background-color: transparent !important;
    transition: all var(--transition-fast) !important;
  }

  .nav-link:hover {
    color: var(--primary-dark) !important;
  }

  .nav-link.active {
    color: var(--primary-dark) !important;
    font-weight: 800 !important;
    background-color: transparent !important;
    box-shadow: none !important;
  }

  /* --- HERO CAROUSEL TABLET --- */
  .carousel-track-container {
    height: 660px !important; /* Altura do banner aumentada */
  }

  .carousel-slide--new {
    display: grid !important;
    grid-template-columns: 1.2fr 0.8fr;
    padding: 3rem;
    gap: 2rem;
    text-align: left;
    align-items: center;
    max-width: var(--container); /* Conteúdo agrupado no centro */
    margin-inline: auto;
    width: 100%;
  }

  .slide-student-image {
    justify-content: flex-end;
    margin-bottom: 0;
  }

  }

  .slide-student-image img {
    width: 250px;
    height: 290px;
  }

  .slide-content-new {
    align-items: flex-start;
    bottom: 2.5rem !important;
    left: 3rem !important;
    transform: none !important;
    padding: 0.9rem 1.8rem;
    font-size: 0.95rem;
  }

  .carousel-indicators--new {
    bottom: 2.25rem !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
  }

  /* --- SEÇÃO DE CURSOS TABLET (2 COLUNAS) --- */
  .courses-page {
    grid-template-columns: repeat(2, 1fr) !important;
    row-gap: 4rem;
    column-gap: 1.5rem;
    min-height: auto;
  }

  .courses-paginated {
    min-height: auto;
  }

  /* --- DEPOIMENTOS TABLET (RESTAURA MARQUEE) --- */
  .testimonials-track.testimonials-marquee {
    animation: marquee 25s linear infinite !important;
  }

  .testimonial-card {
    column-gap: 1.5rem;
    min-height: auto;
  }

  }

  .courses-paginated {
    min-height: auto;
  }

    animation: marquee 25s linear infinite !important;
  }

  .testimonial-card {
    width: 640px;
    flex: 0 0 640px;
    padding: 4rem 3.5rem;
    min-height: 360px;
  }

  .testimonial-card .testimonial-name {
    font-size: 1.15rem;
  }

  .testimonial-card .testimonial-course {
    font-size: 0.9rem;
  }

  .testimonial-card .testimonial-text {
    line-height: 1.65;
  }

  .testimonial-card .testimonial-avatar {
    width: 72px;
    height: 72px;
  }

  .testimonials-indicators {
    display: none !important;
  }

  /* --- FAQ TABLET --- */
  .faq-panel {
    padding: 3.5rem 3rem;
  }

  .faq-panel-header {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3rem;
  }

  .faq-logo {
    display: flex !important;
  }

  .faq-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 1.5rem 3rem;
  }

  /* --- MINI GALERIA TABLET --- */
  .mini-galeria-title {
    font-size: clamp(2.5rem, 4.5vw, 3.5rem) !important;
    margin-bottom: 2.5rem !important;
  }

  .mini-galeria-tabs {
    gap: 3.5rem !important;
    margin-bottom: 3.5rem !important;
  }

  .mini-galeria-tab {
    font-size: clamp(1.2rem, 1.6vw, 1.5rem) !important;
    padding: 0.75rem 0 !important;
  }

  .mini-galeria-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
  }

  .mini-galeria-item {
    aspect-ratio: 2/1 !important;
    border-radius: 12px !important;
  }

  /* --- LOCALIZAÇÃO TABLET --- */
  .new-location-grid {
    grid-template-columns: 1.1fr 0.9fr !important;
    gap: 3rem;
  }

  .new-location-map-container {
    height: 380px;
  }

  .new-location-address {
    flex-direction: row;
    text-align: left;
    gap: 1.5rem;
  }

  /* --- FOOTER TABLET --- */
  .new-footer-grid {
    grid-template-columns: 1.2fr 1fr 1fr !important;
    gap: 2.5rem;
    text-align: left;
  }

  .new-footer-location {
    justify-content: flex-start;
    align-items: flex-start;
  }

  .new-footer-title,
  .new-footer-socials {
    justify-content: flex-start;
  }

  .new-footer-socials {
    justify-content: flex-start;
  }

  .footer-legal-links {
    justify-content: flex-end;
  }

  /* Destaques */
  .destaques-section {
    padding: 7rem 0 6rem 0 !important;
  }

  /* --- FLOATING CONTROLS --- */
  .floating-sidebar-left {
    display: flex !important;
  }

  /* --- PÁGINA INDIVIDUAL CURSO --- */
  .course-hero {
    text-align: left;
  }

  .course-hero-container {
    grid-template-columns: 1.2fr 0.8fr !important;


  .course-hero-content {
    align-items: flex-start;
  }

  .course-hero-meta {
    flex-direction: row;
    gap: 1.5rem;
  }

  .course-layout-container {
    grid-template-columns: 1.2fr 0.8fr !importa
  }

  /* --- SITE HEADER DESKTOP --- */
  .site-logo-img {
    height: 80px !important; /* Proporção ampliada para telas maiores */
  }

  .nav-link {
    font-size: clamp(1.2rem, 1.5vw, 1.5rem) !important;
  }

  .header-login {
    font-size: clamp(1.1rem, 1.35vw, 1.35rem) !important;
  }

  /* --- HERO CAROUSEL DESKTOP --- */
  .hero-carousel-container {
    padding-left: max(var(--page-gutter), calc(50vw - var(--container-wide-half)));
    padding-right: max(var(--page-gutter), calc(50vw - var(--container-wide-half)));
  }
    width: clamp(64px, 6.5vw, 96px) !important;
    height: clamp(64px, 6.5vw, 96px) !important;
    font-size: clamp(1.8rem, 2.8vw, 3.2rem) !important;
  }

  .floating-side-btn {
    width: clamp(56px, 5.5vw, 84px) !important;
    height: clamp(56px, 5.5vw, 84px) !important;
    font-size: clamp(1.4rem, 2.2vw, 2.3rem) !important;
  }
}

/* ==========================================================================
   5. PROGRESSIVE ENHANCEMENT: NOTEBOOKS / DESKTOP COMUM (min-width: 1024px)
   ========================================================================== */
@media (min-width: 1024px) {
  :root {
    --page-gutter: clamp(24px, 4vw, 48px);
    --section-padding: clamp(5rem, 7vh, 8rem);
    
    /* Fontes do Desktop */
    --h1-size: clamp(3rem, 6vw, 5.2rem);
    --h2-size: clamp(2.4rem, 5vw, 4.2rem);
    --h3-size: clamp(2rem, 4vw, 3rem);
  }

  html, body {
    font-size: 1.09375rem; /* ~17.5px */
  }

  /* --- SITE HEADER DESKTOP --- */
  .site-logo-img {
    height: 80px !important; /* Proporção ampliada para telas maiores */
  }

  .nav-link {
    font-size: clamp(1.2rem, 1.5vw, 1.5rem) !important;
  }

  .header-login {
    font-size: clamp(1.1rem, 1.35vw, 1.35rem) !important;
    margin-right: 2.5rem !important;
  }

  /* --- HERO CAROUSEL DESKTOP --- */
  .hero-carousel-container {
    padding-left: var(--hero-side-width);
    padding-right: var(--hero-side-width);
  }

  .hero-carousel-container::before,
  .hero-carousel-container::after {
    display: block !important;
  }

  .hero-carousel-container::before {
    left: 0;
    width: calc(var(--hero-side-width) - var(--gap-sm));
  }

  .hero-carousel-container::after {
    right: 0;
    width: calc(var(--hero-side-width) - var(--gap-sm));
  }

  .carousel-track-container {
    height: 880px !important; /* Altura generosa no notebook */
  }

  .carousel-slide--new {
    padding: 3.5rem 6rem 3.5rem 5rem !important; /* Ajustado para as proporções exatas do print (5rem left, 6rem right) */
    gap: 3.5rem;
    max-width: var(--container); /* Alinha conteúdo central com as seções da página */
    margin-inline: auto;
    width: 100%;
  }

  .slide-student-image {
    position: relative !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    justify-self: end !important;
  }

  .slide-student-image img {
    width: auto !important;
    height: clamp(560px, 42vw, 680px) !important; /* Altura ampliada proporcionalmente */
    aspect-ratio: 1 / 1.15 !important;
    object-fit: cover !important;
    border-radius: 0 !important;
    border: none !important;
    box-shadow: none !important;
  }

  .slide-phi-logo {
    display: block !important;
    font-size: 8.5rem !important;
    font-family: 'Times New Roman', Georgia, serif !important;
    font-weight: 400 !important;
    top: 1.5rem !important;
    right: 1.5rem !important;
  }

  /* Alinhamento dinâmico e fluido do botão Matricule-se (flui naturalmente no desktop) */
  .btn-matricule-slide {
    padding: 1.1rem 2.25rem;
    font-size: 1.05rem;
  }

  .carousel-indicators--new {
  .course-card-item-price {
    font-size: clamp(2.2rem, 4vw, 4rem) !important;
  }

  .course-card-item-matricula {
    padding: 1rem 2.25rem !important;
    font-size: 1.15rem !important;
  }

  /* FAQ */
  .faq-panel {
    padding: 6.5rem 7.5rem !important;
  }

  /* Localização */
  .new-location-grid {
    grid-template-columns: 1.2fr 0.8fr !important;
    gap: 4rem;
  }

  .new-location-map-container {
    height: 420px;
  }

  /* Footer */
  .new-footer-grid {
    grid-template-columns: 1.5fr 1fr 1fr !important;
    gap: 4rem;
  }
}
  /* FAQ */
  .faq-panel {
    padding: 6.5rem 7.5rem !important;
  }

  /* Localização */
  .new-location-grid {
    grid-template-columns: 1.2fr 0.8fr !important;
    gap: 4rem;
  }

  .new-location-map-container {
    height: 480px !important;
  }

  /* Footer */
  .new-footer-grid {
    grid-template-columns: 1.5fr 1fr 1fr !important;
    gap: 4rem;
  }
}

@media (min-width: 1600px) {
  .carousel-track-container {
    height: 1080px !important; /* Altura para monitores 1600px */
  }

  .slide-student-image img {
    height: clamp(720px, 42vw, 840px) !important;
  :root {
    --page-gutter: clamp(32px, 4vw, 80px);
  }

  html, body {
    font-size: 1.15625rem; /* ~18.5px */
  }

  .site-logo-img {
    height: 90px !important;
  }

  .nav-link {
    font-size: clamp(1.25rem, 1.6vw, 1.6rem) !important;
  }

  .header-login {
    font-size: clamp(1.15rem, 1.4vw, 1.4rem) !important;
  }

  .carousel-track-container {
    height: 1000px !important; /* Altura premium para monitores 1440px */
  }

  .slide-student-image img {
    height: clamp(660px, 42vw, 780px) !important; /* Altura proporcional */
  }

  .carousel-indicators--new {
    bottom: 1.75rem !important;
    left: 50% !important;
  }
  
  .course-card-item {
    padding: 2.75rem 2.25rem 4rem 2.25rem;
  }
}

@media (min-width: 1600px) {
  .carousel-track-container {

@media (min-width: 1600px) {
  .carousel-track-container {
    height: 1080px !important; /* Altura para monitores 1600px */
  }

  .slide-student-image img {
    height: clamp(720px, 42vw, 840px) !important;
  }

  .carousel-indicators--new {
    bottom: 1.75rem !important;
    left: 50% !important;
    right: auto !important;
    transform: translateX(-50%) !important;
    z-index: 10 !important;
  }
}

@media (min-width: 1920px) {
@media (min-width: 1920px) {
  .carousel-track-container {
    height: 1160px !important; /* Altura monumental para telas Full HD 1920px+ */
  }

  .site-logo-img {
    height: 100px !important;
  }

  .nav-link {
    font-size: clamp(1.3rem, 1.7vw, 1.7rem) !important;
  }

  .header-login {
    font-size: clamp(1.2rem, 1.5vw, 1.5rem) !important;
  }

  .slide-student-image img {
    height: clamp(780px, 42vw, 900px) !important;
  }

  .carousel-indicators--new {
    bottom: 1.75rem !important;
    left: 50% !important;
    right: auto !important;
    transform: translateX(-50%) !important;
    z-index: 10 !important;
  }
}

@media (max-width: 900px) {
  .faq-item.stretch {
    grid-column: auto !important;
  }
}
`;

fs.writeFileSync('./css/responsive.css', cssContent);
console.log('responsive.css updated successfully.');
