#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:43:05 2018

@author: pmalhotr
"""

##Conditional Splits Assignment 1

hours=float(input("Input no of hours:"))
rate_per_hour=float(input("Rate per hour:"))
gross_pay=0.0
if hours>40:
    gross_pay=(1.5)*(hours-40)*rate_per_hour+40*rate_per_hour
else:
    gross_pay=rate_per_hour*hours
print(gross_pay)
    

##Assignment Two 
##Prompt for score between 0 to 1. If out of range print error else grade

score=input("Input the score:")
try:
    f_score=float(score)
    if f_score>=0 and f_score<=1:
        if f_score>=0.9 and f_score<=1:
            print("A")
        elif f_score>=0.8 and f_score<0.9:
            print("B")
        elif f_score>=0.7 and f_score<0.8:
            print("C")
        elif f_score>=0.6 and f_score<0.7:
            print("D")
        elif f_score<0.7:
            print("F")
    else:
        print("Error:Score out of range")
except:
    print("ERROR ! non numerical value ")

