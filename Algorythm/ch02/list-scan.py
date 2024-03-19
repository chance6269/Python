# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:17:48 2024

@author: jcp
"""

# 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)

x = ['John','George', 'Paul','Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    
# %%
# 리스트의 모든 원소를 enumerate() 함수로 스캔하기

x = ['John','George', 'Paul','Ringo']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
    
# %%
# 리스트의 모든 원소를 enumerate() 함수로 스캔하기(1부터 카운트)

x = ['John','George', 'Paul','Ringo']

for i, name in enumerate(x, 1):
    print(f'x[{i}] = {name}')
    
# %%
# 리스트의 모든 원소를 스캔하기(인덱스 값 사용하지 않음)

x = ['John','George', 'Paul','Ringo']

for i in x:
    print(i)