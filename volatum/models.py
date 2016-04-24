from django.db import models

# Create your models here.

# NO FLY ZONE data model
# http://openflights.org/data.html
class Airport(models.Model):
    airport_id = models.IntegerField()
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

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


class Elevation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.FloatField()


    def __str__(self):
        return self.name