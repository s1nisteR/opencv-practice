import cv2 as cv


image = cv.imread('Photos/park.jpg')
cv.imshow('Original Window', image)



gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscaled Image', gray)


blurredImage = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT) #(25,25) is the kernel size
                                                                #Can only be positive and odd numbers
                                                                #Keep both numbers same
                                                                #Controls the AMOUNT of blurring
cv.imshow("Blurred Image", blurredImage )

cannyImage = cv.Canny(blurredImage, 100, 175) #(edges detection casess used. The ammounts of blurreing controls the amount of details in the canny image(age detection images)
cv.imshow('Original Edge Cascade', cannyImage)


dilated = cv.dilate(cannyImage , (7,7), iterations=3)#(edges lines will be thicker than normal, erosion:opposite of dialted images)
cv.imshow('Dilated', dilated)

eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded Image', eroded)


cv.waitKey(0)
