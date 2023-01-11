#!/usr/bin/env python3

'''Looping challenge| Richard Braun'''


def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    
    veggies = ['carrots','celery']
       
    choice = input('Pick a farm(NE Farm, W Farm, SE Farm, E Farm)')
    choice = choice.capitalize()

    if choice == farms[0]['name']:
        #if veggies in farms[0]['agriculture']:
                
        #else:    
        print (farms[0]['agriculture'])
    elif choice == farms[1]['name']:
        print (farms[1]['agriculture'])
    elif choice == farms[2]['name']:
        print (farms[2]['agriculture'])
   # elif choice == farms[3]['name']:
    #    print(farms[3]['agriculture'])
    else:
        print('Thats not a farm')
        main()

    

if __name__ == "__main__":
    main()

