import os
import face_recognition
import numpy as np


class FaceDetect :
    def __init__(self, srcImgPath) :
        self.srcFaces = []
        self.srcImgPath = srcImgPath
        self.init_res_imgs()
    
    # 加载数据库的图像
    def init_res_imgs(self) :
        for i in os.listdir(self.srcImgPath) :
            self.srcFaces.append(self.encode_face_path(os.path.join(self.srcImgPath, i)))
    
    # 比对人脸
    def compare_face(self, compareFace) :
        try:
            res = face_recognition.compare_faces(self.srcFaces, compareFace,tolerance=0.5)
            print(res)

            return not (np.sum(res)==0)
        except Exception as e:
            return False
    
    # 编码图像
    def encode_face_path(self, facePath) :
        try:
            
            return face_recognition.face_encodings(face_recognition.load_image_file(facePath))[0]
        except Exception as e:
            return None
    
    # 编码图像
    def encode_face_image(self, faceImg) :
        reg = face_recognition.face_encodings(faceImg)
        if reg :
            return reg[0]
    