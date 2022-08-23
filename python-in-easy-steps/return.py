#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:41:40 2021

@author: harry
"""

num = input('Enter an integer: ')
def square(num):
    if not num.isdigit() :
        return 'Invalid Entry'
    num = int(num)
    return num * num
print(num , 'squared is: ' , square(num))
