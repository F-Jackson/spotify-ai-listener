from rest_framework import status
from rest_framework.response import Response

from catalog.constants._views import MUSIC_RECOMEND_MUSICS_NEED, MUSIC_SEARCH_NEED
from catalog.logic.common import request_keys_verifier
from catalog.logic.musics.recomend import get_genres_and_clusters, recomend
from catalog.logic.musics.search import search


def recomend_musics(request) -> Response:
    if request_keys_verifier(request.data, MUSIC_RECOMEND_MUSICS_NEED):
        genres, clusters = get_genres_and_clusters(request.data)
        musics = recomend(genres, clusters)

        if musics:
            return Response(musics, status=status.HTTP_200_OK)

        return Response('Nothing to recomend', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(f'Request need to have: {MUSIC_RECOMEND_MUSICS_NEED}', status=status.HTTP_400_BAD_REQUEST)


def search_musics(request):
    if request_keys_verifier(request.data, MUSIC_SEARCH_NEED):
        return search(request.data['search_text'])
    return Response(f'Request need to have: {MUSIC_SEARCH_NEED}', status=status.HTTP_400_BAD_REQUEST)
