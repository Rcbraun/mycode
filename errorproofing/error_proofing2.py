#!/usr/bin/python3
"""try except else and finally | Alta3 Research"""

# python standard library
import uuid

# generate a UUID based on the host id, sequence number, and current time
# simulating a ticketed job number
ticket = uuid.uuid1()

#opens a configuration file of the users input
try:
    print('Type the name of the configuration file to load.')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileobj.read()
#general error if there is no configuration file 
except:
    x = 'General error with obtaining configuration file!'

#if there were no errors 
else:
    x = 'Switch config file found.'

#whether there were arrors or no it prints results out to log file
finally: 
    with open("try04.log", "a") as zlog:
        print('\n\nWriting results of routine to log file')
        print(ticket, " - ", x, file=zlog)
  
