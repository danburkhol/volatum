import math
import Location

def offlimit (lat, long, rad = 10, mph = 0):
    count = 0
    miles = 0
    with open("airports.dat", 'r') as f:
        for line in f:
            Name = line.split(',')[1]
          
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
            
         
            count+=1
            print(longR, latR)
            miles = findDis(lat, latR, long, longR)
            print(count, miles, latR, longR)
            if miles <= rad + mph * .015:
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
    

if __name__ == '__main__':
    coord = Location.getLocation()
    #rad = int(input('rad: '))
    offlimit = offlimit(coord[0], coord[1])
    settings = True
    if not offlimit == 'good':
        dontfly(settings)
        print(offlimit)
    
