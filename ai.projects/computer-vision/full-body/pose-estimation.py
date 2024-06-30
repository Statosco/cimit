import cv2
import mediapipe as mp
import time
from random import randrange

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils

pose = mpPose.Pose()

cap = cv2.VideoCapture('ai.projects/computer-vision/full-body/pexels_videos_2785535 (540p).mp4')
pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx,cy), 10, (randrange(256), randrange(256), randrange(256)))


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 4)


    cv2.imshow("z-runner", img)
    cv2.waitKey(1)