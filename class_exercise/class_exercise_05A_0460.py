# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:20:24 2023

@author: sheetal
"""

#2 dimensional list
list1 = ['Joe','Kim']
list2 = ['Sam','Sue']
list3 = ['Kelly','Chris']

_2d_list = []
_2d_list.append(list1)
_2d_list.append(list2)
_2d_list.append(list3)

print(_2d_list)

for row in _2d_list:
    print(row)

row_size = 20
col_size = 20    
#we use nested for loop to create 2d matrix
#external loop takes care of row
list_2D = []
for row in range(row_size):
    row_list = []
    #internal/inner loop taked care of colums
    for col in range(col_size):
        row_list.append(col+1)
    #end of the internal/inner loop
    #we finished initialize the row_list
    #we append it to the list_2D
    list_2D.append(row_list)
    print(row_list)
 
    

        
        
