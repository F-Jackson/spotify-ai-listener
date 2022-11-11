from django.contrib.auth import authenticate, login, logout
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response

from user.constants._views import LOGIN_USER_NEED

from user.logic.common import request_keys_verifier


def sign_in(request) -> Response:
    if request_keys_verifier(request.data, LOGIN_USER_NEED):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_404_NOT_FOUND)


def sign_out(request) -> Response:
    logout(request)
    return Response(status=status.HTTP_200_OK)
