#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:08:27 2021

@author: harry
"""

string = 'python in easy steps'

print('\nCapitalized:\t' , string.capitalize())

print('\nTitled:\t\t'  , string.title())

print('\nCentered:\t' , string.center(30, '*'))

print('\nUppercase:\t' , string.upper())

print('Joined:\t\t' , string.join('**'))

print('\nJustified:\t' , string.rjust(30, '*'))

print('\nReplaced:\t', string.replace('s' , '*'))