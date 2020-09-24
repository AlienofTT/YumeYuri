from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets
from .models import Manga
from .permissions import IsOwnerOrReadOnly
from .serializers import MangaSerializer, UserSerializer


# Create your views here.
class MangaViewSet(viewsets.ModelViewSet):
	queryset = Manga.objects.all()
	serializer_class = MangaSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

