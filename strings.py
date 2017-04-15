#!/usr/bin/python3
#A string is a sequence of charachters
print ("Hello")
print ("World")
print ("new")
#methods of a available for string can be found by
print (dir(str))

def stringconcatination ():
	name ='prabin'+'bernard'
	return name

def lengthofstring ():
	name = "prabin bernard"
	return len(name)

def indexslicestring ():
	name ="prabinbernard"
	# returns the first charachter
	print (name[1])
	print (name[:6])
	print (name[6:])
