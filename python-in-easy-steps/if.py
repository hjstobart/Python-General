#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:32:10 2021

@author: harry
"""

num = int(input('Please enter a number: '))
if num > 5 :
    print('Number is greater than 5')
elif num < 5 :
    print('Number is less than 5')
else :
    print('Number is equalt to 5')
    
if num > 7 and num < 9 :
    print('Number is 8')
if num == 1 or num == 3 :
    print('Number is 1 or 3')