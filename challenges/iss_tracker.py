#!/usr/bin/env python3

"""Creates an ISS Tracker that updates everytime you run it"""

import json
import requests
import datetime as dt
import reverse_geocoder as rg

def main():

    iss_now = 'http://api.open-notify.org/iss-now.json'
    iss_raw = requests.get(iss_now)

    iss = iss_raw.json()
     #iss = {'longitude': 'xxxx',
     #       'latitude':'xxxx',
     #       'timestamp':'xxxx',
     #       'message':'xxxx'}
    print (iss)
    epoch_time = iss['timestamp']
    date = dt.datetime.fromtimestamp(epoch_time)
    
    print('CURRENT LOCATION OF THE ISS')
    print(f'Timestamp: {date}')
    print(f"Longitude: {iss.get('iss_position').get('longitude')}")
    print(f"Latitude: {iss.get('iss_position').get('latitude')}")



    lat= iss.get('iss_position').get('latitude')
    lon= iss.get('iss_position').get('longitude')

    # reverse_geocoder MUST be passed a tuple as the argument!
    coords_tuple= (lat, lon)

    result = rg.search(coords_tuple, verbose=False)
                                 # verbose=False removes an annoying output that reads 
                                 # "Loading formatted geocoded file..."
    print(result[0].get('name') , result[0].get('cc'))


main()

