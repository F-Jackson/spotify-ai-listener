from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from user.logic.common import verify_user_auth
from .logic.musics.musics import recomend_musics, search_musics
from .models import *
from .pagination import CustomPagination
from .serializers import *

from .logic.musics_in_library import get_musics_in_library, put_musics_in_library, delete_musics_in_library
from .logic.library import delete_library, get_library, update_library, get_librarys, create_librarys


class MusicList(APIView):
    """Get list of musics based on the mode"""
    def post(self, request):
        """Return list of musics based on the chosen mode"""

        if 'mode' in request.data:
            if request.data['mode'] == 'search':
                return search_musics(request)
            elif request.data['mode'] == 'recomend':
                return recomend_musics(request)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class MusicViewset(viewsets.ViewSet):
    queryset = MusicModel.objects.all()
    serializer_class = MusicSerializer(queryset, many=True)
    pagination_class = CustomPagination


class LibraryList(APIView):
    """All user librarys"""

    def get(self, request) -> Response:
        """Get all librarys from user"""

        valid_jwt = verify_user_auth(request=request, get_user=True)
        if valid_jwt:
            return get_librarys(valid_jwt)

        return Response({'error': 'jwt'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request) -> Response:
        """Create new library for user"""

        valid_jwt = verify_user_auth(request, get_user=True)
        if valid_jwt:
            return create_librarys(request, valid_jwt)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class LibraryDetail(APIView):
    """User library"""
    def get(self, request, pk: int) -> Response:
        """Get library info"""

        valid_jwt = verify_user_auth(request, get_user=True)
        if valid_jwt:
            return get_library(pk, valid_jwt)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk: int) -> Response:
        """Update library info"""

        valid_jwt = verify_user_auth(request, get_user=True)
        if valid_jwt:
            return update_library(request, pk, valid_jwt)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int) -> Response:
        """Delete library"""
        valid_jwt = verify_user_auth(request, get_user=True)
        if valid_jwt:
            return delete_library(pk, valid_jwt)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class MusicsInLibrarysList(APIView):
    def get(self, request, pk):
        """Get all music in a library"""

        valid_jwt = verify_user_auth(request, get_user=True)
        if valid_jwt:
            return get_musics_in_library(pk, valid_jwt)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """Put music in a library"""

        valid_jwt = verify_user_auth(request, get_user=True)
        if valid_jwt:
            return put_musics_in_library(request, pk, valid_jwt)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Remove music in a library"""

        valid_jwt = verify_user_auth(request, get_user=True)
        if valid_jwt:
            return delete_musics_in_library(request, pk, valid_jwt)

        return Response(status=status.HTTP_400_BAD_REQUEST)
