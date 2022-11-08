from django.contrib import admin
from .models import *


class MusicAdmin(admin.ModelAdmin):
    pass


admin.site.register(MusicModel, MusicAdmin)


class LibraryAdmin(admin.ModelAdmin):
    pass


admin.site.register(LibraryModel, LibraryAdmin)
