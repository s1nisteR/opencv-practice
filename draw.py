import cv2 as cv
import numpy as np

blank = cv.imread('Photos/cat.jpg')

#Manually painting an image over a range
blank[0:100, 0:100] = 0,255,0
cv.imshow('Painted Image', blank)

#Drawing a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=2) #thickness=-1 for fill
cv.imshow('Rectangle', blank)

#Drawing a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,0,0), thickness=-1)
cv.imshow('Circle', blank)

#Drawing a line
cv.line(blank, (0,0), (blank.shape[1], blank.shape[0]), (255,255,255), thickness=10)
cv.imshow('Line', blank)

#Putting text
cv.putText(blank, "Jesmin", (blank.shape[1]//2, blank.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 2.0, (255,255,255), thickness=1)
cv.imshow('Text', blank)

cv.waitKey(0)










