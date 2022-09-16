#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:36:29 2021

@author: harry
"""

from Polygon import *

class Triangle(Polygon):
    def area(self) :
        return (self.width * self.height) /2
    
