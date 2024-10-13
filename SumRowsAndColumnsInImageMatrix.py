import numpy as np

from PIL import Image

x = Image.open('MonaLisa.jpg')
x = x.convert('L')
array = np.array(x)

print("*******************************")
print(array)
print("*******************************")
print("**************SUM**************")
print(array.sum(axis = 1))
print(array.sum(axis = 0))