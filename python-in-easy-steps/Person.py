#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:42:47 2021

@author: harry
"""

class Person :
    
    ''' A base class to define Person properties '''
    
    def __init__(self, name):
        self.name = name
        
    def speak(self , msg = '(Calling The Base Class)' ) :
        print(self.name , msg)

            
            