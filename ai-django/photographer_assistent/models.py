from django.db import models
from .constants.models import *
from account.models import UserModel


class MusicModel(models.Model):
    name: str = models.CharField(max_length=255, blank=False, null=False)
    author: str = models.CharField(max_length=255, blank=False, null=False)
    track_id: str = models.CharField(default='None', max_length=255, blank=False, null=False)
    genre: str = models.CharField(
        default=GENRES_CHOICES[0],
        max_length=2,
        choices=GENRES_CHOICES,
        blank=False,
        null=False
    )
    cluster_class = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'
        ordering = ['genre']


class LibraryModel(models.Model):
    name: str = models.CharField(max_length=75, blank=False)
    photo = models.ImageField(blank=True)
    play_random: bool = models.BooleanField(default=False)
    use_ai: bool = models.BooleanField(default=True)
    musics = models.JSONField(default=MUSICS_DEFAULT)
    user_owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Librarys'
        ordering = ['user_owner']
