from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.template import RequestContext

from volatum.models import AirportN, Drone
from NoFly import addDB
from drone import registerDrone

# Create your views here.

def index(request):


    airports = [AirportN(airport_id=523, name='Tampa Intl Airport', latitude=27.9835, longitude=82.5371), ]
    drones = Drone.objects.all()

    return render(request, 'demo/index.html', {'airport_data': airports, 'drone_data': drones})



def zipsearch(request):
    return HttpResponse(request.get_full_path())

def addAirPortsToDB(request):
    addDB()

    return HttpResponse('Added to DB')


def drone(request):
    # Example POST request from Drone data
    # volatum.mybluemix.net/drone?lat=VALUE&log=VALUE&speed=VALUE&alt=VALUE


    try:
        coordinates = (float( request.GET.__getitem__('lat').encode('utf8') ), float( request.GET.__getitem__('log').encode('utf8') ) )
    except:
        return render(request, 'volatum/index.html', {'drones': Drone.objects.all()})

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

    #render(request, template, {key:value of data})
    return render(request, 'volatum/index.html', {'input':Airport.objects.all()})


def airportdb(request):
    airports = Airport.objects.all()


    #render(request, template, {key:value of data})
    return render(request, 'volatum/index.html', {'input':airports})