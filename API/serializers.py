from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Manga


class MangaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Manga
		fields = ['url', 'id', 'title', 'bgmId', 'dmzjId', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
	# mangas = serializers.PrimaryKeyRelatedField(many=True, queryset=Manga.objects.all())
	mangas = serializers.HyperlinkedRelatedField(many=True, view_name='manga-detail', read_only=True)

	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'mangas']
