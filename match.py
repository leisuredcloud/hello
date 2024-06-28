# -*- coding: utf-8 -*-      
import datetime
import math

today=datetime.datetime.today()
year=today.year

name=input("what's your name? ")

ageinput=input("hi, %s, how old are you? " % name)
try:
    agereal=int(ageinput)
except ValueError:
    agereal=0

match agereal:
    case x if x<=0:
        print("hi, %s, you didnt' tell me your real age!"  % name)
    case x if x<=6:
        print("hi, %s, you are so young!"  % name)
    case x if x<=12:
        print("hi, %s, you are teenager!" % name)
    case x if x>=60:
        print("hi, %s, you are so old!" % name)
    case _:
        bornyear= year-int(agereal)
        print("hi,%s you were born in %i" % name, bornyear)