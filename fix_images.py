import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
css_files = glob.glob('**/*.css', recursive=True)

# 1. We will replace all .png, .jpg, .jpeg with .webp in src="", href="", url()
# EXCEPT if it contains favicon or apple-touch-icon
def ext_replacer(match):
    prefix = match.group(1) # src=" etc
    url = match.group(2)
    ext = match.group(3)
    suffix = match.group(4)
    
    if 'favicon' in url.lower() or 'apple-touch' in url.lower():
        return match.group(0)
    
    return f"{prefix}{url}.webp{suffix}"

# Regex for src="something.png", url('something.png'), etc.
# Match groups: (prefix)(url_without_ext)(\.png|\.jpg|\.jpeg)(suffix)
# Not the most bulletproof, let's just do a simple replace on the file content for .png, .jpg, .jpeg
# with a lookahead to ensure it's followed by quote or space or )

def raw_replacer(match):
    name = match.group(1)
    ext = match.group(2)
    after = match.group(3)
    if 'favicon' in name.lower() or 'apple-touch' in name.lower() or 'vestibular-student-new' in name.lower():
        return match.group(0)
    return f"{name}.webp{after}"

def add_lazy_loading(match):
    tag_content = match.group(1)
    # Check if already has loading=
    if re.search(r'\bloading=', tag_content, re.IGNORECASE):
        return match.group(0)
        
    # Check if it's logo or header
    if re.search(r'(logo|cabecalho|topo)', tag_content, re.IGNORECASE):
        return match.group(0)
        
    return f'<img loading="lazy"{tag_content}>'

for file_path in html_files + css_files:
    if '.gemini' in file_path or '.git' in file_path:
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    
    # Replace extensions (handling Mac unicode paths without exact match)
    new_content = re.sub(r'([^"\'\s]+)\.(png|jpg|jpeg)(["\'\s)?#])', raw_replacer, new_content, flags=re.IGNORECASE)
    
    # Add lazy loading
    if file_path.endswith('.html'):
        # using re.DOTALL to match across newlines
        new_content = re.sub(r'<img\s+([^>]+)>', add_lazy_loading, new_content, flags=re.IGNORECASE | re.DOTALL)
        
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file_path}")

