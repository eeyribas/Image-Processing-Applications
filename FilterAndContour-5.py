import cv2
import time
import numpy as np

startTime = time.time()

img = cv2.imread('MonaLisa.jpg')
sharpeningKernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpened = cv2.filter2D(img, -1, sharpeningKernel)
ret, thresh = cv2.threshold(sharpened,127,255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(thresh, kernel, iterations = 1)
dilation = cv2.dilate(erosion, kernel, iterations = 3)
gray = cv2.cvtColor(dilation, cv2.COLOR_BGR2GRAY)
returns, thresh = cv2.threshold(gray,1,255, cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1,(0, 0, 255),4)
cv2.imwrite('Image.bmp', img)

endTime = time.time()
print(endTime - startTime)