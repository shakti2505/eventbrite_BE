from django.contrib import admin
from .models import Event, Like

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display= ['user_id', 'event_name','event_date', 'event_location','event_img',]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display= ['id','event']

