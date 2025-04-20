import cv2
import time
import numpy as np

startTime=time.time()

img1=cv2.imread('MonaLisa.jpg')
img2=cv2.imread('OpenCV.jpg')
kernel=np.ones((5, 5), np.uint8)
erosion1=cv2.erode(img1, kernel, iterations=1)
cv2.imwrite('Image1.bmp', erosion1)
erosion2=cv2.erode(img2, kernel, iterations=1)
cv2.imwrite('Image2.bmp', erosion2)

endTime=time.time()
print(endTime-startTime)