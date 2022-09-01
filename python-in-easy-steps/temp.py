#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 22:17:52 2021

@author: harry
"""

def farenheit(x):
    
    celcius = float(x)
    
    farenheit = ((9 * celcius) / 5) + 32
    
    print(farenheit)
    
def celcius(x):
    
    farenheit = float(x)
    
    celcius = (farenheit - 32)*(5 / 9)
    
    print(celcius)