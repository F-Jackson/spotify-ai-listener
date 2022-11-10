from rest_framework import serializers
from .models import *


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        exclude = ('cluster_class',)


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryModel
        exclude = ('user_owner',)
