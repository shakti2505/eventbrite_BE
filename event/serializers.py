from rest_framework import serializers

from .models import Event, Like


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','user_id', 'event_name','event_date', 'event_location','event_img',]



class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'event']

