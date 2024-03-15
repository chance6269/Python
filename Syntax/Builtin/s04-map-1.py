# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:06:45 2024

@author: jcp
"""

# map()
# map(func, iterable)
# 데이터의 각 요소에 함수(func)를 적용한 결과를 리턴

# %%

# 람다함수

lst = [1,3,5,7,9]
lstm = map(lambda x : x * 2, lst)

print(lstm)
print(list(lstm)) # [2, 6, 10, 14, 18]