import mediapipe as mp
import cv2
from random import randrange
import time


class FACEDETECTOR():
    def __init__(self, minDetectionCon= 0.5):
        self.minDetectionCon = minDetectionCon


        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(minDetectionCon)


    def findFaces(self, img, draw=True):
        imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRgb)

        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbx = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)

                bboxs.append([bbx, detection.score])
                img = self.fancyDraw(img,bbx)

                cv2.putText(img, f'{int(detection.score[0]* 100)}%', (bbx[0],bbx[1]-20), cv2.FONT_HERSHEY_PLAIN,3, (randrange(255), randrange(255), randrange(255)),2)
        return img, bboxs
    

    def fancyDraw(self, img, bbox, l=30, t=5, rt=1):
        x, y, w, h = bbox
        x1,y1 = x+w, y+h

        cv2.rectangle(img, bbox, (randrange(255), randrange(255), randrange(255)), 2)

        cv2.line(img, (x,y), (x+l,y),(0, 255,0),rt)
        #top left
        cv2.line(img, (x,y), (x+l,y),(0, 255,0),t)
        cv2.line(img, (x,y), (x,y+l),(0, 255,0),t)
        #top right
        cv2.line(img, (x1,y), (x1-l,y),(0, 255,0),t)
        cv2.line(img, (x1,y), (x1,y+l),(0, 255,0),t)


        #bottom left
        cv2.line(img, (x,y1), (x+l,y1),(0, 255,0),t)
        cv2.line(img, (x,y1), (x,y1-l),(0, 255,0),t)
        #bottom right
        cv2.line(img, (x1,y1), (x1-l,y1),(0, 255,0),t)
        cv2.line(img, (x1,y1), (x1,y1-l),(0, 255,0),t)

        return img



def main():
    cap = cv2.VideoCapture("ai.projects\\computer-vision\\face-detection\\production_id_3762907 (540p).mp4")
    pTime = 0

    detect = FACEDETECTOR()
    while True:
        success, img = cap.read()
        img, bboxs = detect.findFaces(img)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f'FPS {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (randrange(255), randrange(255), randrange(255)), 2)

        cv2.imshow("z-video", img)
        cv2.waitKey()


if __name__ == '__main__':
    main()