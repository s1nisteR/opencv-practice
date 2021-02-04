import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Original', img)

grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Jesmin", grayscale)

#Condition for Laplacian: Cannot take negative values
#Laplacian Edge Detection
lap = cv.Laplacian(grayscale, cv.CV_64F)
absouluteLap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian Edge Detection', absouluteLap)

#Sobel Edge Detection
sobelx = cv.Sobel(grayscale, cv.CV_64F, 1, 0)

sobely = cv.Sobel(grayscale, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Combined Sobel", combined_sobel)


#Canny image
cannyImage = cv.Canny(grayscale, 100, 175)
cv.imshow("Canny Image", cannyImage)

cv.waitKey(0)