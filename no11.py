# 1217070085, Vilda Azizah Wiguna 
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('kitten.jpg')

# Mengonversi gambar ke ruang warna HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Memisahkan saluran warna Hue, Saturation, dan Value
hue_channel, saturation_channel, value_channel = cv2.split(hsv_image)

# Menghitung histogram untuk masing-masing saluran warna
hist_hue = cv2.calcHist([hue_channel], [0], None, [256], [0, 256])
hist_saturation = cv2.calcHist([saturation_channel], [0], None, [256], [0, 256])
hist_value = cv2.calcHist([value_channel], [0], None, [256], [0, 256])

# Menampilkan histogram
plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.plot(hist_hue, color='r')
plt.title('Histogram Hue Channel')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')

plt.subplot(3, 1, 2)
plt.plot(hist_saturation, color='g')
plt.title('Histogram Saturation Channel')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')

plt.subplot(3, 1, 3)
plt.plot(hist_value, color='b')
plt.title('Histogram Value Channel')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')

plt.tight_layout()
plt.show()
