from django.urls import path

from catalog import views

urlpatterns = [
    path('catalog/', views.MusicList.as_view()),
    path('catalog/list/', views.MusicViewset.as_view({'get': 'list'})),
    path('librarys/', views.LibraryList.as_view()),
    path('librarys/<int:pk>/', views.LibraryDetail.as_view()),
    path('librarys-musics/<int:pk>/', views.MusicsInLibrarysList.as_view())
]
