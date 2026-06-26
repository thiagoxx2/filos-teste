import os
import glob
import re
import subprocess
import sys

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

directory = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE"
os.chdir(directory)

image_files = []
for ext in ('*.png', '*.jpg', '*.jpeg'):
    image_files.extend(glob.glob(f'**/{ext}', recursive=True))

html_files = glob.glob('**/*.html', recursive=True)
css_files = glob.glob('**/*.css', recursive=True)

# List of files we actually converted
converted_files = []

for img_path in image_files:
    basename = os.path.basename(img_path).lower()
    # Skip favicons and apple touch icons
    if 'favicon' in basename or 'apple-touch' in basename:
        continue
        
    # Skip if inside .gemini or .git or node_modules
    if '.gemini' in img_path or '.git' in img_path or 'node_modules' in img_path:
        continue

    # Convert to webp
    webp_path = os.path.splitext(img_path)[0] + '.webp'
    
    try:
        with Image.open(img_path) as img:
            # Convert to RGB if it's RGBA and saving as JPEG-like WebP, 
            # but WebP supports alpha, so we just save it directly.
            img.save(webp_path, 'webp', quality=85)
            
        orig_name = os.path.basename(img_path)
        webp_name = os.path.basename(webp_path)
        converted_files.append((orig_name, webp_name))
        print(f"Converted {orig_name} -> {webp_name}")
    except Exception as e:
        print(f"Failed to convert {img_path}: {e}")

# Remove duplicates in converted_files (if same filename in different dirs, we just replace the filename string)
converted_files = list(set(converted_files))

def add_lazy_loading(match):
    tag = match.group(0)
    attrs = match.group(1)
    
    if 'loading=' in attrs.lower():
        return tag
        
    if 'logo' in attrs.lower() or 'cabecalho' in attrs.lower() or 'topo' in attrs.lower():
        return tag
        
    return f'<img loading="lazy" {attrs}>'

# Update HTML and CSS
for file_path in html_files + css_files:
    if '.gemini' in file_path or '.git' in file_path:
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    
    # Replace filenames
    for orig_name, webp_name in converted_files:
        # Use regex to replace only whole filenames to avoid partial matches
        # E.g. replace 'banner.png' but not 'old_banner.png' if orig_name is 'banner.png'
        # But since we replace 'banner.png' with 'banner.webp', it's safe either way.
        pattern = re.compile(re.escape(orig_name), re.IGNORECASE)
        new_content = pattern.sub(webp_name, new_content)
        
    # Add lazy loading to HTML
    if file_path.endswith('.html'):
        new_content = re.sub(r'<img\s+([^>]+)>', add_lazy_loading, new_content, flags=re.IGNORECASE)
        
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

print("Done optimizing images and updating references!")
