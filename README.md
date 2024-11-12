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
