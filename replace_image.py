import shutil
import os

def replace_image():
    # Define the path for the new image and the existing image in the static directory
    new_image_path = './ad_images/ad2.jpg'  # Replace this with the actual path to the new image
    static_image_path = os.path.join('testproject', 'static', 'images', 'ad.jpg')  # Adjust project structure as needed

    # Replace the old image with the new image
    shutil.copy('./ad_images/ad2.jpg', './myapp/static/images/ad.jpg')
    

replace_image()
