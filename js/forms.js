/**
 * forms.js - Form validation and LGPD compliance checks
 * Faculdade Filos
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  const forms = document.querySelectorAll('.validated-form');

  // 1. Tratamento padrão dos formulários genéricos com .validated-form
  if (forms.length > 0) {
    forms.forEach(form => {
      // Ignora o form da ouvidoria para tratarmos separadamente com mensagens customizadas
      if (form.id === 'ouvidoriaForm') return;

      const submitBtn = form.querySelector('[type="submit"]');
      const privacyCheckbox = form.querySelector('.privacy-accept-checkbox');
      const feedbackEl = form.querySelector('.form-feedback') || createFeedbackElement(form);

      // Disable submit if privacy checkbox exists and is not checked
      if (privacyCheckbox && submitBtn) {
        // Initial state
        submitBtn.disabled = !privacyCheckbox.checked;
        
        privacyCheckbox.addEventListener('change', () => {
          submitBtn.disabled = !privacyCheckbox.checked;
        });
      }

      form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Clear previous feedbacks
        feedbackEl.className = 'form-feedback';
        feedbackEl.textContent = '';
        feedbackEl.style.display = 'none';

        // Validation
        let isValid = true;
        const requiredInputs = form.querySelectorAll('[required]');
        
        requiredInputs.forEach(input => {
          if (!input.value.trim()) {
            isValid = false;
            highlightError(input);
          } else {
            clearHighlight(input);
          }

          // Email validation
          if (input.type === 'email' && input.value.trim()) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(input.value.trim())) {
              isValid = false;
              highlightError(input);
            }
          }

          // Phone validation basic
          if (input.type === 'tel' && input.value.trim()) {
            const cleanPhone = input.value.replace(/\D/g, '');
            if (cleanPhone.length < 10) {
              isValid = false;
              highlightError(input);
            }
          }
        });

        if (privacyCheckbox && !privacyCheckbox.checked) {
          isValid = false;
          highlightError(privacyCheckbox.parentElement);
        }

        if (!isValid) {
          showFeedback(feedbackEl, 'error', 'Por favor, preencha todos os campos obrigatórios corretamente.');
          return;
        }

        // Simulate submission (HostGator friendly)
        if (submitBtn) {
          const originalText = submitBtn.textContent;
          submitBtn.textContent = 'Enviando...';
          submitBtn.disabled = true;

          // Check if user accepted marketing cookies to fire analytics events
          const consent = window.FilosCookies ? window.FilosCookies.getConsent() : null;
          
          setTimeout(() => {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
            
            // Fire pixel/analytics conversions if marketing/statistics are allowed
            if (consent && consent.marketing) {
              console.log("Analytics: Firing lead generation conversion event.");
              // if (window.gtag) gtag('event', 'generate_lead');
            }

            // Success feedback
            showFeedback(feedbackEl, 'success', 'Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.');
            form.reset();
            if (privacyCheckbox) {
              submitBtn.disabled = true; // Disabled again since form is reset and checkbox is unchecked
            }
          }, 1500);
        }
      });
    });

    // Format phone numbers automatically in tel inputs (e.g. (99) 99999-9999)
    const telInputs = document.querySelectorAll('input[type="tel"]');
    telInputs.forEach(tel => {
      tel.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, '');
        if (value.length > 11) value = value.slice(0, 11);
        
        let formatted = '';
        if (value.length > 0) {
          formatted = '(' + value.slice(0, 2);
          if (value.length > 2) {
            formatted += ') ' + value.slice(2, 7);
            if (value.length > 7) {
              formatted += '-' + value.slice(7);
            }
          }
        }
        e.target.value = formatted;
      });
    });
  }

  // 2. Tratamento específico do formulário da Ouvidoria
  const ouvidoriaForm = document.getElementById('ouvidoriaForm');
  if (ouvidoriaForm) {
    const feedbackEl = ouvidoriaForm.querySelector('.form-feedback') || createFeedbackElement(ouvidoriaForm);
    const submitBtn = ouvidoriaForm.querySelector('.ouvidoria-btn-submit');

    ouvidoriaForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Limpar feedbacks anteriores
      feedbackEl.className = 'form-feedback';
      feedbackEl.textContent = '';
      feedbackEl.style.display = 'none';

      let isValid = true;

      // Validar campos normais do formulário
      const requiredInputs = ouvidoriaForm.querySelectorAll('[required]');
      requiredInputs.forEach(input => {
        if (!input.value.trim()) {
          isValid = false;
          highlightError(input);
        } else {
          clearHighlight(input);
        }

        if (input.type === 'email' && input.value.trim()) {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(input.value.trim())) {
            isValid = false;
            highlightError(input);
          }
        }
      });

      // Validar reCAPTCHA oficial do Google
      const recaptchaResponse = typeof grecaptcha !== 'undefined' ? grecaptcha.getResponse() : '';
      if (!recaptchaResponse) {
        isValid = false;
        const recaptchaContainer = ouvidoriaForm.querySelector('.g-recaptcha');
        if (recaptchaContainer) {
          highlightError(recaptchaContainer);
        }
      }

      if (!isValid) {
        if (!recaptchaResponse) {
          showFeedback(feedbackEl, 'error', 'Por favor, confirme que você não é um robô resolvendo o reCAPTCHA.');
        } else {
          showFeedback(feedbackEl, 'error', 'Por favor, preencha todos os campos obrigatórios corretamente.');
        }
        return;
      }

      // Envio assíncrono para o PHP
      if (submitBtn) {
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Enviando relato...';
        submitBtn.disabled = true;

        const formData = new FormData(ouvidoriaForm);

        fetch(ouvidoriaForm.getAttribute('action') || 'send_ouvidoria.php', {
          method: 'POST',
          body: formData
        })
        .then(response => response.json().catch(() => {
          throw new Error('Resposta inválida do servidor');
        }))
        .then(data => {
          submitBtn.textContent = originalText;
          submitBtn.disabled = false;

          if (data.success) {
            showFeedback(feedbackEl, 'success', data.message);
            ouvidoriaForm.reset();
            if (typeof grecaptcha !== 'undefined') {
              grecaptcha.reset();
            }
          } else {
            showFeedback(feedbackEl, 'error', data.message || 'Ocorreu um erro ao enviar o relato.');
          }
        })
        .catch(err => {
          submitBtn.textContent = originalText;
          submitBtn.disabled = false;
          showFeedback(feedbackEl, 'error', 'Erro de conexão ou envio do formulário. Por favor, verifique sua conexão e tente novamente.');
          console.error(err);
        });
      }
    });
  }

  // Create feedback container on the fly if it's missing in HTML
  function createFeedbackElement(form) {
    const feedback = document.createElement('div');
    feedback.className = 'form-feedback';
    feedback.style.display = 'none';
    feedback.style.marginTop = '1rem';
    feedback.style.padding = '0.75rem';
    feedback.style.borderRadius = 'var(--radius-sm)';
    feedback.style.fontSize = '0.875rem';
    feedback.style.fontWeight = '600';
    feedback.style.textAlign = 'center';
    
    // Add before the submit wrapper or at the end
    const lastElement = form.lastElementChild;
    form.insertBefore(feedback, lastElement);
    return feedback;
  }

  function highlightError(input) {
    input.style.borderColor = '#ef4444';
    input.style.backgroundColor = '#fef2f2';
    
    // Quick listener to clear error when user types
    input.addEventListener('input', function clear() {
      clearHighlight(input);
      input.removeEventListener('input', clear);
    });

    if (input.classList.contains('ouvidoria-recaptcha-checkbox-wrapper')) {
      input.addEventListener('click', function clear() {
        clearHighlight(input);
        input.removeEventListener('click', clear);
      });
    }
  }

  function clearHighlight(input) {
    input.style.borderColor = '';
    input.style.backgroundColor = '';
  }

  function showFeedback(element, type, message) {
    element.textContent = message;
    element.style.display = 'block';
    
    if (type === 'success') {
      element.style.backgroundColor = 'var(--cta-green-light)';
      element.style.color = 'var(--cta-green-hover)';
      element.style.border = '1px solid var(--cta-green)';
    } else {
      element.style.backgroundColor = '#fef2f2';
      element.style.color = '#b91c1c';
      element.style.border = '1px solid #f87171';
    }

    // Scroll to feedback if on mobile
    if (window.innerWidth < 768) {
      element.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }
});
