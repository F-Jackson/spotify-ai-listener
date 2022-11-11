from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response

from user.logic.common import get_object
from user.serializers import UserSerializer

from user.constants._views import INFO_NOT_GET_USER, INFO_MODELS_TO_GET


def get_infos(request) -> Response:
    model = request.user
    serializer = UserSerializer(model)

    response = dict(serializer.data)

    models = get_relations(request, *INFO_MODELS_TO_GET)

    response.update(models)

    return Response(response, status=status.HTTP_200_OK)


def get_relations(request, *models) -> dict:
    models_dict = {}
    for model in models:
        if type(model) == tuple:
            model_data = get_model(request, model[1])
            model_name = model[0]
            models_dict.update({model_name: model_data})
        else:
            model_data = get_model(request, model)
            models_dict.update(model_data)
    return models_dict


def get_model(request, model) -> dict:
    data = {}
    model_obj = get_object(request, model)
    model_dict = model_to_dict(model_obj)
    for key, value in model_dict.items():
        if key not in INFO_NOT_GET_USER:
            data[key] = value
    return data
