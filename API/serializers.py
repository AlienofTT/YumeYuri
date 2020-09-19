from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Manga


class MangaSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Manga
		fields = ['id', 'title', 'bgmId', 'dmzjId', 'owner']


class UserSerializer(serializers.ModelSerializer):
	mangas = serializers.PrimaryKeyRelatedField(many=True, queryset=Manga.objects.all())

	class Meta:
		model = User
		fields = ['id', 'username', 'mangas']
