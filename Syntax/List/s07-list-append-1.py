# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:22:21 2024

@author: jcp
"""

# 리스트 추가 : append()
# 기존에 있는 리스트에 하나의 요소를 추가

lst = ['삼성','SK','LG']

lst.append(['APPLE','HD'])

print(lst) # ['삼성', 'SK', 'LG', ['APPLE', 'HD']]

lst.append('IBM')

print(lst) # ['삼성', 'SK', 'LG', ['APPLE', 'HD'], 'IBM']

# %%
# 리스트 확장 : extend
# + 와 동일.
lst = ['삼성','SK','LG']

lst.extend(['APPLE','HD'])

print(lst) # ['삼성', 'SK', 'LG', 'APPLE', 'HD']