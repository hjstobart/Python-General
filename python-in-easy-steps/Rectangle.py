#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:35:35 2021

@author: harry
"""

from Polygon import *

class Rectangle(Polygon) :
    def area(self) :
        return self.width * self.height
    
    