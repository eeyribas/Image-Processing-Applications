import cv2

img1 = cv2.imread('MonaLisa.jpg')
img2 = cv2.imread('OpenCV.jpg')
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
returns, thresh = cv2.threshold(gray,1,1, cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 5)
    cv2.imwrite('Image.jpg', img2)