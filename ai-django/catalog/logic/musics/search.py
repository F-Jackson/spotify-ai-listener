from rest_framework import status
from rest_framework.response import Response
from collections import Counter

from rest_framework.utils.serializer_helpers import ReturnDict

from catalog.logic.musics.prepare_text import prepare_text
from catalog.models import MusicModel
from catalog.serializers import MusicSerializer


def find_text_model(text: list[str]) -> Counter:
    ids = []
    for txt in text:
        f = MusicModel.objects.filter(search__contains=txt)
        if f:
            for j in f:
                ids.append(j.pk)
    if not ids:
        raise Exception("No matches for your search")

    ids_count = Counter(ids)
    return ids_count


def sort_counter(counter: Counter) -> list:
    sort = sorted(counter.items(), key=lambda item: -item[1])
    return sort


def get_models(id_list: list) -> list[MusicModel]:
    models = []
    for key, num_ocurr in id_list:
        music = MusicModel.objects.get(pk=key)
        models.append(music)
    return models


def serialize(model_list: list[MusicModel]) -> ReturnDict:
    serializer = MusicSerializer(model_list, many=True)
    return serializer.data


def search(text: str) -> Response:
    try:
        new_text = prepare_text(text)
        ids = find_text_model(new_text)
        sorted_ids = sort_counter(ids)
        models = get_models(sorted_ids)
        serializer_data = serialize(models)
    except Exception as e:
        return Response({'errors': e.args}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer_data, status=status.HTTP_200_OK)
