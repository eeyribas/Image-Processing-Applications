import cv2

img1=cv2.imread('MonaLisa.jpg')
img2=cv2.imread('MonaLisa.jpg')
gray=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
returns, thresh=cv2.threshold(gray,1,1, cv2.THRESH_BINARY)

contours, hierachy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(img2,[cnt], -1,(0, 0, 255),2)
    cv2.imwrite('Image.png', img2)