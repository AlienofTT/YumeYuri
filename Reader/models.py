from django.db import models


# Create your models here.
class Manga(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	bgmId = models.IntegerField(null=True)
	dmzjId = models.CharField(max_length=100)


class Chapter(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	manga = models.ForeignKey(Manga, on_delete=models.CASCADE)


class Image(models.Model):
	id = models.AutoField(primary_key=True)
	fileName = models.CharField(max_length=100)
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
