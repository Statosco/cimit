import cv2
from random import randrange

faceDEtector = cv2.CascadeClassifier('ai.projects/har-cascade-project/haarcascade_frontalface_default.xml')
smileDetector = cv2.CascadeClassifier('ai.projects/har-cascade-project/smile_cascade.xml')
eye = cv2.CascadeClassifier('ai.projects/har-cascade-project/haarcascade_eye.xml')


webcam = cv2.VideoCapture('ai.projects/har-cascade-project/stock-footage-stylish-zoom-out-montage-of-smiling-mixed-race-woman-becoming-part-of-multi-ethnic-group-of-people.webm')

while True:
    seccefulFrame, frame = webcam.read()

    if not seccefulFrame:
        break
    greyScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDEtector.detectMultiScale(greyScale)

    eyeDetecter = eye.detectMultiScale(greyScale, scaleFactor=1.3, minNeighbors=10)
    

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 1)


        theFace = frame[y:y+h, x:x+w]

        faceGreyScale = cv2.cvtColor(theFace, cv2.COLOR_BGR2GRAY)
        smiles = smileDetector.detectMultiScale(faceGreyScale, scaleFactor=1.7, minNeighbors=20)

        if len(smiles) > 0:
            cv2.putText(frame, 'smiling', (x, y+h+40), fontScale=1,fontFace=cv2.FONT_HERSHEY_PLAIN, color=(randrange(256), randrange(256), randrange(256)))

    for (x__, y__, w__, h__) in eyeDetecter:
        cv2.rectangle(frame, (x__, y__), (x__ + w__, y__ + h__), (randrange(256), randrange(256), randrange(256)), 1)

        # for(x_, y_, w_, h_) in smiles:
            # cv2.rectangle(theFace, (x_, y_), (x_ + w_, y_ + h_), (randrange(256), randrange(256), randrange(256)), 1)

     
    cv2.imshow('z-faces', frame)

    key =cv2.waitKey(1)
    if key==81 or key ==113:
        break
    
webcam.release()     

