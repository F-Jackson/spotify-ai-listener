from django.db import models
from django.contrib.auth.models import User

from .constants.models import *


class UserModel(models.Model):
    user = models.OneToOneField(User, blank=True, unique=True, on_delete=models.CASCADE)
    country_code = models.IntegerField(blank=True, null=True)
    genre = models.CharField(default=GENRES_COICHES[0][0], max_length=1, blank=False, null=False)
    photo = models.ImageField(upload_to='profile_pic', default='default_user.webp')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['user']


class ColorConfigsModel(models.Model):
    user = models.OneToOneField(User, blank=True, unique=True, on_delete=models.CASCADE)
    background_color = models.CharField(default=BACKGROUND_COLOR, max_length=7, blank=False, null=False)
    menu_color = models.CharField(default=MENU_COLOR, max_length=7, blank=False, null=False)
    button_color = models.CharField(default=BUTTON_COLOR, max_length=7, blank=False, null=False)
    text_color = models.CharField(default=TEXT_COLOR, max_length=7, blank=False, null=False)
    music_background_color = models.CharField(default=MUSIC_BACKGROUND_COLOR, max_length=7, blank=False, null=False)

    class Meta:
        verbose_name = 'color_config'
        verbose_name_plural = 'color_configs'
        ordering = ['user']


class UserStaticsModel(models.Model):
    user = models.OneToOneField(User, blank=True, unique=True, on_delete=models.CASCADE)
    time_using = models.TimeField(null=True, blank=True)
    clustering_stats = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'user_static'
        verbose_name_plural = 'user_statics'
        ordering = ['user']
