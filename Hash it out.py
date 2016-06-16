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
    
print (answer([0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]))
#x = [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]
#print (x[-1])