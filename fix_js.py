import re

path = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/js/main.js"
with open(path, "r", encoding="utf-8") as f:
    js = f.read()

# I need to fix the ending.
# Right now the end looks like:
#         });
#     });
#   });
# });
# Let's replace the whole chunk starting from `const headers = ` to the end of file with the correct code.

good_js = """
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
});
"""

# Replace everything from `const headers = `
js = re.sub(r'const headers = document\.querySelectorAll\("\.matriz-accordion-header"\);.*', good_js, js, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(js)
    
print("Fixed main.js syntax!")
