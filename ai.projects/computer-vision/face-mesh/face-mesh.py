import mediapipe as mp
import cv2
from random import randrange as r
import time

cap = cv2.VideoCapture("ai.projects\\computer-vision\\face-detection\\production_id_3762907 (540p).mp4")
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpecs = mpDraw.DrawingSpec(thickness=1, circle_radius=1)



while True:
    success, img = cap.read()

    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgrgb)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION, drawSpecs, drawSpecs)

            for lm in faceLms.landmark:
                print(lm)
                ih, iw, ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih)
                print(x,y)


    cTime = time.time()
    fps= 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN,4, (r(255),r(255),r(255)), 2)


    cv2.imshow("z-mesh", img)
    cv2.waitKey(1)