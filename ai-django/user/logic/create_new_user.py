from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from user.serializers import UserSerializer
from account.models import ColorConfigsModel, UserModel, UserStaticsModel
from user.logic.common import verify_user_existence, request_keys_verifier

from user.constants._views import NEW_USER_NEEDS


def create_user(request) -> Response:
    if request_keys_verifier(request.data, NEW_USER_NEEDS):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user_exist = verify_user_existence(username=username, email=email)

        if not user_exist:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                return _create_user_sucessfull(username, email, password)
            else:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Verify infos'}, status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_404_NOT_FOUND)


def _create_user_sucessfull(*data):
    user = _create_new_user(*data)

    _create_relations_objs(
        {"user": user},
        UserModel,
        UserStaticsModel,
        ColorConfigsModel
    )

    return Response(status=status.HTTP_201_CREATED)


def _create_new_user(username: str, email: str, password: str):
    return User.objects.create_user(
        username=username,
        email=email,
        password=password
    )


def _create_relations_objs(key: dict, *models) -> None:
    for model in models:
        model.objects.create(**key).save()
