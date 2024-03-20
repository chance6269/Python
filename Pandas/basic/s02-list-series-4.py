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

# 인덱스 다중 선택 : 개별지정
# KeyError: 'key of type tuple not found and not a MultiIndex
# print(sr['원주율', '알파벳'])
# 리스트 형태로 줘야함
print(sr[ ['원주율', '알파벳'] ])

#%%

# 인덱스 다중 선택 : 범위지정
print(sr['원주율': '숫자'])

#%%

# KeyError: 'key of type tuple not found and not a MultiIndex'
# print(sr[ ('원주율', '알파벳') ])
# print(sr[ '원주율', '알파벳' ])

#%%

selindex = ['원주율', '알파벳']
print(sr[ selindex ])