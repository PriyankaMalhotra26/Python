#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:16:38 2018

@author: pmalhotr
"""
##Practice e.g
x = 'From marquard@uct.ac.za'
x.find("q")

x = 'From marquard@uct.ac.za'
start_point=x.find("uct")
print(x[start_point:start_point+3])

for letter in "banana":
    print(letter)
    
greet="Hello Bob"
print(greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

string="       priyanka     malhotra     "
print(len(string.strip()))


###Assignment 

text = "X-DSPAM-Confidence:    0.8475"
start_position=text.find(":")
num=text[start_position+1:]
print(float(num))
