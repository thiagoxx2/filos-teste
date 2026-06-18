import glob
import os

html_files = glob.glob('cursos/*.html')
count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    slug = os.path.basename(file_path).replace('.html', '')

    start_idx = html.find('section-matriz-admin')
    if start_idx != -1:
        end_idx = html.find('</section>', start_idx)
        if end_idx != -1:
            end_idx += len('</section>')
            
            placeholder = f'\n\n  <div class="related-courses-placeholder" data-current-course="{slug}"></div>\n'
            
            if 'class="related-courses-placeholder"' not in html:
                html = html[:end_idx] + placeholder + html[end_idx:]
                count += 1
    
    script_tag = '<script src="../js/related-courses.js"></script>'
    if script_tag not in html:
        body_idx = html.rfind('</body>')
        if body_idx != -1:
            html = html[:body_idx] + f'  {script_tag}\n' + html[body_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Injected related courses into {count} html files.")
