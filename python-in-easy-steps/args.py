#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:37:22 2021

@author: harry
"""

def echo(user, lang, sys):
    print('User: ', user , 'Language: ', lang, 'System:' , sys)
    
echo( 'Mike' , 'Python' , 'Windows')

echo(lang = 'Python' , sys = 'Mac OS' , user = 'Annie')

def mirror(user = 'Carole' , lang = 'Python'):
    print('\nUser:' , user , 'Language: ', lang)
    
mirror()
mirror(lang = 'Java')
mirror(user = 'Tony')
mirror('Susan' , 'C++')
