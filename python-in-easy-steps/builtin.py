#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:18:34 2021

@author: harry
"""

from Bird import *

zola = Bird('Beep, beep!')

print('\nBuilt-in instance attributes...')
for attrib in dir(zola) :
    if attrib[0] == '_' :
        print(attrib)
        
print('\nClass Dictionary...')
for item in Bird.__dict__ :
    print(item , ':' , Bird.__dict__[item])
    
print('\nInstance Dictionary...')
for item in zola.__dict__ :
    print(item, ':' , zola.__dict__[item])
    
    
