# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:14:46 2023

@author: sheetal
"""

#Question 1

you = int(input('What is your stylish?(0-10)'))
date = int(input('What is your date’s stylish?(0-10)'))

if you <=2 or date <= 2:
    print('Result: 0')
elif you >= 8  or date >= 8:
    print('Result: 2')
else:
    print('Result: 1')
           
      
# Question2

year = int(input('Please type in the car Year:'))
mileage = float(input('Please type in the car mileage:'))
color = input('Please type in the car color:')
model = input('Please type in the car model:')
price = float(input('Please type in the car price:'))

# nested control flow
 
if year > 2015:
    if mileage < 30000:
        if color in ['White','Black','Grey']:
            if model in ['Truck','SUV']:
                if 20000 <= price <= 30000:
                    print('Yes! this is the car that I am looking for.')
                else:
                    print('Sorry, this is not the car that I am looking for.')
            else:
                print('Sorry, this is not the car that I am looking for.')
        else:
            print('Sorry, this is not the car that I am looking for.')
    else:
        print('Sorry, this is not the car that I am looking for.')
else:
    print('Sorry, this is not the car that I am looking for.')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

     

        
