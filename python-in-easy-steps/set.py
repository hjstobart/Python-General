#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:14:37 2021

@author: harry
"""

zoo = ( 'Kangaroo' , 'Leopard' , 'Moose')
print( 'Tuple: ' , zoo , '\t length' , len(zoo))
print(type(zoo))

bag = {'Red' , 'Green' , 'Blue'}
bag.add('Yellow')
print( '\nSet: ' , bag, '\t length' , len(bag))
print(type(bag))

print('\n Is Green in Bag set?: ' , 'Green' in bag)
print('\n Is Orange in Bag set?: ' , 'Orange' in bag)

box = {'Red' , 'Purple' , 'Yellow'}
print('\n Set: ', box , '\t\t length', len(box))
print('Common to both sets: ' , bag.intersection(box))

