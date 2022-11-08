from rest_framework import viewsets
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class ColorConfigsViewSet(viewsets.ModelViewSet):
    queryset = ColorConfigsModel.objects.all()
    serializer_class = ColorConfigsSerializer


class UserStaticsViewSet(viewsets.ModelViewSet):
    queryset = UserStaticsModel.objects.all()
    serializer_class = UserStaticsSerializer
