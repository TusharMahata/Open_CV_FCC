import cv2 as cv

#img = cv.imread('D:\Open_CV_FCC\images\Pormoni.jpg')

#cv.imshow('She', img)
# reading videos

capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()