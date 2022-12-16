from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from jwt_auth.logic.create_login_token import ClientTokenLogin
from user.constants._views import LOGIN_USER_NEED

from user.logic.common import request_keys_verifier


def sign_in(request) -> Response:
    if request_keys_verifier(request.data, LOGIN_USER_NEED):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            user_id = getattr(user, 'id')

            new_data = _create_jwt(user_id)
            return Response(new_data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_404_NOT_FOUND)


def _create_jwt(user_id: int) -> dict:
    new_data = {}

    jwt = ClientTokenLogin(user_id)
    jwt.create_login_tokens()

    new_data['token'] = jwt.client_token

    return new_data


def sign_out(user_id: int, client_token: str) -> Response:

    return Response(status=status.HTTP_200_OK)
