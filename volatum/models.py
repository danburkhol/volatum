from django.db import models

# Create your models here.

# NO FLY ZONE data model
# http://openflights.org/data.html
class Airport(models.Model):
    airport_id = models.IntegerField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    iata_faa = models.CharField(max_length=10)
    icao = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
    timezone_offset = models.IntegerField()
    dst = models.CharField(max_length=100)
    timezone_tz = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NoFlyZone(models.Model):


    def __str__(self):
        return self.name


class Drone(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    drone_id = models.CharField(max_length=25)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
    last_seen = models.DateTimeField()

    def __str__(self):
        return self.name


class Weather(models.Model):


    def __str__(self):
        return self.name