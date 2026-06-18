import re

with open("css/pages.css", "r", encoding="utf-8") as f:
    css = f.read()

pattern = r'/\* Ajustes finos visuais solicitados para compensar a largura do grid \*/.*'

new_css = """/* Ajustes finos visuais solicitados para compensar a largura do grid */
@media (max-width: 767px) {
  .home #cursos .filter-circle:nth-child(1) {
    transform: translateX(17px) !important;
  }
  .home #cursos .filter-circle:nth-child(2) {
    transform: translateX(-17px) !important;
  }
  .home #cursos .filter-circle:nth-child(3) {
    transform: translateX(-2px) !important;
  }
  .home #cursos .filter-circle:nth-child(4) {
    transform: translateX(2px) !important;
  }
}"""

css = re.sub(pattern, new_css, css, flags=re.DOTALL)

with open("css/pages.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Recentered.")
