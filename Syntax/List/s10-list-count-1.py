# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:29:59 2024

@author: jcp
"""

# 리스트에서 해당하는 값을 포함하는 갯수 세기 : count()
# 갯수 = 리스트.count(값)
# 리턴 : 해당하는 값과 일치하는 요소의 갯수, 없으면 0

lst = ['삼성','SK','LG','APPLE','HD','LG']

value= 'LG'
count = lst.count(value)

print(count) # 2