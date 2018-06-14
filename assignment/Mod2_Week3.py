#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:36:25 2018

@author: pmalhotr
"""

###Assignment1

file_loc="/Users/pmalhotr/JupyterNoteBook/InputFiles/"
file_name=input("Input the filename:")
file_path=file_loc+file_name
print(file_path)
file_handle=open(file_path)
file_store=file_handle.read()
print(file_store.upper())


#Variation 2
file_name=input("Enter the file name:")

f_handle=open(file_name)
for lines in f_handle:
    lines1=lines.rstrip()
    print(lines1.upper())
    
    
###Assignment2
file_loc="/Users/pmalhotr/JupyterNoteBook/InputFiles/" 
file_name=input("Enter the file Name")
file_path=file_loc+file_name
file_handle=open(file_path)
count=0
number=0.0
for line in file_handle:
    if line.find("X-DSPAM-Confidence:")>=0:
        start_point=line.rstrip().find(":")
        count=count+1
        #print(line[start_point+1:])
        number=number+float(line[start_point+1:])
print("Average spam confidence:",number/count)

##Variation 2

# Use the file name mbox-short.txt as the file name
file_loc=input("File_name")
counter=0
total=0.0
f_handle1=open(file_loc)
for lines3 in f_handle1:
    lines4=lines3.rstrip()
    if lines4.startswith("X-DSPAM-Confidence:")==True:
        total=float(lines4[lines4.find(":")+1:])+total
        
        counter=counter+1


print("Average spam confidence:",total/counter)


