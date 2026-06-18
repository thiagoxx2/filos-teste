import glob
import os
import re

html_files = glob.glob('cursos/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # The user asked me to REPLACE the manual related courses with the placeholder.
    # Let's find <div class="matriz-footer-cta"> or <section class="section section-related-courses">
    # and remove it if it exists.
    
    # Wait, the user said "A seção deve aparecer logo após o fechamento da seção: <section class="section-matriz-admin">"
    # Some files might have `<div class="matriz-footer-cta">` outside the section, which shouldn't be there according to the previous task (where I moved it inside, or maybe I didn't?). Let me check a fresh file.
    pass
