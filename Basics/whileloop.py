#!/usr/bin/python3
def password (prompt,retries=4) :
    while True:
        password= input(prompt)
        if password == "Welcome123" :
            print("Welcome to Homeworld")
            break
        else :
            print ("Your password is wrong !! Please try again")
        retries = retries - 1
        if retries < 0 :
            raise ValueError ("Invalid response :Run out of try")

password("Enter the password: ")
