import mediapipe as mp
import cv2
from random import randrange as r
import time



class FACEMESHDETECTOR():
    def __init__(self, staticMode = False, maxFaces=4, minDetectionCon=0.5, minTrackCon=0.5):
        self.staticMode = staticMode 
        self.maxFaces = maxFaces
        self.minDetectionCon=minDetectionCon
        self.minTrackCon = minTrackCon
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode=self.staticMode,
            max_num_faces=self.maxFaces,
            min_detection_confidence=self.minDetectionCon,
            min_tracking_confidence=self.minTrackCon
        )
        self.drawSpecs = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):


        self.imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgrgb)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.drawSpecs.color = (r(255), r(255), r(255))
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_TESSELATION, self.drawSpecs, self.drawSpecs)
                face = []
                for i, lm in enumerate(faceLms.landmark):
                    # print(lm)
                    ih, iw, ic = img.shape
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    # print(x,y)
                    cv2.putText(img, str(i), (x,y), cv2.FONT_HERSHEY_PLAIN,0.5, (r(255),r(255),r(255)), 1)

                    face.append([x,y])
                faces.append(face)
        return img, faces

    


def main():
    cap = cv2.VideoCapture("ai.projects\\computer-vision\\face-detection\\production_id_3762907 (540p).mp4")


    pTime = 0
    detector = FACEMESHDETECTOR()

    while True:
        success, img = cap.read()

        img, faces = detector.findFaceMesh(img)
        if len(faces) != 0:
            print(len(faces))
        cTime = time.time()
        fps= 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN,4, (r(255),r(255),r(255)), 2)


        cv2.imshow("z-mesh", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()