#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:12:02 2021

@author: harry
"""

from Bird import *

chick = Bird('Cheep, cheep!')
chick.age = '1 week'

print('\nChick says:' , chick.talk())
print('Chick age:' , chick.age)

chick.age = '2 weeks'
print('Chick now:' , chick.age)

setattr(chick, 'age' , '3 weeks')

print('\nChick attributes...')
for attrib in dir(chick) :
    if attrib[0] != '_' :
        print(attrib , ':' , getattr(chick,attrib))
        
delattr(chick, 'age')
print('\nChick age Attribute?:' , hasattr(chick, 'age'))
