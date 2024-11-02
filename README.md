AgeDetection (연령 판단 모델)

OpenCV 와 dlib를 사용하여 얼굴 인식
- dliv : 이미지 처리 및 기계 학습, 얼굴인식 등을 할 수 있는 c++로 개발된 고성능의 라이브러리
  <h4> -> 카메라에서 사람인식 후 이미지 전송 코드에서 제거 예정</h4>
age_deploy.prototxt 가중치 모델 파일 <br>
age_net.caffemodel 환경 파일

detection.py 실행 방법 
- python .\detection.py [예측 이미지]

※ dlib 이용 시 아나콘다(가상환경 실행) 필요

