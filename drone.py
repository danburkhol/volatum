from datetime import datetime
from volatum.models import Drone

def registerDrone(drone_input):
    # drone_input
    # location      touple[lat, log]
    # speed         in mp/h
    # alt           feet
    # drone_id

    # If no drone ID was provided from the user
    if not drone_input['drone_id']:
        pass

    d = Drone.objects.get(drone_id=drone_input['drone_id'])

    # If it's not in the database, create a new entry
    if not d:
        d = Drone(drone_id=drone_input['drone_id'])

    d.latitude = drone_input['location']['lat']
    d.longitude = drone_input['location']['lat']
    d.altitude = drone_input['alt']
    d.last_seen = datetime.now()

    d.save()

