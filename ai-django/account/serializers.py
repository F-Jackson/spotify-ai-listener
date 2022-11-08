from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ('created_date',)


class ColorConfigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorConfigsModel
        fields = '__all__'


class UserStaticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStaticsModel
        exclude = ('clustering_stats', 'last_login_date')
