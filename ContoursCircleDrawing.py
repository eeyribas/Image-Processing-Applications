import cv2

img1=cv2.imread('MonaLisa.jpg')
img2=cv2.imread('MonaLisa.jpg')
gray=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
returns, thresh=cv2.threshold(gray,1,1, cv2.THRESH_BINARY)

contours, hierachy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    (x, y), radius=cv2.minEnclosingCircle(cnt)
    center=(int(x), int(y))
    radius=int(radius)
    cv2.circle(img2, center, radius, (0, 0, 255), 4)
    cv2.imwrite('Image.png', img2)