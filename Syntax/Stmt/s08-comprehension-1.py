# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:28:22 2024

@author: jcp
"""

# 리스트 컴프리헨션(comprehension, 내포)

lst = [1,2,3,4,5]

# 리스트에서 하나씩 꺼내서 10을 곱하여 리스트 구성
lstx = [n * 10 for n in lst]
print(lstx) # [10, 20, 30, 40, 50]

# %%

# 리스트에서 짝수만 구해서 3을 곱하여 리스트 구성
even= [n * 3 for n in lst if n%2==0]
print(even)