from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets
from .models import *
from .permissions import *
from .serializers import *


# Create your views here.
class MagazineViewSet(viewsets.ModelViewSet):
	queryset = Magazine.objects.all()
	serializer_class = MagazineSerializer
	permission_classes = [permissions.IsAdminUser]


class MangaViewSet(viewsets.ModelViewSet):
	queryset = Manga.objects.all()
	serializer_class = MangaSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMangaOwnerOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class ChapterViewSet(viewsets.ModelViewSet):
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsChapterOwnerOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

