#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 22:06:50 2021

@author: harry
"""

from re import *

pattern  = \
    compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    
def get_address() :
    address = input('Enter your email address: ')
    is_valid = pattern.match(address)
    
    if is_valid :
        print('Valid email address: ', is_valid.grop())
        
    else :
        print('Invalid email address! Please retry...\n')
        

get_address()