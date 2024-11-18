from django.shortcuts import render
from django.conf import settings
import os
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html', {'MEDIA_URL': settings.MEDIA_URL})

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