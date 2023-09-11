from rembg import remove
from PIL import Imageç

input_path = 'imagen.jpg'
output_path = 'imagen_final.png'
input = Image.open(input_path)
outpu = remove(input)
outpu.save(output_path)