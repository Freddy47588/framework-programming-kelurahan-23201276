# warga/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet

# Buat sebuah router dan daftarkan ViewSet kita
router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'aduan', WargaViewSet, basename='aduan')

# URL API sekarang ditentukan secara otomatis oleh router.
urlpatterns = [
    path('', include(router.urls)),
]
