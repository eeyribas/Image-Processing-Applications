import cv2
import numpy as np

img = cv2.imread('MonaLisa.jpg')
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
sharpenKernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpened = cv2.filter2D(erosion, -1, sharpenKernel)

ret, thresh = cv2.threshold(sharpened,127,255, cv2.THRESH_BINARY)
cv2.imwrite('Image.bmp', thresh)