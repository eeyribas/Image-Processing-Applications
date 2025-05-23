import cv2
import numpy as np

from matplotlib import pyplot as plt

img=cv2.imread('MonaLisa.jpg')
kernel1=np.ones((5, 5), np.uint8)
kernel2=np.ones((5, 5), np.uint8)
blur=cv2.blur(img,(1, 1))
erosion=cv2.erode(blur, kernel2, iterations=2)
opening=cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel2)
dilation=cv2.dilate(opening, kernel1, iterations=1)
sobel=cv2.Sobel(dilation, cv2.CV_64F,1,1, ksize=1)

plt.figure(1, figsize=(20, 16))
plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 2)
plt.imshow(blur)
plt.title('Blur Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 3)
plt.imshow(dilation)
plt.title('Erosion-Opening-Dilation Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 4)
plt.imshow(sobel)
plt.title('Sobel X-Y Image')
plt.xticks([])
plt.yticks([])
plt.savefig('MonaLisa-Test.jpg')
plt.show()