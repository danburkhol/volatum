from django.shortcuts import render
from django.http import HttpResponse

from volatum.models import Airport
from airportdb import addToDB

# Create your views here.

def index(request):
    #addToDB()

    return HttpResponse("Hello, world.")


def zipsearch(request):
    return HttpResponse(request.get_full_path())

def drone(request):
    
    return HttpResponse("Drone Check - Hello, George :) ")

def airport(request):
    #airports = Airports.objects.all()
    #for x in airports:
    #    print(x)


    x = Airport(airport_id=4, name='dullas', city='amazon',

                 country='united states of swag', iata_faa='PWN', icao='LEET',

                 latitude=58.39405, longitude=47.12830, altitude=68,

                 timezone_offset=5, dst=1, timezone_tz='New York/Americas')

    y = Airport(airport_id=4, name='dullas', city='amazon',

                country='united states of swag', iata_faa='PWN', icao='LEET',

                latitude=58.39405, longitude=47.12830, altitude=68,

                timezone_offset=5, dst=1, timezone_tz='New York/Americas')

    input = [x, y]


    #render(request, template, {key:value of data})
    return render(request, 'volatum/index.html', {'input':input})


