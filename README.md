# Volatum
Team Musk Entry for the 2016 NASA Space Apps Challenge hosted in Tampa, FL @ SOFWERX

# Team Roster
- Daniel Burkholder
- Junior Recinos
- John Astafanous
- Stephen Astafanous
- Kevin McKernan

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


### Example HTTP GET Request to get drone area conditions ###
```sh
http://volatum.mybluemix.net/drone?speed=3&alt=20&lat=27.5000&log=-82.00&drone_id=1337bluemixertest
```

### Examples ###
```sh
http://volatum.mybluemix.net/
http://volatum.mybluemix.net/airport_test
http://volatum.mybluemix.net/airport_test_db
http://volatum.mybluemix.net/drone

```

### Run the local server ###
```sh
$ python manage.py runserver
```