from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return UserModel.objects.get(user=pk)
        except UserModel.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        if request.user.is_authenticated:
            model = self.get_object(request.user)
            serializer = UserSerializer(model)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, format=None):
        if request.user.is_authenticated:
            model = self.get_object(request.user)
            serializer = UserSerializer(model, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ColorConfigsDetail(APIView):
    def get_object(self, pk):
        try:
            return ColorConfigsModel.objects.get(user=pk)
        except ColorConfigsModel.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        if request.user.is_authenticated:
            model = self.get_object(request.user)
            serializer = ColorConfigsSerializer(model)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, format=None):
        if request.user.is_authenticated:
            model = self.get_object(request.user)
            serializer = ColorConfigsSerializer(model, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserStaticsDetail(APIView):
    def get_object(self, pk):
        try:
            return UserStaticsModel.objects.get(user=pk)
        except UserStaticsModel.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        if request.user.is_authenticated:
            model = self.get_object(request.user)
            serializer = UserStaticsSerializer(model)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, format=None):
        if request.user.is_authenticated:
            model = self.get_object(request.user)
            serializer = UserStaticsSerializer(model, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
