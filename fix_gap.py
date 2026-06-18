with open("css/pages.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("column-gap: clamp(0.65rem, 2.4vw, 1rem);", "column-gap: clamp(0.25rem, 1.5vw, 0.5rem);")
css = css.replace("column-gap: clamp(0.45rem, 2vw, 0.75rem);", "column-gap: clamp(0.15rem, 1vw, 0.3rem);")

with open("css/pages.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Gap fixed again.")
