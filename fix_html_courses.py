import glob
import os
import re

html_files = glob.glob('cursos/*.html')
count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    slug = os.path.basename(file_path).replace('.html', '')

    # Remove the randomly injected placeholder
    html = re.sub(r'\n\n  <div class="related-courses-placeholder" data-current-course="[^"]+"></div>\n', '', html)
    html = re.sub(r'  <div class="related-courses-placeholder" data-current-course="[^"]+"></div>\n', '', html)
    
    # Check if there is an old <section class="... section-related-courses" ...>
    old_section_pattern = re.compile(r'<section\s+class="[^"]*section-related-courses[^"]*"[^>]*>.*?</section>', re.DOTALL)
    
    if old_section_pattern.search(html):
        # Replace the entire old section with the placeholder
        placeholder = f'<div class="related-courses-placeholder" data-current-course="{slug}"></div>'
        html = old_section_pattern.sub(placeholder, html)
        count += 1
    else:
        # If no old section was found, we insert the placeholder right after the end of section-matriz-admin
        # Wait, the user said "A seção deve aparecer logo após o fechamento da seção: <section class="section-matriz-admin">"
        # Let's find </section> after section-matriz-admin
        match = re.search(r'(<section[^>]*class="[^"]*section-matriz-admin[^"]*"[^>]*>.*?</section>)', html, re.DOTALL)
        if match:
            placeholder = f'\n<div class="related-courses-placeholder" data-current-course="{slug}"></div>\n'
            # Only inject if not already there
            if f'data-current-course="{slug}"' not in html:
                html = html[:match.end()] + placeholder + html[match.end():]
                count += 1
                
    # Check if script is added
    script_tag = '<script src="../js/related-courses.js"></script>'
    if script_tag not in html:
        body_idx = html.rfind('</body>')
        if body_idx != -1:
            html = html[:body_idx] + f'  {script_tag}\n' + html[body_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Fixed {count} files.")
