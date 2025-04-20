import numpy as np
from PIL import Image

x=Image.open('MonaLisa.jpg')
x=x.convert('L')
arr1=np.array(x)
np.savetxt("Array.txt", np.array(x), fmt = "%s")
arr2=np.gradient(arr1)
print(arr2)