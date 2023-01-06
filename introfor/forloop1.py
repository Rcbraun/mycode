#!/usr/bin/env python3

"""Learning about for loops"""


def main():
    vendors = ['cisco','juniper','big_ip','f5','arista'] #creates list vendors
    approved_vendors = ["cisco",'juniper','big_ip'] #creats second list of strings

    for x in vendors: #loop across the list vendors
        print('\nThe vendor is:' +x, end="") #each time throught the loop print x
        if x not in approved_vendors:
            print(' - NOT AN APPROVED VENDOR!', end= "")
    print('\nOur loop has ended') #when the loop ends prints this

main()


