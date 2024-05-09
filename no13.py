# 1217070085, Vilda Azizah Wiguna 
import cv2
import numpy as np 

image = cv2.imread('kitten.jpg')

#untuk mengetahui ukuran citra lebar dan tinggi 
(height, width) = image.shape[0:2]
rotasiMatriks = cv2.getRotationMatrix2D((width/2, height/2), -90, 0.5)

#rotasi depat menggunakan method wrapAffine mengambil citra asli 
rotasicitra = cv2.warpAffine(image, rotasiMatriks, (width, height))
cv2.imshow('citra rotasi', rotasicitra)
cv2.waitKey(0)