#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:48:05 2021

@author: harry
"""

chars = ['A' , 'B' , 'C']
fruit = ('Apple' , 'Banana' , 'Cherry')
dict = {'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Mac'}

print('\n Elements: \t' , end = ' ')
for item in chars :
    print( item , end = ' ')
    
print('\n Enumerated: \t' , end = ' ')
for item in enumerate(chars) :
    print(item , end = ' ')
    
print('\n Zipped: \t' , end = ' ')
for item in zip(chars , fruit) :
    print(item , end = ' ')

print('\n Paired: ')
for key , value in dict.items() :
    print( key, '=' , value)
    
    