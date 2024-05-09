import cv2
import matplotlib.pyplot as plt

image = cv2.imread('kitten.jpg')

if image is not None:
    # Konversi ke HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Pisahkan saluran HSV
    h, s, v = cv2.split(hsv_image)

    # Hitung histogram untuk setiap saluran
    hist_h = cv2.calcHist([h], [0], None, [256], [0, 256])
    hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
    hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])

    # Tampilkan histogram menggunakan Matplotlib
    plt.figure(figsize=(10, 6))
    plt.title('Histogram for Hue, Saturation, and Value Channels')
    plt.plot(hist_h, color='r', label='Hue')
    plt.plot(hist_s, color='g', label='Saturation')
    plt.plot(hist_v, color='b', label='Value')
    plt.xlabel('Bins')
    plt.ylabel('Number of Pixels')
    plt.legend()
    plt.show()