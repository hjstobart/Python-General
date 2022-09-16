#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:46:42 2021

@author: harry
"""

text = 'Hello, welcome to Software Testing Help. In this article: "Loops in Python", you’ll learn about loops with practical examples. Great right? Make sure to follow along as we learn together.'

for punc in '.,:\n?!"' :
    text = text.replace(punc , '')
text = text.lower()

text = text.split()

wordcount = {}
for word in text :
    wordcount[word] = wordcount.get(word , 0) + 1
    
wordcount = {w : c for w , c in sorted(wordcount.items(), key = lambda item : item[1] , reverse = True)}
print(wordcount)