#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:25:42 2021

@author: harry
"""

a = 1
b = 2

print('\n Variable a is: ' , 'One' if (a == 1) else 'Not one')
print('\n Variable a is: ' , 'Even' if (a % 2 == 0) else 'Odd')

print('\n Variable b is: ' , 'One' if (b == 1) else 'Not one')
print('\n Variable b is: ' , 'Even' if (b % 2 == 0) else 'Odd')

max = a if (a > b) else b

print('\n Greater value is: ' , max)
