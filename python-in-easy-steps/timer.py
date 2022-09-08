#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:57:09 2021

@author: harry
"""

from time import *

start_timer = time()

struct = localtime(start_timer)

print('\nStarting countdown at: ', strftime('%X' , struct))

i= 10
while i > -1 : 
    print(i)
    i -= 1
    sleep(1)

end_timer = time()

difference = round(end_timer - start_timer)

print('\nRuntime: ' , difference, 'Seconds')