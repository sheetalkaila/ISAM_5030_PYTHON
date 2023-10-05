# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:15:34 2023

@author: sheetal
"""
#Question1.

Booklist = ['Lord of ring','Avartar','Harry Potter','Spare','Bible','Roma','Python']
Week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#1.In one week, every day you will read one book. Print out these 7 books

print('#########Q1########')
for i in range(len(Booklist)):
    print('On',Week[i],'you will read',Booklist[i])

#2.What if you want read book every other day? Print out the book you want read every other day since Monday

print('#########Q2########')
for i in range(0,len(Booklist),2):
    print('On',Week[i],'you will read',Booklist[i])

#3.What if you want read book every other day? Print out the book you want read every other day since Tuesday

print('#########Q3########')
for i in range(1,len(Booklist),2):
    print('On',Week[i],'you will read',Booklist[i])

#4.What if you want read book every three days? Print out the book you want read every other day since Monday

print('#########Q4########')
for i in range(0,len(Booklist),3):
    print('On',Week[i],'you will read',Booklist[i])

#5.Go through the book list find if you have book name == ‘Roma’

print('#########Q5########')
t_flag = False
for book in Booklist:
    if book.startswith('Roma'):
        print('Yes, we have a book ‘Roma’!')
        t_flag = True
#end of for loop
if t_flag == False:
    print('Sorry we do not have a book ‘Roma’!')

#6.Go through the book list print out the book before ‘Roma’ and after ‘Roma’

print('#########Q6########')
roma_indx = Booklist.index('Roma')
if roma_indx < 0:
    print('We do not have a book Roma!')
else:
    print('The book before Roma is', Booklist[roma_indx - 1])
    print('The book before Roma is', Booklist[roma_indx + 1])

#7.Go through the book list find if you have two books ‘Spare’ and ‘Bible’ are located right next to each other. Either one can be first.

print('#########Q7########')
roma_indx = Booklist.index('Spare')
if roma_indx < 0:
    print('We do not have a book Spare!')
else:
    book_before = Booklist[roma_indx - 1]
    book_after = Booklist[roma_indx + 1]
    if book_before.startswith('Bible') or book_after.startswith('Bible'):
        print('Yes we have two books ‘Spare’ and ‘Bible’ are located  next to each other')
    else:
        print('No, two books ‘Spare’ and ‘Bible’ are not located next to each other')

#8.Reverse the booklist.

print('#########Q8########')
print(Booklist[::-1])


    




















