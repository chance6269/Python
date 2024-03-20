# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:13:34 2024

@author: Solero
"""

# 판단스(pandas)


import pandas as pd

lst = ['2024-03-20', 3.14, 'ABC', 100, True]

# 리스트는 시리즈의 값으로 지정
# 인덱스: 인자로 지정
# 값 : 리스트가 지정
sr = pd.Series(lst, index=[1,2,3,4,5])
print(sr)
print(sr[1])
"""
1    2024-03-20
2          3.14
3           ABC
4           100
5          True
"""

#%%

# 시리즈에서 인덱스 속성 참조
print(sr.index) # Int64Index([1, 2, 3, 4, 5], dtype='int64'))

#%%

# 시리즈에서 값 속성 참조
print(sr.values) # ['2024-03-20' 3.14 'ABC' 100 True]

#%%

#%%

# loc
# 인덱스로 값을 참조
print(sr.loc[2]) # 3.14
print(sr.loc[3]) # ABC

#%%

# iloc
# 순번으로 값을 참조
print(sr.iloc[1]) # 3.14
print(sr.iloc[2]) # ABC

#%%

# 인덱스로 값을 참조
# ※ 권고하지 않음
print(sr[0]) # KeyError: 0
print(sr[2]) # 3.14
print(sr[3]) # ABC