from rest_framework import status
from rest_framework.response import Response

from user.constants._views import INFO_TO_DELETE_USER

from user.logic.common import request_keys_verifier


def delete_user(request) -> Response:
    if request_keys_verifier(request.data, INFO_TO_DELETE_USER):
        if authorize(request):
            request.user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)


def authorize(request) -> bool:
    autorizations = (
        request.user.check_password(request.data['password']),
    )
    return all(autorizations)
