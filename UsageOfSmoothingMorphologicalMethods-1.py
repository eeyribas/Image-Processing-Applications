import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread('MonaLisa.jpg')
kernel = np.ones((5,5),np.uint8)
blur = cv2.blur(img,(2,2))
erosion = cv2.erode(blur,kernel,iterations = 2)
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)

plt.figure(1)
plt.subplot(4,1,1),plt.imshow(img),plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(4,1,2),plt.imshow(blur),plt.title('Blur (Smoothing)')
plt.xticks([]), plt.yticks([])
plt.subplot(4,1,3),plt.imshow(erosion),plt.title('Erosion (Morphological F.)')
plt.xticks([]), plt.yticks([])
plt.subplot(4,1,4),plt.imshow(opening),plt.title('Opening (Morphological F.)')
plt.xticks([]), plt.yticks([])

plt.show()