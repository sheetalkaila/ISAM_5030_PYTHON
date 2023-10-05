# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:34:02 2023

@author: sheetal
"""

#class_exercise_02A.py
#Control flow statement

is_cold = input('It is cold outside?')

if is_cold == 'Yes':
    print('Wear a coat!')
else:
    print('Nice weather!')
    
degree_str = input('What is the temperature now?(0-110 degree)')
degree = int(degree_str)

#hot >= 90, cold <= 60
if degree  >= 90:
    print('It is time for swim!')
elif degree <= 60:
    print('Wear a coat!')
else:
    print('Nice weather!')
    
    
score = input('What is your score?')
score = int(score)

if score >= 90:
    print('Your Grade is A!')
elif score >= 80:
    print('Your Grade is B!')
elif score >= 70:
    print('Your Grade is C!')
elif score >= 60:
    print('Your Grade is D!')
else:
    print('Your Grade is F!')
    

    
    