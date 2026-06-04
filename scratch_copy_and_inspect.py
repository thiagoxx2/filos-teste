import os
import shutil
import struct

brain_dir = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d0ec2c93-74d2-477a-8e59-d52eadea87f7/"
dest_filos_images = "/Users/shayenefreita/FACULDADE FILOS/assets/images/"
dest_teste_images = "/Users/shayenefreita/FILOS TESTE 2/assets/images/"

os.makedirs(dest_filos_images, exist_ok=True)
os.makedirs(dest_teste_images, exist_ok=True)

files = [
    "media__1779907132368.png",
    "media__1779907245207.png",
    "media__1779907327983.png"
]

print("Iniciando cópia e inspeção...")
for filename in files:
    src_path = os.path.join(brain_dir, filename)
    if not os.path.exists(src_path):
        print(f"Erro: Arquivo não encontrado: {src_path}")
        continue
    
    # Obter dimensões do PNG
    w, h = 0, 0
    with open(src_path, "rb") as f:
        data = f.read(24)
        if len(data) >= 24 and data[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", data[16:24])
    
    size_bytes = os.path.getsize(src_path)
    print(f"Arquivo: {filename} | Dimensões: {w}x{h} | Tamanho: {size_bytes} bytes")
    
    # Copiar com nome original para consulta
    shutil.copy2(src_path, os.path.join(dest_filos_images, filename))
    shutil.copy2(src_path, os.path.join(dest_teste_images, filename))
    
    # Determinar nome amigável com base nas proporções e tamanho
    # 1. Mockup da matriz curricular (provavelmente é a tela inteira do print: 1046x643 ou similar)
    # 2. Estudante com jaqueta rosa recortada/isolada (provavelmente vertical, ex: 800x1200 ou similar)
    # 3. Matriz em tabela (provavelmente uma tabela larga ou quadrada, ex: 900x750 ou similar)
    friendly_name = None
    if w > 0 and h > 0:
        ratio = w / h
        if ratio > 1.4: # Muito larga (provavelmente a tela do print da matriz que é 1000+ de largura por 600+ de altura)
            friendly_name = "mockup-matriz.png"
        elif ratio < 0.9: # Vertical (provavelmente a estudante)
            friendly_name = "student-pink-isolated.png"
        else: # Próximo de quadrado (provavelmente a tabela da matriz curricular)
            friendly_name = "tabela-matriz.png"
            
    if friendly_name:
        print(f"-> Copiando como: {friendly_name}")
        shutil.copy2(src_path, os.path.join(dest_filos_images, friendly_name))
        shutil.copy2(src_path, os.path.join(dest_teste_images, friendly_name))

print("Finalizado com sucesso!")
