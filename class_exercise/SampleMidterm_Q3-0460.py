    # -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:22:08 2023

@author: sheetal
"""

def sum67(num_list):
    add_flag = True
    num_sum = 0
    
    for num in num_list:
        if num == 6:
            add_flag = False
        elif num == 7:
            if add_flag == True: # you meet 7 before you meet 6
                num_sum += num
            else: # you meet 7 after uou meet 6
                add_flag = True
        elif add_flag == True:
            num_sum += num
     #end for loop       
    return num_sum  
   
print(sum67([1,2,2]))            
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2])) 
print(sum67([1, 6, 99, 99, 7, 3,1,6,1,7,10]))

        