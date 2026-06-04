/**
 * faq.js - Accordion mechanism for FAQ section
 * Faculdade Filos
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  const faqItems = document.querySelectorAll('.faq-item');

  if (faqItems.length > 0) {
    faqItems.forEach(item => {
      const questionBtn = item.querySelector('.faq-question');
      const answer = item.querySelector('.faq-answer');

      if (questionBtn && answer) {
        // Accessibility attributes
        questionBtn.setAttribute('aria-expanded', 'false');
        
        questionBtn.addEventListener('click', (e) => {
          e.preventDefault();
          
          const isActive = item.classList.contains('active');
          const rowVal = item.getAttribute('data-row');
          const rowPartners = rowVal ? document.querySelectorAll(`.faq-item[data-row="${rowVal}"]`) : [item];

          // Close all other items first (Single Open Policy)
          faqItems.forEach(otherItem => {
            if (otherItem !== item) {
              otherItem.classList.remove('active');
              otherItem.classList.remove('stretch');
              const otherBtn = otherItem.querySelector('.faq-question');
              const otherAnswer = otherItem.querySelector('.faq-answer');
              if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
              if (otherAnswer) otherAnswer.style.maxHeight = null;
            }
          });

          // Toggle current item
          if (isActive) {
            item.classList.remove('active');
            questionBtn.setAttribute('aria-expanded', 'false');
            answer.style.maxHeight = null;
            // Remove stretch from all row partners
            rowPartners.forEach(p => p.classList.remove('stretch'));
          } else {
            item.classList.add('active');
            questionBtn.setAttribute('aria-expanded', 'true');
            // Set max-height dynamically to enable smooth CSS height animation
            answer.style.maxHeight = answer.scrollHeight + 'px';
            // Add stretch to all row partners
            rowPartners.forEach(p => p.classList.add('stretch'));
          }
        });
      }
    });
  }

  // Handle window resize: recalculate active accordions max-height
  window.addEventListener('resize', () => {
    if (faqItems.length > 0) {
      faqItems.forEach(item => {
        if (item.classList.contains('active')) {
          const answer = item.querySelector('.faq-answer');
          if (answer) {
            answer.style.maxHeight = answer.scrollHeight + 'px';
          }
        }
      });
    }
  });

});
