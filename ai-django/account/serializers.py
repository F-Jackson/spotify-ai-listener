from rest_framework import serializers
from .models import *


class OtherSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ('id', 'user')


class ColorConfigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorConfigsModel
        exclude = ('id', 'user')


class UserStaticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStaticsModel
        exclude = ('id', 'user', 'clustering_stats', 'time_using')
