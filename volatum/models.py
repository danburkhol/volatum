from django.db import models

# Create your models here.

#NO FLY ZONE data model
class Airports(models.Model):
    airport_id = models.IntegerField()
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    iata_faa = models.CharField(max_length=3)
    icao = models.CharField(max_length=4)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
    timezone_offset = models.IntegerField()
    dst = models.CharField(max_length=1)
    timezone_tz = models.CharField(max_length=50)

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