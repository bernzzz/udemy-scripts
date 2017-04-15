#!/usr/bin/python3
def simplefor ():

	words = ['cat' , 'dog' , 'windows' , 'prabinbernard']

	for items in words :
		print (items)


#If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items)
# Loop over a slice copy of the entire list.
def forstatement () :

	words = ['cat' , 'dog' , 'windows' , 'prabinbernard']

	for items in words [:] :

		if len(items) > 2 :

			words.insert(0, items)
	print (words)
forstatement()
