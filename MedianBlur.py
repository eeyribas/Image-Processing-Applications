import cv2

from matplotlib import pyplot as plt

img = cv2.imread('MonaLisa.jpg')
blur = cv2.medianBlur(img,5)

plt.subplot(121)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(blur)
plt.title('Median Blur Image')
plt.xticks([])
plt.yticks([])

plt.show()