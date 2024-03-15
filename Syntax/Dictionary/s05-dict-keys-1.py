# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:17:04 2024

@author: jcp
"""

student = {
    'name': '홍길동',
    'age':34,
    '주소':'한양',
    '생존':False
    }

print(student)

#%%

# Key 리스트 만들기 : dict.keys()
# 키 목록을 얻기
dk = student.keys()
print(dk) # dict_keys(['name', 'age', '주소', '생존'])

# %%

# dict.keys()를 튜플로 전환
tk = tuple(dk)
print(tk) # ('name', 'age', '주소', '생존')