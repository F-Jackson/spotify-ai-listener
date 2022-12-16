from catalog.constants._views import LIBRARYS_CREATE_NEED, LIBRARYS_UPDATE_FILTER, LIBRARY_REQUEST_PUT, \
    LIBRARY_REQUEST_DELETE

MUSIC_LIST = {
    'url': '/catalog',
    'methods': [
        {
            'method': 'get',
            'info': 'Return list of musics based on the chosen mode',
            'request template': {
                'mode': 'search or recomend'
            }
        }
    ]
}

MUSIC_DETAIL = {
    'url': '/catalog/<int:music_id>',
    'methods': [
        {
            'method': 'get',
            'info': 'Return the music info'
        }
    ]
}

LIBRARY_LIST = {
    'url': '/librarys',
    'methods': [
        {
            'method': 'get',
            'info': 'Get all librarys from user'
        },
        {
            'method': 'put',
            'info': 'Create new library for user',
            'request template': LIBRARYS_CREATE_NEED
        }
    ]
}

LIBRARY_DETAIL = {
    'url': '/librarys/<int:library_id>',
    'methods': [
        {
            'method': 'get',
            'info': 'Get library info'
        },
        {
            'method': 'patch',
            'info': 'Update library info',
            'request template': LIBRARYS_UPDATE_FILTER
        },
        {
            'method': 'delete',
            'info': 'Delete library'
        }
    ]
}

MUSICS_IN_LIBRARYS_LIST = {
    'url': '/librarys/<int:library_id>/catalog',
    'methods': [
        {
            'method': 'get',
            'info': 'Get all music in a library'
        },
        {
            'method': 'put',
            'info': 'Put music in a library',
            'request template': LIBRARY_REQUEST_PUT
        },
        {
            'method': 'delete',
            'info': 'Remove music in a library',
            'request template': LIBRARY_REQUEST_DELETE
        }
    ]
}

DOCS = [
    MUSIC_LIST,
    MUSIC_DETAIL,
    LIBRARY_LIST,
    LIBRARY_DETAIL,
    MUSICS_IN_LIBRARYS_LIST
]
