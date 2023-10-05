# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:41:19 2023

@author: sheetal
"""

Weekday = int(input('What is weekday of today?(1-7)'))
Time = int(input('What is the time now?(1-12)'))
Timezone = input('Is it AM or PM?')

if Weekday == 1 or Weekday == 2 or Weekday == 3 or Weekday == 4 or Weekday == 5:
    if (Time in range(9,12) and Timezone == 'AM') or ((Time in range(1,7) or Time == 12) and Timezone == 'PM'):
        print('I am working!')
    elif ((Time in range(1,10) or Time == 12) and Timezone == 'AM') or ((Time in range(6,12)) and Timezone == 'PM'):
        print('I am off my job now!')
        
elif Weekday == 6 or Weekday == 7:
    if (Time == 11 and Timezone == 'AM') or ((Time in range(1,12) or Time == 12) and Timezone == 'PM'):
        print('I am on vacation!')
    elif ((Time in range(1,12) or Time == 12) and Timezone == 'AM') or ((Time == 12) and Timezone == 'PM'):
        print('I am sleeping!')
        
        
        
        
        
        
        
        
        