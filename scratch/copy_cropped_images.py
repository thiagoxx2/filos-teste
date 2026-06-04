import os
import shutil

src_pink = "/Users/shayenefreita/FACULDADE FILOS/assets/images/student-pink-isolated.png"
src_portrait = "/Users/shayenefreita/FACULDADE FILOS/assets/images/student-portrait.png"

dest_dir = "/Users/shayenefreita/FILOS TESTE 2/assets/images"
dest_pink = os.path.join(dest_dir, "student-pink-isolated.png")
dest_portrait = os.path.join(dest_dir, "student-portrait.png")

# Certificar que o diretório de destino existe
os.makedirs(dest_dir, exist_ok=True)

print("Copiando student-pink-isolated.png...")
shutil.copy2(src_pink, dest_pink)

print("Copiando student-portrait.png...")
shutil.copy2(src_portrait, dest_portrait)

print("Sincronização de imagens concluída com sucesso!")
