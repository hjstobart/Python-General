#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:57:27 2021

@author: harry
"""

title = '\nPython in easy steps\n'
for char in title : print(char , end= ' ')

for char in title : 
    if char == 'y' :
        print('*' , end = ' ')
        continue
    print(char , end = ' ')
    
for char in title :
    if char == 'y' :
        print('*' , end = ' ')
        pass
    print(char , end = ' ')
