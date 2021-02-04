<u>Reading Files</u>

```python
import cv2 as cv

#Reading Images
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)
cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True:
	isTrue, frame = capture.read()
	cv.imshow('Video', frame)
	if cv.waitKey(20) & 0xFF==ord('d'):
		break
capture.release()
cv.destroyAllWindows()
```



<u>Resizing And Rescaling Images And Video Frames</u>

```python
import cv2 as cv

# img = cv.imread('../Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)
    
# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
```

<u>Drawing Shapes And Text</u>

```python
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #np.zeros((height, width, color channnels), ...)
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[200:300, 300:400] = 0,0,255 
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Jason!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
```

<u>5 Essential Functions In OpenCV</u>

```python
import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
```

<u>Image Transformations</u>

```python
import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
```

# More on Edge Detection

Grayscale the image first (REQUIRED)

```python
#Laplacian Edge Detection
lap = cv.Laplacian(image, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) #absolute such that gradients are all positive
#Gradients can be negative or positive depending on black to white and white to black
#We make all of those gradients positive
#Show the image now using imshow

#Sobel Edge Detection
#Sobel can be applied on x and y axes.
#We will create one for x axis and another for y axis and then combine them together
sobelx = cv.Sobel(image, cv.CV_64F, 1, 0) #1 is x direction, 0 is y direction
sobely = cv.Sobel(image, cv.CV_64F, 0, 1)
#Show these two images using imshow

#Now combine the sobels
combined_sobel = cv.bitwise_or(sobelx, sobely) #Explain bitwise or

#Show canny as well and explain how canny is a multistep processing(advanced algorithm)
```

# Face DETECTION With Haar Cascades

<u>To be continued</u>

