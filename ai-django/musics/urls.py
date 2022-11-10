from django.urls import path

from musics import views

urlpatterns = [
    path('musics/', views.MusicList.as_view()),
    path('musics/<int:pk>', views.MusicDetail.as_view()),
    path('librarys/', views.LibraryList.as_view()),
    path('librarys/<int:pk>', views.LibraryDetail.as_view())
]