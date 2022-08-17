#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:55:48 2021

@author: harry
"""

from Duck import *
from Mouse import *

def describe(object) :
    object.talk()
    object.coat()
    
donald = Duck()
mickey = Mouse()

describe(donald)
describe(mickey)