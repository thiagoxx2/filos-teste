#!/usr/bin/env python3
import os
import re

ROOT = "/Users/shayenefreita/FACULDADE FILOS"
cursos_dir = os.path.join(ROOT, "cursos")

# Remove o bloco .inscription-card-switches inteiro
pattern = re.compile(
    r'\s*<div class="inscription-card-switches">.*?</div>\s*</div>\s*',
    re.DOTALL
)

count = 0
for fname in sorted(os.listdir(cursos_dir)):
    if not fname.endswith(".html"):
        continue
    path = os.path.join(cursos_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = pattern.sub('\n', content, count=1)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  OK: {fname}")
        count += 1
    else:
        print(f"  SEM MATCH: {fname}")

print(f"\nTotal atualizado: {count} arquivos")
