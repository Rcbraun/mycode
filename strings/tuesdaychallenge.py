#!/usr/bin/python3


def main():

  mylist = [1,2,3,4,5, "Python"]
  name = input("What is your name? \n")

  # This is what you should see when print runs-
  # Hi <name>! Welcome to Day 2 of Python Training!
  print(f"Hi {name.capitalize()}! Welcome to Day  {mylist[0]} of {mylist[5]} Training!")


main()
