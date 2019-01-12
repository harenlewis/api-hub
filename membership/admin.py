from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login')

admin.site.register(User, UserAdmin)
