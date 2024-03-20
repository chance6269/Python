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
sr = pd.Series(lst, index=['날짜', '원주율', '알파벳', '숫자', '존재'])
print(sr)
"""
날짜     2024-03-20
원주율          3.14
알파벳           ABC
숫자            100
존재           True
dtype: object
"""

#%%

# 시리즈에서 인덱스 속성 참조
print(sr.index) # Index(['날짜', '원주율', '알파벳', '숫자', '존재'], dtype='object')

#%%

# 시리즈에서 값 속성 참조
print(sr.values) # ['2024-03-20' 3.14 'ABC' 100 True]

#%%

# reindex() : 재배열(순서변경)
# 기존 데이터 바뀌지 않음 새로운 시리즈를 생성
sr1 = sr.reindex(['존재', '날짜', '원주율', '알파벳', '숫자'])
print(sr1)
"""
존재           True
날짜     2024-03-20
원주율          3.14
알파벳           ABC
숫자            100
dtype: object
"""

#%%

# 인덱스로 값을 참조
print(sr['원주율']) # 3.14
print(sr['알파벳']) # ABC

#%%

# loc
# 인덱스로 값을 참조
print(sr.loc['원주율']) # 3.14
print(sr.loc['알파벳']) # ABC

#%%

# iloc
# 순번으로 값을 참조
print(sr1.iloc[2]) # 3.14
print(sr1.iloc[3]) # ABC

#%%

# 권고하지 않음
print(sr1[2]) # 3.14
print(sr1[3]) # ABC