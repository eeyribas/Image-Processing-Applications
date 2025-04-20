import cv2

from matplotlib import pyplot as plt

img=cv2.imread('OpenCV.jpg')
blur=cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(121)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(blur)
plt.title('Bilateral Image')
plt.xticks([])
plt.yticks([])
plt.show()