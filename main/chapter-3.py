import cv2
import numpy as np

img = cv2.imread("../resources/Photos/cat.jpg")
print(img.shape)

img_resized = cv2.resize(img, (300, 200))
print(img_resized.shape)

img_croped = img[0:200, 200:500]

cv2.imshow("img", img)
# cv2.imshow("resized", img_resized)
cv2.imshow("croped", img_croped)

cv2.waitKey(0)