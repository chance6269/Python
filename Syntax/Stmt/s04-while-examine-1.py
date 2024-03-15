# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:14:06 2024

@author: jcp
"""

# [문제] while문을 이용하여 아래의 문제를 해결하라.
# 1부터 100까지의 연속으로 숫자를 1씩 증가시켜
# 3의 배수와 5의 배수를 각각 구하라.

multi3 = []
multi5 = []

n = 1

while True:
    if n > 100:
        break
    if n % 3 == 0:
        multi3.append(n)
    if n % 5 == 0:
        multi5.append(n)
    n += 1
    
print("3의 배수 : ",multi3)    
print("5의 배수 : ",multi5)    
# %%
# [문제2]
#  continue 문을 활용하라
multi3 = []
multi5 = []

n = 1

while True:
    if n <= 100:
        if n % 3 == 0:
            multi3.append(n)
        if n % 5 == 0:
            multi5.append(n)
        n += 1
        continue
    break
    
print("3의 배수 : ",*multi3)    
print("5의 배수 : ",*multi5)    