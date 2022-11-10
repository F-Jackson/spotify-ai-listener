from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class MusicList(APIView):
    def get(self, request, format=None):
        musics = MusicModel.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)


class MusicDetail(APIView):
    def get_object(self, pk):
        try:
            return MusicModel.objects.get(pk=pk)
        except MusicModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music)
        return Response(serializer.data)


class LibraryList(APIView):
    def get(self, request, format=None):
        librarys = LibraryModel.objects.all()
        serializer = LibrarySerializer(librarys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LibraryDetail(APIView):
    def get_object(self, pk):
        try:
            return LibraryModel.objects.get(pk=pk)
        except LibraryModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        library = self.get_object(pk)
        serializer = LibrarySerializer(library)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        library = self.get_object(pk)
        serializer = LibrarySerializer(library, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        library = self.get_object(pk)
        library.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)