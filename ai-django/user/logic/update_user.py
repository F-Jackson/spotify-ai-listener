from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from account.models import ColorConfigsModel, UserModel
from account.serializers import ColorConfigsSerializer, OtherSettingsSerializer
from user.constants._views import USER_UPDATE_NEED
from user.logic.common import get_object, request_keys_verifier, dont_has_email
from user.serializers import UserSerializer


def update_user(jwt: dict, request) -> Response:
    data = {'token': jwt['token']}

    if request_keys_verifier(request.data, USER_UPDATE_NEED):
        user_data = _get_data_from_request(request, False)
        other_data = _get_data_from_request(request, True)

        if dont_has_email(jwt['user'], user_data['email']):
            data.update({'user': jwt['user']})
            return _update_or_error(data, user_data, other_data)
        else:
            data.update({'error': 'already taken'})
    return Response(data, status=status.HTTP_404_NOT_FOUND)


def _get_data_from_request(request, is_dict: bool) -> dict:
    data = {}
    for key, value in request.data.items():
        if key != "password" and is_dict == _type_is_dict(value):
            data[key] = value
    return data


def _type_is_dict(value) -> bool:
    return type(value) == dict


def _update_or_error(data: dict[str | User], user_data, other_data) -> Response:
    updaters = [
        (UserSerializer, data['user'], user_data),
        (OtherSettingsSerializer, get_object(data['user'], UserModel), other_data['other_settings']),
        (ColorConfigsSerializer, get_object(data['user'], ColorConfigsModel), other_data['color_configs'])
    ]

    serializers, erros = _prepare_models(updaters)

    if erros:
        return Response({'error': erros, 'token': data['token']}, status=status.HTTP_404_NOT_FOUND)
    else:
        return _update_serializers(serializers, data['token'])


def _prepare_models(updaters):
    serializers = []
    erros = []
    for serializer, model, data in updaters:
        serializer_with_data = serializer(model, data=data, partial=True)
        if serializer_with_data.is_valid():
            serializers.append(serializer_with_data)
        else:
            erros.append(serializer_with_data.errors)
    return serializers, erros


def _update_serializers(serializers, token: str) -> Response:
    for serializer in serializers:
        serializer.save()
    return Response({'token': token}, status=status.HTTP_200_OK)
