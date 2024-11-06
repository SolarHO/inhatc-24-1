# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:14:35 2024

@author: cczzs
"""

# YOLOv5 학습 실행
import subprocess
import os

# 경로 설정
root_dir = './cap-dataset'  # 데이터셋 폴더 경로
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
# YOLOv5 학습 실행
result = subprocess.run([
    'python', 'train.py',
    '--img', '640',
    '--batch', '16',
    '--epochs', '50',
    '--data', os.path.join(root_dir, 'dataset.yaml'),
    '--weights', 'yolov5s.pt',
    '--name', 'cap_detection',
    '--workers', '0'
], capture_output=True, text=True)

print(result.stdout)
print(result.stderr)