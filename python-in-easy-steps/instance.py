#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:22:49 2021

@author: harry
"""

from Bird import *

print('\nClass Instances of:\n' , Bird.__doc__)

polly = Bird('Squawk, squawk!')

print('\nNumber of birds:', polly.count)
print('Polly says:', polly.talk())

harry = Bird('Tweet, tweet!')

print('\nNumber of birds:' , harry.count)
print('Harry says:' , harry.talk())