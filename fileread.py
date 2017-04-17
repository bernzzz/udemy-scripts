#!/usr/bin/python3
files = open("test.txt",'r')
content =files.readlines()
cleanlist=[]
for i in content :
    cleanlist.append(i.rstrip())
files.close()
for items in cleanlist :
    print (items)

# the same can be achieved by creating a clean list on the fly using list comprehension

content=[i.rstrip() for i in content]
#hello
