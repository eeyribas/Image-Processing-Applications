import cv2
import numpy as np

img = cv2.imread('MonaLisa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
returns, thresh = cv2.threshold(gray,80,255, cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    area = cv2.contourArea(cnt)

    if (area > 1):
        cv2.drawContours(img,[cnt], -1,(0, 255, 0),2)
        cv2.imshow('RGB', img)
        cv2.waitKey(5000)
        print(len(cnt))

contours = np.array(contours)
print(contours)