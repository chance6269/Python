# -*- coding: utf-8 -*-




# 판단스(pandas)


import pandas as pd

# dict
dx = {'a':1, 'b':2, 'c':3}

# 시리즈 : 1차원
# 키 -> 인덱스(index)
# 값 -> 값(value)
sr = pd.Series(dx) # 딕셔너리 -> 판다스(시리즈) 객체 생성
print(type(sr)) # <class 'pandas.core.series.Series'>
print(sr) # (3,)
"""
a    1
b    2
c    3
dtype: int64
"""

#%%
# 시리즈에서 인덱스 속성 참조
print(sr.index) # Index(['a', 'b', 'c'], dtype='object')
print(sr.index[2]) # c

#%%

# 시리즈에서 값 속성 참조
print(sr.values) # [1 2 3]