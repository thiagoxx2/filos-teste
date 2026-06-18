import re

with open("css/pages.css", "r", encoding="utf-8") as f:
    css = f.read()

# The previous block to replace starts with: /* HOME — filtros de cursos com 2 itens por linha no mobile */
# and we can simply replace everything from there to the end of the file, because we appended it at the very end.
# Just to be safe, we use a regex to replace it.
pattern = r'/\* HOME — filtros de cursos com 2 itens por linha no mobile \*/.*'

new_css = """
/* HOME — filtros de cursos centralizados e compactos no mobile */
@media (max-width: 767px) {
  .home #cursos .courses-filter-circles {
    display: grid !important;
    grid-template-columns: repeat(2, max-content) !important;
    justify-content: center !important;
    align-items: center;
    justify-items: start;

    column-gap: clamp(1.4rem, 5vw, 2.2rem);
    row-gap: clamp(0.9rem, 3vw, 1.25rem);

    width: 100%;
    max-width: 100%;
    margin-inline: auto;
    padding-inline: 0.75rem;
  }

  .home #cursos .filter-circle {
    width: auto !important;
    min-width: 0;
    display: inline-flex;
    align-items: center;
    justify-content: flex-start;
    gap: clamp(0.42rem, 1.6vw, 0.6rem);
    padding: 0;
  }

  .home #cursos .filter-circle-dot {
    width: clamp(0.55rem, 2vw, 0.7rem);
    height: clamp(0.55rem, 2vw, 0.7rem);
    min-width: clamp(0.55rem, 2vw, 0.7rem);
    border-width: 2px;
    flex: 0 0 auto;
  }

  .home #cursos .filter-circle-label {
    font-size: clamp(0.9rem, 3.7vw, 1.18rem);
    line-height: 1.05;
    letter-spacing: -0.02em;
    white-space: nowrap;
  }

  .home #cursos .filter-circle.active .filter-circle-label {
    font-weight: 800;
  }
}

/* Celulares menores: mantém 2 por linha, ainda centralizado */
@media (max-width: 480px) {
  .home #cursos .courses-filter-circles {
    grid-template-columns: repeat(2, max-content) !important;
    justify-content: center !important;

    column-gap: clamp(1rem, 4vw, 1.5rem);
    row-gap: 0.85rem;

    padding-inline: 0.5rem;
  }

  .home #cursos .filter-circle {
    gap: 0.4rem;
  }

  .home #cursos .filter-circle-label {
    font-size: clamp(0.82rem, 3.55vw, 1rem);
    line-height: 1.05;
    white-space: nowrap;
  }

  .home #cursos .filter-circle-dot {
    width: 0.55rem;
    height: 0.55rem;
    min-width: 0.55rem;
  }
}
"""

css = re.sub(pattern, new_css.strip(), css, flags=re.DOTALL)

with open("css/pages.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS replaced.")
