import os
import cv2 as cv
import numpy as np

people = ['Mbbappe' ,'Messi', 'Musiala']
DIR = r'D:\Open_CV_FCC\images\Footballer'

haar_cascade = cv.CascadeClassifier('D:\Open_CV_FCC\haar_face.xml')


features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person) 

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            #print(img_path)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
print(f'Length of Features = {len(features)}')
print(f'Length of Labels = {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
face_recognizer.save('face_tarin.yml ')
np.save('features.npy', features)
np.save('labels.npy', labels)