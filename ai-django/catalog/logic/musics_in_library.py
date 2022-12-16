from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from catalog.constants._views import LIBRARY_REQUEST_PUT, LIBRARY_REQUEST_DELETE
from catalog.models import LibraryModel, MusicInLibraryModel, MusicModel
from catalog.serializers import MusicSerializer


def _verify_request(request, key: str, list_type: type = int) -> bool:
    if key in request.data.keys():
        if type(request.data[key]) == list:
            if all(isinstance(num, list_type) for num in request.data[key]):
                return True
    return False


def _get_library(user: User, pk: int) -> LibraryModel | None:
    try:
        library = LibraryModel.objects.get(user_owner=user, pk=pk)
    except LibraryModel.DoesNotExist:
        return None
    else:
        return library


def _get_models(music, library) -> MusicInLibraryModel:
    return MusicInLibraryModel.objects.filter(music=music, library=library)


def _get_music(pk: int) -> MusicModel | None:
    try:
        music = MusicModel.objects.get(pk=pk)
    except MusicModel.DoesNotExist:
        return None
    else:
        return music


def get_musics_in_library(pk: int, jwt: dict[str, str | User]) -> Response:
    data = {"token": jwt['token']}

    library = _get_library(jwt['user'], pk)
    if library:
        musics = MusicInLibraryModel.objects.filter(library=library)

        data['musics'] = []
        if musics:
            for music in musics:
                music_data = getattr(music, 'music')
                serializer = MusicSerializer(music_data)
                data['musics'].append(serializer.data)

        return Response(data, status=status.HTTP_200_OK)

    data.update({'error': 'Cant find library'})
    return Response(data, status=status.HTTP_404_NOT_FOUND)


def put_musics_in_library(request, pk: int, jwt: dict[str, str | User]) -> Response:
    data = {'token': jwt['token']}

    library = _get_library(jwt['user'], pk)
    request_is_correct = _verify_request(request, LIBRARY_REQUEST_PUT)

    if request_is_correct and library:
        for music_id in request.data[LIBRARY_REQUEST_PUT]:
            music = _get_music(music_id)
            if music:
                MusicInLibraryModel.objects.get_or_create(library=library, music=music)

        return Response(data, status=status.HTTP_201_CREATED)

    data.update({'error': 'Can not insert the catalog in the library'})
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


def delete_musics_in_library(request, pk: int, jwt: dict[str, str | User]) -> Response:
    data = {'token': jwt['token']}

    library = _get_library(jwt['user'], pk)
    request_is_correct = _verify_request(request, LIBRARY_REQUEST_DELETE)

    if request_is_correct and library:
        for music_id in request.data[LIBRARY_REQUEST_DELETE]:
            music = _get_music(music_id)

            if music:
                try:
                    music_in_library = MusicInLibraryModel.objects.get(library=library, music=music)
                except MusicInLibraryModel.DoesNotExist:
                    pass
                else:
                    music_in_library.delete()

        return Response(data, status=status.HTTP_204_NO_CONTENT)

    data.update({'error': 'Can not delete the catalog in the library'})
    return Response(data, status=status.HTTP_400_BAD_REQUEST)
