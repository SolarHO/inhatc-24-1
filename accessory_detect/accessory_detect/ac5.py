# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 00:50:52 2024

@author: cczzs
"""

import torch

# 모델 경로
model_path = r'.\weights\best.pt'

# 테스트 이미지 경로
test_image_path = r'.\ac3.jpg'

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

results = model(test_image_path)

# 결과 데이터프레임 추출
detections = results.pandas().xyxy[0]

# 검출 대상
accessory_classes = ['Glasses', 'Sunglasses', 'Necklace', 'Earring']

# 신뢰도 기준 설정
confidence_threshold = 0.7

for accessory in accessory_classes:
    accessory_detections = detections[detections['name'] == accessory] # 악세사리 검출
    
    if not accessory_detections.empty:
        # 신뢰도 이상 악세사리 필터링
        confidence_detections = accessory_detections[accessory_detections['confidence'] >= confidence_threshold]
        
        if not confidence_detections.empty:
            print(f"'{accessory}' 검출됨:")
            for index, row in confidence_detections.iterrows():
                print(f"    신뢰도: {row['confidence']*100:.2f}%")
        else:
            print(f"'{accessory}' 검출됨 (신뢰도 {confidence_threshold*100}% 이상 없음).")
    else:
        print(f"'{accessory}' 검출되지 않음.")
