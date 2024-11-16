import torch

model_path = './best.pt'

test_image_path = './cap1.jpg'

model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

results = model(test_image_path)

# 결과 데이터프레임 추출
detections = results.pandas().xyxy[0]

cap_detections = detections[detections['name'] == 'cap'] # cap 클래스 검출


confidence_percent = 0.9

# 모자 검출 여부와 확률 출력
if not cap_detections.empty:
    # 검출 되는지만
    if cap_detections[cap_detections['confidence'] >= confidence_percent] is not None:
        print("검출됨")
    
    # ****************검출 후 신뢰도까지**********************
    # confidence_detections = cap_detections[cap_detections['confidence'] >= confidence_percent]
    # if not confidence_detections.empty:
    #     for index, row in confidence_detections.iterrows():
    #         print(f"모자 검출됨: {row['confidence']*100:.2f}%")
    # else:
    #     print("90% 이상의 신뢰도로 검출된 모자가 없음")
    # ******************************************************
else:
    print("모자 검출되지 않음")