import math
import Location

def offlimit (lat, long, rad = 5, sscale = 0):
    with open("airports.dat", 'r') as f:
        for line in f:
            Name = line.split(',')[1]
            latR = line.split(',')[6]
            longR = line.split(',')[7]
            try:
                latR = int(float(latR))
            except ValueError:
                break
            try:
                longR = int(float(longR))
            except ValueError:
                   break
            miles = findDis(lat, latR, long, longR)
            if miles <= rad:
                return Name
    return 'good'

def dontfly (settings):
    if settings == True:
        print('STOP')
        return True
    else:
        return False

def addData():
    pass

def findDis(lat1, lat2, long1, long2):
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)
    dlat = lat1 - lat2
    dlong = long1 - long2 
    a = pow(math.sin(dlat/2),2) + math.cos(lat1) * math.cos(lat2) * pow(math.sin(dlong/2),2)
    c =  2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    miles = c * 3961
    return miles
    

if __name__ == '__main__':
    coord = Location.getLocation()
    #rad = int(input('rad: '))
    offlimit = offlimit(coord[0], coord[1])
    settings = True
    if not offlimit == 'good':
        dontfly(settings)
        print(offlimit)
    
