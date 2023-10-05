# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:37:10 2023

@author: sheetal
"""

weekday = int(input('What is the weekday of today? (1-7)'))
hour = int(input('What is time now?(1-12)'))
is_AM = input('Is AM or PM?(AM r PM)')

if weekday == 6 or weekday == 7:
    #this is weekend, cond. 1: 11AM, 12PM, 1-11PM
    if hour == 11 and is_AM == 'AM':
        print('I am on vaction!')
    elif hour == 12 and is_AM == 'PM':
        print('I am on vaction!')
    elif 1 <= hour <= 11 and is_AM == 'PM':
        print('I am on vaction!')
    else:
        print('I am sleeping!')
else:
    #this is weekday, cond 1: 9-11AM, 12PM, 1-6PM, working hours
    if 9 <= hour <= 11 and is_AM == 'AM':
        print('I am working!')
    elif hour == 12 and is_AM == 'PM': 
        print('I am working!')
    elif 1 <= hour <= 6 and is_AM == 'PM':
        print('I am working!')
    else:
        print('I am off my job now!')
    