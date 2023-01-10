#!/usr/bin/env python3

"""Creates an ISS Tracker that updates everytime you run it"""

import json
import requests
import datetime as dt


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
    longitude= iss ['iss_position'('longitude')]
    latitude = iss ['latitude']

    print('CURRENT LOCATION OF THE ISS')
    print(f'Timestamp: {date}')
    print(f'Longitude: {longitude}')
    print(f'Latitude: {latitude}')



main()

