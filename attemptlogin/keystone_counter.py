#!/usr/bin/env python3

"""Counts failed login attempts in the keystone.common.wsgi log file"""

def main():
    
    fail = 0 #creats a fail counter

    with open('keystone.common.wsgi', 'r') as key_file: #opens the keystone.common.wsgi file
       

        fail = 0 #creats a fail counter
        post = 0
        get = 0
        failips= [] 
       # key_file_lines = key_file.readlines() #breaks the file up into strings per line
        
        #with open("key_file_lines.txt",'w')as work:
           # work.write(key_file_lines)

        for line in key_file:#loops the following code for ever line in key_file_lines
            

            if ' Authorization failed' in line:
                fail +=1
                ip= line.split()[-1]
                failips.append(ip)
                with open('errors.txt','a') as errorfile:
                    errorfile.write(line + '\n')
    print('keystone.common.wsgi Closed \nFailed Logins:', fail)
    print ('The IPs from the failed requests are:' , ip)

main()


