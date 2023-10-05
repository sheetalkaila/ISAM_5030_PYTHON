# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:29:14 2023

@author: sheetal
"""

#class_exercise_02

#without value, a variable cannot be used
lastname = 'Kaila'
firstname = 'Sheetal'

print(lastname,firstname)

lastname = 3.1415
firstname = 0

print(lastname,firstname)

_2lastname = 'x'
#python is a case sensitive programming language
last_name = 'x'
Last_name = 'xx'

#boolean value is used to control code flow
is_cold_flag = True
is_cold_flag = False

#CASTING example
number_str = '12345'
number = int(number_str)
float_str = '3.1415'
number = float(float_str)
#a flaot string with a decimal point cannot be casted to an int

result = number/2
print(result)

number_123 = 123
number_456 = 456
print(number_123 + number_456)

_123_str = str(number_123)
_456_str = str(number_456)
print(_123_str+_456_str)


A = 1 + 2
B = 2 - 1
C = 2 * 2
D = 4 / 3
E = 5 // 2
print(A,B,C,D,E)

A = 2**3 #exponential
remainder = 7%4
print(A)
print(remainder)














