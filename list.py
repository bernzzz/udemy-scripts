#!/usr/bin/python3
#sequence of items similar to strings , strings is made of strings(charachters), lists can contain various datatypes (string,integer,etc)
lists = ["hello","1","damaien","24"]
print (lists)
#methods of a available for list can be found by
print (dir(list))
#appending an item to the list
lists.append("master")
print (lists)
#help--gives info about the methods
help(lists.remove)


def indexslicelist ():

	numbers = [1,2,3,4,5,]
	print (numbers[1])
	print (numbers[:3])
