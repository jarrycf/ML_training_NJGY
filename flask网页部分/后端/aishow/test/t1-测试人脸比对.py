from faceDetect import FaceDetect

import cv2
cap=cv2.VideoCapture(0)
faceDetect = FaceDetect('../data/img')

while True:
    res,frame=cap.read()
    if res:
        frame=cv2.flip(frame,1)
        cv2.imshow('res',frame)
    if cv2.waitKey(1)==ord('q'):
        try:
            comp = faceDetect.encode_face_image(frame)
            print(faceDetect.compare_face(comp))
        except Exception as e:
            print(e)
    elif cv2.waitKey(1) == ord('a') :
        cap.release()
