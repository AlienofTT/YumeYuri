from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .models import Manga
from .serializers import MangaSerializer


# Create your views here.


def index(request):
	return HttpResponse("Hello, API Index.")


class MangaList(generics.ListCreateAPIView):
	queryset = Manga.objects.all()
	serializer_class = MangaSerializer


class MangaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Manga.objects.all()
	serializer_class = MangaSerializer
