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

capture = cv.VideoCapture(1)
changeRes(900, 900)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Original Video', frame)
    if cv.waitKey(300) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
