from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer

from account.models import UserModel, UserStaticsModel, ColorConfigsModel


class UserView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            model = request.user
            serializer = UserSerializer(model)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        else:
            username = request.data["username"]
            password = request.data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        if not request.user.is_authenticated:
            user = User.objects.filter(username=request.data['username'], email=request.data['email'])

            if not user:
                user = User.objects.create_user(
                    username=request.data['username'],
                    password=request.data['password'],
                    email=request.data['email']
                )
                serializer = UserSerializer(user)
                UserModel.objects.create(user=user)
                UserStaticsModel.objects.create(user=user)
                ColorConfigsModel.objects.create(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        if request.user.is_authenticated:
            model = request.user
            serializer = UserSerializer(model, data=request.data)
            if serializer.is_valid():
                model.save()
                logout(request)
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        if request.user.is_authenticated:
            if request.user.check_password(request.data['password']):
                request.user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_404_NOT_FOUND)
