import cv2 as cv 

img = cv.imread('D:\Open_CV_FCC\images\stars.jpeg')
cv.imshow('Cats', img)
print(type(img))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#threshold
ret, thresh = cv.threshold(blur, 50, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

#Canny edges
canny = cv.Canny(thresh, 125, 175)
cv.imshow('Canny Edges', canny)
print(f'{len(canny)} canny(s) found!')



#contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
#cv.imshow('contours', hierarchies)

cv.waitKey(0)