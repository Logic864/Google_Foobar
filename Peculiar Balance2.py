# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:31:58 2016

@author: Jesse
"""

def test(x):
    wght = []
    result = []
    l = ["-", "R","L"]
    
    for i in range(0, x):
        if 3**i < x*2:
            wght.append(3**i)
        else:
            break;
    
    for i in range(len(wght)):
        z = int((x + ((3 ** i - 1) / 2)) / 3 ** i)
        result.append(l[z%3])
            
    return result;
            
print(test(int(input())))    