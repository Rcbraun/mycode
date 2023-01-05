#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display list1[1] which should only display arista_eos
    print(list1[1])
    
    #creats a new list containing a single item
    list2 = ["juniper"]

    #extends list1 by list2 
    list1.extend(list2)

    #display list1
    print(list1)

    #creats list3
    list3 = ["10.1.0.1", '10.2.0.1','10.3.0.1']

    #appends list1 by list3
    list1.append(list3)

    #displays list1
    print(list1)
    
    #displays the 5th item in list1
    print(list1[4])

    #displays the first item in the list
    print(list1[4][0])


main()

