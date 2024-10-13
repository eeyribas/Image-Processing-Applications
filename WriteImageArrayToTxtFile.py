import numpy as np
from PIL import Image

x = Image.open('MonaLisa.jpg')
x=x.convert('L')
arr = np.array(x)
np.savetxt("Array.txt", np.array(x), fmt="%s")
print(arr)