#!/usr/bin/python3

# inputs the users name

name = input ("Let me know your name: ")
day = input ("What day of the week is it? \n")
print ("Hello, "+ name + "! Happy "+ day + "!")
exit()



# Best Practice
## F String (formatted string)
### {variables}
print(f"Hello, {name}! Happy {day}!")
