import NoFly

import volatum.models

def addToDB():
    with open("airports.dat", 'r') as f:
        for line in f:
            Name = line.split(',')[1]
            latR = line.split(',')[6]
            longR = line.split(',')[7]


            x = Airport(airport_id=line.split(',')[0], name=line.split(',')[1], city=line.split(',')[2],
                        country=line.split(',')[3], iata_faa=line.split(',')[4], icao=line.split(',')[5],
                        latitude=line.split(',')[6], longitude=line.split(',')[7], altitude=line.split(',')[8],
                        timezone_offset=line.split(',')[9], dst=line.split(',')[10], timezone_tz=line.split(',')[11])
            x.save()

