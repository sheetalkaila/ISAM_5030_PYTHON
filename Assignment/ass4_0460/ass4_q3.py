# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 12:44:42 2023

@author: sheetal
"""

#Question3

#1.square with 4 borders

row_size = int(input('Please type in row size:'))
column_size = int(input('Please type in column size:'))


for row in range(row_size):
    for col in range(column_size):
        if row == 0 or row == row_size-1 or col == 0 or col == column_size-1: 
            print('*',end='')
        else:
            print(' ',end='')       
    print('')

#2.square with left, right borders and 1 diagonal line

for row in range(row_size):
    for col in range(column_size):
        if row == 0 or row == row_size-1 or row == col:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
       
#3.square with upper right triangle filled with "*"

for row in range(row_size):
    for col in range(column_size):
        if row == 0 or col == column_size - 1 or row == col or col > row:
            print('*',end='')
        else:
            print(' ',end='')
    print('')








