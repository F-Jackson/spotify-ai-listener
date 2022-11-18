import csv
import django
import os

from catalog.logic.musics.prepare_text import prepare_text

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from catalog.models import MusicModel


def run():
    with open('SpotifyFeatures.csv', encoding="utf8", errors="ignore") as file:
        reader = csv.reader(file)
        next(reader)

        MusicModel.objects.all().delete()

        for row in reader:
            search = ' '.join([*prepare_text(row[3]), *prepare_text(row[4]), *prepare_text(row[5])])
            print(search)
            MusicModel.objects.get_or_create(
                genre=row[3],
                author=row[4],
                name=row[5],
                track_id=row[6],
                cluster_class=row[-1],
                search=search
            )

# {
#     "username": "jacks",
#     "first_name": "",
#     "last_name": "",
#     "email": "test@test.com",
#     "color_configs": {
#         "background_color": "#FFFFFF",
#         "menu_color": "#FFFFFF",
#         "button_color": "#000000",
#         "text_color": "#FFFFFF",
#         "music_background_color": "#A6A6A6"
#     }
# }
#
# {
# "username": "jacks",
# "email": "test@test.com",
# "password": "123"
# }
#
# {
#    "username":"jacks",
#    "first_name":"",
#    "last_name":"",
#    "email":"test@test.com",
#    "color_configs":{
#       "background_color":"#FFFFFF",
#       "menu_color":"#FFFFFF",
#       "button_color":"#000000",
#       "text_color":"#FFFFFF",
#       "music_background_color":"#A6A6A6"
#    },
#    "other_settings":{
#       "country_code":null,
#       "genre":"U"
#    }
# }
#
# {
#    "username":"jac@ks",
#    "first_name":"",
#    "last_name":"",
#    "email":"test@test.com",
#    "color_configs":{
#       "background_color":"#FFFFFFF",
#       "menu_color":"#FFFFFF",
#       "button_color":"#000000",
#       "text_color":"#FFFFFF",
#       "music_background_color":"#A6A6A6"
#    },
#    "other_settings":{
#       "country_code":null,
#       "genre":"PO"
#    }
# }
#
# {
#     "musics_ids_to_put": [1, 2]
# }

if __name__ == '__main__':
    run()
