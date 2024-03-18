# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:06:55 2024

@author: jcp
"""

# functools.reduce(func, iterable) : 
#  function을 반복 가능한 객체의 요소에 차례대로 누적 적용하여
#  이 객체를 하나의 값으로 줄이는 함수

# 입력 인수 data의 요소를 모두 더하여 반환하는 add() 함수
def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1,2,3,4,5]
result = add(data)
print(result)

# %%
import functools

data = [1,2,3,4,5]
result = functools.reduce(lambda x,y: x + y, data) # ((((1+2)+3)+4)+5)
print(result)

# %% 
# 최대값 구하기
num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num) # 8