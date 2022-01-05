from django.db import models
from django.db.models import Model

class sensorData(models.Model):
    time = models.DateTimeField()
    bikeId = models.PositiveIntegerField()
    location_lat = models.DecimalField(max_digits=12, decimal_places=8)
    location_lon = models.DecimalField(max_digits=12, decimal_places=8)
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    humidity = models.DecimalField(max_digits=6, decimal_places=2)
    gaz1 = models.DecimalField(max_digits=6, decimal_places=2)
    gaz2 = models.DecimalField(max_digits=6, decimal_places=2)