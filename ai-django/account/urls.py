from django.urls import path

from account import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>', views.UserDetail.as_view()),
    path('color_settings/<int:pk>', views.ColorConfigsDetail.as_view()),
    path('statiscs/<int:pk>', views.UserStaticsDetail.as_view()),
]
