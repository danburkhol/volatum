#Elevation recognition utility functions
#By Junior Recinos

import urllib.request
import json
import math

#get the elevation at given coordinates
def get_elevetion(latitude, longitude):
	#elevation api call
	response = urllib.request.urlopen('https://maps.googleapis.com/maps/api/elevation/json?locations=' + str(latitude) +',' + str(longitude) + '&key=AIzaSyDI03ffKcFoSS91qoiIZkp69gohHqGV66o')
	string = response.read().decode('utf-8')
	jdata = json.loads(string)

	#creating dictionary {(latitude, longitude): elevation}
	elevation = {(latitude, longitude):float(json.dumps(jdata['results'][0]['elevation']))}
	return elevation



	#helper function, gets next coordinate 
def next_coordinate(latitude, longitude, distance = 0.5, bearing = 0):
	#turning data into radians
	latitude = math.radians(latitude)
	longitude = math.radians(longitude)
	bearing = math.radians(bearing)

	#calculating next latitude and next longitude (doing math)
	nextlatitude = math.asin(math.sin(latitude)*math.cos(distance/3960) + math.cos(latitude) * math.sin(distance/3960)*math.cos(bearing))
	nextlongitude = longitude + math.atan2(math.sin(bearing)*math.sin(distance/3960)*math.cos(latitude), math.cos(distance/3960)-math.sin(latitude)*math.sin(nextlatitude))

	#turning back to degrees
	nextlatitude = math.degrees(nextlatitude)
	nextlongitude = math.degrees(nextlongitude)

	#return next coordinate as a tuple
	nextCoordinate = (nextlatitude, nextlongitude)
	return nextCoordinate



	#collects elevation data around the drone, returns a list of dictionaries
def look_elevation_ahead(latitude, longitude, bearing = 0, distance = 5):
	#list containing dictionaries with the coordinates and coresponding elevation
	elevations_ahead = []

	#collecting data at various distances
	for degree in range(-20 + bearing, 21 + bearing):
		if degree % 10 == 0:
			distance = 2.5
			nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
			elevations_ahead.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))
		if degree % 20 == 0:
			distance = 1.0
			nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
			elevations_ahead.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))
		if degree % 5 == 0:
			distance = 5.0
			nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
			elevations_ahead.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))

	return elevations_ahead

def elevation_data(latitude = 27.96191289, longitude = -82.4443672):
	gives_me_all_the_data = []
	for degree in range(0,361):
		if degree % 36 == 0:
			distance = 0.5
			nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
			gives_me_all_the_data.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))
		if degree % 20 == 0:
			distance = 1.0
			nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
			gives_me_all_the_data.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))
		if degree % 12 == 0:
			distance = 2.0
			nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
			gives_me_all_the_data.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))
		if degree % 10 == 0:
			distance = 3.0
			nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
			gives_me_all_the_data.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))
		if degree % 5 == 0:
			distance = 4.0
			nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
			gives_me_all_the_data.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))	
		distance = 5.0
		nextCoordinates = next_coordinate(latitude, longitude, distance, degree)
		gives_me_all_the_data.append(get_elevetion(nextCoordinates[0], nextCoordinates[1]))
	return gives_me_all_the_data





if __name__ == '__main__':

	mcoordinates = (43.8791, 103.4591)
	elevations = elevation_data()
	for elevation in elevations:
		print(elevation)




