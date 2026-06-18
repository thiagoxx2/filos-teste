css = """
/* Bloco de exibição de preços do card de curso */
.course-card-price-display {
  display: flex;
  flex-direction: column;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.course-card-price-from {
  font-size: 0.85rem;
  color: var(--text-gray);
  margin-bottom: 0.2rem;
}

.course-card-price-old {
  text-decoration: line-through;
  font-weight: 500;
  color: #6c757d;
}

.course-card-price-current-label {
  font-size: 0.8rem;
  color: var(--text-gray);
  margin-bottom: 0.2rem;
}

.course-card-price-current {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--cta-green);
  line-height: 1;
  margin-bottom: 0.3rem;
}

.course-card-price-current span {
  font-size: 1rem;
  font-weight: 500;
}

.course-card-price-note {
  font-size: 0.7rem;
  color: var(--text-gray);
  opacity: 0.8;
}

/* Ajustes no card para não sobrepor */
.course-card-item {
  min-height: 520px; /* Aumentado para acomodar o bloco de preço maior */
}

@media (max-width: 767px) {
  .course-card-item {
    min-height: 500px;
  }
}
"""

with open("css/pages.css", "a", encoding="utf-8") as f:
    f.write(css)

print("CSS appended.")
