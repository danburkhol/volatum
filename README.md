# Volatum
Team Musk Entry for the 2016 NASA Space Apps Challenge hosted in Tampa, FL @ SOFWERX

### Project: Don't Crash My Drone ###
https://2016.spaceappschallenge.org/challenges/aero/dont-crash-my-drone

Create an app that will enable small drone operators to know more about specific weather parameters, local terrain and no fly zones within a five-mile radius of their GPS location.



# Team Roster
- Daniel Burkholder - Project Management, Backend (IBM Bluemix, Django, PostgreSQL), Programmer:
- Junior Recinos - Programmer: Weather, Terrain data
- John Astafanous - Programmer: Frontend
- Stephen Astafanous - Programmer: No-Fly-Zones
- Kevin McKernan - Programmer: General, Planning

### Installation ###
```sh
$ git clone https://github.com/danburkhol/volatum
$ cd volatum
$ pip install -r requirements.txt
```

### Run the local server ###
```sh
$ python manage.py runserver
```


### Examples ###

Send your drone's current location, speed, and altitude to Volatum
```sh
http://volatum.mybluemix.net/drone?speed=3&alt=20&lat=27.5000&log=-82.00&drone_id=1337bluemixertest
```

```sh
http://volatum.mybluemix.net/
http://volatum.mybluemix.net/airport_test
http://volatum.mybluemix.net/airport_test_db
http://volatum.mybluemix.net/drone
```
