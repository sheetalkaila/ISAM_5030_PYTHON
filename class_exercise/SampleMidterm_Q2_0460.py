# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:04:24 2023

@author: sheetal
"""

input_salary = 0
salary_list = []
mgr_counter = 0

while input_salary != -1:
    input_salary = int(input('What is your salary?'))
    if input_salary >= 0:
        salary_list.append(input_salary)
    if input_salary >= 90000:
        mgr_counter += 1
        
#end the while loop
print('There are total ' ,len(salary_list) , ' Salaries')
salary_list.sort()

print('The min salary is:' , salary_list[0])
print('The 2nd min salary is:' , salary_list[1])

print('The max salary is:' , salary_list[-1])
print('The 2nd max salary is:' , salary_list[-2])
        
avg_salary = (sum(salary_list) - salary_list[-1] - salary_list[0])/(len(salary_list) - 2)
print('The average salary after removing max/min salary is:' ,avg_salary)
print('Number of managers:',mgr_counter)

