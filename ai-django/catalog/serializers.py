from rest_framework import serializers
from .models import *
from .validators.library import validate_photo


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        fields = "__all__"


class LibrarySerializer(serializers.ModelSerializer):
    def validate_photo(self, value):
        errors = validate_photo(value)
        if errors:
            raise serializers.ValidationError(errors)
        return value

    class Meta:
        model = LibraryModel
        exclude = ('user_owner',)


class MusicsInLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicInLibraryModel
        exclude = ('id',)
