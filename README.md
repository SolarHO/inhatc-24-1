# Djnago 이용 직관적 광고 노출 웹 페이지

1. Django와 Google cloud storage(GCS)를 연결
2. 서버 가동시 GCS의 inhatc_test 버킷 아래 AD 폴더에 있는 모든 이미지 내부 폴더에 저장
3. 얼굴 분석 후 넘겨받은 변수로 웹 페이지상 노출되는 광고 이미지 실시간으로 갱신

- Cloud console URL:
https://console.cloud.google.com/storage/browser/inhatc_test
- GCS 호출 URL = https://storage.cloud.google.com
- GCS bucket name = 'inhatc_test'

## Google Cloud Storage

![스크린샷 2024-11-16 215031](https://github.com/user-attachments/assets/ca7a7602-7a6d-42f3-94e9-06214bc62fb4)


## Django page

![20241125_03h07m29s_grim](https://github.com/user-attachments/assets/39a4d74a-e9a4-48d4-a069-ffda924cb5b5)
