import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_filters = """      <div class="courses-filter-circles">
        <button class="filter-circle active" data-filter="all">
          <span class="filter-circle-dot"></span>
          <span class="filter-circle-label">TODOS</span>
        </button>
        <button class="filter-circle" data-filter="bacharelado">
          <span class="filter-circle-dot"></span>
          <span class="filter-circle-label">Bacharelado</span>
        </button>
        <button class="filter-circle" data-filter="licenciatura">
          <span class="filter-circle-dot"></span>
          <span class="filter-circle-label">Licenciatura</span>
        </button>
        <button class="filter-circle" data-filter="tecnologo">
          <span class="filter-circle-dot"></span>
          <span class="filter-circle-label">Tecnólogo</span>
        </button>
        <button class="filter-circle" data-filter="pos-graduacao">
          <span class="filter-circle-dot"></span>
          <span class="filter-circle-label">Pós-Graduação</span>
        </button>
        <button class="filter-circle" data-filter="extensao">
          <span class="filter-circle-dot"></span>
          <span class="filter-circle-label">Extensão</span>
        </button>
      </div>"""

# Replace the block
html = re.sub(r'<div class="courses-filter-circles">.*?</div>', new_filters, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Filters updated in index.html")
