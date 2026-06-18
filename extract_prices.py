import re
from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all("div", class_="course-card-item")

course_data = {}

for card in cards:
    name_el = card.find("h3")
    if not name_el: continue
    name = name_el.get_text(strip=True)
    
    price_el = card.find("div", class_="course-card-item-price")
    if price_el:
        price = price_el.get_text(strip=True)
    else:
        price = ""
        
    course_data[name] = price

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

# For each course dictionary in JS, replace price: "299,90" with price: "<actual_price>"
for name, price in course_data.items():
    # Find the object in JS that has name: "name"
    # and update its price. 
    # Because formatting might vary, we can do a regex replace block by block
    # It's easier to find the block: name: "Exact Name", ... price: "..."
    # and replace the price
    escaped_name = re.escape(name)
    # The block might be like:
    # name: "Engenharia de Software",
    # period: "Noturno", ... price: "299,90"
    
    pattern = r'(name:\s*"' + escaped_name + r'".*?price:\s*")[^"]*(")'
    js = re.sub(pattern, r'\g<1>' + price + r'\g<2>', js, flags=re.DOTALL)

with open("js/related-courses.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Prices updated!")
