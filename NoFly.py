import math
import Location
from volatum.models import AirportN

def offlimit (lat, long, rad = 10, mph = 0):
    with open("airports.dat", 'r') as f:
        for line in f:
            for i in range(1,20):
                latR = line.split(',')[i]
                try:
                    latR = float(latR)
                    isfloat = True
                except ValueError:
                    isfloat = False
                    continue
                if isfloat:
                    longR = line.split(',')[i+1]
                    longR = float(longR)
                    break
            miles = findDis(lat, latR, long, longR)
            if miles <= rad + mph * .015:
                return True
    return False

def dontfly (settings):
    if settings == True:
        print('STOP')
        return True
    else:
        return False

def getID():
    idlist = []
    with open("airports.dat", 'r') as f:
        for line in f:
           idair = line.split(',')[0]
           idlist.append(idair)
    return idlist
    

def getNames():
    namelist = []
    with open("airports.dat", 'r') as f:
        for line in f:
            name = line.split('"')[1]
            namelist.append(name)
    return namelist

def getLat():
    latlist = []
    with open("airports.dat", 'r') as f:
        for line in f:
            for i in range(1,10):
                latR = line.split(',')[i]
                try:
                    latR = float(latR)
                    isfloat = True
                except ValueError:
                    isfloat = False
                    continue
                
                if isfloat:
                	latlist.append(latR)
                	break
    return latlist

def getLong():
    longlist = []
    with open("airports.dat", 'r') as f:
        for line in f:
            for i in range(1,10):
                latR = line.split(',')[i]
                try:
                    latR = float(latR)
                    isfloat = True
                except ValueError:
                    isfloat = False
                    continue
                
                if isfloat:
                	longR = line.split(',')[i+1]
                	longR = float(longR)
                	longlist.append(longR)
                	break
    return longlist



def findDis(lat1, lat2, long1, long2, count = 0 ):
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)
    dlat = lat1 - lat2
    dlong = long1 - long2 
    a = pow(math.sin(dlat/2),2) + math.cos(lat1) * math.cos(lat2) * pow(math.sin(dlong/2),2)
    c =  2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    miles = c * 3960
    return miles

def addDB():
    n = getNames()
    i = getID()
    z = getLat()
    x = getLong()

    AirportN.objects.all()

    for a in range(0, len(i)):

        b = AirportN(airport_id=i[a], name=n[a], latitude=z[a], longitude=x[a])
        b.save()


if __name__ == '__main__':
    coord = Location.getLocation()
    #rad = int(input('rad: '))
    offlimit = offlimit(coord[0], coord[1])
    settings = True
    if offlimit:
        dontfly(settings)
        print(offlimit)
    n = getNames()
    i = getID()
    z = getLat()
    x = getLong()
    
    l = n + i
    for v in range(0, len(i)):
    	print(i[v], l[v], z[v], x[v])
    
