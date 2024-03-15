# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:30:27 2024

@author: jcp
"""

# 대칭 차집합(symmetric difference)
# 한쪽에는 있지만 양쪽 모두에 있지 않은 요소
# 교집합을 제외한 나머지 요소들의 집합.
# 대칭 차집합: ^(circumflex)
# 메소드 : set.symmetric_difference()

# %%
a = {'서울','대전','대구','부산','제주'}
b = {'서울','대전','대구','부산','전주', '목포'}
c = {'서울','대전','대구','부산','제주'}

# 
sd1 = a.symmetric_difference(b)
print(sd1) # {'제주', '목포', '전주'}

sd2 = a ^ b
print(sd2) # {'제주', '목포', '전주'}

# %%
# [문제]
# 위의 set a, b를 차집합, 합집합을 결합해서 대칭 차집합을 구하라
symm = a.union(b) - a.intersection(b)
symm2 = (a | b) - (a & b)
print(symm) # {'전주', '목포', '제주'}
print(symm2)