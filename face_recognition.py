import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('D:\Open_CV_FCC\haar_face.xml')
people = ['Mbbappe' ,'Messi', 'Musiala']

#features = np.load('features.npy')
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_tarin.yml')

img = cv.imread(r'D:\footballer_pic\messi pic - Google Search\le.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)