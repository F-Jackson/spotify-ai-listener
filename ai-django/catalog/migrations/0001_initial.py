# Generated by Django 4.1.3 on 2022-11-18 00:29

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
            name='LibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('play_random', models.BooleanField(default=False)),
                ('use_ai', models.BooleanField(default=True)),
                ('user_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Library',
                'verbose_name_plural': 'Librarys',
                'ordering': ['user_owner'],
            },
        ),
        migrations.CreateModel(
            name='MusicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('track_id', models.CharField(default='None', max_length=255)),
                ('genre', models.CharField(default='pop', max_length=255)),
                ('cluster_class', models.IntegerField(default=0)),
                ('search', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Music',
                'verbose_name_plural': 'Musics',
                'ordering': ['genre'],
            },
        ),
        migrations.CreateModel(
            name='MusicInLibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.librarymodel')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.musicmodel')),
            ],
        ),
    ]
