import re

with open("css/pages.css", "r", encoding="utf-8") as f:
    css = f.read()

# We want to replace the block added in the previous turn.
# It starts with: /* Bloco de exibição de preços do card de curso */
# And ends with:
# @media (max-width: 767px) {
#   .course-card-item {
#     min-height: 500px;
#   }
# }

new_css = """
/* Bloco compacto de preço — somente cursos superiores com valor oficial */
.course-card-price-display {
  width: 100%;
  margin-top: auto;
  margin-bottom: clamp(0.85rem, 1.2vw, 1.1rem);
  padding: clamp(0.7rem, 1vw, 0.9rem) 0 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.12rem;
}

.course-card-price-from {
  margin: 0;
  font-family: var(--font-body);
  font-size: clamp(0.78rem, 0.85vw, 0.9rem);
  line-height: 1.1;
  color: rgba(255, 255, 255, 0.48);
}

.course-card-price-old {
  color: rgba(255, 255, 255, 0.48);
  text-decoration: line-through;
  text-decoration-thickness: 1.5px;
  font-weight: 600;
}

.course-card-price-current-label {
  margin: 0.12rem 0 0;
  font-family: var(--font-body);
  font-size: clamp(0.82rem, 0.9vw, 0.95rem);
  line-height: 1.1;
  color: rgba(255, 255, 255, 0.78);
}

.course-card-price-current {
  margin: 0.1rem 0 0;
  display: flex;
  align-items: flex-start;
  gap: 0.28rem;
  font-family: var(--font-title);
  line-height: 0.95;
  color: var(--cta-green);
  letter-spacing: -0.04em;
}

.course-card-price-currency {
  padding-top: 0.28em;
  font-size: clamp(1rem, 1.25vw, 1.35rem);
  font-weight: 800;
  letter-spacing: -0.02em;
}

.course-card-price-current strong {
  font-size: clamp(2rem, 2.9vw, 3.05rem);
  font-weight: 900;
  color: var(--cta-green);
}

.course-card-price-asterisk {
  padding-top: 0.12em;
  font-size: clamp(1rem, 1.2vw, 1.35rem);
  font-weight: 800;
  color: var(--cta-green);
}

.course-card-price-note {
  margin: 0.18rem 0 0;
  font-family: var(--font-body);
  font-size: clamp(0.66rem, 0.72vw, 0.76rem);
  line-height: 1.15;
  color: rgba(255, 255, 255, 0.58);
}

/* Card sem preço não deve ficar artificialmente alto */
.course-card-item {
  min-height: 480px;
}

.course-card-item-body {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.course-card-item-footer {
  margin-top: auto;
}

@media (max-width: 767px) {
  .course-card-item {
    min-height: 460px;
  }

  .course-card-price-current strong {
    font-size: clamp(2.15rem, 10vw, 2.85rem);
  }
}
"""

pattern = r'/\* Bloco de exibição de preços do card de curso \*/.*'
css = re.sub(pattern, new_css.strip(), css, flags=re.DOTALL)

with open("css/pages.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS replaced.")
