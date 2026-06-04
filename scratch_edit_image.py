from PIL import Image

def process_image(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Tolerância para o azul escuro: RGB próximo a (13, 27, 42)
    # Apenas remover as partes sólidas, mas o CSS diz "#0d1b2a" que é (13, 27, 42)
    # Vamos usar uma flood fill mais inteligente
    
    # Ou melhor, dado que a imagem atual 'vestibular-student-card.png'
    # já tem as partes superiores transparentes e o cara sai para fora...
    # Talvez eu só precise ajustar o CSS para que ele não corte a imagem!
    
    pass

