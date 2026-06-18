import re
import os

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE"

# 1. Extract CSS and JS from administracao.html
with open(os.path.join(repo_dir, "cursos/administracao.html"), "r", encoding="utf-8") as f:
    admin_html = f.read()

css_match = re.search(r'/\* --- ESTILOS SEÇÃO MATRIZ CURRICULAR --- \*/.*?(?=</style>)', admin_html, re.DOTALL)
if css_match:
    matriz_css_block = css_match.group(0).strip()
else:
    print("CSS block not found.")
    matriz_css_block = ""

# The JS for accordion in administracao.html
js_match = re.search(r'const headers = document\.querySelectorAll\("\.matriz-accordion-header"\);.*?(?=\s*}\);\s*}\);\s*</script>)', admin_html, re.DOTALL)
if js_match:
    accordion_js = js_match.group(0).strip()
    accordion_js += "\n    });\n  });"
else:
    print("JS not found")
    accordion_js = """
  const headers = document.querySelectorAll(".matriz-accordion-header");
  if(headers.length > 0) {
    headers.forEach(header => {
      header.addEventListener("click", function() {
        const item = this.parentElement;
        const content = item.querySelector(".matriz-accordion-content");
        const isExpanded = this.getAttribute("aria-expanded") === "true";
        this.setAttribute("aria-expanded", !isExpanded);
        item.classList.toggle("active");
        if (item.classList.contains("active")) {
          content.style.maxHeight = content.scrollHeight + "px";
        } else {
          content.style.maxHeight = "0";
        }
      });
    });
  }
"""

# 2. Append CSS to pages.css
pages_css_path = os.path.join(repo_dir, "css/pages.css")
with open(pages_css_path, "a", encoding="utf-8") as f:
    f.write("\n\n" + matriz_css_block + "\n")

# 3. Append JS to main.js
main_js_path = os.path.join(repo_dir, "js/main.js")
with open(main_js_path, "r", encoding="utf-8") as f:
    main_js = f.read()

if "matriz-accordion-header" not in main_js:
    # Append inside the DOMContentLoaded block
    main_js = main_js.replace("});\n\n\n", f"\n{accordion_js}\n\n}});\n\n\n")
    # if the replace didn't work because of the spacing, let's just do:
    if "matriz-accordion-header" not in main_js:
        main_js = main_js.rstrip()
        if main_js.endswith("});"):
            main_js = main_js[:-3] + f"\n{accordion_js}\n}});\n"
        else:
            main_js += f"\ndocument.addEventListener('DOMContentLoaded', () => {{\n{accordion_js}\n}});\n"

    with open(main_js_path, "w", encoding="utf-8") as f:
        f.write(main_js)

# 4. Remove `<style>...</style>` from radiologia.html
rad_path = os.path.join(repo_dir, "cursos/radiologia.html")
with open(rad_path, "r", encoding="utf-8") as f:
    rad_html = f.read()

rad_html = re.sub(r'<style>\s*/\* --- ESTILOS SEÇÃO MATRIZ CURRICULAR --- \*/.*?</style>', '', rad_html, flags=re.DOTALL)

with open(rad_path, "w", encoding="utf-8") as f:
    f.write(rad_html)

print("Done fixing CSS and JS globally.")
