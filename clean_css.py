import re

with open("css/pages.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace everything from .related-courses-carousel-wrapper down to .section-related-courses .carousel-nav-btn.next
start_str = ".related-courses-carousel-wrapper {"
end_str = ".section-related-courses .carousel-nav-btn.next {\n  right: -12px;\n}"

start_idx = css.find(start_str)
end_idx = css.find(end_str)

if start_idx != -1 and end_idx != -1:
    end_idx += len(end_str)
    new_css = css[:start_idx].rstrip() + "\n\n" + css[end_idx:].lstrip()
    with open("css/pages.css", "w", encoding="utf-8") as f:
        f.write(new_css)
    print("CSS block removed successfully.")
else:
    print(f"Could not find start or end index. start={start_idx}, end={end_idx}")

