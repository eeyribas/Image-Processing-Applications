import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread('MonaLisa.jpg')
kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((5,5),np.uint8)
median = cv2.medianBlur(img,9)
erosion = cv2.erode(median,kernel2,iterations = 2)
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel2)
dilation = cv2.dilate(opening,kernel1,iterations = 1)

plt.figure(8, figsize=(20,16))
plt.subplot(4,1,1),plt.imshow(img),plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(4,1,2),plt.imshow(median),plt.title('Median(Smoothing F.)')
plt.xticks([]), plt.yticks([])
plt.subplot(4,1,3),plt.imshow(opening),plt.title('Erosion-Opening (Morphological F.)')
plt.xticks([]), plt.yticks([])
plt.subplot(4,1,4),plt.imshow(dilation),plt.title('Dilation(Morphological F.)')
plt.xticks([]), plt.yticks([])

plt.show()