#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:45:01 2021

@author: harry
"""


def sum_n(N):
    total = sum(i for i in range(1,N+1))
    print(total)


def invsum(N):
    total = sum(1/(2**i) for i in range(1,N+1))
    print(total)
 



#var1 = int(input('Please enter a number: ', ))
def globalfunction(var1) :
    
    var1 = int(var1)
    
    if var1 < 10 and var1 >0 :
        print('Working on quantum scale.')
        invsum(var1)
    
    elif var1 >=10 and var1 <=100 :
        print('Working on normal scale.')
        sum_n(var1)
            
    elif var1 > 100 :
        print('Working at the relativistic scale.')
        for i in range(1,6):
            print(var1/i)
    
    else :
        print('Error.')
    
    

globalfunction(1)
globalfunction(34)
globalfunction(200)    



