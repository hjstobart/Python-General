#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 17:15:01 2021

@author: harry
"""

def calculate(a , b , operator) :
    if operator == '+' :
        print(a + b)
    elif operator == '-' :
        print(a - b)
    elif operator == '*' :
        print(a * b)
    elif operator == '/' :
        print(a / b)
    else :
        print('Please enter an appropriate operator.')


a = float(input('Please enter the first number: '))
b = float(input('Please enter the second number: '))
operator = input('Please enter the operator: ')

calculate(a,b,operator)

    