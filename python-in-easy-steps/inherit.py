#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:37:33 2021

@author: harry
"""

from Rectangle import *
from Triangle import *

rect = Rectangle()
trey = Triangle()

rect.set_values(4, 5)
trey.set_values(4, 5)

print('Rectangle area:' , rect.area())

print('Triangle area;', trey.area())
