from rest_framework import status
from rest_framework.response import Response

from catalog.constants._views import LIBRARY_REQUEST_PUT, LIBRARY_REQUEST_DELETE
from catalog.models import LibraryModel, MusicInLibraryModel, MusicModel
from catalog.serializers import MusicsInLibrarySerializer


def verify_request(request, key: str, list_type: type = int) -> bool:
    if key in request.data.keys():
        if type(request.data[key]) == list:
            if all(isinstance(num, list_type) for num in request.data[key]):
                return True
    return False


def get_library(request, pk) -> bool:
    return LibraryModel.objects.get(user_owner=request.user, pk=pk)


def get_models(music, library) -> MusicInLibraryModel:
    return MusicInLibraryModel.objects.filter(music=music, library=library)


def verify_existence_and_delete(music, library):
    music_in_library = MusicInLibraryModel.objects.filter(library=library, music=music)
    if music_in_library:
        music_in_library.delete()


def get_musics_in_library(request, pk) -> Response:
    library = get_library(request, pk)
    if library:
        musics = MusicInLibraryModel.objects.filter(library=library)
        if musics:
            serializer = MusicsInLibrarySerializer(musics, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    return Response('Can not find ', status=status.HTTP_404_NOT_FOUND)


def put_musics_in_library(request, pk) -> Response:
    library = get_library(request, pk)
    request_is_correct = verify_request(request, LIBRARY_REQUEST_PUT)
    if request_is_correct and library:
        for music_id in request.data[LIBRARY_REQUEST_PUT]:
            music = MusicModel.objects.get(pk=music_id)
            if music:
                verify_existence_and_delete(music_id, library)
                MusicInLibraryModel.objects.create(library=library, music=music)

        return Response(status=status.HTTP_201_CREATED)

    return Response('Can not insert the catalog in the library', status=status.HTTP_400_BAD_REQUEST)


def delete_musics_in_library(request, pk) -> Response:
    library = get_library(request, pk)
    request_is_correct = verify_request(request, LIBRARY_REQUEST_DELETE)
    if request_is_correct and library:
        for music_id in request.data[LIBRARY_REQUEST_DELETE]:
            verify_existence_and_delete(music_id, library)

        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response('Can not delete the catalog in the library', status=status.HTTP_400_BAD_REQUEST)
