# 💻 무선네트워크 프로젝트 C반 1조


## 조원 : 김 산(RealSan1), 김민수(NanHangBok), 조영철(yeoncheoljo), 이선호(SolarHO)

<hr>

# 🚀프로젝트 주제
- OpenCV를 통한 얼굴 인식과 AI 모델판단(성별, 연령, 악세서리) 맞춤형 옥외 광고 시스템

# 📃구현 계획
- 카메라 모듈과 라즈베리파이의 연동
- 피사체 속성 구분 AI모델(성별, 연령, 악세서리) 구축
- 필요 광고 데이터를 저장하기 위한 Googel Cloud Storage 구축 및 광고 데이터 저장
- 판단 데이터를 이용한 실시간 광고 웹 페이지 구성(Django 활용)

# 🛠️주요 기술 및 장치
- 라즈베리파이 5
- 카메라모듈(ENTUS WC33 Full HD 360)
- OpenCV
- Google Cloud Storage
- Django

# 👩🏻‍💻역할분담
- 김 산: 연령대 구분 AI 모델 설계 및 개발, 맞춤 광고 추천 로직 설계 및 개발
- 김민수: 남녀구분 AI 모델 설계 및 개발, 악세서리 인식 AI 모델 설계 및 개발
- 조영철: 카메라 모듈과 라즈베리파이의 연동, AI모델 적용과 Django 서버와의 연동 및 테스트
- 이선호: 클라우드 스토리지 구축 및 Django 서버와 연동, 직관적 광고 웹 페이지 개발

# 🏗️시스템 아키텍처
![시스템 아키텍처 drawio](https://github.com/user-attachments/assets/47ff527d-23d6-4266-86c8-66ca3050df6d)
- __인식부:__ 광고가 노출되는 모니터를 바라보고 있는 사람을 인식하여 사진을 촬영 후 판단부로 전달
- __판단부:__ 촬영된 사진을 판단모델을 이용하여 연령, 성별, 착용 아이템을 구분하여 맞춤 광고를 매핑 후 서버에 전달
- __서버:__ 가동 시 클라우드 스토리지에서 광고 이미지를 다운로드, 판단 결과로 전달받은 맞춤 형 광고 이미지를 실질적 웹 페이지에 표시

# 완료 피드백
- Success
> AI 판단 모델(연령, 성별, 악세서리) 개발 완료
> 클라우드 스토리지에서 광고 이미지 업로드와 웹 페이지 로딩 테스트 완료
> 카메라 모듈을 통한 실질적 모델 테스트 완료

- Exception
> 악세서리 판단 AI 모델의 연동 실패

<hr>

# [GenderDetection (성별 판단 모델)](https://github.com/SolarHO/inhatc-24-1/tree/main/Detect)
OpenCV를 통해 얼굴 인식 <br>
CNN구조를 통해 성별 추론
#### 사용 코드
```
model = Sequential([
    Input(shape=(200, 200, 3)),  # 입력 데이터 / 200,200 사이즈 3개의 채널 (RGB 컬러)
    Conv2D(36, kernel_size=3),  # 36개의 필터 사이즈 3*3
    BatchNormalization(),  # 모델 학습 안정화
    Activation('relu'),  # relu 활성화 함수 사용
    MaxPooling2D(pool_size=3, strides=2),  # 다운샘플링 3*3 사이즈로 2칸씩 이동
    Conv2D(64, kernel_size=3),  # 64개의 필터 사이즈 3*3
    BatchNormalization(),
    Activation('relu'),
    MaxPooling2D(pool_size=3, strides=2),
    Conv2D(128, kernel_size=3),  # 128개의 필터 사이즈 3*3
    BatchNormalization(),
    Activation('relu'),
    MaxPooling2D(pool_size=3, strides=2),
    Conv2D(256, kernel_size=3),  # 256개의 필터 사이즈 3*3
    BatchNormalization(),
    Activation('relu'),
    MaxPooling2D(pool_size=3, strides=2),
    Conv2D(512, kernel_size=3),  # 512개의 필터 사이즈 3*3
    BatchNormalization(),
    Activation('relu'),
    MaxPooling2D(pool_size=3, strides=2),
    Flatten(),  # 다차원 데이터를 1차원 벡터로 변환
    Dropout(0.25),  # 오버피팅(과적합) 방지 
    Dense(512, activation='relu'),  # Dense 안전연결레이어
    Dropout(0.5),
    Dense(2, activation='softmax', name='gender') # 출력 데이터 남성 여성 2개
])
```
<hr>

# [AgeDetection (연령 판단 모델)](https://github.com/SolarHO/inhatc-24-1/tree/main/ageDetection)

OpenCV와 dlib를 사용하여 얼굴 인식
- dliv : 이미지 처리 및 기계 학습, 얼굴인식 라이브러리
- age_deploy.prototxt 가중치 모델 파일
- age_net.caffemodel 환경 파일

### 연령목록
['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
- 나이가 비슷한 사람들 사이에서는 차이를 구별불가, 비슷한 얼굴 특징을 공유하는 연령대를 하나의 그룹화
- 그룹으로 나누면 모델이 연령 범위 내에서 오차를 더 쉽게 관리


### detection.py 실행 방법 
- python .\detection.py [예측 이미지]

![test](https://github.com/user-attachments/assets/8b2414f4-f430-4e1f-b614-d0a6d6097ef3)


※ dlib 이용 시 아나콘다(가상환경 실행) 필요

### ETC
- MiVOLO: Multi-input Transformer for Age and Gender Estimation (코넬 대학)
- 얼굴 이미지가 보이지 않더라도 몸 전체 이미지를 활용해 나이와 성별을 동시에 예측할 수 있는 모델
- 얼굴과 몸 정보를 동시에 사용할 때 성능이 더욱 향상

### 비전 트랜스포머 
- 글로벌 관계 학습(트랜스포머의 셀프 어텐션 사용)
- 작은 이미지 패치를 독립적으로 처리 후 관계 학습
- 대량의 데이터에서 뛰어난 성능 발휘

# 아이템 검출

## [CapDetection (모자 인식 모델)](https://github.com/SolarHO/inhatc-24-1/tree/main/cap_detect_model)
## [AccessoryDetection (악세사리 인식 모델)](https://github.com/SolarHO/inhatc-24-1/tree/main/accessory_detect)

YOLOv5 모델 사용
- YOLO : Object Detection Framework 중 하나
- 실시간 객체 탐지
- 이미지와 객체의 위치정보가 담겨있는 라벨링 데이터를 통해 학습
- 데이터 형태 예시)
  - 5 0.379369 0.419819 0.035085 0.081811
  - 5 0.577118 0.412881 0.032533 0.081332
  - nc: 6  # 총 클래스 개수
  - names: ['Background', 'Hat', 'Glasses frame', 'Sunglasses', 'Necklace', 'Earrings']
<br>
악세사리 인식 모델
- 목걸이, 귀걸이, 선글라스, 안경테 인식
<br>

### 모자 검출 Image 및 인식률
![cap1](https://github.com/user-attachments/assets/c177c6ae-e8ed-43d2-8e99-2276f6e00919)

### 악세사리 검출 Image 및 인식률
![ac](https://github.com/user-attachments/assets/2d2c405c-e053-4e29-87a4-ac74e1e69cf0)

<hr>

# [Recommendation (광고 추천)](https://github.com/SolarHO/inhatc-24-1/tree/main/recommendation)
- 콘텐츠 기반 필터링
- CountVectorizer와 cosine_similarity를 이용한 광고 추천
  - CountVectorizer : 텍스트 데이터를 숫자 벡터(행렬)로 변환
  - Cosine Similarity : 두 벡터 간의 각도를 기반으로 하며, 0에서 1 사이의 값을 반환
 
![콘첸츠 기반](https://github.com/user-attachments/assets/ea0324e0-839a-4d7e-a499-8f5c56501c66)

### 장점
- 새로운 사용자라도 선호도를 추론하지 않아도 추천 가능
- 제품 간의 텍스트 정보를 활용하므로 데이터 요구사항이 비교적 낮음

### 단점
- 입력된 제품의 정보에 국한되므로 추천 범위가 제한적
 
### 임베딩과 코사인 유사도의 차이
|특징|임베딩(Embedding)|코사인 유사도(Cosine Similarity)|
|---|---|---|
|기능|데이터를 벡터로 변환 (데이터 표현 방법)|두 벡터 간의 유사도를 측정|
|입력|고차원 데이터(텍스트, 이미지 등)|두 벡터|
|출력|벡터(임베딩 벡터)|유사도 값 (0 ~ 1 또는 -1 ~ 1)|
|적용 단계|모델 학습 또는 데이터 전처리 단계에서 생성|모델 학습 후 또는 추천/검색 단계에서 활용|
|사용 사례|추천 시스템, 텍스트/이미지 특징 표현, 데이터 압축|검색 엔진, 추천 시스템, 클러스터링, 문서/문장/단어 유사도 계산|

- 코사인 유사도(Cosine Similarity) 사용 이유
  - CountVectorizer를 사용하면 고차원적인 임베딩 공간을 구축할 필요 없이 텍스트의 핵심적인 패턴을 포착
  - 임베딩을 통한 고차원 벡터 공간 생성은 종종 더 복잡하고 계산량이 많을 수 있으며, 이로 인해 대규모 데이터셋에서 처리 성능에 영향을 줄 수 있습니다.
  - 코사인 유사도를 사용한 벡터화는 계산 효율성을 높음

### [Recommendation.csv](https://github.com/SolarHO/inhatc-24-1/blob/main/recommendation/data/recommender.csv)

|Index|Age_Group|Sex|Keywords|Product|
|---|---|---|---|---|
|8|8-12|Male|게임 리그오브레전드 메이플스토리 브롤스타즈|문화상품권
|9|8-12|Male|게임 블럭 스티브 크리퍼|마인크래프트
|10|8-12|Female|음악 예술|피아노
|11|8-12|Female|아이돌 다꾸 아이브|다이어리
|12|8-12|Female|캐릭터 토끼 유아가방 어린이 패션|가방
|13|8-12|Female|어린이 패션 햇빛|모자
|14|8-12|Female|캐릭터 돈 선물|캐릭터지갑
<br>

1. 정확성을 높이기 위한 Kewwords, Product 결합
  -  df['Combined'] = df['Product'] + ' ' + df['Keywords'].fillna('')

2. CountVectorizer로 텍스트 벡터화
  -  count_vector = CountVectorizer(ngram_range=(1, 3))

3. 코사인 유사도 계산
  - combined_c_sim = cosine_similarity(c_vector_combined, c_vector_combined).argsort()[:, ::-1]

### 모델 인식 상태(카메라 인식 상태에 따른 처리)

- 연령대 O 성별 O 착용제품 O
  + 연령대와 성별을 기준으로 제품 추천
  <pre>
  <code>
    product = recommender(Age_Group='8-12', Sex='Female', Item="가방") 
    print(product) # 모자
  </code>
</pre>

- 연령대 O 성별 X 착용제품 O
  + 연령대를 기준으로 제품 추천
  <pre>
  <code>
    product = recommender(Age_Group='8-12', Item="가방")
    print(product) # 캐릭터지갑
  </code>
</pre>

- 연령대 O 성별 X 착용제품 X
  + 연령대만을 기준으로 제품 추천
  <pre>
  <code>
    product = recommender(Age_Group='8-12')
    print(product) # 닌텐도
  </code>
</pre>

- 연령대 X 성별 X 착용제품 X
  + Table에서 랜덤으로 제품 추천
  <pre>
  <code>
    product = recommender()
    print(product) # 골프
  </code>
</pre>

## 협업 필터링
- 사용자 간의 행동(예: 구매, 클릭 등)이나 사용자와 아이템 간의 관계 데이터를 기반으로 추천
- 사용자 또는 제품이 적을 경우(특히 신규 서비스), 추천 품질이 낮음
 
# [CameraModule (카메라 모듈 연동)](https://github.com/SolarHO/inhatc-24-1/tree/main/camera)

1. 카메라 피드는 OpenCV를 사용하여 초기화되며, 피드에 접근할 수 없는 경우 오류메시지와 함께 프로그램이 종료됩니다.
2. 사진을 찍는 빈도는 5초로 설정했으며, 얼굴이 감지되면 각 얼굴의 경계 상자 좌표를 사용하여 얼굴 영역을 자릅니다.
3. 감지된 얼굴을 통해 사전 훈련된 모델을 사용하여 연령과 성별을 예측합니다.
4. 예측한 성별예측의 정확도가 80%이상일 경우 광고를 추천받아 Django페이지의 광고를 업데이트 합니다.
5. 2-4번 과정이 반복되며, 'q'입력시에 프로그램을 종료합니다.

#### 카메라모듈 최종코드
```
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

        #정확도가 80이상일떼만 광고 변경
        if(confidence >= 80) :
            prd, img = recommender_image.recommender(Age_Group=age, Sex=gender, Item=None)
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
```
