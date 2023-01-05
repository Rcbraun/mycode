#!/usr/bin/env python3

"""Try Except Else and Finally, Error Proofing!"""


#imports python standard library
import uuid                

#start with an infinite loop, error handling, and escapes
def main():                

    while True:

#divides user input x/y (must be integers)
        try:               
            print("\nLet's divide x by y!")
            x = int(input('What is the integer value of x?'))
            y = int(input('What is the integer value of y?'))
            print("The value of x/y: ",x/y)

#Prevents program from crashing due to a division by zero
        except ZeroDivisionError as err:  
            print("Handling run-time error:", err)
       
#Prevents program from crashing due to a non 'int' input from the user
        except ValueError as err:
            print("That was not a legal value for division:",err)
      
#Prevents program from crashing due to an unexpected reason            
        except Exception as err:
            print("We did not anticipate that:",err)
#raise by itself simply calls the previous exception that was thrown            
            raise

#else ONLY runs if there were no errors
        else:
            print("\nThanks for learning to handle errors.")
            break


main()
