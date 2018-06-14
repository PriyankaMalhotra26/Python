#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:02:56 2018

@author: pmalhotr
"""

##Functions
## Time and hour_rate for gross_pay but as a function

def computepay(hour,rate_per_hour):
    if hour>40:
        gross_pay=((hour-40)*rate_per_hour*1.5)+(40*rate_per_hour)
    else:
        gross_pay=hour*rate_per_hour
    return gross_pay

try:
    hour=float(input("Input no of hours:"))
except:
    print("The hours entered are INVALID!")
try:
    rate_per_hour=float(input("input no of hours"))
except:
    print("The rate per hour is INVALID")

print(computepay(hour,rate_per_hour))

################################

def computepay(hours,rate):
    pay=0.0
    if hours>40:
        pay=40*float(rate)+(float(hours)-40)*float(rate)*1.5
        return pay 
    else:
        pay=float(hours)*float(rate)
        return pay
h1=input("Input Hours:")
r1=input("Input rate:")

h=float(h1)
r=float(r1)

compute_pay=computepay(h,r)
print(compute_pay)

