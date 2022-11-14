from django.contrib.auth.models import User
from rest_framework import serializers

from user.validators.user import validate_username, validate_password, validate_names, validate_email


class UserSerializer(serializers.ModelSerializer):
    def validate_username(self, value):
        erros = validate_username(value)
        if erros:
            raise serializers.ValidationError(erros)
        return value

    def validate_password(self, value):
        erros = validate_password(value)
        if erros:
            raise serializers.ValidationError(erros)
        return value

    def validate_first_name(self, value):
        erros = validate_names(value)
        if erros:
            raise serializers.ValidationError(erros)
        return value

    def validate_second_name(self, value):
        erros = validate_names(value)
        if erros:
            raise serializers.ValidationError(erros)
        return value

    def validate_email(self, value):
        erros = validate_email(value)
        if erros:
            raise serializers.ValidationError(erros)
        return value

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'last_login']
