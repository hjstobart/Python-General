#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:28:17 2021

@author: harry
"""

global_var = 1

def my_vars() :
    print('Global variable: ', global_var)
    
    local_var = 2
    print('Local variable: ', local_var)
    
    global inner_var
    inner_var = 3
    
my_vars()

print('Coerced Global: ', inner_var)
