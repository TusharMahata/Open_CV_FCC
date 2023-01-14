import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#img = cv.imread('D:\Open_CV_FCC\images\Pormoni.jpg')

#cv.imshow('She', img)
# reading videos

capture = cv.VideoCapture('videos/dog.mp4')
count = 0
blank = np.empty((540,960, 3), np.dtype('uint8'))
print(blank.shape)
#cv.imshow('blank', blank)

#exit()
while True:
    isTrue, frame = capture.read()
    #print(frame.shape)
    #cv.drawFrameAxes(blank, frame, -1, (155, 155, 0), 2)
    pic = cv.imwrite(".\create_images\/"+str(count)+'.jpg', frame)
    #pic = cv.imread('D:\Open_CV_FCC\create_images')
    cv.imshow('all', pic)
    count = count + 1
    #print(frame.shape)
    #blank[count] = frame
    if count == 10:
        break

    #print(type(frame))
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    #cv.imshow('Video', gray)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
def something(pic):
      
    imgplot = plt.imshow(pic)
c= 0
while(c<=10):
    pic = mpimg.imread('.\create_images\0.jpg')
    something(pic)
    #cv.imshow(str(c), pic)
    c = c+1
    
    #cv.waitKey(5000)
#cv.waitKey(0)




