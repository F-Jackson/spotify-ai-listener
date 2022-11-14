from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from user.serializers import UserSerializer
from account.models import ColorConfigsModel, UserModel, UserStaticsModel
from user.logic.common import verify_user_existence, verify_serializer, request_keys_verifier

from user.constants._views import NEW_USER_NEEDS


def create_user(request) -> Response:
    if request_keys_verifier(request.data, NEW_USER_NEEDS):
        user_exist = verify_user_existence(username=request.data['username'], email=request.data['email'])
        if not user_exist:
            serializer = UserSerializer(data=request.data)
            if verify_serializer(serializer):
                return create_user_sucessfull(request)
            else:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Verify infos'}, status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_404_NOT_FOUND)


def create_user_sucessfull(request):
    user = create_new_user(request)

    create_relations_objs(
        {"user": user},
        UserModel,
        UserStaticsModel,
        ColorConfigsModel
    )

    return Response(status=status.HTTP_201_CREATED)


def create_new_user(request):
    return User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        email=request.data['email']
    )


def create_relations_objs(key: dict, *models) -> None:
    for model in models:
        model.objects.create(**key).save()
