# warga/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'aduan', PengaduanViewSet, basename='aduan')

urlpatterns = [
    path('', include(router.urls)),
]
