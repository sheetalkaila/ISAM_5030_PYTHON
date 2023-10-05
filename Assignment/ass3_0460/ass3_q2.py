# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:40:17 2023

@author: sheetal
"""

n = int(input('Type a positive number that not equal to 1 :'))


while n != 1:
    if n % 2 == 0:
        print(str(n) +' is even, so I take half:' +str(int(n/2)))
        n = int(n/2)
    elif n % 2 == 1:
        print(str(n)+' is odd, so I make 3n+1:'+ str(int(3*n+1)))
        n = int(3*n + 1)
   
        

