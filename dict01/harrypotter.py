#!/usr/bin/env python3
"""Which Hogwarts House do you belong in? | Richard Braun"""

def main():
 
    #establishes counters for each house
    G = 0
    S = 0
    R = 0
    H = 0

    #presents the overall question
    print('\nWhich Howarts House do you belong in?\n')
    
    #initial question dictionary
    question1 = {"question" : "Pick a candy.",
                 "A" : ["Chocolate Frogs" , "Gryffindor"],
                 "B" : ["Bertie Bott's Every Flavor Beans" , "Hufflepuff"],
                 "C" : ["Honeydukes Sherbert Lemons" , "Ravenclaw"],
                 "D" : ["Fizzy Wizzy" , "Slytherin"]}

    while True:
        #input question 1 and possible answers saves to A1
        A1 = input (f"Question 1 - {question1.get('question')}\n A {question1.get('A')[0]}\n B {question1.get('B')[0]}\n C {question1.get('C')[0]}\n D {question1.get('D')[0]}\n " )
        A1 = A1.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A1 == 'A':
            G += 1
            break
        elif A1 == 'B':
            H += 1
            break
        elif A1 == 'C':
            R += 1
            break
        elif A1 == 'D':
            S += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')
            

    #quistion 2 dictionary
    question2 = {"question" : "Pick a Pet",
                 "A" : ["Lizard" , "Slytherin"],
                 "B" : ["Dog" , "Gryffindor"],
                 "C" : ["Cat" , "Ravenclaw"],
                 "D" : ["Ferret" , "Hufflepuff"]}

    while True:
        #input question 2 and possible answers saves to A2
        A2= input (f"Question 2 - {question2.get('question')}\n A {question2.get('A')[0]}\n B {question2.get('B')[0]}\n C {question2.get('C')[0]}\n D {question2.get('D')[0]}\n " )
        A2 = A2.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A2 == 'A':
            S += 1
            break
        elif A2 == 'B':
            G += 1
            break
        elif A2 == 'C':
            R += 1
            break
        elif A2 == 'D':
            H += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')




    #question 3 dictionary
    question3 = {"question" : "Pick a Class",
                 "A" : ["Charms" , "Ravenclaw"],
                 "B" : ["Potions" , "Slytherin"],
                 "C" : ["History of Magic" , "Hufflepuff"],
                 "D" : ["Transfiguration" , "Gryffindor"]}
    while True:
        #input question 3 and possible answers saves to A3
        A3= input (f"Question 3 - {question3.get('question')}\n A {question3.get('A')[0]}\n B {question3.get('B')[0]}\n C {question3.get('C')[0]}\n D {question3.get('D')[0]}\n " )
        A3 = A3.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A3 == 'A':
            R += 1
            break
        elif A3 == 'B':
            S += 1
            break
        elif A3 == 'C':
            H += 1
            break
        elif A3 == 'D':
            G += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')

    #question 4 dictionary
    question4 = {"question" :"If your best friend cheated on a test you would?",
                 "A":["Offer to help them study for the next one", "Hufflepuff"],
                 "B":["Offer to let them cheat off of your test next time" , "Slytherin"],
                 "C":["Tell on them, that's not fair","Gryffindor"],
                 "D":["Ignore it","Ravenclaw"]}
    while True:
        #input question 4 and possible answers saves to A4
        A4= input (f"Question 4 - {question4.get('question')}\n A {question4.get('A')[0]}\n B {question4.get('B')[0]}\n C {question4.get('C')[0]}\n D {question4.get('D')[0]}\n " )
        A4 = A4.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A4 == 'A':
            H += 1
            break
        elif A4 == 'B':
            S += 1
            break
        elif A4 == 'C':
            G += 1
            break
        elif A4 == 'D':
            R += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')

    #question 5 dictionary
    question5 = {"question":"Pick a color",
                 "A":["Blue","Ravenclaw"],
                 "B":["Yellow","Hufflepuff"],
                 "C":["Red","Gryffindor"],
                 "D":["Green","Slytherin"]}
    while True:
        #input question 5 and possible answers saves to A5
        A5= input (f"Question 5 - {question5.get('question')}\n A {question5.get('A')[0]}\n B {question5.get('B')[0]}\n C {question5.get('C')[0]}\n D {question5.get('D')[0]}\n " )
        A5 = A5.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A5 == 'A':
            R += 1
            break
        elif A5 == 'B':
            H += 1
            break
        elif A5 == 'C':
            G += 1
            break
        elif A5 == 'D':
            S += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')
    #question 6 dictionary
    question6 = {"question":"If you could only do one thing for the rest of your life you would...",
                 "A":["Explore the world", "Gryffindor"],
                 "B":["Start your own company","Slytherin"],
                 "C":["Stay in school forever","Ravenclaw"],
                 "D":["Start a family","Hufflepuff"]}
    while True:
        #input question 6 and possible answers saves to A6
        A6= input (f"Question 6 - {question6.get('question')}\n A {question6.get('A')[0]}\n B {question6.get('B')[0]}\n C {question6.get('C')[0]}\n D {question6.get('D')[0]}\n " )
        A6 = A6.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A6 == 'A':
            G += 1
            break
        elif A6 == 'B':
            S += 1
            break
        elif A6 == 'C':
            R += 1
            break
        elif A6 == 'D':
            H += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')

    #question 7 dictionary
    question7 = {"question":"If you were going on vacation you would go...",
                 "A":["London","Slytherin"],
                 "B":["The wilderness","Gryffindor"],
                 "C":["Home to my family","Hufflepuff"],
                 "D":["The Beach","Ravenclaw"]}
    while True:
        #input question 7 and possible answers saves to A7
        A7= input (f"Question 7 - {question7.get('question')}\n A {question7.get('A')[0]}\n B {question7.get('B')[0]}\n C {question7.get('C')[0]}\n D {question7.get('D')[0]}\n " )
        A7 = A7.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A7 == 'A':
            S += 1
            break
        elif A7 == 'B':
            G += 1
            break
        elif A7 == 'C':
            H += 1
            break
        elif A7 == 'D':
            R += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')

    #question 8 dictionary
    question8 = {"question":"Your Patronus would be a...",
                 "A":["Panther","Ravenclaw"],
                 "B":["Fox","Slytherin"],
                 "C":["Hedgehog","Gryffindor"],
                 "D":["Cat","Hufflepuff"]}
    while True:
        #input question 8 and possible answers saves to A8
        A8= input (f"Question 8 - {question8.get('question')}\n A {question8.get('A')[0]}\n B {question8.get('B')[0]}\n C {question8.get('C')[0]}\n D {question8.get('D')[0]}\n " )
        A8 = A8.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A8 == 'A':
            R += 1
            break
        elif A8 == 'B':
            S += 1
            break
        elif A8 == 'C':
            G += 1
            break
        elif A8 == 'D':
            H += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')
    #question 9 dictionary
    question9 = {"question":"On a Saturday night you could be found...",
                 "A":["At the movies or a concert","Ravenclaw"],
                 "B":["Staying in with friends","Hufflepuff"],
                 "C":["Bar hopping","Gryffindor"],
                 "D":["Sleeping","Slytherin"]}
    while True:
        #input question 9 and possible answers saves to A9
        A9= input (f"Question 9 - {question9.get('question')}\n A {question9.get('A')[0]}\n B {question9.get('B')[0]}\n C {question9.get('C')[0]}\n D {question9.get('D')[0]}\n " )
        A9 = A9.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A9 == 'A':
            R += 1
            break
        elif A9 == 'B':
            H += 1
            break
        elif A9 == 'C':
            G += 1
            break
        elif A9 == 'D':
            S += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')
    #question 10 dictionary
    question10 = {"question":"Your mom sends you Howler for something you didn't do wrong. you...",
                  "A":["Feel bad that you upset her","Hufflepuff"],
                  "B":["Are embarassed that everyone heard but don't care that she's mad","Ravenclaw"],
                  "C":["Write her back to let her know she's wrong","Gryffindor"],
                  "D":["Say she's crazy and that you're obviously right","Slytherin"]}
    while True:
        #input question 10 and possible answers saves to A10
        A10=input (f"Question 10 - {question10.get('question')}\n A {question10.get('A')[0]}\n B {question10.get('B')[0]}\n C {question10.get('C')[0]}\n D {question10.get('D')[0]}\n " )
        A10 = A10.title() #capitalizes input
    
        #increases counter if user input matches a multiple choice, and shames the user if they input an illegal answer
        if A10 == 'A':
            H += 1
            break
        elif A10 == 'B':
            R += 1
            break
        elif A10 == 'C':
            G += 1
            break
        elif A10 == 'D':
            S += 1
            break
        else:
            print('That was not a valid option, you might be a muggle\n')
    #prints the counter totals for each house
    print(f'Gryffindor:{G}\nSlytherin:{S}\nHufflepuff{H}\nRavenclaw:{R}')

    if G > R and G > S and G > H:
        print('\n You belong in GRYFFINDOR')
    elif R > G and R > S and R>H:
        print('\n You belong in RAVENCLAW')
    elif S>G and S>R and S>H:
        print ('\n You belong in SLYTHERIN')
    elif H>S and H>R and H>G:
        print ('\n You belong in HUFFLEPUFF')
    else:
        print ('\n How did a muggle get in here!!')


main()

