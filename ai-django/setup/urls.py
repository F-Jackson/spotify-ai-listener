from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from photographer_assistent.views import *
from account.views import *


router = routers.DefaultRouter()
router.register(r'musics', MusicViewSet)
router.register(r'librarys', LibraryViewSet)
router.register(r'users', UserStaticsViewSet)
router.register(r'color_configs', ColorConfigsViewSet)
router.register(r'statics', UserStaticsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
