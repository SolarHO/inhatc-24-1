from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('image-last-modified/', views.image_last_modified, name='image_last_modified'),
    path('', views.show_adimage, name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
