# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:59:53 2023

@author: sheet
"""

#nested if else statement
#class_exercise_03

#college admission rule
#GPA ? SAT_score ?

GPA = float(input('What is your GPA?(0-4.0)'))
SAT = float(input('What is your SAT?(400-1600)'))

# if GPA >= 3.5:
#     if SAT >= 1200:
#         print('Congrats! You are admitted with scholarship!')
#     elif SAT >= 1000:
#         print('Congrats! You are admitted!')
#     elif GPA >= 3.9: #special case we do not care SAT
#         print('Congrats! You are admitted!')
#     elif SAT >= 800:
#         print('You are on waiting list!')
#     else:
#         print('We are regret that we cannot admit you at this moment!')
        
# elif GPA >= 3.0: #only GPA  < 3.5 will come here 
#     if SAT >= 1000:
#         print('Congrats! You are admitted!')
#     elif SAT >= 800:
#         print('You are on waiting list!')
#     elif GPA >= 3.0:
#         print('We are regret that we cannot admit you at this moment!')
        
# else:
#     print('We are regret that we cannot admit you at this moment!')
    
if GPA >= 3.5 and SAT >= 1200:
    print('Congrats! You are admitted with scholarship!') 
elif GPA >= 3.0 and SAT >= 1000:
    print('Congrats! You are admitted!')
elif GPA >= 3.0 and SAT >= 800:
    print('You are on waiting list!')
elif GPA >=3.9: #special case
    print('Congrats! You are admitted!')
else:
    print('We are regret that we cannot admit you at this moment!')
    

    
    
    
    
    
    