# 1217070085, Vilda Azizah Wiguna
import cv2
import numpy as np

image = cv2.imread('kitten.jpg')

# Menambahkan kecerahan dengan nilai konstanta = 100
brightened_image = cv2.add(image, np.array([100,100,100], dtype=np.uint8))

# Menampilkan gambar sebelum dan sesudah peningkatan kecerahan
cv2.imshow('Original Image', image)
cv2.imshow('Brightened Image', brightened_image)

# Menunggu input dari pengguna
cv2.waitKey(0)
cv2.destroyAllWindows()
