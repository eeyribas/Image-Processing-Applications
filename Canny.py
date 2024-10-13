import cv2

from matplotlib import pyplot as plt

img = cv2.imread('MonaLisa.jpg', 0)
canny = cv2.Canny(img, 100, 200)

plt.subplot(121)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(canny)
plt.title('Canny Image')
plt.xticks([])
plt.yticks([])

plt.show()