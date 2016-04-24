from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.template import RequestContext

from volatum.models import Airport, Drone
from airportdb import addToDB
from drone import registerDrone, mkDrone

# Create your views here.

def index(request):
    #addToDB()

    return HttpResponse("Hello, world.")


def zipsearch(request):
    return HttpResponse(request.get_full_path())

def addAirPortsToDB(request):
    addToDB()


def drone(request):
    # Example POST request from Drone data
    # volatum.mybluemix.net/drone?lat=VALUE&log=VALUE&speed=VALUE&alt=VALUE

    if request.method == 'GET':

        coordinates = (float( request.GET.__getitem__('lat').encode('utf8') ), float( request.GET.__getitem__('log').encode('utf8') ) )

        # If drone input has no lat or log
        if not coordinates:
            # Exit the request
            return HttpResponse('Drone check input invalid, no latitude and longitude')


        drone_input = {'location':coordinates,
                       'speed':float(request.GET.__getitem__('speed').encode('utf8')),
                       'alt':int(request.GET.__getitem__('alt').encode('utf8')),
                       'drone_id':request.GET.__getitem__('drone_id').encode('utf8')}

        registerDrone(drone_input)


    return render(request, 'volatum/index.html', {'drones': Drone.objects.all()})



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


def airportdb(request):
    airports = Airport.objects.all()


    #render(request, template, {key:value of data})
    return render(request, 'volatum/index.html', {'input':airports})