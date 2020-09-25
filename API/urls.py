from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

router = DefaultRouter()
router.register(r'magazine', MagazineViewSet)
router.register(r'manga', MangaViewSet)
router.register(r'chapter', ChapterViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
