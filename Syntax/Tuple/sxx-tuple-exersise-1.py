# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:44:04 2024

@author: jcp
"""

# [문제]
# 튜플(1,3,5,7,9)에서 인덱스 2번째의 값 5를 10으로 바꿔라

t = (1,3,5,7,9)

# t = (1,3,t[2]*2,7,9)


t1 = t[:2]
t2 = t[3:]
t3 = t1+(10,)+t2
print(t3)

# %%

tl = list(t)

tl[2] = 10

tl = tuple(tl)
print(tl)
