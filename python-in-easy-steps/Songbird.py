#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:23:57 2021

@author: harry
"""

class Songbird :
    
    def __init__(self , name , song) :
        self.name = name
        self.song = song
        print(self.name , 'Is Born...')
        
    def sing (self) :
        print(self.name , 'Sings:' , self.song)
        
    def __del__(self) :
        print(self.name , 'Flew Away!\n')
    
    