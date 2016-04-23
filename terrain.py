#By Junior Recinos

import urllib.request
import json

#get the elevation at given coordinates
def get_elevetion(latitude, longitude):
	response = urllib.request.urlopen('https://maps.googleapis.com/maps/api/elevation/json?locations=' + str(latitude) +',' + str(-longitude) + '&key=AIzaSyDI03ffKcFoSS91qoiIZkp69gohHqGV66o')
	string = response.read().decode('utf-8')
	jdata = json.loads(string)
	return json.dumps(jdata['results'][0]['elevation'])

#print(get_elevetion(40,70))

