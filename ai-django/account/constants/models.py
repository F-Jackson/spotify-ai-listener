BACKGROUND_COLOR = '#FFFFFF'
MENU_COLOR = '#FFFFFF'
BUTTON_COLOR = '#000000'
TEXT_COLOR = '#FFFFFF'
MUSIC_BACKGROUND_COLOR = '#A6A6A6'

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
