from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='test/')
    uploaded_at = models.DateTimeField(auto_now_add=True)