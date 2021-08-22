import cv2

capture = cv2.VideoCapture(0)
capture.set(10,100)


# while True:
#     _, frame = capture.read()
#     cv2.imshow("video", frame)
#
#     if cv2.waitKey(0) == ord("q"):
#         break


while True:
    _, frame = capture.read()
    frame = cv2.resize(frame, (300, 200))
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break
