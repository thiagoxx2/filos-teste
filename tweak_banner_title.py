import re

with open("css/pages.css", "r", encoding="utf-8") as f:
    css = f.read()

# Increase banner height by 20px
css = css.replace("padding: 4rem 0 calc(clamp(8rem, 9.5vw, 11.5rem) - 25px) 0;", "padding: 4rem 0 calc(clamp(8rem, 9.5vw, 11.5rem) - 5px) 0;")

# Push down the title by 30px
old_title_css = """.why-admin-title {
  font-family: var(--font-title);
  font-size: clamp(2.35rem, 3.6vw, 3.3rem);
  font-weight: 800;
  color: var(--primary-dark);
  margin-bottom: 2.1rem;
  text-align: center;
}"""

new_title_css = """.why-admin-title {
  font-family: var(--font-title);
  font-size: clamp(2.35rem, 3.6vw, 3.3rem);
  font-weight: 800;
  color: var(--primary-dark);
  margin-top: 30px;
  margin-bottom: 2.1rem;
  text-align: center;
}"""

if old_title_css in css:
    css = css.replace(old_title_css, new_title_css)
else:
    print("WARNING: title CSS block not found exactly as expected.")

with open("css/pages.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Modifications applied.")
