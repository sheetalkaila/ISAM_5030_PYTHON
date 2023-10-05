# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:48:04 2023

@author: sheetal
"""

#for loop practice

num = 1
# 5 numbers
num_list = []
print(num_list)
num_list = [1,2,3,4,10]
name_list = ['Alice','Bob','Charlie','David','Edward']
print(num_list)

# for each element in the loop list
for i in num_list:
    print(i)

#the for-in loop does not contain index information
counter = 0
for name in name_list:
    print(name,' stays at room:',counter)
    counter+=1
    
#for loop using range function, it uses an index/counter
#to go through each element
#for index in range(5): from 0-4
for index in range(len(num_list)):
    print(num_list[index])
    
for index in range(len(name_list)):
    print(name_list[index],' stays at room:',index)
    