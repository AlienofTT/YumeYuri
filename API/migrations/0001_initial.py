# Generated by Django 3.1.1 on 2020-09-18 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('bgmId', models.IntegerField(null=True)),
                ('dmzjId', models.CharField(max_length=100, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mangas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fileName', models.CharField(max_length=100)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.manga'),
        ),
    ]
