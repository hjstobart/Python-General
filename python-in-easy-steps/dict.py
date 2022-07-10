#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:23:15 2021

@author: harry
"""

dict = { 'name' : 'Bob' , 'ref' : 'Python' , 'sys' : 'Mac'}
print('Dictionary: ' , dict)

print('\n Reference: ', dict['ref'])

print( '\n Keys: ', dict.keys())

del dict['name']
dict['user'] = 'Tom'
print('\n Dictionary: ' , dict)

print('\n Is there a name key?: ', 'name' in dict)
