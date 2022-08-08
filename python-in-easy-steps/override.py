#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:47:17 2021

@author: harry
"""

from Man import *
from Hombre import *

guy_1 = Man('Richard')
guy_2 = Hombre('Ricardo')

guy_1.speak('It\'s a beautiful evening!\n')
guy_2.speak('Es una tarde hermosa!\n')

Person.speak(guy_1)
Person.speak(guy_2)