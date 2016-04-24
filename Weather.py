#from datetime import datetime
#from volatum.models import Drone
from volatum.models import Weather
import urllib.request
import json


def coor_weather(longitude, latitude):
    response = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?lat=' + str(latitude) + '&lon=' + str(longitude) + '&APPID=9b0d0c63e41990b58d93ecaea70070ca')
    string = response.read().decode('utf-8')
    jdata = json.loads(string)
    return json.loads(json.dumps(jdata, indent=4, sort_keys=True))


def zip_weather(zipcode):
    response = urllib.request.urlopen('http://api.openweathermap.org./data/2.5/weather?zip=' + str(zipcode) + ',us&APPID=9b0d0c63e41990b58d93ecaea70070ca')
    string = response.read().decode('utf-8')
    jdata = json.loads(string)
    return json.loads(json.dumps(jdata, indent=4, sort_keys=True))


def checkWeather(drone_input):
    w = coor_weather(drone_input['location']['lat'], drone_input['location']['log'])
    pass

