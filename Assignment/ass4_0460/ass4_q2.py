# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:47:12 2023

@author: sheetal
"""

#Question2

row_size = int(input('Please type in row size:'))
column_size = int(input('Please type in column size:'))


for row in range(row_size):
    for col in range(column_size):
        if row == 0 or row == row_size-1 or col == 0 or col == column_size-1: 
            print('*',end='')
        else:
            print(' ',end='')       
    print('')
    

    
    
    
    