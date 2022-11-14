from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from account.models import ColorConfigsModel, UserModel
from account.serializers import ColorConfigsSerializer, OtherSettingsSerializer
from user.constants._views import USER_UPDATE_NEED
from user.logic.common import get_object, verify_serializer, request_keys_verifier
from user.serializers import UserSerializer


def update_user(request) -> Response:
    if request_keys_verifier(request.data, USER_UPDATE_NEED):
        user_data = get_data_from_request(request, False)
        other_data = get_data_from_request(request, True)

        if dont_has_email(request.user, user_data):
            return update_or_error(request, user_data, other_data)
        else:
            return Response({'email': 'already taken'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def get_data_from_request(request, is_dict: bool) -> dict:
    data = {}
    for key, value in request.data.items():
        if key != "password" and is_dict == type_is_dict(value):
            data[key] = value
    return data


def type_is_dict(value) -> bool:
    return type(value) == dict


def dont_has_email(user, user_data) -> bool:
    if user.email != user_data['email']:
        user = User.objects.get(email=user_data['email'])

        return user is None
    return True


def update_or_error(request, user_data, other_data) -> Response:
    updaters = [
        (UserSerializer, request.user, user_data),
        (OtherSettingsSerializer, get_object(request, UserModel), other_data['other_settings']),
        (ColorConfigsSerializer, get_object(request, ColorConfigsModel), other_data['color_configs']),
    ]

    serializers, erros = prepare_models(updaters)

    if erros:
        return Response(erros, status=status.HTTP_404_NOT_FOUND)
    else:
        return update_serializers(request, serializers)


def prepare_models(updaters):
    serializers = []
    erros = []
    for serializer, model, data in updaters:
        serializer_with_data = serializer(model, data=data, partial=True)
        if verify_serializer(serializer_with_data):
            serializers.append(serializer_with_data)
        else:
            erros.append(serializer_with_data.errors)
    return serializers, erros


def update_serializers(request, serializers) -> Response:
    for serializer in serializers:
        serializer.save()
    logout(request)
    return Response(status=status.HTTP_200_OK)
