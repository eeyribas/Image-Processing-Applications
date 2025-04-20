import cv2
import numpy as np

from matplotlib import pyplot as plt

img=cv2.imread('MonaLisa.jpg')
kernel=np.ones((5, 5), np.uint8)
erosion1=cv2.erode(img, kernel, iterations=2)
opening1=cv2.morphologyEx(erosion1, cv2.MORPH_OPEN, kernel)
dilation1=cv2.dilate(opening1, kernel, iterations=1)

blur2=cv2.blur(img,(1, 1))
erosion2=cv2.erode(blur2, kernel, iterations=2)
opening2=cv2.morphologyEx(erosion2, cv2.MORPH_OPEN, kernel)
dilation2=cv2.dilate(opening2, kernel, iterations=1)
sobel2=cv2.Sobel(dilation2, cv2.CV_64F,1,1, ksize=1)

gaussian3=cv2.GaussianBlur(img,(5, 5),0)
erosion3=cv2.erode(gaussian3, kernel, iterations=2)
sobel3=cv2.Sobel(erosion3, cv2.CV_64F,1,0, ksize=1)
opening3=cv2.morphologyEx(sobel3, cv2.MORPH_OPEN, kernel)
dilation3=cv2.dilate(opening3, kernel, iterations=1)

median4=cv2.medianBlur(img,9)
erosion4=cv2.erode(median4, kernel, iterations=2)
opening4=cv2.morphologyEx(erosion4, cv2.MORPH_OPEN, kernel)
dilation4=cv2.dilate(opening4, kernel, iterations=1)

plt.figure(1, figsize=(6, 8))
plt.subplot(5, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 2)
plt.imshow(dilation1)
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 3)
plt.imshow(sobel2),
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 4)
plt.imshow(dilation3),
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 5)
plt.imshow(dilation4)
plt.xticks([])
plt.yticks([])
plt.savefig('Image.png')
plt.show()