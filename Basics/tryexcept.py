#!/usr/bin/python3
while True :
    try :
        number = int(input("Enter a number: "))

    except ValueError as e :
        print (("Oops only number please" + "\n" "Error code :  %s") % e)
    else :
        print  ("number accepted")
        break
