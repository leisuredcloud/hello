# -*- coding: utf-8 -*-      
import datetime
import math

def multi(*numlist):
    if(len(numlist)==0):
        print("No number to calculate")
        return 0;

    multiresult=1
    for x in numlist:
        if(not isinstance(x, int, float)):
            print("Only number can be calculated")
            return
        else:
            multiresult=multiresult*x

    return multiresult

print(multi(4,5,6))