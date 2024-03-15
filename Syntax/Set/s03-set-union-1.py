# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:20:48 2024

@author: jcp
"""

# 합집합: |
# 메소드: set.union()

# %%

s1 = set('123456')
s2 = set('456789')

print(s1) # {'4', '5', '1', '3', '6', '2'}
print(s2) # {'4', '8', '5', '9', '6', '7'}

# 양쪽 모두 선택
# 중복되는 요소는 하나만 선택

s3 = s1 | s2 # {'4', '5', '8', '1', '3', '9', '6', '2', '7'}
print(s3)

# %%
s4 = s1.union(s2)
print(s4) # {'4', '5', '8', '1', '3', '9', '6', '2', '7'}