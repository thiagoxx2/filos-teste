with open("css/pages.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("transform: translateX(-5px) !important;", "transform: translateX(-35px) !important;")
css = css.replace("transform: translateX(3px) !important;", "transform: translateX(5px) !important;")

with open("css/pages.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Large transform applied.")
