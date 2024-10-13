import cv2
import numpy as np

from PIL import Image

image = cv2.imread("MonaLisa.jpg")
for i in range(0, 123):
    k = 21
    m = i * k
    cropped = image[0 : 500, 0 + m : k + m]
    cv2.imwrite("Image" + str(i) + ".bmp", cropped)

x = Image.open('Image53.bmp')
x = x.convert('L')
arr = np.array(x)
np.savetxt("Array.txt", np.array(x), fmt = "%s")
print(arr)
print("********************")
length = np.shape(x)
print(length)