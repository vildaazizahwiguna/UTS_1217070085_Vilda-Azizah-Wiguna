# 1217070085, Vilda Azizah Wiguna 
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('kitten.jpg')

# Normalisasi gambar
normalized_image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Mengonversi gambar ke grayscale (untuk histogram)
gray_image = cv2.cvtColor(normalized_image, cv2.COLOR_BGR2GRAY)

# Menghitung histogram gambar
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Menampilkan gambar dan histogram
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(normalized_image, cv2.COLOR_BGR2RGB))
plt.title('Normalized Image')

plt.subplot(1, 2, 2)
plt.plot(hist, color='black')
plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()