# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:16:52 2024

@author: jcp
"""

# clear()
# id는 변하지 않는다.

lst = ['삼성','SK','LG','HD']
print(id(lst),lst)

lst.clear()
print(id(lst),lst)

# del
lst = ['삼성','SK','LG','HD']
del lst[:]
print(id(lst),lst)

# 그냥 빈 리스트 할당
lst = [] 
print(id(lst),lst)
# id가 바뀜.