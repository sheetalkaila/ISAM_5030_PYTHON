# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 18:23:38 2023

@author: sheet
"""

#width= input('type the width:')
#height = input('type the height:')

#area = int(width) * int(height);
#print("your rectangle size is " +str(width)+'*'+str(height)+", area is:" + str(area));*/


weight_lb = float(input('Please type in your weight in lbs:'))
height_in = float(input('Please type in your height in inches:'))

feet = int(height_in) // 12
inches = int(height_in) % 12

print('this is ' + str(feet) + ' feet ' + str(inches)+' inches'+'. '+ str(feet)+'*'+'12'+'+'+str(inches)+' = '+ str(int(height_in)))

def calculate_bmi(w_lb, h_in):
    bmi = (w_lb / h_in**2) * 703
    return bmi
        
def get_bmi_category(bmi):
    if bmi < 16.0:
        return("Severely Underweight")
    elif  16.0 <= bmi <= 18.4:
        return("Underweight")
    elif 18.5 <= bmi <= 24.9:
        return("Normal")
    elif 25.0 <= bmi <= 29.9:
        return("Overweight")
    elif 30.0 <= bmi <= 34.9:
        return("Moderately Obese")
    elif 35.0 <= bmi <= 39.9:
        return("Severely Obese")
    elif bmi > 40.0:
        return("Morbidly Obese")
    
bmi_ = calculate_bmi(weight_lb, height_in)
bmi = round(bmi_,1)
bmi_category =  get_bmi_category(bmi)  
        
print('Your BMI is:' + str(bmi) + ',' + 'you are ' + bmi_category + '.')


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

