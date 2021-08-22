import cv2
import numpy as np

img = cv2.imread("../resources/Photos/brandable-box-8mCsyImZRGY-unsplash (1).jpg")
img = cv2.resize(img, (500, 500))

width, height = 250, 350

pts1 = np.float32([[66, 234], [268, 260], [74, 395], [254, 465]])
pts2 = np.float32([[0, 0], [width, 0], [height, 0], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("img", img)
cv2.imshow("dont know", img_output)

cv2.waitKey(0)
