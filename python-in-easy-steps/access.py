#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:29:04 2021

@author: harry
"""

file = open('example.txt' , 'w')

print('File Name: ' , file.name)

print('File Open Mode: ' , file.mode)

print('Readable: ' , file.readable())

print('Writable: ' , file.writable())

def get_status(f) :
    if (f.closed != False) :
        return 'Closed'
    else :
        return 'Open'

print('File Status: ', get_status(file))
file.close()
print('\nFile Status' , get_status(file))



