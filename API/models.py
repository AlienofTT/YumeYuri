from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Magazine(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)


class Manga(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	owner = models.ForeignKey(User, related_name='mangas', on_delete=models.SET_DEFAULT, default=1)
	magazine = models.ForeignKey(Magazine, related_name='mangas', on_delete=models.SET_NULL, null=True)
	bgm_id = models.IntegerField(default=-1)
	dmzj_id = models.CharField(null=True, max_length=50)


class Volume(models.Model):
	id = models.AutoField(primary_key=True)
	manga = models.ForeignKey(Manga, related_name='volumes', on_delete=models.CASCADE)
	title = models.CharField(max_length=10)


class Chapter(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(null=True, max_length=50)
	manga = models.ForeignKey(Manga, related_name='chapters', on_delete=models.CASCADE)
	volume = models.ForeignKey(Volume, related_name='chapters', on_delete=models.CASCADE, null=True)


class Image(models.Model):
	id = models.AutoField(primary_key=True)
	fileName = models.CharField(max_length=50)
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
