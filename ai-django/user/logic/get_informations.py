from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from user.logic.common import get_object
from user.serializers import UserSerializer

from user.constants._views import INFO_MODELS_TO_GET


def get_infos(jwt: dict) -> Response:
    data = {'token': jwt['token']}
    user_data = {}

    serializer = UserSerializer(jwt['user'])

    user_data.update(serializer.data)

    relations = _get_relations(jwt['user'], *INFO_MODELS_TO_GET)

    user_data.update(relations)

    data.update({'user': user_data})

    return Response(data, status=status.HTTP_200_OK)


def _get_relations(user: User, *models) -> dict:
    models_dict = {}
    for model in models:
        if 'name' in model.keys():
            model_data = _get_model(user, model['model'], model['serializer'])
            model_name = model['name']
            models_dict.update({model_name: model_data})
        else:
            model_data = _get_model(user, model['model'], model['serializer'])
            models_dict.update(model_data)
    return models_dict


def _get_model(user: User, model, serializer) -> dict:
    model_obj = get_object(user, model)
    if model_obj:
        data = serializer(model_obj).data
    else:
        data = None

    return data
