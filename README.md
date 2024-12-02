# Djnago 이용 직관적 광고 노출 웹 페이지

1. Django와 Google cloud storage(GCS)를 연결
2. 서버 가동시 GCS의 inhatc_test(임시) 버킷 아래 AD 폴더에 있는 모든 이미지 내부 폴더에 저장
3. 이미지 분석 후 넘겨받은 변수로 웹 페이지상 노출되는 광고 이미지 실시간으로 갱신

<hr>

## Django 프레임워크와 GCS(Google cloud storage) 사용 이유

![시스템 아키텍쳐2 drawio](https://github.com/user-attachments/assets/28bc40cc-b495-4bb4-84ec-bd550786ea16)

> 다수의 모듈 이용시 각 모듈마다 광고 이미지를 업로드 할 필요 없이 모듈에서  
> Django 서버 동작과 동시에 클라우드 스토리지에서 광고 이미지를 불러와  
> 일관된 광고 이미지 사용과 광고 이미지 업데이트의 편이성을 확보

## Google Cloud Storage

- 광고 이미지는 GCS(Google Cloud Storage)를 이용하며 클라우드 스토리지 내에 버킷(inhatc_test)(임시)을 생성하여 하위 폴더(AD) 내에 광고 이미지를 저장한다.
- 저장된 이미지는 모듈에서 Django 서버를 가동 시 자동으로 해당 폴더 내에 있는 모든 광고 이미지를 불러와서 모듈에 저장한다.
<pre>
  <code>
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
  </code>
</pre>

> Cloud console URL: https://console.cloud.google.com/storage/browser/inhatc_test   
> GCS 호출 URL = https://storage.cloud.google.com   
> GCS bucket name = **'inhatc_test'**

![스크린샷 2024-11-16 215031](https://github.com/user-attachments/assets/ca7a7602-7a6d-42f3-94e9-06214bc62fb4)



## Django page

- 장고 페이지는 5초마다 이미지가 변경되었는지 확인하여 이미지 변경시 자동으로 새로고침된다.
  ```
  //html템플릿 script코드
   <script>
    let lastModifiedTime = {{ last_modified_time|default:0 }};  // Make sure it's a valid timestamp

    // Ensure it's a valid number (timestamp)
    if (isNaN(lastModifiedTime)) {
        console.error('Invalid last modified time:', lastModifiedTime);
        lastModifiedTime = 0;  // Set a default value if it's not valid
    }

    // Periodically check for changes in the image
    setInterval(() => {
        fetch('/image-last-modified/')
            .then(response => response.json())
            .then(data => {
                const newLastModifiedTime = data.last_modified;

                // Compare the current last_modified_time with the new one
                if (lastModifiedTime !== newLastModifiedTime) {
                    // If the time has changed, refresh the page
                    location.reload();
                }

                // Update the stored last_modified_time for next comparison
                lastModifiedTime = newLastModifiedTime;
            })
            .catch(error => console.error('Error fetching last modified time:', error));
    }, 5000);  // Check every 5 seconds</script>
  ```
- 이미지는 /static/images의 ad.jpg이미지를 로드하며 해당 이미지 변경시의 timestamp를 통해 변경을 감지한다.
  ```
  #views.py 이미지 로드 관련 코드
  def show_adimage(request):
    # Path to the image
    image_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'images', 'ad.jpg')
    
    # Get the last modified time of the image
    if os.path.exists(image_path):
        last_modified_time = os.path.getmtime(image_path)
    else:
        last_modified_time = 0  # Default to 0 if the image doesn't exist

    # Pass last_modified_time to the template
    return render(request, 'home.html', {'last_modified_time': last_modified_time})

def image_last_modified(request):
    # Path to the image
    image_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'images', 'ad.jpg')

    if not os.path.exists(image_path):
        return JsonResponse({'error': 'Image not found'}, status=404)
    
    # Get the last modified time of the image
    last_modified_time = os.path.getmtime(image_path)
    
    # Return last modified time in JSON response
    return JsonResponse({'last_modified': last_modified_time})
      ```
- 광고이미지는 Django서버 실행시에 Google Cloud Storage에서 받아오며, ad_images디렉토리에 recommeder.csv파일의 인덱스번호.jpg로 저장된다.

![20241125_03h07m29s_grim](https://github.com/user-attachments/assets/39a4d74a-e9a4-48d4-a069-ffda924cb5b5)
