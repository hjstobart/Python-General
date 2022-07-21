#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:46:08 2021

@author: harry
"""

from Person import *

class Hombre(Person) :
    def speak(self, msg) :
        print(self.name , ':\n\tHola!' , msg)
        
        