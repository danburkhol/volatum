import math
import Location
import imaplib
import codecs


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
    massiveList = []
 
        #Take line
    for line in open('airports.dat', 'r'):
        L = []
     
        L = line.split(',')
               
        massiveList.append(L)
        print(L)

    return miles
    

if __name__ == '__main__':
  #  coord = Location.getLocation()
   # #rad = int(input('rad: '))
    #offlimit = offlimit(coord[0], coord[1])
    #settings = True
    #if not offlimit == 'good':
     #   dontfly(settings)
      #  print(offlimit)
    addData()
