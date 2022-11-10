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
"email": "test@test.com",
"password": "123"
}

if __name__ == '__main__':
    run()
