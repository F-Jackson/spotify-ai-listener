from django.contrib.auth import logout
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

        updaters = (
            (UserSerializer, request.user, user_data),
            (ColorConfigsSerializer, get_object(request, ColorConfigsModel), other_data['color_configs']),
            (OtherSettingsSerializer, get_object(request, UserModel), other_data['other_settings']),
        )

        try:
            serializers = prepare_models(updaters)
        except ValueError as e:
            return Response(e.args, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            for serializer in serializers:
                serializer.save()
            logout(request)
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def get_data_from_request(request, is_dict: bool) -> dict:
    data = {}
    for key, value in request.data.items():
        if key != "password" and is_dict == type_is_dict(value):
            data[key] = value
    return data


def type_is_dict(value) -> bool:
    return type(value) == dict


def prepare_models(updaters) -> list:
    serializers = []
    for serializer, model, data in updaters:
        serializer_with_data = serializer(model, data=data, partial=True)
        if verify_serializer(serializer_with_data):
            serializers.append(serializer_with_data)
            continue
        raise ValueError("Wrong format in the given values")
    return serializers
