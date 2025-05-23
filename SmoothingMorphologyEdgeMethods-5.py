import cv2
import numpy as np

from matplotlib import pyplot as plt

img=cv2.imread('MonaLisa.jpg')
blur=cv2.blur(img,(5, 5))
gaussian=cv2.GaussianBlur(img,(5, 5),0)
median=cv2.medianBlur(img,5)
plt.figure(1, figsize=(20, 16))
plt.subplot(5, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 2)
plt.imshow(blur)
plt.title('Blur Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 3)
plt.imshow(gaussian)
plt.title('Gaussian Blur Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 4)
plt.imshow(median)
plt.title('Median Blur Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 5)
plt.imshow(median)
plt.title('Bileteral Filter Image')
plt.xticks([])
plt.yticks([])
plt.savefig('Image1.png')

laplacian=cv2.Laplacian(img, cv2.CV_64F)
sobelX=cv2.Sobel(img, cv2.CV_64F,1,0, ksize=1)
sobelY=cv2.Sobel(img, cv2.CV_64F,0,1, ksize=1)
canny=cv2.Canny(img, 200, 200)
plt.figure(2, figsize=(20, 16))
plt.subplot(5, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 2)
plt.imshow(laplacian)
plt.title('Laplace Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 3)
plt.imshow(sobelX)
plt.title('Sobel-X Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 4)
plt.imshow(sobelY)
plt.title('Sobel-Y Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 5)
plt.imshow(canny)
plt.title('Canny Image')
plt.xticks([])
plt.yticks([])
plt.savefig('Image2.png')

kernel=np.ones((5, 5), np.uint8)
erosion=cv2.erode(img, kernel, iterations=1)
dilation=cv2.dilate(img, kernel, iterations=1)
opening=cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing=cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient=cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat=cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat=cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
plt.figure(3, figsize=(20, 16))
plt.subplot(5, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 2)
plt.imshow(erosion)
plt.title('Erosion Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 3)
plt.imshow(dilation)
plt.title('Dilation Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 4)
plt.imshow(opening)
plt.title('Opening Image')
plt.xticks([])
plt.yticks([])
plt.subplot(5, 1, 5)
plt.imshow(closing)
plt.title('Closing Image')
plt.xticks([])
plt.yticks([])
plt.savefig('Image3.png')

plt.figure(4, figsize=(20, 16))
plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 2)
plt.imshow(gradient)
plt.title('Gradient Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 3)
plt.imshow(tophat)
plt.title('Top Hat Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 4)
plt.imshow(blackhat)
plt.title('Black Hat Image')
plt.xticks([])
plt.yticks([])
plt.savefig('Image4.png')

plt.figure(5, figsize=(20, 16))
kernel2=np.ones((5, 5), np.uint8)
erosion2=cv2.erode(img, kernel2, iterations=2)
opening2=cv2.morphologyEx(erosion2, cv2.MORPH_OPEN, kernel2)
dilation2=cv2.dilate(opening2, kernel, iterations=1)
plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 2)
plt.imshow(erosion2)
plt.title('Erosion Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 3)
plt.imshow(opening2)
plt.title('Opening Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 4)
plt.imshow(dilation2)
plt.title('Dilation Image')
plt.xticks([])
plt.yticks([])
plt.savefig('Image5.png')

plt.figure(6, figsize=(20, 16))
kernel3=np.ones((5, 5), np.uint8)
blur3=cv2.blur(img,(1, 1))
erosion3=cv2.erode(blur3, kernel3, iterations=2)
opening3=cv2.morphologyEx(erosion3, cv2.MORPH_OPEN, kernel3)
dilation3=cv2.dilate(opening3, kernel, iterations=1)
sobel3=cv2.Sobel(dilation3, cv2.CV_64F,1,1, ksize=1)
plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 2)
plt.imshow(blur3)
plt.title('Blur Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 3)
plt.imshow(dilation3)
plt.title('Erosion-Opening-Dilation Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 4)
plt.imshow(sobel3)
plt.title('Sobel X-Y Image')
plt.xticks([])
plt.yticks([])
plt.savefig('Image6.png')

plt.figure(7, figsize=(20, 16))
kernel4=np.ones((5, 5), np.uint8)
gaussian4=cv2.GaussianBlur(img,(5, 5),0)
erosion4=cv2.erode(gaussian4, kernel4, iterations=2)
sobel4=cv2.Sobel(erosion4, cv2.CV_64F,1,0, ksize=1)
opening4=cv2.morphologyEx(sobel4, cv2.MORPH_OPEN, kernel4)
dilation4=cv2.dilate(opening4, kernel4, iterations=1)
plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 2)
plt.imshow(gaussian4)
plt.title('Gaussian Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 3)
plt.imshow(opening4)
plt.title('Erosion-Sobel Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 4)
plt.imshow(dilation4)
plt.title('Opening - Dilation Image')
plt.xticks([])
plt.yticks([])
plt.savefig('Image7.png')

plt.figure(8, figsize=(20, 16))
kernel5=np.ones((5, 5), np.uint8)
median5=cv2.medianBlur(img,9)
erosion5=cv2.erode(median5, kernel5, iterations=2)
opening5=cv2.morphologyEx(erosion5, cv2.MORPH_OPEN, kernel5)
dilation5=cv2.dilate(opening5, kernel, iterations=1)
plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 2)
plt.imshow(median5)
plt.title('Median Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 3)
plt.imshow(opening5)
plt.title('Erosion-Opening Image')
plt.xticks([])
plt.yticks([])
plt.subplot(4, 1, 4)
plt.imshow(dilation5)
plt.title('Dilation Image')
plt.xticks([])
plt.yticks([])
plt.savefig('Image8.png')

plt.show()