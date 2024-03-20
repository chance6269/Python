# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:13:34 2024

@author: Solero
"""

# 판단스(pandas)


import pandas as pd

lst = ['2024-03-20', 3.14, 'ABC', 100, True]

# 리스트는 시리즈의 값으로 지정
# 인덱스: 0부터 순차적으로 지정
# 값 : 리스트가 지정
sr = pd.Series(lst)
print(sr)

#%%

# 시리즈에서 인덱스 속성 참조
print(sr.index) # RangeIndex(start=0, stop=5, step=1)

#%%

# 시리즈에서 값 속성 참조
print(sr.values) # ['2024-03-20' 3.14 'ABC' 100 True]


#%%