# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:44:48 2023

@author: sheetal
"""

doctorlist=['Alice Bond','Bob Madoff','Charlie Potter','David Dickonson','Tiffany Austin','Frank Oliver','Mary Bond']
print(doctorlist)

#Q1:
print('#########Q1########')
for i in range(len(doctorlist)):
    print(i+1,'-',doctorlist[i])
    
#Q2: 1,3,5,7
print('#########Q2########')
for i in range(0,len(doctorlist),2):
    print(i+1,'-',doctorlist[i])
    
#Q3: 2,4,6
print('#########Q3########')
for i in range(1,len(doctorlist),2):
    print(i+1,'-',doctorlist[i])
    
#Q4: 1,4,7
print('#########Q4########')
for i in range(0,len(doctorlist),3):
    print(i+1,'-',doctorlist[i])
    
print('#########Q5########')
t_flag = False
for doctor in doctorlist:
    if doctor.startswith('Tiffany'):
        print('Yes, we have a Dr. Tiffany!')
        t_flag = True
#end of for loop
if t_flag == False:
    print('Sorry we cannot find Dr. Tiffany!')
 
print('#########Q6########') 
tiffany_indx = doctorlist.index('Tiffany Austin')
if tiffany_indx < 0:
    print('We do not have Dr. Tiffany!')
else:
    print('Doctor before Tiffany:' , doctorlist[tiffany_indx - 1])
    print('Doctor after Tiffany:' , doctorlist[tiffany_indx + 1])
    
print('#########Q7########') 
tiffany_indx = doctorlist.index('Tiffany Austin')
if tiffany_indx < 0:
    print('We do not have Dr. Tiffany!')
else:
    doc_before = doctorlist[tiffany_indx - 1]
    doc_after = doctorlist[tiffany_indx + 1]
    if doc_before.startswith('Frank') or doc_after.startswith('Frank'):
        print('Yes we have Tiffany and Frank working next to each other!')
    else:
        print('No, Dr. Tiffany and Frank do not work next to each other!')
    
print('#########Q8########')
for doctor in doctorlist:
    if doctor.startswith('Alice') or doctor.startswith('Tiffany') or doctor.startswith('Mary'):
        print(doctor,'working day is:', doctorlist.index(doctor)+1)

print('#########Q9########') 
print(doctorlist[::-1])
  
 
    
 
    
 
    
 
    
 
    
 
    
    