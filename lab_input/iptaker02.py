#!usr/bin/python3

"""Alta3 Research | RZFeeser
   print() -concatenate vs print a series of items"""

def main():

	#collect string input from user
	user_input = input("Please enter an IPv4 IP address:")

	## the line below creates a single string that is passed to print()
	# print ("You told me the IPv4 address is: " + user_input)

	##print() can be giver a series of objects separated by a comma
	print("You told me the IPv4 address is: ", user_input)

	#collect string input from user about vendor
	vendor_input = input("Please provide the vendor name associated with this device ")

	#displays the vendor name
	print("This device is associated with: ", vendor_input)

main()

