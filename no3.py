# 1217070085, Vilda Azizah Wiguna
import cv2
import numpy as np 
import matplotlib.pyplot as plt

image = cv2.imread("kitten.jpg")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()