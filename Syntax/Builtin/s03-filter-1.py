# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:30:21 2024

@author: jcp
"""

# filter()
# 반복 가능한 데이터를 지정한 함수를 통해서 필터링

# %%

# 리스트에서 양수만 필터링해서 리턴하는 함수
def positive(lst):
    result = []
    for i in lst:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,7,9,-99]))

# %%
x = 10
b = x > 0
print(b) # True

# %%

def posfunc(x):
    return x > 0

fr = filter(posfunc, [1,-3,2,0,-5,7,9,-99])
print(fr) # <filter object at 0x000001BCE811FB50>

# filter 객체의 결과(참) - > list
print(list(fr)) # [1, 2, 7, 9]

fr2 = filter(posfunc, [-3,-5,-99])

print(fr2)
print(list(fr2)) # []