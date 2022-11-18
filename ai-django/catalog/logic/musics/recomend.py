from rest_framework.utils.serializer_helpers import ReturnDict

from catalog.models import MusicModel
from catalog.serializers import MusicSerializer


def dict_values_type_is_valid(valid_type, *values) -> bool:
    for value in values:
        if type(value) != valid_type:
            return False
    return True


def get_musics(genre: str, cluster: int, amount_to_get: int) -> list[MusicModel]:
    return MusicModel.objects.filter(genre=genre, cluster_class=cluster).order_by('?')[0:amount_to_get]


def add_music_in_set(music: list[MusicModel], music_set: set) -> None:
    if music:
        music_set.update(music)


def recomend(genres: dict, clusters: dict) -> ReturnDict:
    musics_set = set()
    for genre_key, genre_value in genres.items():
        for cluster_key, cluster_value in clusters.items():
            if not dict_values_type_is_valid(int, genre_value, cluster_value):
                continue
            len_to_get = genre_value + cluster_value
            musics_list = get_musics(genre_key, cluster_key, len_to_get)
            add_music_in_set(musics_list, musics_set)

    serializer = MusicSerializer(musics_set, many=True)

    return serializer.data


def get_genres_and_clusters(request):
    genres = request['genres'] if type(request['genres']) == dict else {}
    clusters = request['clusters'] if type(request['clusters']) == dict else {}

    return genres, clusters
