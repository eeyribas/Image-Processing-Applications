import cv2
import numpy as np

img = cv2.imread("MonaLisa.jpg")
for i in range(0, 50):
    for j in range(0, 20):
        k = j * 25
        m = i * 50
        cropped = img[0 + k : 25 + k, 0 + m : 50 + m]
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(cropped, kernel, iterations = 1)
        cv2.imwrite("Image" + str(i) + str(j) + ".bmp", erosion)