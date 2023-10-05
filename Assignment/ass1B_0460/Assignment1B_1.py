# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:32:23 2023

@author: sheetal
"""

#1.1	How many data types we have in python? 
#(String, numbers (int, float), Boolean Type, Sequence data types, Binary types)

#1.2	Write a python code to create different values in different data types, and store them in different variables.

text_str = 'Hello World!'
num_str = '369'
float_str = '6.74'
num_int = 20
num_float = 15.6
is_bool_true = True
is_bool_false = False

#1.3	Print these variables out.

print(text_str)
print(num_str)
print(float_str)
print(num_int)
print(num_float)
print(is_bool_true)
print(is_bool_false)

#1.4	Can you convert these data types to each other? Convert them to each other, then print them out.

#convert str to int
text_str = 'Hello World!'
#text_int = int(text_str) 
# print(text_int)  //a text string can not be casted to an int

num_str = '369'
num_int = int(num_str)
print(num_int)

float_str = '6.74'
#float_int = int(float_str)
#print(float_int)  //a float string with a decimal point cannot be casted to an int

#convert str to float
text_str = 'Hello World!'
#text_float = float(text_str)
#print(text_float) //could not convert string to float

num_str = '369'
num_float = float(num_str)
print(num_float)

float_str = '6.74'
num_float = float(float_str)
print(num_float)
print('#############')
#convert str to bool
text_str = 'Hello World!'
text_bool = bool(text_str) 
print(text_bool)

num_str = '369'
num_bool = bool(num_str) 
print(num_bool)

float_str = '6.74'
float_bool = bool(float_str) 
print(num_bool)

#convert int to str
num_int = 20
num_str = str(num_int)
print(num_str)

#convert int to flaot
num_int = 20
num_float = float(num_int)
print(num_float)

#convert int to bool
num_int = 20
num_bool = bool(num_int)
print(num_bool)

#convert float to str
num_float = 15.6
num_str = str(num_float)
print(num_str)

#convert float to int
num_float = 15.6
num_int = int(num_float)
print(num_int)

#convert float to bool
num_float = 15.6
num_bool = bool(num_float)
print(num_bool)

#convert bool to str
is_bool_trur = True
is_bool__true_str = str(is_bool_trur)
print(is_bool__true_str)

is_bool_false = False
is_bool__false_str = str(is_bool_false)
print(is_bool__false_str)

#convert bool to int
is_bool_trur = True
is_bool__true_int = int(is_bool_trur)
print(is_bool__true_int)

is_bool_false = False
is_bool__false_int = int(is_bool_false)
print(is_bool__false_int)

#convert bool to float
is_bool_trur = True
is_bool__true_float = float(is_bool_trur)
print(is_bool__true_float)

is_bool_false = False
is_bool__false_float = float(is_bool_false)
print(is_bool__false_float)





