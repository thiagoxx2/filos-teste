/**
 * gallery.js - Mini Gallery tabs and Lightbox popup
 * Faculdade Filos
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  // --- GALLERY FILTER TABS ---
  const tabButtons = document.querySelectorAll('.gallery-tab');
  const galleryItems = document.querySelectorAll('.gallery-item');

  if (tabButtons.length > 0 && galleryItems.length > 0) {
    tabButtons.forEach(tab => {
      tab.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Remove active class from tabs
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tab.classList.add('active');
        
        const filterVal = tab.getAttribute('data-tag').toLowerCase().trim();
        
        galleryItems.forEach(item => {
          const itemTag = item.getAttribute('data-tag').toLowerCase().trim();
          
          if (filterVal === 'all' || filterVal === 'todos' || itemTag === filterVal) {
            item.style.display = 'block';
            setTimeout(() => {
              item.style.opacity = '1';
              item.style.transform = 'scale(1)';
            }, 10);
          } else {
            item.style.opacity = '0';
            item.style.transform = 'scale(0.95)';
            setTimeout(() => {
              // Confirm tab filter hasn't changed before hiding
              const activeTab = document.querySelector('.gallery-tab.active');
              const currentFilter = activeTab.getAttribute('data-tag').toLowerCase().trim();
              const recheckedTag = item.getAttribute('data-tag').toLowerCase().trim();
              
              if (currentFilter !== 'all' && currentFilter !== 'todos' && recheckedTag !== currentFilter) {
                item.style.display = 'none';
              }
            }, 250);
          }
        });
      });
    });

    // Style transitions dynamically
    galleryItems.forEach(item => {
      item.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
      item.style.opacity = '1';
      item.style.transform = 'scale(1)';
    });
  }


  // --- LIGHTBOX POPUP ---
  const lightbox = document.getElementById('gallery-lightbox');
  const lightboxImg = lightbox ? lightbox.querySelector('.lightbox-image') : null;
  const lightboxCaption = lightbox ? lightbox.querySelector('.lightbox-caption') : null;
  const lightboxClose = lightbox ? lightbox.querySelector('.lightbox-close') : null;

  if (lightbox && lightboxImg && galleryItems.length > 0) {
    galleryItems.forEach(item => {
      item.addEventListener('click', () => {
        const img = item.querySelector('img');
        const title = item.querySelector('.gallery-overlay-title');
        
        if (img) {
          lightboxImg.src = img.src;
          lightboxImg.alt = img.alt || 'Imagem Faculdade Filos';
          
          if (lightboxCaption) {
            lightboxCaption.textContent = title ? title.textContent : '';
          }
          
          lightbox.classList.add('active');
          document.body.style.overflow = 'hidden'; // Stop background scrolling
        }
      });
    });

    // Close Lightbox
    const closeLightbox = () => {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
      // Reset image src after transition to avoid flash next time it opens
      setTimeout(() => {
        lightboxImg.src = '';
      }, 300);
    };

    if (lightboxClose) {
      lightboxClose.addEventListener('click', closeLightbox);
    }

    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) {
        closeLightbox();
      }
    });

    // Keyboard ESC key to close
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightbox.classList.contains('active')) {
        closeLightbox();
      }
    });
  }
});
