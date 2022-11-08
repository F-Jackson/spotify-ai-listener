from rest_framework import viewsets
from .models import *
from .serializers import *


class MusicViewSet(viewsets.ModelViewSet):
    queryset = MusicModel.objects.all()
    serializer_class = MusicSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = LibraryModel.objects.all()
    serializer_class = LibrarySerializer
