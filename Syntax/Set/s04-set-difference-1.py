# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:24:37 2024

@author: jcp
"""

# 차집합 : -
# 메소드 : set.difference()


# %%

s1 = set('123456')
s2 = set('456789')

print(s1) # {'4', '5', '1', '3', '6', '2'}
print(s2) # {'4', '8', '5', '9', '6', '7'}

# a 에서 b를 제외한 나머지 요소
s3 = s1 - s2
print(s3) # {'2', '1', '3'}

# %%
s4 = s1.difference(s2)
print(s4) # {'2', '1', '3'}