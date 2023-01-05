#!/usr/bin/env python3

def main():
    
    #asks user for input on which character to learn about
    char_name = input('Which character do you want to know about? (Starlord, Mystique, Hulk)\n')
    
    #corrects capitalization
    char_name = char_name.title()
    
    #Proves that the input was saved to variable 'char_name'
    print(f'You chose {char_name}.')
    

    #asks user for the input on which statistic to lean about
    char_stat = input('What statistic do you want to know about? (real name, powers, archenemy)\n')
    
    #corrects capitalization
    char_stat = char_stat.lower()

    #proves that the user input was saved to the variable 'char_stat'
    print(f"You want to learn about {char_name}'s {char_stat}.")

    #creates the dictionary 'marvelchars' 
    marvelchars= {
     "Starlord":
      {"real name": "peter quill",
      "powers": "dance moves",
      "archenemy": "Thanos"},

     "Mystique":
      {"real name": "raven darkholme",
      "powers": "shape shifter",
      "archenemy": "Professor X"},

     "Hulk":
      {"real name": "bruce banner",
      "powers": "super strength",
      "archenemy": "adrenaline"}
             }
    #prints out the results 
    print(f"{char_name}'s {char_stat} is {marvelchars.get(char_name).get(char_stat).title()}")
    
    #allows the user to try again
    again = input('Would you like to lean more? (y/n)\n')
    again = again.title()
   
    #while continue arguement
    while again == "Y" :
       main()
    
    #exits the program if anything other than a 'y' is input
    if "Y" != again:
       print('Good Day')
       exit()


main()

