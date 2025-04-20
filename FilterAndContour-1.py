import cv2
import numpy as np

img=cv2.imread('MonaLisa.jpg')
kernel=np.ones((5, 5), np.uint8)
median=cv2.medianBlur(img,9)
erosion=cv2.erode(median, kernel, iterations=2)
opening=cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
dilation=cv2.dilate(opening, kernel, iterations=1)
gray=cv2.cvtColor(dilation, cv2.COLOR_BGR2GRAY)
returns, thresh=cv2.threshold(gray,1,1, cv2.THRESH_BINARY)

contours, hierachy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1,(0, 0, 255),4)
cv2.imwrite('Image.png', img)