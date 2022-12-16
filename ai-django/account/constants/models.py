BACKGROUND_COLOR = '#FFFFFF'
MENU_COLOR = '#000000'
BUTTON_COLOR = '#00FF00'
TEXT_COLOR = '#FFFFFF'
MUSIC_BACKGROUND_COLOR = '#000000'

GENRES_COICHES = (
    ('U', 'Undefined'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
)

def LAST_SONGS_DEFAULT():
    return {
        'songs_ids': [

        ]
    }


def CLUSTERING_STATS_DEFAULT():
    return {
        'listened_points': {
            "0": 10,
            "1": 10,
            "2": 10,
            "3": 10,
            "4": 10,
            "5": 10,
            "6": 10
        }
    }
