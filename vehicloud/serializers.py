# serializers.py
from rest_framework import serializers

from .models import sensorData

class sensorDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sensorData
        fields = ('id', 'bikeId','time', 'location_lat', 'location_lon', 'temperature', 'humidity', 'gaz1', 'gaz2')