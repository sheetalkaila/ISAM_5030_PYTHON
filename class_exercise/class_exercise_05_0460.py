# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:02:06 2023

@author: sheetal
"""

#list exercise

num_list = [1,2,3,4]
str_list = ['Alice','Bob','Charlie','David','Edward','Nemo']
hybrid_list = ['Alice',3.5,'Bob',4.0]

num_list.append(5)
print(num_list)
num_list.insert(0,'Zero')
print(num_list)
#num_list.extend(str_list)
num_list = num_list + str_list
print(num_list)

new_num_list = [1,2,3]

new_num_list = new_num_list*3
print(new_num_list)

#slicing: print out the first 3 items
print(str_list[0:3])       #same as for i in range(0,3):
#when slicing has only 1 number, that number is the endIndex
print(str_list[:4])

#when slicing has 2 number, 1st is the start Index
#2nd number is the end Index
print(str_list[2:4])

#slicing can have 3 numbers, 1st startIndex, 2nd EndIndex, 3rd stepsize
print(str_list[0:5:2])
#print string backwards
print(str_list[::-1])
str_list_reversed = str_list[::-1]
print(str_list)
print(str_list_reversed)

if 'Nemo' in str_list:
    print('Nemo is our guest!')
else:
    print('Nemo is NOT our guest!')

print(str_list)
#str_list.remove('Charlie')
#remove element by index
del str_list[2]
#str_list.remove('Sun')

print(str_list)

#reverse
str_list.reverse()
print(str_list)

#sort
str_list.append('alice')
str_list.sort()
print(str_list)
print(min(str_list))
print(max(str_list))

#print 2nd min
print(str_list[1])
print(str_list[-2])
#sort desending
str_list.sort(reverse = True)
print(str_list)

gpa_list = [1.1,2.2,3.3,4.4,5.5]

#create another variable points to the same list
gpa_list_copy = gpa_list
#here we create a momery copy
gpa_list_copy = [] + gpa_list

print(gpa_list_copy)
gpa_list[0] = 0

print(gpa_list_copy)
















































