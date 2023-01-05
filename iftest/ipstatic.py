#!/usr/bin/env python3

def main():
    ipchk = input('Apply for an IP Address: ')

    if ipchk == '192.168.70.1':
      print(f'Looks like the IP address of the Gateway was set: {ipchk} This is not reccomended.')
    
    elif ipchk:
        print(f'Looks like the IP address was set: {ipchk}')

    else:
        print('You did not provide input.')

main()



