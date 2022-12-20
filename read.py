import cv2 as cv

img = cv.imread('D:\Open_CV_FCC\images\Porimoni.jpg')


def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


cv.imshow('She', rescaleFrame(img))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', rescaleFrame(gray))


cv.waitKey(0)
