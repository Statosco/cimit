import mediapipe as mp
import cv2
from random import randrange
import time

cap = cv2.VideoCapture("ai.projects\\computer-vision\\face-detection\\production_id_3762907 (540p).mp4")
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.8)

while True:
    success, img = cap.read()

    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRgb)
    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbx = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)

            cv2.rectangle(img, bbx, (randrange(255), randrange(255), randrange(255)), 2)
            cv2.putText(img, f'{int(detection.score[0]* 100)}%', (bbx[0],bbx[1]-20), cv2.FONT_HERSHEY_PLAIN,3, (randrange(255), randrange(255), randrange(255), 2) )


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN,3, (randrange(255), randrange(255), randrange(255), 2) )

    cv2.imshow("z-video", img)
    cv2.waitKey(1)
