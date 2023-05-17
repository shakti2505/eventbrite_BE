from django.shortcuts import render
from .serializers import EventSerializers
from .models import Event
from rest_framework import viewsets



   
class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class =EventSerializers

