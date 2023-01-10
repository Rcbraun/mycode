#!/usr/bin/env python3

import time

def main():
    
    while True:
        beer =(input('How many bottles of beer(0-99)'))
        try: 
            beer = int(beer)
            if beer <= 99:
               break
            elif beer>99:
               print('Too many bottles')

        except:
            print("That won't work")

    for beer in range(beer,0,-1):
        
        print(f'{beer} bottles of beer on the wall,{beer} bottles of beer! Take one down pass it around')
        print(f'{beer-1} bottles of beer on the wall')        
        time.sleep(0.5)        
   
main()
     
