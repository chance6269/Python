# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:29:48 2024

@author: jcp
"""

# dict.update(dict)
# 기존의 딕셔너리에 새로운 딕셔너리를 결합

weeks = {1:'월',2:'화',3:'수',4:'목',5:'금'}

sat = {6:'토'}

weeks.update(sat)
print(weeks)

# %%
# 딕셔너리에서는 더하기(+)를 지원하지 않는다.

sun = {7:'일'}
weeks += sun # TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'