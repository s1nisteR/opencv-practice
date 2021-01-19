import cv2 as cv

"""
picture = cv.imread("Photos/cat.jpg")
cv.imshow("My first program", picture)
cv.waitKey(0)
"""

#Video loading
capture =  cv.VideoCapture("Videos/kitten.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow("My second program", frame)
    if cv.waitKey(5) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
