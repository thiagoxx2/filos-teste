import re

css_to_append = """
/* HOME — filtros de cursos com 2 itens por linha no mobile */
@media (max-width: 767px) {
  .home #cursos .courses-filter-circles {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    column-gap: clamp(1.1rem, 5vw, 2rem);
    row-gap: clamp(1.15rem, 4.5vw, 1.8rem);
    align-items: center;
    justify-items: start;
    width: min(100%, 640px);
    margin-inline: auto;
    padding-inline: clamp(1.25rem, 5vw, 2rem);
  }

  .home #cursos .filter-circle {
    width: 100%;
    min-width: 0;
    display: inline-flex;
    align-items: center;
    justify-content: flex-start;
    gap: clamp(0.45rem, 2vw, 0.7rem);
    padding: 0;
  }

  .home #cursos .filter-circle-dot {
    width: clamp(0.58rem, 2.4vw, 0.78rem);
    height: clamp(0.58rem, 2.4vw, 0.78rem);
    min-width: clamp(0.58rem, 2.4vw, 0.78rem);
    border-width: 2px;
    flex: 0 0 auto;
  }

  .home #cursos .filter-circle-label {
    font-size: clamp(0.92rem, 4.2vw, 1.28rem);
    line-height: 1.08;
    letter-spacing: -0.02em;
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: normal;
  }

  .home #cursos .filter-circle.active .filter-circle-label {
    font-weight: 800;
  }
}

/* Mesmo em celulares pequenos, manter 2 por linha */
@media (max-width: 480px) {
  .home #cursos .courses-filter-circles {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    width: 100%;
    column-gap: 0.9rem;
    row-gap: 1rem;
    padding-inline: 1rem;
  }

  .home #cursos .filter-circle-label {
    font-size: clamp(0.82rem, 3.9vw, 1.05rem);
    line-height: 1.08;
  }

  .home #cursos .filter-circle-dot {
    width: 0.58rem;
    height: 0.58rem;
    min-width: 0.58rem;
  }
}
"""

with open("css/pages.css", "a", encoding="utf-8") as f:
    f.write(css_to_append)

print("Mobile CSS appended.")
