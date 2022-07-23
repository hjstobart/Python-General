#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:43:03 2021

@author: harry
"""

from decimal import *

item = Decimal(0.70)
rate = Decimal(1.05)

tax = item * rate
total = item + tax

print('Item:\t' , '%.20f' % item)
print('Tax:\t' , '%.20f' % tax)
print('Total:\t' , '%.20f' % total)