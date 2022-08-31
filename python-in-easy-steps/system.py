#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:32:38 2021

@author: harry
"""

import sys , keyword

print('Pyhton version: ' , sys.version)

print('Python interpreter location: ' , sys.executable)

print('Python module search path: ')
for dir in sys.path :
    print(dir)

print('Python Keywords: ')
for word in keyword.kwlist :
    print(word)

