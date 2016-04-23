from django.shortcuts import render
from django.http import HttpResponse

from volatum.models import Airports
from airportdb import addToDB

# Create your views here.

def index(request):
    addToDB()

    return HttpResponse("Hello, world.")


def zipsearch(request):
    return HttpResponse(request.get_full_path())

def drone(request):
    
    return HttpResponse("Drone Check")

def airport(request):
    airports = Airports.objects.all()
    return render(request, 'volatum/index.html')


