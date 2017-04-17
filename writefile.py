#!/usr/bin/python3
names = ["jhon","casius","maria"]
filehandler=open("test.txt", 'w')

for items in names :
    filehandler.write(items+"\n")
filehandler.close()

#append to a files
filehandler=open("test.txt", 'a')

for items in names :
    filehandler.write(items+"\n")
filehandler.close()
