import cv2 as cv 
import numpy as np

img = cv.imread('D:\Open_CV_FCC\images\Trisha.jpg')
cv.imshow('trisha',img)

blank = np.zeros((500,500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

#blank[200:300, 300:400] = 0, 0, 255
#cv.imshow('Green', blank)

cv.rectangle(blank, (200,200), (400, 400), (230, 140, 110), thickness=-1)
cv.imshow('Rectiangle', blank)

cv.circle(blank, (160, 160), 60, (140, 0, 200), thickness=4 )
cv.imshow('Circle', blank)

cv.line(blank, (200, 200), (400, 400), (0, 0, 255), thickness=2)
cv.imshow('With Line', blank)
# we also can put there text, other stuffs like those

cv.waitKey(0)