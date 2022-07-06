#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:37:50 2021

@author: harry
"""

a = input('Enter a number: ')
b = input('Now enter another number: ')

sum = a + b
print('Data type sum: ' , sum , type(sum))

sum = int(a) + int(b)
print('Data type sum: ' , sum , type(sum))

sum = float(sum)
print('Data type sum: ' , sum , type(sum))

sum = chr(int(sum))
print('Data type sum: ' , sum , type(sum))
60