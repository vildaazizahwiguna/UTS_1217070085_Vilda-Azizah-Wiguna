# 1217070085, Vilda Azizah Wiguna 
from PIL import Image

def split_image_into_bands(image_path):
    # Buka gambar
    image = Image.open(image_path)
    
    # Pisahkan ke dalam band-band
    bands = image.split()
    
    return bands

# Contoh penggunaan
image_path = "kitten.jpg"
bands = split_image_into_bands(image_path)

# Menyimpan setiap band sebagai gambar terpisah
for i, band in enumerate(bands):
    band.save(f"band_{i}.jpg")
