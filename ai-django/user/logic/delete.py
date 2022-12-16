from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from jwt_auth.models import RefreshTokens
from user.constants._views import INFO_TO_DELETE_USER

from user.logic.common import request_keys_verifier


def delete_user(jwt: dict, request) -> Response:
    if request_keys_verifier(request.data, INFO_TO_DELETE_USER):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(pk=jwt['user_id'], username=username, password=password)

        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        try:
            refresh_token = RefreshTokens.objects.get(user_id=jwt['user_id'])
        except RefreshTokens.DoesNotExist:
            pass
        else:
            refresh_token.delete()

    return Response(status=status.HTTP_404_NOT_FOUND)
