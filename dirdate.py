#!/usr/bin/python3
import os
import datetime

#Global Variables


def datetoday () :

    currentdate = datetime.date.today().strftime("%Y-%m-%d")
    return currentdate

def makedir (path) :
        try :
            os.mkdir(path + "/" + datetoday())
        except OSError as O :
            print (O)
makedir(path= "/home/bernard/Desktop/python-masterclass/udemy-scripts")
