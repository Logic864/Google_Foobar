# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:31:58 2016
@author: Jesse

Peculiar balance
================
Can we save them? Beta Rabbit is trying to break into a lab that contains the
only known zombie cure - but there's an obstacle. The door will only open if a
challenge is solved correctly. The future of the zombified rabbit population is
at stake, so Beta reads the  challenge: There is a scale with an object on the
left-hand side, whose mass is given in some number of units.
Predictably, the task is to  balance the two sides.
But there is a catch: You only have this peculiar weight set,
having masses 1, 3, 9, 27, ... units. That is, one  for each power of 3.
Being a brilliant mathematician, Beta Rabbit quickly discovers that any number
of units of mass can be balanced exactly using this set. To help Beta get into
the room, write a method called answer(x), which outputs a list of strings
representing where the weights should be  placed, in order for the two sides to
be balanced, assuming that weight on the left has mass x units.
The first element of the output list should correspond to the 1-unit weight,
the second element to the 3-unit weight, and so on. Each string is one of:
"L" : put weight on left-hand side
"R" : put weight on right-hand side
"-" : do not use weight
To ensure that the output is the smallest possible, the last element of the list
must not be "-". x will always be a positive integer, no larger than 1000000000.
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
