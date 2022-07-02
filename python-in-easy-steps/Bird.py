#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:12:38 2021

@author: harry
"""

class Bird :
    '''A base class to define bird properties'''
    count = 0
    
    def __init__(self, chat) :
        
        self.sound = chat
        Bird.count += 1
        
    def talk(self) :
        return self.sound