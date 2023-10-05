# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:46:46 2023

@author: sheetal
"""

#practice with while loop and for loop

print(1)
print(2)
print(3)

number = 1

#while loop
while number < 101:
    print(number)
    print('check hotel room no.', number)
    number +=1

print('End of while loop')

#stop while loop use a sentinel
# how to create a do first, then check condition
score = 0
#write a do while loop use break
while True:
    score = int(input('What is your score? (0-100) Type -1 to stop!'))
    if score == -1: #-1 is your sentinel
        break #break the loop
    elif score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    else:
        print('D')
######################################
#end of while loop
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

