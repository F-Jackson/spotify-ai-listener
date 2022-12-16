from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .logic.common import verify_user_auth
from .logic.create_new_user import create_user
from .logic.delete import delete_user
from .logic.get_informations import get_infos
from .logic.login import sign_in
from .logic.update_user import update_user


class UserView(APIView):
    """View for normal users"""
    def get(self, request) -> Response:
        """Get logged user infos or return 404"""

        valid_jwt = verify_user_auth(request=request, get_user=True)
        if valid_jwt:
            return get_infos(valid_jwt)
        return Response('Please Login Again', status=status.HTTP_404_NOT_FOUND)

    def post(self, request) -> Response:
        """Sign in user"""
        return sign_in(request)

    def put(self, request) -> Response:
        """If user is not logged create new user else return 404"""

        valid_jwt = verify_user_auth(request)
        if not valid_jwt:
            return create_user(request)
        return Response('Please Logout', status=status.HTTP_404_NOT_FOUND)

    def patch(self, request) -> Response:
        """If user is logged update user else return 404"""

        valid_jwt = verify_user_auth(request=request, get_user=True)
        if valid_jwt:
            return update_user(valid_jwt, request)
        return Response('Please Login Again', status=status.HTTP_404_NOT_FOUND)

    def delete(self, request) -> Response:
        """Delete Account"""

        valid_jwt = verify_user_auth(request=request, get_user=False)
        if valid_jwt:
            return delete_user(valid_jwt, request)
        return Response(status=status.HTTP_404_NOT_FOUND)
