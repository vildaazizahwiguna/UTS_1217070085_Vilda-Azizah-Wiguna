# 1217070085, Vilda Azizah Wiguna
import cv2

image = cv2.imread('kitten.jpg')

# Mengonversi gambar ke ruang warna HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Memisahkan saluran warna Hue, Saturation, dan Value
hue_channel, saturation_channel, value_channel = cv2.split(hsv_image)

# Menampilkan masing-masing saluran warna
cv2.imshow('Hue Channel', hue_channel)
cv2.imshow('Saturation Channel', saturation_channel)
cv2.imshow('Value Channel', value_channel)

# Menunggu input dari pengguna
cv2.waitKey(0)
cv2.destroyAllWindows()
