MAX_LIBRARYS_PER_USER = 9

LIBRARYS_CREATE_NEED = (
    'name'
)

LIBRARYS_UPDATE_FILTER = (
    'name',
    'photo',
    'play_random',
    'use_ai'
)

LIBRARY_REQUEST_DELETE = 'musics_ids_to_delete'

LIBRARY_REQUEST_PUT = 'musics_ids_to_put'


MUSIC_RECOMEND_MUSICS_NEED = (
    'mode',
    'genres',
    'clusters'
)


MUSIC_SEARCH_NEED = (
    'mode',
    'search_text'
)
