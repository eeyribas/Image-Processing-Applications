import cv2

from matplotlib import pyplot as plt

img = cv2.imread('MonaLisa.jpg')
blur = cv2.GaussianBlur(img,(5, 5),0)

plt.subplot(121)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(blur)
plt.title('Gaussian Blur Image')
plt.xticks([])
plt.yticks([])

plt.show()