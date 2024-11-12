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

def replace_image():
    # Define the path for the new image and the existing image in the static directory
    new_image_path = './ad_images/kirby.png'  # Replace this with the actual path to the new image
    static_image_path = os.path.join('net_Prj', 'static', 'images', '플랑크톤.png')  # Adjust project structure as needed
    # Replace the old image with the new image
    shutil.copy('./ad_images/kirby.png', './myapp/static/images/플랑크톤.png')
    
replace_image()