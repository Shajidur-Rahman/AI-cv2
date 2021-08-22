import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)
# print(img.shape)

# img[200:400, 200:400] = 255,255,255

cv2.line(img, (0, 0), (500, 500), (255, 255, 255), thickness=4)
cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), cv2.FILLED)
cv2.circle(img, (250, 250), 60, (255, 255, 255), cv2.FILLED)
cv2.putText(img, " Hello World ! ", (10, 500), cv2.FONT_ITALIC, 1, (255, 255, 0), 2)

cv2.imshow("img", img)

cv2.waitKey(0)
