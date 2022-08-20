#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:10:33 2021

@author: harry
"""

day = 32
try: 
    if day > 31 :
        raise ValueError('Invalid day number.')
except ValueError as msg :
        print('The program has found an' , msg)
finally :
        print('But today is beatiful anyway.')
        