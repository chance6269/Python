# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:37:34 2024

@author: jcp
"""

# sort()
# 정렬순서 : 대문자, 소문자, 한글
# 제약조건 : 리스트의 자료형이 모두 동일해야 한다.

lst = ['a','c','b']

# %%
# 오름차순
lst.sort()
print(lst) # [56, 67, 70, 90, 99, 100]

# %%
# 내림차순 :
#  먼저 sort()로 정렬후 reverse()

lst.sort()
lst.reverse()
print(lst) # [100, 99, 90, 70, 67, 56]
# %%
lst = ['a','Abc','B',99,10,88]
lst.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'