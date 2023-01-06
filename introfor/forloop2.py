#!/usr/bin/env python3

"""Intro into for loops"""

def main():
    for i in range(4):
        print(i)

    for x in range(10):
        print (x, end = " ")
    for z in range(10):
        print(z)

    fruitbowl= ['apple','pear','grapes']
    foo = open('ourfile.txt','w')
    for fruit in fruitbowl:
        print (fruit)
    for fruit in fruitbowl:
        print(fruit, file=foo)
    foo.close()

main()
