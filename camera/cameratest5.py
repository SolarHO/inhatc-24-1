import cv2
import dlib
import numpy as np
from datetime import datetime, timedelta
from google.cloud import storage
from tensorflow.keras.models import load_model
from google.oauth2 import service_account
from tensorflow.keras.preprocessing.image import img_to_array
import recommender_image
import re

#장고 관련 모듈
import os
import shutil
from django.conf import settings

# 모델 파일 경로 설정
AGE_MODEL = 'weights/age_deploy.prototxt'
AGE_PROTO = 'weights/age_net.caffemodel'
GENDER_MODEL_PATH = 'gender_classification_cnn_last.h5'
MODEL_MEAN = (78.4263377603, 87.7689143744, 114.895847746)

# DNN 모델 로드
age_net = cv2.dnn.readNetFromCaffe(AGE_MODEL, AGE_PROTO)
gender_model = load_model(GENDER_MODEL_PATH)

# 나이 그룹 리스트
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

# 얼굴 검출 모델 로드
face_detector = dlib.get_frontal_face_detector()

# 카메라 설정
camera = cv2.VideoCapture(0)
capture_interval = 5  # 초 단위 캡처 간격
last_capture_time = datetime.now() - timedelta(seconds=capture_interval)

age, gender = None, None

def predict_age_and_gender(face):
    # 나이 예측
    blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN, swapRB=False)
    age_net.setInput(blob)
    age_preds = age_net.forward()
    age = ageList[age_preds[0].argmax()]
    age = age[1:-1]
    
    # 성별 예측
    face_resized = cv2.resize(face, (200, 200))
    face_resized = img_to_array(face_resized) / 255.0
    face_resized = np.expand_dims(face_resized, axis=0)
    gender_preds = gender_model.predict(face_resized)
    gender = "Female" if np.argmax(gender_preds) == 1 else "Male"
    confidence = np.max(gender_preds) * 100

    return age, gender, confidence
    
#장고 화면에 띄울 광고 이미지 변경    
def replace_image(img_path):
    static_image_path = os.path.join('net_Prj', 'static', 'images', 'ad.jpg')  # static 이미지 경로(페이지에 표시될 이미지)
    # 기존 이미지를 새 이미지(img_path)로 교체
    shutil.copy(img_path, '/home/inhatc/django/net_Prj/main/static/images/ad.jpg')

while True:


    ret, frame = camera.read()
    if not ret:
        print("Failed to capture frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)
    
    if faces is None :
        break
    
    if len(faces) > 0 and (datetime.now() - last_capture_time).total_seconds() >= capture_interval:
        last_capture_time = datetime.now()
        
        for face in faces:
            x, y, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
            face_img = frame[y:y2, x:x2]
            
            age, gender, confidence = predict_age_and_gender(face_img)

            # 얼굴 주변에 사각형 및 예측 결과 표시
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 200, 200), 2)
            cv2.putText(frame, f"{age}, {gender} ({confidence:.2f}%)", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # 이미지 저장
        #timestamp = last_capture_time.strftime('%Y%m%d_%H%M%S')
        #filename = f"person_detected_{timestamp}.jpg"
        #cv2.imwrite(filename, frame)
        #print(f"Image saved: {filename}")
        print(age)
        print(gender)
        print(confidence)

        prd, img = recommender_image.recommender(Age_Group='38-43', Sex='Female', Item=None)
        print(prd)
        print(img)
        
        replace_image(img)#장고 화면에 띄울 광고 이미지 변경
        image = cv2.imread(img)
        cv2.imshow('test',image)
        # #클라우드에 파일 업로드
        # image_path = f"/home/inhatc/project/{filename}"
        # bucket_name = "inhatc_test"
        # destination_blob_name = f"test/test_{timestamp}.jpg"
        # credentials_path = "/home/inhatc/project/fluted-polymer-440606-a2-450d3d134caa.json"
        
        # upload_image_to_gcs(image_path, bucket_name, destination_blob_name, credentials_path)
        
    cv2.imshow("Camera", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
