from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manga/', views.MangaList.as_view()),
    path('manga/<int:pk>', views.MangaDetail.as_view())
]
