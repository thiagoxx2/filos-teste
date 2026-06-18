import re
import os
import json

with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

match = re.search(r'(const courses = \[.*?\];)', js, re.DOTALL)
courses_array_str = match.group(1).replace('const courses = ', '').rstrip(';')
courses_array_str = re.sub(r',\s*\]', ']', courses_array_str)

courses = json.loads(courses_array_str)
js_slugs = [c["slug"] for c in courses]
js_urls = [c["url"] for c in courses]

html_files = os.listdir("cursos")
html_files = [f for f in html_files if f.endswith(".html")]

print("Courses in JS array:", len(courses))
print("HTML files in cursos/:", len(html_files))

missing_html = []
for url in js_urls:
    filename = url.replace("cursos/", "") if url.startswith("cursos/") else url
    if filename not in html_files and filename != "":
        missing_html.append(filename)

print("URLs in JS but missing HTML file:", missing_html)

missing_js = []
for f in html_files:
    if f not in [url.replace("cursos/", "") for url in js_urls]:
        missing_js.append(f)

print("HTML files missing in JS array:", missing_js)
