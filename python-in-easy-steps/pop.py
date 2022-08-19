#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:00:29 2021

@author: harry
"""

basket = ['Apple' , 'Bun' , 'Cola']
crate = ['Egg' , 'Fig' , 'Grape']

print('Basket list: ' , basket )
print('Basket elements: ' , len(basket))

basket.append('Damson')
print('Appended: ' , basket)
print('Last item removed: ' , basket.pop())
print('Basket list: ' , basket)

basket.extend(crate)
print('Extended: ' , basket)
del basket[1]
print('Item removed: ' , basket)
del basket[1:3]
print('Slice removed: ' , basket)