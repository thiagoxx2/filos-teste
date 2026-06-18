import re
import os
import json

old_prices = {}
html_files = os.listdir("cursos")

for file in html_files:
    if not file.endswith(".html"): continue
    with open(os.path.join("cursos", file), "r", encoding="utf-8") as f:
        content = f.read()
        
        # Look for course-price-old
        match = re.search(r'<span class="course-price-old">R\$\s*([\d\.,]+)</span>', content)
        if match:
            slug = file.replace(".html", "")
            old_prices[slug] = match.group(1)

print(json.dumps(old_prices, indent=2))
