# 💻 무선네트워크 프로젝트 C반 1조


## 조원 : 김 산(RealSan1), 김민수(NanHangBok), 조영철(yeoncheoljo), 이선호(SolarHO)

<hr>

# 🚀프로젝트 주제
- OpenCV를 통한 얼굴 인식과 AI 모델판단(성별, 연령, 악세서리) 맞춤형 광고 노출 시스템

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

# 진행사항

# 완료 피드백
-Success
> AI 판단 모델(연령, 성별, 악세서리) 개발 완료
> 클라우드 스토리지에서 광고 이미지 업로드와 웹 페이지 로딩 테스트 완료
> 카메라 모듈을 통한 실질적 모델 테스트 완료

-Exception
> 악세서리 판단 AI 모델의 연동 실패

# 결론

<hr>

# [GenderDetection (성별 판단 모델)](https://github.com/SolarHO/inhatc-24-1/tree/main/Detect)
OpenCV를 통해 얼굴 인식
CNN구조를 통해 성별 추론

<hr>

# [AgeDetection (연령 판단 모델)](https://github.com/SolarHO/inhatc-24-1/tree/main/ageDetection)

OpenCV와 dlib를 사용하여 얼굴 인식
- dliv : 이미지 처리 및 기계 학습, 얼굴인식 등을 할 수 있는 c++로 개발된 고성능의 라이브러리
  <h4> -> 카메라에서 사람인식 후 이미지 전송 (제거 예정)</h4>
age_deploy.prototxt 가중치 모델 파일 <br>
age_net.caffemodel 환경 파일

detection.py 실행 방법 
- python .\detection.py [예측 이미지]

![test](https://github.com/user-attachments/assets/8b2414f4-f430-4e1f-b614-d0a6d6097ef3)

※ dlib 이용 시 아나콘다(가상환경 실행) 필요

<hr>

# 아이템 검출

## [CapDetection (모자 인식 모델)](https://github.com/SolarHO/inhatc-24-1/tree/main/cap_detect_model)
## [AccessoryDetection (악세사리 인식 모델)](https://github.com/SolarHO/inhatc-24-1/tree/main/accessory_detect)

YOLOv5 모델 사용
- YOLO : Object Detection Framework 중 하나
- 실시간 객체 탐지
- 이미지와 객체의 위치정보가 담겨있는 라벨링 데이터를 통해 학습

악세사리 인식 모델
- 목걸이, 귀걸이, 선글라스, 안경테 인식

### 모자 검출 Image 및 인식률
![cap1](https://github.com/user-attachments/assets/c177c6ae-e8ed-43d2-8e99-2276f6e00919)

### 악세사리 검출 Image 및 인식률
![ac](https://github.com/user-attachments/assets/2d2c405c-e053-4e29-87a4-ac74e1e69cf0)

<hr>

# [Recommendation (광고 추천)](https://github.com/SolarHO/inhatc-24-1/tree/main/recommendation)

CountVectorizer와 cosine_similarity를 이용한 광고 추천

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
<br>
모델 인식 상태

- 연령대 O 성별 O 착용제품 O
  + 연령대와 성별을 기준으로 제품 추천
  <pre>
  <code>
    product = recommender(Age_Group='8-12', Sex='Female', Item="가방")
    print(product)
  </code>
</pre>

- 연령대 O 성별 X 착용제품 O
  + 연령대를 기준으로 제품 추천
  <pre>
  <code>
    product = recommender(Age_Group='8-12', Item="가방")
    print(product)
  </code>
</pre>

- 연령대 O 성별 X 착용제품 X
  + 연령대만을 기준으로 제품 추천
  <pre>
  <code>
    product = recommender(Age_Group='8-12')
    print(product)
  </code>
</pre>

- 연령대 X 성별 X 착용제품 X
  + Table에서 랜덤으로 제품 추천
  <pre>
  <code>
    product = recommender()
    print(product)
  </code>
</pre>

 
<hr>
