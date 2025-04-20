import cv2

from matplotlib import pyplot as plt

img=cv2.imread('MonaLisa.jpg', 0)
sobelX=cv2.Sobel(img, cv2.CV_64F,1,0, ksize=5)
sobelY=cv2.Sobel(img, cv2.CV_64F,0,1, ksize=5)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(2, 2, 2)
plt.imshow(sobelX, cmap='gray')
plt.title('Sobel X Image')
plt.xticks([])
plt.yticks([])
plt.subplot(2, 2, 3)
plt.imshow(sobelY, cmap='gray')
plt.title('Sobel Y Image')
plt.xticks([])
plt.yticks([])
plt.show()