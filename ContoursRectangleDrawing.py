import cv2

img = cv2.imread('MonaLisa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
returns, thresh = cv2.threshold(gray,80,255, cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('RGB', img)
    cv2.waitKey(5000)
    print(len(cnt))