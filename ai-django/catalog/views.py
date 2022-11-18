from django.http import Http404
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .logic.musics.musics import recomend_musics, search_musics
from .models import *
from .serializers import *

from .logic.musics_in_library import get_musics_in_library, put_musics_in_library, delete_musics_in_library
from .logic.library import delete_library, get_library, update_library, get_librarys, create_librarys


class MusicList(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if 'mode' in request.data:
            if request.data['mode'] == 'search':
                return search_musics(request)
            elif request.data['mode'] == 'recomend':
                return recomend_musics(request)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class MusicDetail(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return MusicModel.objects.get(pk=pk)
        except MusicModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        music = self.get_object(pk)
        serializer = MusicSerializer(music)
        return Response(serializer.data)


class LibraryList(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request) -> Response:
        return get_librarys(request)

    def put(self, request) -> Response:
        return create_librarys(request)


class LibraryDetail(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk) -> Response:
        return get_library(request, pk)

    def patch(self, request, pk) -> Response:
        return update_library(request, pk)

    def delete(self, request, pk) -> Response:
        return delete_library(request, pk)


class MusicsInLibrarysList(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        return get_musics_in_library(request, pk)

    def put(self, request, pk):
        return put_musics_in_library(request, pk)

    def delete(self, request, pk):
        return delete_musics_in_library(request, pk)
