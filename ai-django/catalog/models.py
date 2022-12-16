from django.contrib.auth.models import User
from django.db import models


class MusicModel(models.Model):
    name: str = models.CharField(max_length=255, blank=False, null=False)
    author: str = models.CharField(max_length=255, blank=False, null=False)
    track_id: str = models.CharField(default='None', max_length=255, blank=False, null=False)
    genre: str = models.CharField(
        default='pop',
        max_length=255,
        blank=False,
        null=False
    )
    cluster_class = models.IntegerField(default=0, blank=False, null=False)
    search: str = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'
        ordering = ['genre']


class LibraryModel(models.Model):
    name: str = models.CharField(max_length=75, blank=False)
    photo = models.ImageField(blank=True)
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Librarys'
        ordering = ['user_owner']


class MusicInLibraryModel(models.Model):
    music = models.ForeignKey(MusicModel, on_delete=models.CASCADE)
    library = models.ForeignKey(LibraryModel, on_delete=models.CASCADE)
