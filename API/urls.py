from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('',
         views.api_root),
    path('manga/',
         views.MangaList.as_view(),
         name='manga-list'),
    path('manga/<int:pk>',
         views.MangaDetail.as_view(),
         name='manga-detail'),
    path('user/',
         views.UserList.as_view(),
         name='user-list'),
    path('user/<int:pk>',
         views.UserDetail.as_view(),
         name='user-detail')
])
