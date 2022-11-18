from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from catalog.constants._views import LIBRARYS_UPDATE_FILTER, MAX_LIBRARYS_PER_USER, LIBRARYS_CREATE_NEED
from catalog.logic.common import request_keys_filter, request_keys_verifier
from catalog.models import LibraryModel
from catalog.serializers import LibrarySerializer


def get_object(request, pk) -> LibraryModel:
    try:
        return LibraryModel.objects.get(user_owner=request.user, pk=pk)
    except LibraryModel.DoesNotExist:
        raise Http404


def get_library(request, pk):
    library = get_object(request, pk)
    serializer = LibrarySerializer(library)
    return Response(serializer.data)


def update_library(request, pk):
    library = get_object(request, pk)
    data = request_keys_filter(request.data, LIBRARYS_UPDATE_FILTER)

    serializer = LibrarySerializer(library, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def delete_library(request, pk) -> Response:
    library = get_object(request, pk)
    library.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def get_librarys(request) -> Response:
    librarys = LibraryModel.objects.filter(user_owner=request.user)
    serializer = LibrarySerializer(librarys, many=True)
    return Response(serializer.data)


def create_librarys(request) -> Response:
    if request_keys_verifier(request.data, LIBRARYS_CREATE_NEED):
        librarys = LibraryModel.objects.filter(user_owner=request.user)
        if len(librarys) < MAX_LIBRARYS_PER_USER:
            serializer = LibrarySerializer(data=request.data)
            if serializer.is_valid():
                LibraryModel.objects.create(name=request.data['name'], user_owner=request.user).save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(f'Librarys limit reachead: {MAX_LIBRARYS_PER_USER}', status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status=status.HTTP_400_BAD_REQUEST)
