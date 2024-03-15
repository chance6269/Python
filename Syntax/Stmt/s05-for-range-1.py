# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:18:52 2024

@author: jcp
"""

# range(start, end, step)
#  - start: default = 0
#  - end : end - 1
#  - step
#  range(end)

m = range(1, 11, 2)
t = 0
for n in m:
    print(n, end='')
    if n != 9:
        print(', ', end='')
        
    t += n
    
    