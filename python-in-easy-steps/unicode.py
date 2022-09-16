#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:14:39 2021

@author: harry
"""

s = 'Röd'

print('\nRed String: ' , s)
print('Type: ', type(s), '\tLength: ' , len(s))

s = s.encode('utf-8')
print('\nEncoded string: ', s)
print('Type: ', type(s) , '\tLength: ', len(s))

s = s.decode('utf-8')
print('\nDecoded string: ', s)
print('Type: ', type(s) , '\tLength: ' , len(s))

import unicodedata
for i in range(len(s)):
    print(s[i] , unicodedata.name(s[i]), sep = ' : ')
    
s = b'Gr\xc3\xb6n'

print('\nGreen String: ', s.decode('utf-8'))

s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print('Green String: ', s)