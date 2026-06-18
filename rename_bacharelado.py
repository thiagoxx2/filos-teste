import re
import glob

def replace_in_file(path, old_str, new_str):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# index.html
replace_in_file("index.html", "Bacharelado", "Graduação")
replace_in_file("index.html", "bacharelado", "graduacao")

# js/related-courses.js
replace_in_file("js/related-courses.js", "Bacharelado", "Graduação")
replace_in_file("js/related-courses.js", "bacharelado", "graduacao")

# css/components.css
replace_in_file("css/components.css", "bacharelado", "graduacao")

# js/main.js
replace_in_file("js/main.js", "bacharelado", "graduacao")
replace_in_file("js/main.js", "Bacharelado", "Graduação")

# cursos/*.html
for file in glob.glob("cursos/*.html"):
    replace_in_file(file, "Bacharelado", "Graduação")
    replace_in_file(file, "bacharelado", "graduacao")

print("Nomenclature updated.")
