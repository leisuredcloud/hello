import datetime

today=datetime.datetime.today()
year=today.year

name=input("what's your name?")
print("hello",name)
age=input("how old are you!")
bornyear= year-int(age)
print("you were born in ",bornyear)