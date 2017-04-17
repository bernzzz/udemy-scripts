#!/usr/bin/python3
var = ["kol","mol","dor"]
with open("test.txt", 'a') as file :
    for items in var :
        print (items)
        file.writelines("\n"+items)
