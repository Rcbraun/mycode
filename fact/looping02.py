#!/usr/bin/env python3

"""Sorting data into seperate files"""


import os

#chdir.os(~/mycode/fact/)

def main():


    with open("dnsservers.txt","r") as dnsfile: #opens file in read mode
        
        dnslist = dnsfile.readlines()#creates list of lines in the dnsfile
        
        for svr in dnslist: #loop over lines
            print(svr, end="")

    print ('dnsfile is closed')#shows that the file is closed


main()



