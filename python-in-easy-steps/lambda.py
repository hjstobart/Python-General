#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:48:45 2021

@author: harry
"""

def function_1(x) : return x**2
def function_2(x) : return x**3
def function_3(x) : return x**4

callbacks = [function_1 , function_2 , function_3]

print('\nNamed Functions:')
for function in callbacks : print('Result: ' , function(3))

callbacks = \
    [lambda x : x**2 , lambda x : x**3 , lambda x : x**4]

print('\nAnonymous functions: ')
for function in callbacks : print('Result: ', function(3))
