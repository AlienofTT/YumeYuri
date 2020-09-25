from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class MagazineSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Magazine
		fields = ['title', 'id']


class MangaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Manga
		fields = ['url', 'id', 'title', 'bgm_id', 'dmzj_id', 'owner']


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
	manga_name = serializers.CharField(source='manga.title', read_only=True)
	manga = serializers.HyperlinkedRelatedField(view_name='manga-detail', queryset=Manga.objects.all())

	class Meta:
		model = Chapter
		fields = ['url', 'id', 'title', 'manga_name', 'manga']


class UserSerializer(serializers.HyperlinkedModelSerializer):
	# mangas = serializers.PrimaryKeyRelatedField(many=True, queryset=Manga.objects.all())
	mangas = serializers.HyperlinkedRelatedField(many=True, view_name='manga-detail', read_only=True)

	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'mangas']
