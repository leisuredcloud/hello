# -*- coding: utf-8 -*-      
import datetime
import math

def quadratic(a, b, c):
    print("Quadratic equation:%sx²+%sx+%s=0:" %(a,b,c))
    if (b*b-4*a*c)<0 :
        print("no solution")
        return
    elif (b*b-4*a*c)==0 :
        print("has one root:", -b/(2*a))
        return
    else:
        x1= (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2= (-b-math.sqrt(b*b-4*a*c))/(2*a)
        print("has 2 distinct roots，one is:%s; the other is %s" %(x1,x2))
        return 

print("Now we will resolve equation problem with computer.")
print("Today we use quadratic quation:ax²+bx+c=0 as a example") 
print("please input the value of a,b,c，leave a space between numbers")
a,b,c = input().split(" ")

if a=="0":
    raise TypeError("a can\'t be zero")
 
for x in[a,b,c]:
    try:
       int(x)                                             # 尝试将输入转换为整数
    except ValueError:
       raise TypeError("what you input is not a number")  # 如果转换失败，说明输入的是文字

quadratic(int(a),int(b),int(c))
