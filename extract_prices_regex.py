import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Split html into chunks by course-card-item
cards = html.split('class="course-card-item"')

course_data = {}

for card in cards[1:]:
    # find <h3>...</h3>
    name_match = re.search(r'<h3>(.*?)</h3>', card, re.DOTALL | re.IGNORECASE)
    if not name_match: continue
    name = name_match.group(1).strip()
    
    # find course-card-item-price
    price_match = re.search(r'class="course-card-item-price"[^>]*>(.*?)</div>', card, re.DOTALL | re.IGNORECASE)
    price = price_match.group(1).strip() if price_match else ""
    
    course_data[name] = price
    print(f"Found: {name} -> {price}")

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

for name, price in course_data.items():
    escaped_name = re.escape(name)
    pattern = r'(name:\s*"' + escaped_name + r'".*?price:\s*")[^"]*(")'
    js = re.sub(pattern, r'\g<1>' + price + r'\g<2>', js, flags=re.DOTALL)

with open("js/related-courses.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Prices updated successfully!")
