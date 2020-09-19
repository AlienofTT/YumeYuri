from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework import permissions

from .models import Manga
from .permissions import IsOwnerOrReadOnly
from .serializers import MangaSerializer, UserSerializer


# Create your views here.


def index(request):
	return HttpResponse("Hello, API Index.")


class MangaList(generics.ListCreateAPIView):
	queryset = Manga.objects.all()
	serializer_class = MangaSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class MangaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Manga.objects.all()
	serializer_class = MangaSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
