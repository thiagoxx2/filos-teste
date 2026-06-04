/**
 * courses-filter.js - Filter courses by category on the Home Page
 * Faculdade Filos
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  const filterButtons = document.querySelectorAll('.filter-btn');
  const courseCards = document.querySelectorAll('.course-card');

  if (filterButtons.length > 0 && courseCards.length > 0) {
    
    filterButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Remove active class from all buttons
        filterButtons.forEach(button => button.classList.remove('active'));
        
        // Add active class to clicked button
        btn.classList.add('active');
        
        const filterValue = btn.getAttribute('data-filter').toLowerCase().trim();
        
        // Filter cards
        courseCards.forEach(card => {
          const cardCategory = card.getAttribute('data-category').toLowerCase().trim();
          
          if (filterValue === 'all' || filterValue === 'todos' || cardCategory === filterValue) {
            // Smooth reveal
            card.style.display = 'flex';
            // Trigger reflow to apply opacity transitions smoothly
            void card.offsetWidth;
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
          } else {
            // Smooth hide
            card.style.opacity = '0';
            card.style.transform = 'scale(0.95)';
            // Delay display none to allow fade/scale transitions
            setTimeout(() => {
              // Re-check filter state before hiding, in case the user clicked another tab quickly
              const currentActiveBtn = document.querySelector('.filter-btn.active');
              const currentFilter = currentActiveBtn.getAttribute('data-filter').toLowerCase().trim();
              const recheckedCategory = card.getAttribute('data-category').toLowerCase().trim();
              
              if (currentFilter !== 'all' && currentFilter !== 'todos' && recheckedCategory !== currentFilter) {
                card.style.display = 'none';
              }
            }, 250); // Matches normal/fast transition durations
          }
        });
      });
    });

    // Set transition styles dynamically if not already in stylesheet
    courseCards.forEach(card => {
      card.style.transition = 'opacity 0.25s ease, transform 0.25s ease, box-shadow 0.3s ease, border-color 0.3s ease';
      card.style.opacity = '1';
      card.style.transform = 'scale(1)';
    });
  }
});
