# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 18:23:38 2023

@author: sheetal
"""


# Assignment_1B Question2

weight_lb = input('Please type in your weight in lbs:')
print('NOTE: If your height is 5ft and 10inches then your height in inch will be 5*12+10 = 70 inches')
height_in = input('Please type in your height in inches:')

weight_lb = float(weight_lb)
height_in = float(height_in)

BMI = round((weight_lb /height_in**2) * 703,2)


if BMI < 16.0:
    print('Your BMI is:',BMI,',you are Severely Underweight.')
elif  16.0 <= BMI <= 18.4:
    print('Your BMI is:',BMI,',you are Underweight.')
elif 18.5 <= BMI <= 24.9:
    print('Your BMI is:',BMI,',you are Normal.')
elif 25.0 <= BMI <= 29.9:
    print('Your BMI is:',BMI,',you are Overweight.')
elif 30.0 <= BMI <= 34.9:
    print('Your BMI is:',BMI,',you are Moderately Obese.')
elif 35.0 <= BMI <= 39.9:
    print('Your BMI is:',BMI,',you are Severely Obese.')
elif BMI > 40.0:
    print('Your BMI is:',BMI,',you are Morbidly Obese.')
    


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

