from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Event, Ticket, User

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(User, UserAdmin)