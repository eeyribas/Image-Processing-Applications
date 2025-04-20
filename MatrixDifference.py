import numpy as np

from PIL import Image

x1=Image.open('MonaLisa.jpg')
x1=x1.convert('L')
arr1=np.array(x1)
print("********************")
print(arr1)
print("********************")

x2=Image.open('OpenCV.jpg')
x2=x2.convert('L')
arr2=np.array(x2)
print("********************")
print(arr2)
print("********************")

x3=np.subtract(x1, x2)
np.savetxt("Array.txt", np.array(x3), fmt="%s")
print("********************")
print(x3)
print("********************")