#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:16:06 2021

@author: harry
"""

chars = ['Aplpha' , 'Beta' , 'Gamma' , 'Delta' , 'Epsilon']

def display(elem):
    assert type(elem) is int , 'Argument must be an integer!'
    print('List element)' , elem , '=' , chars[elem])
    
elem = 4
display(elem)

elem = elem/2 
display(elem)
