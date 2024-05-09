# 1217070085, Vilda Azizah Wiguna
import cv2
import os 

image = cv2.imread('kitten.jpg')

#menampilkan resolusi gambar 
height, widht, channel = image.shape
print(f'resolusi gambar : {widht} x {height} piksel' )

#menampilkan ukuran data media penyimpanan 
file_path = 'kitten.jpg'
file_size = os.path.getsize(file_path)
print('ukuran data media penyimpanan : ', file_size, 'bytes')

#menampilkan image data type
print('image data type : ', image.dtype)