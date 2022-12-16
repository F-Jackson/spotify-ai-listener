from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
import json

from catalog.constants._views import LIBRARYS_UPDATE_FILTER, MAX_LIBRARYS_PER_USER, LIBRARYS_CREATE_NEED
from catalog.logic.common import request_keys_filter, request_keys_verifier
from catalog.models import LibraryModel
from catalog.serializers import LibrarySerializer


def _get_object(user: User, pk) -> LibraryModel:
    try:
        return LibraryModel.objects.get(user_owner=user, pk=pk)
    except LibraryModel.DoesNotExist:
        raise Http404


def get_library(pk: int, jwt: dict):
    data = {'token': jwt['token']}

    library = _get_object(jwt['user'], pk)
    serializer = LibrarySerializer(library)

    data.update({'library': serializer.data})
    return Response(data, status=status.HTTP_200_OK)


def update_library(request, pk: int, jwt: dict):
    data = {'token': jwt['token']}

    library = _get_object(jwt['user'], pk)
    new_library_data = request_keys_filter(request.data, LIBRARYS_UPDATE_FILTER)

    serializer = LibrarySerializer(library, data=new_library_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data, status=status.HTTP_200_OK)
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


def delete_library(pk: int, jwt: dict) -> Response:
    data = {'token': jwt['token']}

    library = _get_object(jwt['user'], pk)
    library.delete()
    return Response(data, status=status.HTTP_204_NO_CONTENT)


def get_librarys(jwt: dict[str, str, User]) -> Response:
    data = {'token': jwt['token']}

    librarys = LibraryModel.objects.filter(user_owner=jwt['user'])
    serializer = LibrarySerializer(librarys, many=True)

    data.update({'librarys': serializer.data})

    return Response(data, status=status.HTTP_200_OK)


def create_librarys(request, jwt: dict[str, str, User]) -> Response:
    data = {'token': jwt['token']}

    if request_keys_verifier(request.data, LIBRARYS_CREATE_NEED):
        librarys = LibraryModel.objects.filter(user_owner=jwt['user'])

        can_add_more_libarys = len(librarys) < MAX_LIBRARYS_PER_USER

        if can_add_more_libarys:
            serializer = LibrarySerializer(data=request.data)

            if serializer.is_valid():
                print("valid")
                LibraryModel.objects.create(name=request.data['name'], user_owner=jwt['user']).save()

                return Response(data, status=status.HTTP_201_CREATED)

            print('not valid')
            data.update({'error': serializer.errors})
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        data.update({'error': f'Librarys limit reachead: {MAX_LIBRARYS_PER_USER}'})
        return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response(data, status=status.HTTP_400_BAD_REQUEST)
