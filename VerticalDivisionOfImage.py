import cv2
import time
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("MonaLisa.jpg")

for i in range(0, 123):
    k = 21
    m = i * k
    cropped = image[0:500, 0+m:k+m]
    cv2.imwrite("Image"+str(i)+".bmp", cropped)