with open("css/pages.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("margin-left: -3px;", "transform: translateX(-5px) !important;")
css = css.replace("margin-left: 2px;", "transform: translateX(3px) !important;")

with open("css/pages.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Switched to transform.")
