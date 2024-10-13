import cv2
import time

startTime = time.time()

img = cv2.imread('MonaLisa.jpg')
cv2.imwrite('Image.bmp', img)

endTime = time.time()
print(endTime - startTime)