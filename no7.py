# 1217070085, Vilda Azizah Wiguna 
import cv2

image_bgr = cv2.imread('kitten.jpg')

# Mengonversi dari BGR ke HSV
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

# Menyimpan gambar yang telah diubah ke HSV
cv2.imwrite('gambar_hsv.jpg', image_hsv)

# Menampilkan gambar BGR dan HSV
cv2.imshow('BGR Image', image_bgr)
cv2.imshow('HSV Image', image_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
