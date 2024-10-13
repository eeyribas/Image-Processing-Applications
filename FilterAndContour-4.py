import cv2
import time
import numpy as np

startTime = time.time()

img = cv2.imread('MonaLisa.jpg')
kernel = np.ones((8, 8), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 2)
cv2.imwrite('Image1.bmp', erosion)
dilation = cv2.dilate(erosion, kernel, iterations = 2)
cv2.imwrite('Image2.bmp', dilation)
blur = cv2.blur(dilation,(20, 20),0)
cv2.imwrite('Image3.bmp', blur)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Image4.bmp', gray)
returns, thresh = cv2.threshold(gray,1,1, cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1,(0, 0, 255),4)
cv2.imwrite('Image.bmp', img)

endTime = time.time()
print(endTime - startTime)