import os
import re

def update_html_files():
    root_dir = '/Users/shayenefreita/FACULDADE FILOS'
    replacements = [
        (r'responsive\.css\?v=6\.13', 'responsive.css?v=6.14')
    ]
    
    count = 0
    for root, dirs, files in os.walk(root_dir):
        if any(ignored in root for ignored in ['.git', '.venv', '.kiro', 'site-packages']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                modified = False
                for pattern, repl in replacements:
                    new_content, n = re.subn(pattern, repl, new_content)
                    if n > 0:
                        modified = True
                
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Atualizado: {os.path.relpath(file_path, root_dir)}")
                    count += 1
                    
    print(f"Total de arquivos HTML updated to v=6.14: {count}")

if __name__ == '__main__':
    update_html_files()
