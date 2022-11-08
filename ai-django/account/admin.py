from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserModel._meta.get_fields()]


admin.site.register(UserModel, UserAdmin)
