import cv2
import mediapipe as mp
import time
from random import randrange


cap = cv2.VideoCapture('ai.projects/computer-vision/handtracking/video (360p).mp4')

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
fps = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handsLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handsLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id  == 4:
                    cv2.circle(img, (cx, cy), 15, (randrange(256), randrange(256), randrange(256)), cv2.FILLED)

            mpDraw.draw_landmarks(img, handsLms, mpHands.HAND_CONNECTIONS)

    cTime = cv2.getTickCount()
    fps = cv2.getTickFrequency() / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 4)

    cv2.imshow("z-video", img)

    # Break the loop if the 'Esc' key is pressed
    if cv2.waitKey(1) == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
