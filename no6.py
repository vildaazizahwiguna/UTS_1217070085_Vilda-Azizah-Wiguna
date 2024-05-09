# 1217070085, Vilda Azizah Wiguna 
import cv2

image = cv2.imread('kitten.jpg')

# Memisahkan saluran warna
blue_channel = image[:,:,0]
green_channel = image[:,:,1]
red_channel = image[:,:,2]

# Menampilkan gambar dari masing-masing saluran warna
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

# Menunggu input dari pengguna
cv2.waitKey(0)
