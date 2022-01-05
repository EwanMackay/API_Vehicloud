from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import sensorDataSerializer
from .models import sensorData

# Create your views here.


class sensorDataViewSet(viewsets.ModelViewSet):
    queryset = sensorData.objects.all().order_by('-id')
    serializer_class = sensorDataSerializer