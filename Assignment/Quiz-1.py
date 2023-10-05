# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:54:11 2023

@author: sheetal
"""

GPA = float(input('Please type in your GPA in 4.0 base (0.0-4.0)'))
GRE = int(input('Please type in your GRE score in percentile(0-100)'))
Award = input('Have you won any national competition award?(Yes/No)')

if Award == 'Yes':
    GRE = GRE * 1.1
    
if GPA >= 3.8 and GRE > 80:
    print('you are admitted with scholarship!')
elif GPA >= 3.0 and GRE > 70:
    print('you are admitted!')
elif GPA >= 2.5:
    print('you are on waitting list!')
elif GPA < 2.5:
    print('we regret to infrom you that we are unable to accept you to out progrm')
    