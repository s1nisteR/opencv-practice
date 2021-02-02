import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Jesmin", img)

#Translation function
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#Rotation function
def rotate(img, angle, rotPoint = None):
    width = img.shape[1]
    height = img.shape[0]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #1.0 for counter clockwise, -1.0 for clockwise
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

"""
#Flipping an image
flippedImage = cv.flip(img, -1) #A flag to specify how to flip the array; 0 means flipping around the x-axis and positive value (for example, 1) means flipping around y-axis. Negative value (for example, -1) means flipping around both axes.
cv.imshow("title", flippedImage)

#Cropping an image
croppedImage = img[100:200, 100:300]
cv.imshow("", croppedImage)
"""

"""
#Resizing an image
resizedImage = cv.resize(img, (200, 200), interpolation=cv.INTER_CUBIC) #use INTER_CUBIC for resizing UP
cv.imshow("resized", resizedImage)

anotherResizedImage = cv.resize(img, (200, 200), interpolation=cv.INTER_AREA) #use INTER_AREA for resizing DOWN
cv.imshow("another resized", anotherResizedImage)
"""

#Tranlate an image
translatedImage = translate(img, 100, 100)
cv.imshow("translated image", translatedImage)
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

#Rotating an image
rotatedImage = rotate(img, 90)
cv.imshow("Rotated Image", rotatedImage)

cv.waitKey(0)


