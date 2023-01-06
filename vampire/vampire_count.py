#!/usr/bin/env python3

"""Counting vampires in the novel Dracula"""

def main():
    v_count = 0
    with open('dracula.txt','r') as dracula: # opens the txt file for the book dracula
        with open('vampytimes.txt','w') as count: #creates a new file to write to named 'vampytimes.txt'under the variable count
            
            for line in dracula: # reads all the lines of dracula as strings
               if 'vampire' in line.lower(): #finds everytime the word 'vampire' is used regardless of the capitalization
                  print(line) #prints each line that has the word 'vampire' in it
                  v_count +=1 #adds a count to 'v_count' for every line that includes 'vampire'
                  count.write(line)#writes each line to vampytimes.txt
    print(v_count)



main()


