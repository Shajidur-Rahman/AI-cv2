import cv2
import numpy as np

img = cv2.imread("../resources/Photos/cat.jpg")

hor = np.hstack((img, img))

cv2.imshow("mine", hor)

cv2.waitKey(0)