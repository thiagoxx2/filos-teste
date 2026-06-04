import re

css_path = 'css/components.css'
with open(css_path, 'r') as f:
    css = f.read()
    
# Let's find rules for carousel-slide--vestibular
print("Mobile:")
for match in re.finditer(r'\.carousel-slide--vestibular[^}]+\}', css):
    print(match.group(0))

print("\nDesktop/General:")
# We already looked at desktop
