import cv2

img = cv2.imread("../resources/Photos/cat.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow("rgb", gray_img)

cv2.waitKey(0)