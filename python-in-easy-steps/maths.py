#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:36:11 2021

@author: harry
"""

import math, random

print('Rounded up 9.5: ' , math.ceil(9.5))
print('Rounded down 9.5: ' , math.floor(9.5))

num = 4

print(num , 'squared is ', math.pow(num, 2))
print(num , 'square root is ', math.sqrt(num))

nums = random.sample(range(1, 49) , 6)
print('Your lucky lotto numbers are: ' , nums)
