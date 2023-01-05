#!/usr/bin/env python3

"""Rock Paper Scissors  | By TLG NDE Cohort"""

import random


def main():
    """body of the game"""
    
   
    h_score = 0 #win/loss tracker
    c_score = 0 #win/loss tracker

    while h_score != 3:
        
        #user inputs a choice
        human = input("First to two wins wins.\nRock, Paper, or Scissors?\n>")
        human = human.title()
        
        #verifies user input is one of the three choices
        if human in ['Rock', 'Paper', 'Scissors']:
            #computer randomly chooses one of three options
            computer = random.choice(['Rock','Paper','Scissors'])
            #prints out both choices
            print(f'I choose {human}\n The computer chose {computer}')

            #determines winner
            if human =='Scissors' and computer =='Paper':
                print('You Win!')
                h_score +=1
                
            elif human == 'Rock' and computer == 'Scissors':
                print('You Win!')
                h_score +=1
                
            elif human == 'Paper' and computer == 'Rock':
                print ('You Win!')
                h_score +=1 

            elif human == computer :
                print('Its a Tie')

            else :
                print('You Lose')
                c_score +=1

            print(f'Score is {h_score}/{c_score}')

        else:
            print("You can't follow simple directions")
            exit()
        if h_score == 2:
            print("You Win")
            h_score = 3

        elif c_score ==2:
            print ("CPU Wins")
            h_score = 3

    

    #play again sequence
    again = input('Play Again? (y/n)')
    again = again.title()

    while again == 'Y':
        main()

        if again != 'Y':
            print('Thanks for playing')
            exit()

main()
#user inputs a choice
#computer generates a random choice
#choices need to be evaluated
#display results
