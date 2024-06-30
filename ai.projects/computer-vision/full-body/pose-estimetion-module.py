import cv2
import mediapipe as mp
import time
from random import randrange

class poseDetector():
    def __init__(self, mode = False, upBody=False,
                 smooth=True,detectionCon=0.5, trackingCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils

        self.pose = self.mpPose.Pose(
                static_image_mode=self.mode,
                smooth_landmarks=self.smooth > 0.0,  # Convert to boolean
                min_detection_confidence=self.detectionCon,
                min_tracking_confidence=self.trackingCon)        
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def getPosition(self, img, draw=True):
        lmList = []

        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 10, (randrange(256), randrange(256), randrange(256)))
        return lmList


def main():
    cap = cv2.VideoCapture('ai.projects/computer-vision/full-body/pexels_videos_2785535 (540p).mp4')
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.getPosition(img)

        print(lmList)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 4)


        cv2.imshow("z-runner", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()