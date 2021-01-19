import cv2 as cv


def rescaleFrame(frame, scale):
    finalWidth = int(frame.shape[1] * scale) #width of original image * scale
    finalHeight = int(frame.shape[0] * scale) #height of original image * scale

    dimensions = (finalWidth, finalHeight)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #returns a new rescaled image

def changeRes(width,height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)

"""
picture = cv.imread("Photos/cat_large.jpg")
resizedImage = rescaleFrame(picture, 0.10)
cv.imshow("My first program", resizedImage)
cv.waitKey(0)
"""

"""
# Reading Videos
capture = cv.VideoCapture('Videos/kitten.mp4')
while True:
    isTrue, frame = capture.read()
    resizedFrame = rescaleFrame(frame, 0.25)
    cv.imshow('Original Video', frame)
    cv.imshow('Video', resizedFrame)
    if cv.waitKey(300) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
"""

capture = cv.VideoCapture(0)
changeRes(400, 400)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Original Video', frame)
    if cv.waitKey(300) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
