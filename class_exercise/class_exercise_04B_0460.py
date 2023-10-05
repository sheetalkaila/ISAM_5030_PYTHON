# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:21:55 2023

@author: sheetal
"""

# for loop with range functions
num_list = [1,2,3,4,5,6,7,8,9,10]
#three number in range function
#1st num: start index,inclusive
#2nd num: end index,exclusive
#3rd num: step size, this how you incraese the index
for index in range(0,10,1):
    print(num_list[index])
    
#print out every other element
print('print out every other odd element')    
for index in range(0,10,2):
    print(num_list[index])
    
#print out every other element   
print('print out every other even element') 
for index in range(1,10,2):
    print(num_list[index])
    
print('Middle section of the list, 3,4,5,6,7')
for index in range(2,7,1):
    print(num_list[index])
    
#if range function has only two number
#range(start_indx, end_indx) step size = 1
for index in range(2,7):
    print(num_list[index])
    
#if range function has only one number
#range(end_indx),start_indx = 0, step size = 1
for index in range(10):
    print(num_list[index])
  
#print out the num_list reverse
for index in range(9,-1,-1):
    print(num_list[index])    

#print out the num_list reverse    
for index in range(4,-1,-1):
    print(num_list[index]) 
    
#print out the num_list reverse, with every other even element
#print(10,8,6,4,2)   
for index in range(9,-1,-2):
    print(num_list[index])  
    
#print out the num_list reverse, with every other even element
#print(9,7,5,3,1)    
for index in range(8,-1,-2):
    print(num_list[index])
    
    
    
    
    
    