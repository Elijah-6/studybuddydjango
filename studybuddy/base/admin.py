from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import User, Room, Topic, Message

admin.site.register(User,UserAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
