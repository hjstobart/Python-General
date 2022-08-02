#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:44:48 2021

@author: harry
"""

from Person import *

''' A derived class to define Man properties '''

class Man(Person) :
    def speak(self, msg) :
        print(self.name , ':\n\tHello!' , msg)
        
