from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

import catalog.urls as music_urls
import user.urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(music_urls)),
    path('user/', include(user_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
