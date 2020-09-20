from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Manga
from .permissions import IsOwnerOrReadOnly
from .serializers import MangaSerializer, UserSerializer


# Create your views here.


def index(request):
	return HttpResponse("Hello, API Index.")


@api_view(['GET'])
def api_root(request, fmt=None):
	return Response({
		'users': reverse('user-list', request=request, format=fmt),
		'mangas': reverse('manga-list', request=request, format=fmt)
	})


class MangaViewSet(viewsets.ModelViewSet):
	queryset = Manga.objects.all()
	serializer_class = MangaSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


'''
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
'''


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	query = User.objects.all()
	serializer_class = UserSerializer


'''
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
'''
