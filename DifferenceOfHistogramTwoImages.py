import cv2

img1 = cv2.imread("MonaLisa.jpg")
img2 = cv2.imread("OpenCV.jpg")
hist1 = cv2.calcHist([img1],[0],None,[2],[0, 256])
hist2 = cv2.calcHist([img2],[0],None,[2],[0, 256])
print(hist1 - hist2)
print("-----------")