from PIL import Image
import time

startTime=time.time()
img=Image.open('MonaLisa.jpg','r')
pixVal=list(img.getdata())

i=0
while (i<1350000):
    if (i%2700==0):
        print(pixVal[i])
        i=i+1
    else:
        print(pixVal[i], end="")
        i=i+1
print('\n')
print(len(pixVal))
print('\n')

endTime=time.time()
print(endTime-startTime)