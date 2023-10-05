# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:15:44 2023

@author: sheetal
"""

print('Hello Sheetal Kaila !')

hours = input('How many hours do you work?')
hourly_rate = input('What is your hourly rate?')

total_amount = int(hours) * float(hourly_rate)

print('You worked' ,hours, 'hours')
print('Your hourly rate is' , '$' + str(hourly_rate), 'per hour')
print('We will pay you:', '$' + str(total_amount))

