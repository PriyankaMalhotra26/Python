#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:14:41 2018

@author: pmalhotr
"""
a="P M A B DDD"
print(a.split())

###assignment1
file_loc="/Users/pmalhotr/JupyterNoteBook/InputFiles/" 
file_name=input("Enter the file Name")
file_path=file_loc+file_name
file_handle=open(file_path)
list1=[]
list2=[]
for lines in file_handle:
    list1=list1+lines.split()
for items in list1:
    if items not in list2:
        list2.append(items)
list2.sort()
print(list2)
    
        
    
    
### #######################
    
file_path = input("Enter file name: ")
file_list_item=list()
file_list_item_final=list()
dedup_list=list()

file_handle=open(file_path)
for lines in file_handle:
    file_list_item=lines.split()
    file_list_item_final=file_list_item_final+file_list_item
    
for item in file_list_item_final:
    if item not in dedup_list:
        dedup_list.append(item)
dedup_list.sort()
print(dedup_list)

#############################
####Assignment2

file_loc="/Users/pmalhotr/JupyterNoteBook/InputFiles/" 
file_name=input("Enter the file Name")
file_path=file_loc+file_name
file_handle=open(file_path)
list1=[]
counter=0

for line in file_handle:
    if line.startswith("From "):
        list1=line.split()
        print(list1[1])
        counter=counter+1
print(counter)
