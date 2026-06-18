css = """
/* Wrapper do carrossel deslizante */
.section-related-courses .courses-carousel-wrapper {
  position: relative;
  width: 100%;
}

.section-related-courses .courses-carousel-track {
  display: flex;
  gap: 1.5rem;
  overflow-x: auto;
  scroll-behavior: smooth;
  scroll-snap-type: x mandatory;
  padding-bottom: 2rem; /* Espaço para sombra/hover dos cards */
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

.section-related-courses .courses-carousel-track::-webkit-scrollbar {
  display: none; /* Chrome, Safari and Opera */
}

.section-related-courses .courses-carousel-item {
  flex: 0 0 calc(33.333% - 1rem);
  scroll-snap-align: start;
}

@media (max-width: 1024px) {
  .section-related-courses .courses-carousel-item {
    flex: 0 0 calc(50% - 0.75rem);
  }
}

@media (max-width: 767px) {
  .section-related-courses .courses-carousel-item {
    flex: 0 0 100%;
  }
}
"""

with open("css/pages.css", "a", encoding="utf-8") as f:
    f.write(css)

print("CSS appended.")
