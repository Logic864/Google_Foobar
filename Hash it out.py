# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:31:48 2016

@author: Jesse
"""

def answer(digest):
    message = []
    
    for j in range(255):
        if digest[0] == ((129*j)^0)%256:
            message.append(j)
            break;
    
    for i in range(1, len(digest)):
        for j in range(255):
           if digest[i] == ((129*j)^message[-1])%256:
                message.append(j)
                break;
            
    return message
    
