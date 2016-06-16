# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:44:04 2016

@author: Jesse
"""

def answer(x):
    
    if (sum(x)/len(x))%2 == 0:
        return len(x)
    else:
        return len(x) - 1
    

print(answer([0, 0, 0, 0, 22]))
    