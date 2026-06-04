import shutil
import os

src = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d0ec2c93-74d2-477a-8e59-d52eadea87f7/media__1779902734279.jpg"
dest1 = "/Users/shayenefreita/FACULDADE FILOS/assets/images/bg-classroom-blur.jpg"
dest2 = "/Users/shayenefreita/FILOS TESTE 2/assets/images/bg-classroom-blur.jpg"

# Certificar que os diretórios de destino existem
os.makedirs(os.path.dirname(dest1), exist_ok=True)
os.makedirs(os.path.dirname(dest2), exist_ok=True)

print("Copiando para:", dest1)
shutil.copy2(src, dest1)
print("Copiando para:", dest2)
shutil.copy2(src, dest2)
print("Sucesso!")
