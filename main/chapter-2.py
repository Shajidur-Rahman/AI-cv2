import cv2
import numpy as np

img = cv2.imread("../resources/Photos/cat.jpg")
kernal = np.ones((5, 5), dtype=np.uint8)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_blur = cv2.GaussianBlur(gray_img, (7, 7), 0)
img_canny = cv2.Canny(img, 100, 100)
img_dialation = cv2.dilate(img_canny, kernal, iterations=1)
img_eroded = cv2.erode(img_dialation, kernal, iterations=1)

# cv2.imshow("gray", gray_img)
# cv2.imshow("blur", img_blur)
# cv2.imshow("canny", img_canny)
cv2.imshow("dialatiuon", img_dialation)
cv2.imshow("eroded", img_eroded)

cv2.waitKey(0)