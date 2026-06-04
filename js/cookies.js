/**
 * cookies.js - LGPD Consent management and Dynamic Script Loading
 * Faculdade Filos
 */

(function () {
  'use strict';

  // Constants
  const STORAGE_KEY = 'filos_cookie_consent';
  
  // State
  let consent = {
    necessary: true,
    statistics: false,
    marketing: false
  };

  // DOM Elements
  let bannerEl = null;
  let modalEl = null;

  // Initialize
  function init() {
    // 1. Check if consent already exists in localStorage
    const storedConsent = localStorage.getItem(STORAGE_KEY);
    
    if (storedConsent) {
      try {
        consent = JSON.parse(storedConsent);
        // Force necessary to be true
        consent.necessary = true;
        // Apply tags based on loaded consent
        applyConsent();
      } catch (e) {
        console.error("Error parsing cookie consent, resetting...", e);
        showBanner();
      }
    } else {
      // No consent yet, show banner after a short delay
      setTimeout(showBanner, 1000);
    }

    // 2. Setup event delegation for consent buttons (works even if DOM is not fully parsed yet, but we bind on DOMContentLoaded)
    document.addEventListener('DOMContentLoaded', () => {
      buildBannerAndModal();
      setupEventListeners();
    });
  }

  // Show Banner
  function showBanner() {
    if (bannerEl) {
      bannerEl.classList.add('show');
    } else {
      // Retry when DOM loads
      document.addEventListener('DOMContentLoaded', () => {
        if (bannerEl) bannerEl.classList.add('show');
      });
    }
  }

  // Hide Banner
  function hideBanner() {
    if (bannerEl) {
      bannerEl.classList.remove('show');
    }
  }

  // Show Modal
  function showModal() {
    if (modalEl) {
      // Sync checkboxes with current consent state
      document.getElementById('cookie-pref-statistics').checked = consent.statistics;
      document.getElementById('cookie-pref-marketing').checked = consent.marketing;
      modalEl.classList.add('active');
    }
  }

  // Hide Modal
  function hideModal() {
    if (modalEl) {
      modalEl.classList.remove('active');
    }
  }

  // Save Consent and apply
  function saveConsent(newConsent) {
    consent = {
      necessary: true,
      statistics: !!newConsent.statistics,
      marketing: !!newConsent.marketing
    };
    
    localStorage.setItem(STORAGE_KEY, JSON.stringify(consent));
    applyConsent();
    hideBanner();
    hideModal();
  }

  // Apply scripts dynamically based on consent
  function applyConsent() {
    // Dispatch custom event for other scripts to know consent changed
    const event = new CustomEvent('cookieConsentChanged', { detail: consent });
    document.dispatchEvent(event);

    // Google Tag Manager / Analytics Consent Mode integration if available
    if (window.gtag) {
      window.gtag('consent', 'update', {
        'analytics_storage': consent.statistics ? 'granted' : 'denied',
        'ad_storage': consent.marketing ? 'granted' : 'denied',
        'ad_user_data': consent.marketing ? 'granted' : 'denied',
        'ad_personalization': consent.marketing ? 'granted' : 'denied'
      });
    }

    // Load dynamic scripts based on consent
    if (consent.statistics) {
      loadStatisticsScripts();
    }
    
    if (consent.marketing) {
      loadMarketingScripts();
    }
  }

  // Dynamic loaders
  function loadScript(src, id) {
    if (document.getElementById(id)) return; // Already loaded
    
    const script = document.createElement('script');
    script.src = src;
    script.id = id;
    script.async = true;
    document.head.appendChild(script);
  }

  function loadStatisticsScripts() {
    console.log("LGPD: Loading statistics scripts (Google Analytics)...");
    // Example: Google Analytics 4 (replace with client's actual ID when ready)
    // For now we use placeholders that won't leak but demonstrate working loading
    // loadScript('https://www.googletagmanager.com/gtag/js?id=G-PLACEHOLDER', 'gtag-script');
    
    // window.dataLayer = window.dataLayer || [];
    // function gtag(){dataLayer.push(arguments);}
    // gtag('js', new Date());
    // gtag('config', 'G-PLACEHOLDER');
  }

  function loadMarketingScripts() {
    console.log("LGPD: Loading marketing scripts (Google Ads, Meta Pixel)...");
    // Example: Meta Pixel (replace with client's actual ID when ready)
    // !function(f,b,e,v,n,t,s)...
  }

  // Build the Banner and Modal in the DOM dynamically
  function buildBannerAndModal() {
    // 1. Create Banner if not exists
    if (!document.getElementById('lgpd-cookies-banner')) {
      bannerEl = document.createElement('div');
      bannerEl.id = 'lgpd-cookies-banner';
      bannerEl.className = 'cookies-banner';
      bannerEl.setAttribute('role', 'dialog');
      bannerEl.setAttribute('aria-live', 'polite');
      bannerEl.innerHTML = `
        <h3 class="cookies-title">Nós respeitamos sua privacidade</h3>
        <p class="cookies-text">
          Utilizamos cookies para oferecer a melhor experiência, melhorar o desempenho do site e personalizar anúncios. 
          Você pode aceitar todos os cookies ou configurar suas preferências na nossa 
          <a href="politica-de-cookies.html">Política de Cookies</a> e 
          <a href="politica-de-privacidade.html">Política de Privacidade</a>.
        </p>
        <div class="cookies-buttons">
          <button id="btn-cookies-accept-all" class="cookies-btn cookies-btn-primary">Aceitar Todos</button>
          <div class="cookies-buttons-row">
            <button id="btn-cookies-reject-all" class="cookies-btn cookies-btn-secondary">Recusar</button>
            <button id="btn-cookies-preferences" class="cookies-btn cookies-btn-secondary">Preferências</button>
          </div>
        </div>
      `;
      document.body.appendChild(bannerEl);
    } else {
      bannerEl = document.getElementById('lgpd-cookies-banner');
    }

    // 2. Create Modal if not exists
    if (!document.getElementById('lgpd-cookies-modal')) {
      modalEl = document.createElement('div');
      modalEl.id = 'lgpd-cookies-modal';
      modalEl.className = 'cookies-modal';
      modalEl.setAttribute('role', 'dialog');
      modalEl.setAttribute('aria-modal', 'true');
      modalEl.innerHTML = `
        <div class="cookies-modal-content">
          <button class="cookies-modal-close" id="btn-cookies-modal-close" aria-label="Fechar">&times;</button>
          <h3 class="cookies-modal-title">Preferências de Cookies</h3>
          <p class="cookies-modal-description">
            Personalize quais cookies você deseja permitir. Cookies necessários não podem ser desativados pois são essenciais para o funcionamento básico do site.
          </p>
          
          <div class="cookies-preferences-list">
            <!-- Necessários -->
            <div class="cookies-preference-item">
              <div class="cookies-pref-info">
                <div class="cookies-pref-header">
                  <h4 class="cookies-pref-name">Cookies Necessários</h4>
                  <span class="cookies-pref-tag">Sempre Ativos</span>
                </div>
                <p class="cookies-pref-description">Estes cookies são cruciais para que você navegue pelo site e use seus recursos básicos com segurança.</p>
              </div>
              <label class="cookies-switch">
                <input type="checkbox" checked disabled>
                <span class="cookies-slider"></span>
              </label>
            </div>
            
            <!-- Estatísticas -->
            <div class="cookies-preference-item">
              <div class="cookies-pref-info">
                <div class="cookies-pref-header">
                  <h4 class="cookies-pref-name">Cookies de Estatísticas</h4>
                </div>
                <p class="cookies-pref-description">Ajudam-nos a entender como os visitantes interagem com o site, coletando e relatando informações anonimamente.</p>
              </div>
              <label class="cookies-switch">
                <input type="checkbox" id="cookie-pref-statistics">
                <span class="cookies-slider"></span>
              </label>
            </div>
            
            <!-- Marketing -->
            <div class="cookies-preference-item">
              <div class="cookies-pref-info">
                <div class="cookies-pref-header">
                  <h4 class="cookies-pref-name">Cookies de Marketing</h4>
                </div>
                <p class="cookies-pref-description">Usados para rastrear visitantes pelos sites para permitir a exibição de anúncios relevantes e atraentes no Google, Meta e outros.</p>
              </div>
              <label class="cookies-switch">
                <input type="checkbox" id="cookie-pref-marketing">
                <span class="cookies-slider"></span>
              </label>
            </div>
          </div>
          
          <div class="cookies-modal-buttons">
            <button id="btn-cookies-save-pref" class="btn btn-dark">Salvar Preferências</button>
          </div>
        </div>
      `;
      document.body.appendChild(modalEl);
    } else {
      modalEl = document.getElementById('lgpd-cookies-modal');
    }
  }

  // Event Listeners setup
  function setupEventListeners() {
    // Acceptance buttons on banner
    document.getElementById('btn-cookies-accept-all').addEventListener('click', () => {
      saveConsent({ statistics: true, marketing: true });
    });

    document.getElementById('btn-cookies-reject-all').addEventListener('click', () => {
      saveConsent({ statistics: false, marketing: false });
    });

    document.getElementById('btn-cookies-preferences').addEventListener('click', showModal);

    // Modal controls
    document.getElementById('btn-cookies-modal-close').addEventListener('click', hideModal);
    
    // Close modal when clicking outside content
    modalEl.addEventListener('click', (e) => {
      if (e.target === modalEl) hideModal();
    });

    // Save preferences inside modal
    document.getElementById('btn-cookies-save-pref').addEventListener('click', () => {
      const stats = document.getElementById('cookie-pref-statistics').checked;
      const mkt = document.getElementById('cookie-pref-marketing').checked;
      saveConsent({ statistics: stats, marketing: mkt });
    });

    // Global footer links trigger for preferences
    document.querySelectorAll('.trigger-cookie-preferences').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        showModal();
      });
    });
  }

  // Run initial diagnostics
  init();

  // Export functions to window
  window.FilosCookies = {
    showPreferences: showModal,
    getConsent: () => ({ ...consent })
  };

})();
