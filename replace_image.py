# replace_image.py
import os
import shutil
from google.cloud import storage
from django.conf import settings

#서버 가동시 클라우드 스토리지에 있는 모든 광고 이미지를 저장하는 함수
def download_gcs_images():
    client = storage.Client(credentials=settings.GS_CREDENTIALS)
    bucket = client.bucket(settings.GS_BUCKET_NAME)
    blobs = bucket.list_blobs(prefix=settings.GS_AD_FOLDER)  # ad 폴더 아래 파일들 가져오기

    if not os.path.exists(settings.LOCAL_AD_FOLDER):
        os.makedirs(settings.LOCAL_AD_FOLDER)  # 로컬 폴더가 없으면 생성

    for blob in blobs:
        if not blob.name.endswith('/'):  # 폴더가 아닌 경우에만 다운로드
            local_file_path = os.path.join(settings.LOCAL_AD_FOLDER, os.path.basename(blob.name))
            blob.download_to_filename(local_file_path)
            print(f"Downloaded {blob.name} to {local_file_path}")

# def replace_image():
#     new_image_path = './ad_images/ad.'  # 새 이미지 경로
#     static_image_path = os.path.join('net_Prj', 'static', 'images', 'ad.png')  # static 이미지 경로(페이지에 표시될 이미지)
#     # 기존 이미지를 새 이미지(new_image_path)로 교체
#     shutil.copy(new_image_path, './main/static/images/ad.png')
    
# replace_image()