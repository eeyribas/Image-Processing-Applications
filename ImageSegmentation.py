import cv2

image = cv2.imread("MonaLisa.jpg")
for i in range(0, 16):
    for j in range(0, 10):
        k = j * 50
        m = i * 161
        cropped = image[0 + k : 50 + k, 0 + m : 161 + m]
        cv2.imwrite("Image" + str(i) + str(j) + ".bmp", cropped)