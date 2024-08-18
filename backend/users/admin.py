from django.contrib import admin

from .models import Preferences, User

# Register your models here.
admin.site.register(Preferences)
admin.site.register(User)
