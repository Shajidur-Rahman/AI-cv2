import cv2

print("packages imported")

# reading images
"""
img = cv2.imread("../resources/Photos/cat.jpg")
cv2.imshow("Cat", img)

cv2.waitKey(0)
"""


capture = cv2.VideoCapture(0)
capture.set(10,100)

while True:
    _, frame = capture.read()
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

print("code completed")