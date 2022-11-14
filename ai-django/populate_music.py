import csv
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


from musics.models import MusicModel


def run():
    with open('SpotifyFeatures.csv') as file:
        reader = csv.reader(file)
        next(reader)

        MusicModel.objects.all().delete()

        for row in reader:
            MusicModel.objects.get_or_create(
                genre=row[2],
                author=row[3],
                name=row[4],
                track_id=row[5],
                cluster_class=row[-1]
            )

{
    "username": "jacks",
    "first_name": "",
    "last_name": "",
    "email": "test@test.com",
    "color_configs": {
        "background_color": "#FFFFFF",
        "menu_color": "#FFFFFF",
        "button_color": "#000000",
        "text_color": "#FFFFFF",
        "music_background_color": "#A6A6A6"
    }
}

{
"username": "jacks",
"email": "test@test.com",
"password": "123"
}

{
   "username":"jacks",
   "first_name":"",
   "last_name":"",
   "email":"test@test.com",
   "color_configs":{
      "background_color":"#FFFFFF",
      "menu_color":"#FFFFFF",
      "button_color":"#000000",
      "text_color":"#FFFFFF",
      "music_background_color":"#A6A6A6"
   },
   "other_settings":{
      "country_code":null,
      "genre":"U"
   }
}

{
   "username":"jac@ks",
   "first_name":"",
   "last_name":"",
   "email":"test@test.com",
   "color_configs":{
      "background_color":"#FFFFFFF",
      "menu_color":"#FFFFFF",
      "button_color":"#000000",
      "text_color":"#FFFFFF",
      "music_background_color":"#A6A6A6"
   },
   "other_settings":{
      "country_code":null,
      "genre":"PO"
   }
}

if __name__ == '__main__':
    run()
