import cv2 as cv 

img = cv.imread('D:\Open_CV_FCC\images\cows.jpeg')
dimensions = (450, 325)

img_resized = cv.resize(img, dimensions)

cv.imshow('Cows', img_resized)

# Converting to grayscale
gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#not_gray = cv.cvtColor(img_resized, cv.COLOR_BGR2HSV)
#cv.imshow('Not_Gray', not_gray)

# Blur
blur = cv.GaussianBlur(img_resized, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#extra_blur = cv.GaussianBlur(img_resized, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Extra_Blur', extra_blur)

#Edge Cascade
canny = cv.Canny(blur, 100, 200)
cv.imshow('Canny Edges', canny)

#Dilated the Image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#Cropping images
cropped = img_resized[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)