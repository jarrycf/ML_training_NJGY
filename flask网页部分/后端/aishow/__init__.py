import random

import cv2
import joblib
import numpy as np
from flask import Flask, render_template, Response, session, make_response, request
from .view.homeview import home
from .view.stuview import stu
from .view.medicalview import medical
from flask_cors import CORS
from .config import  config
from .utils.faceDetect import FaceDetect
faceDetect=FaceDetect('aishow/data/img')
model = joblib.load('aishow/model/my_ridge.pkl')
def create_app():
    app=Flask(__name__)
    app.config.from_object(config)
    app.secret_key='hjh'
    CORS().init_app(app)
    @app.route('/validate',methods=['GET', 'POST'])
    def index():
        file = request.files.getlist('imgData')[0]
        # image1 = cv2.imdecode(np.asarray(bytearray(data['img1'].read()), dtype='uint8'), cv2.IMREAD_COLOR)
        file.save('aishow/data/face.png')
        res=faceDetect.compare_face(faceDetect.encode_face_path('aishow/data/face.png'))
        return f"{res}"
    @app.route('/index',methods=['GET', 'POST'])
    def html():
      return render_template('index.html')
    @app.route('/predict', methods=['POST', 'GET'])
    def predict() :
        print(request.form)
        data = request.form
        transaction_date = float(data['transaction_date'])
        house_age = float(data['house_age'])
        MRT_station = float(data['MRT_station'])
        convenience_stores = float(data['convenience_stores'])
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        result = model.predict(
            [[transaction_date, house_age, MRT_station, convenience_stores, latitude, longitude]])[0]
        return render_template('index.html', **locals())
    @app.route('/addFace', methods=['GET', 'POST'])
    def addFace() :
        file = request.files.getlist('imgData')[0]
        # image1 = cv2.imdecode(np.asarray(bytearray(data['img1'].read()), dtype='uint8'), cv2.IMREAD_COLOR)
        file.save(f'aishow/data/img/face{random.randint(10,1000)}.png')
        return "True"
    app.register_blueprint(stu,url_prefix='/stu')
    app.register_blueprint(home,url_prefix='/home')
    app.register_blueprint(medical,url_prefix='/medical')
    return app