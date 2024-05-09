# 1217070085, Vilda Azizah Wiguna
import cv2
import numpy as np

image = cv2.imread('kitten.jpg')

# Mengonversi gambar menjadi ruang warna HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Mendapatkan saluran Hue, Saturation, dan Value
hue_channel = hsv_image[:,:,0]
saturation_channel = hsv_image[:,:,1]
value_channel = hsv_image[:,:,2]

cv2.imshow('Hue Channel', hue_channel)
cv2.imshow('Saturation Channel', saturation_channel)
cv2.imshow('Value Channel', value_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
