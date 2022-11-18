from django.urls import path

from catalog import views

urlpatterns = [
    path('catalog/', views.MusicList.as_view()),
    path('catalog/<int:pk>', views.MusicDetail.as_view()),
    path('librarys/', views.LibraryList.as_view()),
    path('librarys/<int:pk>', views.LibraryDetail.as_view()),
    path('librarys/<int:pk>/catalog', views.MusicsInLibrarysList.as_view())
]
