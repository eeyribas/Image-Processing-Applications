import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

x = Image.open('MonaLisa.jpg')
x = x.convert('L')
array = np.array(x)
print("*******************************")
print(array)
print("*******************************")

print("**************SUM**************")
print(array.sum(axis=1))
print(array.sum(axis=0))