# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:14:42 2024

@author: jcp
"""

# 리스트 요소 삭제 : remove()
# list.remove(value)
# 처음 찾은 값(value)에 해당하는 요소를 삭제

lst = ['삼성', 'SK','LG', 'APPLE', 'LG']
lst.remove('LG')

print(lst) # ['삼성', 'SK', 'APPLE', 'LG']
# %%
# list.index(value)
# 해당 값의 위치를 리턴

a = [1,2,3]
a.index(3) # 2
