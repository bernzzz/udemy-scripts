#!/usr/bin/python3
def ifstatement () :
	number = int(input("Enter an integer: "))

	if number < 0 :

		number = 0

		print ("Negative changed to zero")

	elif number == 0 :

		print ("Zero")

	elif number > 0 :

		print ("More")

ifstatement()
