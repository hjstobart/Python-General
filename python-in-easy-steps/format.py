#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:58:31 2021

@author: harry
"""

snack = '{} and {}'.format('Burger' , 'Fries')

print('\nReplaced: ', snack)

snack = '{1} and {0}'.format('Burger' , 'Fries')

print('\nReplaced: ', snack)

snack = '%s and %s' % ('Milk', 'Cookies')

print('\nSubstituted: ', snack)
