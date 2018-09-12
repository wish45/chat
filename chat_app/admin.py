from django.contrib import admin
from .models import Room, Message, Oneroom, Onemessage

# Register your models here.

class MsgAdmin(admin.ModelAdmin):
    list_display = ('room', 'userId', 'message', 'timestamp')

class OneRoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'create_at', 'status')

class OneMsgAdmin(admin.ModelAdmin):
    list_display = ('room', 'userId', 'message', 'timestamp')

admin.site.register(Room)
admin.site.register(Message, MsgAdmin)
admin.site.register(Oneroom, OneRoomAdmin)
admin.site.register(Onemessage, OneMsgAdmin)
