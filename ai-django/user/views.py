from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .logic.common import verify_user_auth
from .logic.create_new_user import create_user
from .logic.get_informations import get_infos

from .logic.login import sign_in, sign_out
from .logic.delete import delete_user
from .logic.update_user import update_user


class UserView(APIView):
    def get(self, request) -> Response:
        if verify_user_auth(request):
            return get_infos(request)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request) -> Response:
        if verify_user_auth(request):
            return sign_out(request)
        else:
            return sign_in(request)

    def put(self, request) -> Response:
        if not verify_user_auth(request):
            return create_user(request)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request) -> Response:
        if verify_user_auth(request):
            return update_user(request)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request) -> Response:
        if verify_user_auth(request):
            return delete_user(request)
        return Response(status=status.HTTP_404_NOT_FOUND)
