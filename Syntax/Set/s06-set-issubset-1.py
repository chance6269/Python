# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:07:45 2024

@author: jcp
"""

# 부분집합
# a는 b의 부분집합인가?
# bool = a.issubset(b)

# %%

a = {'서울','대전','대구','부산','제주'}
b = {'서울','대전','대구','부산','전주', '목포'}
c = {'서울','대전','대구','부산'}
d = {'서울','대전','대구','부산'}

# a는 b의 부분집합인가?
sab = a.issubset(b)
print(sab) # False

# c는 a의 부분집합인가?
sca = c.issubset(a)
print(sca) # True