# -*- coding: utf-8 -*-      
import datetime
import math

def quadratic(a, b, c):
    if (b*b-4*a*c)<0 :
        print("无解")
        return
    elif (b*b-4*a*c)==0 :
        print("只有一个解为:", -b/(2*a))
        return
    else:
        x1= (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2= (-b-math.sqrt(b*b-4*a*c))/(2*a)
        print("有两个解，分别是:x1=%s; x2=%s" %(x1,x2))
        return 

today=datetime.datetime.today()
year=today.year

name=input("what's your name?")
print("hello",name)
age=input("how old are you!")
if not age.isdigit():
    raise TypeError("wrong input. Age can be only digital")
match age:
    case x if int(x)< 6:
        print("you are so young!")
    case x if int(x)< 12:
        print("you are teenager!")
    case x if int(x)> 60:
        print("you are so old!")
    case _:
        bornyear= year-int(age)
        print("you were born in ",bornyear)

print("下面我们用电脑解一元二次方程ax2+bx+c=0")
print("请给方程式中的a,b,c赋值，正整数或负整数都可以，以空格为间隔")
a,b,c = input().split(" ")

if a=="0":
    raise TypeError("a can\'t be zero")
 
for x in[a,b,c]:
    if not isinstance(x,float):
        raise TypeError("what you input is not a number")

print("%sx2+%sx+%s=0" %(a,b,c))
quadratic(int(a),int(b),int(c))
