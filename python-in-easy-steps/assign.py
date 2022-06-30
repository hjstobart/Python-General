#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 14:44:33 2021

@author: harry
"""

a = 8
b = 4

print('Assign Values: \t\t' , 'a =' , a , '\tb =' , b)

a += b
print('Add & Assign:\t\t' , 'a =' , a , '(8 += 4)')

a-=b
print('Subtract & Assign:\t' , 'a =' , a , '(12 - 4)')

a *= b
print('Multiply & Assign:\t' , 'a =' , a , '(8 x 4)')

a /= b
print('Divide & Assign:\t\t' , 'a =' , a , '(32 / 4)')

a %= b
print('Modulo & Assign:\t\t' , 'a =' , a , '(8 % 4)')
