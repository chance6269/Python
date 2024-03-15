# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:08:25 2024

@author: jcp
"""

# [문제]

# while문을 이용하여 1부터 100까지의 합을 구하라
# 단, 반복문은 무한루프

total = 0
num = 1
while True:
    if num > 100:
        break
    total += num
    num += 1
    
print(total)