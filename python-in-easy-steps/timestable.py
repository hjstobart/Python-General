#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 17:04:42 2021

@author: harry
"""

def timestable(number):
    if number != float(number) :
        print('Must be an numerical value!')
    else :
        for i in range(1, 13):
            print(i , ' * ' , number , ' = ' , number * i)
            
number = float(input('Please input a number: '))
timestable(number)
