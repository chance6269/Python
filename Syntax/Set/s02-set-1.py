# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:15:08 2024

@author: jcp
"""

# 교집합 : &
# 메소드 : set.intersection()

# %%

s1 = set('123456')
s2 = set('456789')

print(s1) # {'4', '5', '1', '3', '6', '2'}
print(s2) # {'4', '8', '5', '9', '6', '7'}

# 양쪽 모두 존재하는 값을 선택
s3 = s1 & s2
print(s3) # {'4', '6', '5'}

s4 = s1.intersection(s2)
print(s4) # {'4', '6', '5'}