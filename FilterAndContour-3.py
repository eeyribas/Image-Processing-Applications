import cv2
import time
import numpy as np

startTime=time.time()

img=cv2.imread('MonaLisa.jpg')
kernel=np.ones((5, 5), np.uint8)
blur=cv2.blur(img,(4, 4))
erosion=cv2.erode(blur, kernel, iterations=3)
opening=cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
dilation=cv2.dilate(opening, kernel, iterations=2)
gray=cv2.cvtColor(dilation, cv2.COLOR_BGR2GRAY)
returns, thresh=cv2.threshold(gray,1,1, cv2.THRESH_BINARY)

contours, hierachy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1,(0, 0, 255),4)
cv2.imwrite('Image.bmp', img)

endTime=time.time()
print(endTime-startTime)