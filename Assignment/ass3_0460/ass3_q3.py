# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:46:50 2023

@author: sheetal
"""

#1.Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
#rotate_left3([1, 2, 3]) → [2, 3, 1]
#rotate_left3([5, 11, 9]) → [11, 9, 5]
#rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]

print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))

#2.Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
#reverse3([1, 2, 3]) → [3, 2, 1]
#reverse3([5, 11, 9]) → [9, 11, 5]
#reverse3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
  return [nums[2],nums[1],nums[0]]

print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))

#3.Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
#max_end3([1, 2, 3]) → [3, 3, 3]
#max_end3([11, 5, 9]) → [11, 11, 11]
#max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
  max_value = max(nums[0],nums[2])
  return [max_value,max_value,max_value]

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))

#4.Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
#sum2([1, 2, 3]) → 3
#sum2([1, 1]) → 2
#sum2([1, 1, 1, 1]) → 2

def sum2(nums):
  if len(nums) < 2:
    return sum(nums)
  elif len(nums) == 0:
    return 0
  else:
    return (nums[0]+nums[1])

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))
           

#5.Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
#middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
#middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
#middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way(a, b):
  return [a[1],b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))

#6.Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
#make_ends([1, 2, 3]) → [1, 3]
#make_ends([1, 2, 3, 4]) → [1, 4]
#make_ends([7, 4, 6, 2]) → [7, 2]

def make_ends(nums):
  return [nums[0],nums[-1]]

print(make_ends([1, 2, 3]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))

#7.Given an int array length 2, return True if it contains a 2 or a 3.
#has23([2, 5]) → True
#has23([4, 3]) → True
#has23([4, 5]) → False

def has23(nums):
  if nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3:
    return True
  else:
    return False

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))















